#!/usr/bin/env python3
"""S5: wall 窓 NET の系統再解析（theory_research 専用）。

phase0_reproduction.csv の各 site×detector について raw/*.mca を
mca_common だけで再解析し、背景法（右側帯 / 左右直線 / GROSS）を比較、
測定記録.csv の dead time で補正した NET を reports/S5_corrected_net.csv に出力する。
"""

from __future__ import annotations

import csv
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
MEAS = HERE.parent
CODE = MEAS.parent
RAW = MEAS / "raw"
TABLES = MEAS / "tables"
sys.path.insert(0, str(CODE))

import mca_common as mc  # noqa: E402

OUT_CSV = HERE / "reports" / "S5_corrected_net.csv"
PHASE0 = HERE / "tables" / "phase0_reproduction.csv"
REC = TABLES / "測定記録.csv"
WIN_CMP = TABLES / "フラックス_窓比較.csv"

FIELDS = [
    "検出器", "地点", "filename", "wall_net_raw", "wall_net_corrected",
    "stat_err", "sys_bg_err", "dead_time_pct", "bg_method", "notes",
]


@dataclass
class WallVariants:
    right_cps: float
    right_err: float
    right_valid: bool
    right_mode: str
    linear_cps: float
    linear_err: float
    linear_valid: bool
    linear_mode: str
    gross_cps: float
    live_s: float
    peak_ch: int
    right_warning: str
    linear_warning: str


def load_dead_pct() -> dict[str, float]:
    """filename → dead time [%]. 測定記録.csv の dead_pct 列（_build_mca_xlsx: 100×(1−live/real)）。"""
    out: dict[str, float] = {}
    if not REC.exists():
        return out
    with REC.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            fn = (r.get("filename") or "").strip()
            v = (r.get("dead_pct") or r.get("dead_time_pct") or "").strip()
            if fn and v:
                try:
                    out[fn] = float(v)
                except ValueError:
                    pass
    return out


def pct_to_frac(pct: float) -> float:
    return pct / 100.0 if pct > 0 else 0.0


def dead_correct(cps: float, dead_frac: float) -> float:
    if not math.isfinite(cps) or dead_frac <= 0 or dead_frac >= 0.99:
        return cps
    return cps / (1.0 - dead_frac)


def analyze_mca(path: Path) -> WallVariants:
    meta = mc.parse_mca_for_analysis(path)
    counts = np.asarray(meta["counts"], dtype=float)
    live = float(meta["LIVE_TIME"])
    serial = mc.infer_serial(path.name, str(meta.get("serial") or ""))

    wall_r = mc.analyze_wall_window_right_only(counts, serial)
    wall_l = mc.analyze_wall_window_linear(counts, serial)

    def cps(w: mc.RoiAnalysis) -> float:
        return w.net / live if live > 0 else float("nan")

    def cps_err(w: mc.RoiAnalysis) -> float:
        return w.err / live if live > 0 else float("nan")

    gross_cps = wall_r.gross / live if live > 0 else float("nan")

    return WallVariants(
        right_cps=cps(wall_r),
        right_err=cps_err(wall_r),
        right_valid=wall_r.net_valid,
        right_mode=wall_r.bg_mode,
        linear_cps=cps(wall_l),
        linear_err=cps_err(wall_l),
        linear_valid=wall_l.net_valid,
        linear_mode=wall_l.bg_mode,
        gross_cps=gross_cps,
        live_s=live,
        peak_ch=wall_r.roi_peak,
        right_warning=wall_r.warning,
        linear_warning=wall_l.warning,
    )


def sys_bg_spread(v: WallVariants) -> float:
    """背景法間の正 NET 差の半幅 [CPS]。"""
    pos = []
    for x in (v.right_cps, v.linear_cps, v.gross_cps):
        if math.isfinite(x) and x > 0:
            pos.append(x)
    if len(pos) >= 2:
        return 0.5 * (max(pos) - min(pos))
    if len(pos) == 1 and math.isfinite(v.right_cps) and math.isfinite(v.linear_cps):
        return abs(v.right_cps - v.linear_cps)
    return float("nan")


def pick_method(v: WallVariants) -> tuple[float, float, str, float]:
    """(net_cps, stat_err, bg_method, sys_bg_err) を返す。"""
    spread = sys_bg_spread(v)

    # 主値: 右側帯（CONTEXT / mca_common 既定）
    if v.right_valid and v.right_cps > 0:
        return v.right_cps, v.right_err, "sideband_right", spread

    # 右側帯 NET<=0 → 左右直線
    if v.linear_valid and v.linear_cps > 0:
        sy = spread if math.isfinite(spread) else abs(v.linear_cps) * 0.15
        return v.linear_cps, v.linear_err, "sideband_linear", sy

    # 右側帯不可 → GROSS（none_gross 時の実効値）
    if v.right_mode == "none_gross" and v.gross_cps > 0:
        sy = spread if math.isfinite(spread) else v.gross_cps * 0.25
        return v.gross_cps, math.sqrt(max(v.gross_cps * v.live_s, 0)) / v.live_s, "gross", sy

    # 全て失敗: 最大値を報告（負 NET 含む）
    candidates = [
        (v.right_cps, v.right_err, "sideband_right_invalid"),
        (v.linear_cps, v.linear_err, "sideband_linear_invalid"),
        (v.gross_cps, math.sqrt(max(v.gross_cps * v.live_s, 0)) / v.live_s if v.live_s else float("nan"),
         "gross_fallback"),
    ]
    best = max(candidates, key=lambda t: t[0] if math.isfinite(t[0]) else -1e99)
    sy = spread if math.isfinite(spread) else abs(best[0]) * 0.3 if best[0] > 0 else float("nan")
    return best[0], best[1], best[2], sy


def fmt(x: float, nd: int = 6) -> str:
    if x != x or not math.isfinite(x):
        return ""
    return f"{x:.{nd}g}"


def clean_filename(fn: str) -> str:
    return fn.split("（")[0].strip()


def build_row(
    det: str,
    site: str,
    fn: str,
    raw_net: float,
    dead_pct: dict[str, float],
) -> dict:
    path = RAW / fn
    notes: list[str] = []
    if not path.exists():
        return {
            "検出器": det, "地点": site, "filename": fn,
            "wall_net_raw": fmt(raw_net), "wall_net_corrected": "",
            "stat_err": "", "sys_bg_err": "", "dead_time_pct": "",
            "bg_method": "missing_mca", "notes": "raw/*.mca 不在",
        }

    v = analyze_mca(path)
    net, stat, method, sy = pick_method(v)
    dp = dead_pct.get(fn, 0.0)
    df = pct_to_frac(dp)
    net_corr = dead_correct(net, df)

    notes.append(f"R={fmt(v.right_cps,4)} L={fmt(v.linear_cps,4)} G={fmt(v.gross_cps,4)}")
    if v.peak_ch:
        notes.append(f"peak_ch={v.peak_ch}")
    if v.right_mode == "none_gross":
        notes.append("右側帯不可→GROSS")
    if not v.right_valid and v.linear_valid:
        notes.append("右NET<=0→直線背景採用")
    if dp > 0 and df < 0.99:
        notes.append(f"dead補正×{1/(1-df):.4f}")

    return {
        "検出器": det,
        "地点": site,
        "filename": fn,
        "wall_net_raw": fmt(raw_net),
        "wall_net_corrected": fmt(net_corr),
        "stat_err": fmt(stat),
        "sys_bg_err": fmt(sy),
        "dead_time_pct": fmt(dp, 4),
        "bg_method": method,
        "notes": "; ".join(notes),
    }


def main() -> None:
    dead_pct = load_dead_pct()

    rows_out: list[dict] = []
    with PHASE0.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            fn = clean_filename(r.get("filename") or "")
            if mc.is_pf_d2_mca(fn):
                continue
            raw_s = (r.get("wall_net_cps") or "").strip()
            raw_net = float(raw_s) if raw_s else float("nan")
            rows_out.append(build_row(r["検出器"], r["地点"], fn, raw_net, dead_pct))

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows_out)

    print(f"wrote {OUT_CSV} ({len(rows_out)} rows)")


if __name__ == "__main__":
    main()
