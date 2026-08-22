#!/usr/bin/env python3
"""黒鉛パイル（熱中性子管理棟）データから He-3 検出器の効率を求め、各測定点のフラックスを推定する。

参照: 米内ほか, 保健物理 37(2) 118–127 (2002) [JHPS 37_118]
  - 241Am-Be 源強度 Q = 2.26×10^6 n/s (±3%)
  - 黒鉛パイル外部（校正版 A 点）の熱中性子束:
      φ/Q = 9.44×10^-6 n/(s·cm²·source neutron)
  - 外部は Cd カットオフ (0.56 eV) 以下 ≈ 熱中性子、非熱寄与 <1%

幾何:
  - 黒鉛半幅 R_half [cm]: 中心〜表面（デフォルト 95 cm = 190 cm 幅の KEK パイル）
    ※ 1/(R_half+d)² スケールで d1 の 30/80 cm 計数比 (≈2.0) と整合
  - 表面からの距離 d [cm]（ファイル名の 30, 80）
  - φ(d) = (φ/Q)_ref × Q × ((R_half+d_ref)/(R_half+d))²
    d_ref=30 cm を論文 A 点相当とする
"""

from __future__ import annotations

import csv
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from mca_common import analyze_roi, parse_mca  # noqa: E402

# detector_specs（He-3 管ジオメトリ）
SIM_ROOT = ROOT.parent / "04_PHITS_sim" / "equiv_concrete_sites"
sys.path.insert(0, str(SIM_ROOT))
from detector_specs import DETECTORS  # noqa: E402

MEAS_DIR = ROOT / "測定_20260818"
RAW = MEAS_DIR / "raw"
TABLES = MEAS_DIR / "tables"

# --- 文献パラメータ（Yonai et al. 2002）---
Q_AMBE_DEFAULT = 2.26e6  # n/s
PHI_OVER_Q_REF = 9.44e-6  # n/(s·cm²·Q) at d_ref from surface
D_REF_CM = 30.0
R_HALF_DEFAULT = 95.0  # KEK パイル半幅 190/2 cm
D2_D2_DISTANCE_CM = 400.0  # D2/d2: 黒鉛から 400 cm、PE 緩衝のみ（黒鉛なし）


@dataclass
class CountResult:
    filename: str
    detector: str
    serial: str
    dist_cm: float | None
    live_s: float
    dead_frac: float
    rate_total: float
    rate_total_err: float
    rate_roi_net: float
    rate_roi_net_err: float
    roi_lo: int
    roi_hi: int
    saturated: bool
    notes: str


def detector_key_from_name(name: str, serial: str) -> str:
    low = name.lower()
    if "d2" in low or name.startswith("D2") or "_d2" in low:
        return "d2" if serial == "2162" else "D2"
    if "d1" in low or name.startswith("D1") or "_d1" in low:
        return "d1" if serial == "2162" else "D1"
    if serial == "2162":
        return "d1"
    if serial == "1715":
        return "D1"
    return "?"


def parse_distance_cm(stem: str) -> float | None:
    m = re.search(r"(\d+)cm", stem)
    return float(m.group(1)) if m else None


def count_rates(path: Path) -> CountResult:
    m = parse_mca(path)
    c = np.asarray(m["counts"], dtype=float)
    live = float(m["LIVE_TIME"])
    real = float(m["REAL_TIME"])
    dead = max(0.0, 1.0 - live / real) if real > 0 else 0.0
    serial = infer_serial(path.name, str(m.get("serial") or ""))

    ch0_frac = c[0] / max(c.sum(), 1.0)
    saturated = dead > 0.15 or (ch0_frac > 0.3 and dead > 0.05)

    if ch0_frac > 0.3:
        use = c[1:]
        tag = "ch1+"
    else:
        use = c
        tag = "all"

    total = float(use.sum())
    rate = total / live
    rate_err = math.sqrt(max(total, 0.0)) / live

    roi = analyze_roi(m["counts"], serial=serial)
    rate_roi = roi.net / live
    rate_roi_err = roi.err / live

    det = detector_key_from_name(path.stem, serial)
    dist = parse_distance_cm(path.stem)
    notes = f"count={tag}"
    if saturated:
        notes += "; dead time 大/ch0 飽和 — 定量用非推奨"

    return CountResult(
        filename=path.name,
        detector=det,
        serial=serial,
        dist_cm=dist,
        live_s=live,
        dead_frac=dead,
        rate_total=rate,
        rate_total_err=rate_err,
        rate_roi_net=rate_roi,
        rate_roi_net_err=rate_roi_err,
        roi_lo=roi.roi_lo,
        roi_hi=roi.roi_hi,
        saturated=saturated,
        notes=notes + (f"; {roi.warning}" if roi.warning else ""),
    )


def dead_time_correct(rate: float, dead_frac: float) -> float:
    if dead_frac >= 0.99:
        return float("nan")
    return rate / (1.0 - dead_frac)


def thermal_flux(d_cm: float, q: float, r_half: float, d_ref: float = D_REF_CM) -> float:
    """表面から d_cm の熱中性子フラックス [n/cm²/s]。"""
    scale = ((r_half + d_ref) / (r_half + d_cm)) ** 2
    return PHI_OVER_Q_REF * q * scale


def geometric_areas(det_key: str) -> dict[str, float]:
    spec = DETECTORS.get(det_key)
    if spec is None:
        return {}
    r = spec.r_in_cm
    la = spec.active_length_cm
    return {
        "S_end_cm2": math.pi * r * r,
        "S_side_cm2": 2.0 * math.pi * r * la,
        "L_active_cm": la,
        "r_in_cm": r,
    }


def main() -> None:
    import argparse

    p = argparse.ArgumentParser(description="He-3 検出器効率・フラックス推定")
    p.add_argument("--q", type=float, default=Q_AMBE_DEFAULT, help="Am-Be 源強度 [n/s]")
    p.add_argument("--r-half", type=float, default=R_HALF_DEFAULT, help="黒鉛半幅 [cm]")
    p.add_argument(
        "--rate-mode",
        choices=("total", "roi"),
        default="total",
        help="効率較正に使う計数率（熱中性子場では total 推奨）",
    )
    args = p.parse_args()

    kanri_files = sorted(RAW.glob("*熱中性子管理棟*.mca"))
    cal_rows: list[CountResult] = [count_rates(f) for f in kanri_files]

    # --- 較正用（非飽和 & 距離ラベルあり）---
    usable = [
        r
        for r in cal_rows
        if (not r.saturated) and (r.dist_cm is not None) and r.detector in ("d1", "d2", "D1", "D2")
    ]

    def pick_rate(r: CountResult) -> float:
        return r.rate_roi_net if args.rate_mode == "roi" else r.rate_total

    eff: dict[str, dict] = {}

    print("=" * 72)
    print("熱中性子管理棟 — 較正データ")
    print(f"  文献: φ/Q = {PHI_OVER_Q_REF:.3e} n/(s·cm²·Q), Q = {args.q:.3e} n/s")
    print(f"  黒鉛半幅 R_half = {args.r_half} cm, d_ref = {D_REF_CM} cm")
    print(f"  計数率モード: {args.rate_mode}")
    print("=" * 72)

    for r in cal_rows:
        rc = dead_time_correct(pick_rate(r), r.dead_frac)
        d_show = r.dist_cm
        if d_show is None and r.detector in ("D2", "d2"):
            d_show = D2_D2_DISTANCE_CM
        phi = thermal_flux(d_show, args.q, args.r_half) if d_show is not None else float("nan")
        eps_s = rc / phi if d_show and phi > 0 and not math.isnan(rc) else float("nan")
        d_label = f"{d_show:g}" if d_show is not None else "-"
        print(
            f"{r.filename[:42]:42s} {r.detector:3s} d={d_label:>5s}cm "
            f"R={pick_rate(r):8.1f} R_corr={rc:8.1f} φ={phi:8.3f} εS={eps_s:7.1f} cm²  {r.notes}"
        )

    def calibrate_detector(det: str, pair: list[CountResult], *, default_d_cm: float = 80.0) -> None:
        if not pair:
            return
        eps_s_list: list[float] = []
        for r in pair:
            d = r.dist_cm if r.dist_cm is not None else default_d_cm
            rc = dead_time_correct(pick_rate(r), r.dead_frac)
            phi = thermal_flux(d, args.q, args.r_half)
            eps_s_list.append(rc / phi)
        eps_s_mean = float(np.mean(eps_s_list))
        eps_s_std = float(np.std(eps_s_list)) if len(eps_s_list) > 1 else 0.0
        geom = geometric_areas(det)
        s_end = geom.get("S_end_cm2", float("nan"))
        s_side = geom.get("S_side_cm2", float("nan"))
        # ROI 換算係数（較正点 = 30 cm があればそれ、なければ最初の点）
        ref = next((r for r in pair if r.dist_cm == 30.0), pair[0])
        pr = pick_rate(ref)
        f_roi = ref.rate_roi_net / pr if pr > 0 else float("nan")
        eff[det] = {
            "epsilon_S_cm2": eps_s_mean,
            "epsilon_S_std_cm2": eps_s_std,
            "epsilon_S_ROI_cm2": eps_s_mean * f_roi if not math.isnan(f_roi) else float("nan"),
            "f_roi_over_total": f_roi,
            "epsilon_end": eps_s_mean / s_end if s_end else float("nan"),
            "epsilon_side_norm": eps_s_mean / s_side if s_side else float("nan"),
            **geom,
        }

        if len(pair) >= 2 and {r.dist_cm for r in pair} >= {30.0, 80.0}:
            r30 = next(r for r in pair if r.dist_cm == 30.0)
            r80 = next(r for r in pair if r.dist_cm == 80.0)
            obs_ratio = dead_time_correct(pick_rate(r30), r30.dead_frac) / dead_time_correct(
                pick_rate(r80), r80.dead_frac
            )
            pred_ratio = thermal_flux(30.0, 1.0, args.r_half) / thermal_flux(80.0, 1.0, args.r_half)
            ratio_str = f"R30/R80 観測={obs_ratio:.2f}  予測={pred_ratio:.2f}"
        else:
            d0 = pair[0].dist_cm if pair[0].dist_cm is not None else default_d_cm
            ratio_str = f"単点較正 d={d0}cm"

        print(
            f"\n[{det}] ε×S(total) = {eps_s_mean:.1f} ± {eps_s_std:.1f} cm²  "
            f"ε×S(ROI) = {eff[det]['epsilon_S_ROI_cm2']:.1f} cm²  "
            f"(S_end={s_end:.1f}, S_side={s_side:.0f} cm²)"
        )
        print(f"      {ratio_str}")

    # 30/80 cm ペア
    for det in ("d1", "D1", "d2", "D2"):
        pair = [r for r in usable if r.detector == det and r.dist_cm in (30.0, 80.0)]
        if len(pair) >= 2:
            calibrate_detector(det, pair)

    # D2/d2: ファイル名に距離なし → 400 cm 固定（PE 緩衝・黒鉛なし）
    for det in ("D2", "d2"):
        if det in eff:
            continue
        singles = [r for r in cal_rows if r.detector == det and not r.saturated]
        if singles:
            calibrate_detector(det, [singles[-1]], default_d_cm=D2_D2_DISTANCE_CM)

    # --- 全測定のフラックス ---
    record_csv = TABLES / "測定記録.csv"
    rows_out = []
    with record_csv.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        all_recs = list(reader)

    for rec in all_recs:
        fn = rec.get("filename", "")
        path = RAW / fn
        serial = rec.get("シリアル", "")
        det = detector_key_from_name(fn, serial)
        rate_roi = float(rec["roi_net_cps"])
        rate_roi_err = float(rec["roi_net_cps_err"])

        eff_row = eff.get(det, {})
        eps_s = eff_row.get("epsilon_S_cm2")
        eps_s_roi = eff_row.get("epsilon_S_ROI_cm2") or eps_s
        if eps_s_roi and eps_s_roi > 0:
            flux_roi = rate_roi / eps_s_roi
            flux_roi_err = rate_roi_err / eps_s_roi
        else:
            flux_roi = flux_roi_err = float("nan")

        rows_out.append(
            {
                "id": rec["id"],
                "場所": rec["場所"],
                "filename": fn,
                "検出器": det,
                "シリアル": serial,
                "ROI_net_CPS": f"{rate_roi:.6g}",
                "ROI_net_CPS_err": f"{rate_roi_err:.6g}",
                "epsilon_S_cm2": f"{eps_s:.4g}" if eps_s else "",
                "epsilon_S_ROI_cm2": (
                    f"{eps_s_roi:.4g}" if eps_s_roi and not math.isnan(float(eps_s_roi)) else ""
                ),
                "phi_ROI_n_cm2_s": f"{flux_roi:.6g}" if not math.isnan(flux_roi) else "",
                "phi_ROI_err": f"{flux_roi_err:.6g}" if not math.isnan(flux_roi_err) else "",
                "備考": (
                    f"熱中性子校正版 φ/Q=9.44e-6, Q={args.q:.3g}, R_half={args.r_half:g}cm; "
                    f"D2/d2={D2_D2_DISTANCE_CM:g}cm"
                ),
            }
        )

    out_eff = TABLES / "検出器効率_熱中性子校正版.csv"
    out_flux = TABLES / "フラックス_熱中性子校正版.csv"

    with out_eff.open("w", newline="", encoding="utf-8") as f:
        fields = [
            "検出器",
            "epsilon_S_cm2",
            "epsilon_S_std_cm2",
            "epsilon_S_ROI_cm2",
            "f_roi_over_total",
            "epsilon_S_end",
            "epsilon_S_side_norm",
            "S_end_cm2",
            "S_side_cm2",
            "L_active_cm",
            "r_in_cm",
            "Q_n_s",
            "R_half_cm",
            "phi_over_Q",
            "rate_mode",
            "備考",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for det, e in eff.items():
            w.writerow(
                {
                    "検出器": det,
                    "epsilon_S_cm2": f"{e['epsilon_S_cm2']:.4g}",
                    "epsilon_S_std_cm2": f"{e['epsilon_S_std_cm2']:.4g}",
                    "epsilon_S_ROI_cm2": f"{e.get('epsilon_S_ROI_cm2', float('nan')):.4g}",
                    "f_roi_over_total": f"{e.get('f_roi_over_total', float('nan')):.4g}",
                    "epsilon_S_end": f"{e['epsilon_end']:.4g}",
                    "epsilon_S_side_norm": f"{e['epsilon_side_norm']:.4g}",
                    "S_end_cm2": f"{e.get('S_end_cm2', 0):.3g}",
                    "S_side_cm2": f"{e.get('S_side_cm2', 0):.3g}",
                    "L_active_cm": f"{e.get('L_active_cm', 0):.3g}",
                    "r_in_cm": f"{e.get('r_in_cm', 0):.3g}",
                    "Q_n_s": f"{args.q:.6g}",
                    "R_half_cm": f"{args.r_half:g}",
                    "phi_over_Q": f"{PHI_OVER_Q_REF:.6g}",
                    "rate_mode": args.rate_mode,
                    "備考": (
                        "d1: 30&80cm 非飽和平均。D2/d2: 400cm 単点。D1 飽和は除外。"
                    ),
                }
            )

    with out_flux.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
        w.writeheader()
        w.writerows(rows_out)

    print(f"\n出力: {out_eff}")
    print(f"出力: {out_flux}")


if __name__ == "__main__":
    main()
