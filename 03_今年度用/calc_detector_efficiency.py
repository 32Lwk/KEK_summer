#!/usr/bin/env python3
"""黒鉛パイル（熱中性子管理棟）データから He-3 検出器の効率を求め、各測定点のフラックスを推定する。

参照: 米内ほか, 保健物理 37(2) 118–127 (2002)
  - 241Am-Be 源強度 Q = 2.26×10^6 n/s（本測定と同じ源）
  - 黒鉛パイル 190×250×190 cm（半幅 R_half = 95 cm）
  - 外部校正点の熱中性子束 φ/Q = 9.44×10^-6 n/(s·cm²·Q)

較正に使う測定（絶対効率）:
  - 裸管の εS_total はメーカー感度（d1=123, D1=450 cps/nv、公称 ±5%）
  - 黒鉛パイルは窓比 f = R_window/R_total のみ（d1 @ 30/80 cm）
  - D1 は 450 × d1 の窓比 → `calc_D1_efficiency_transfer.py`

使わない / 別扱い:
  - D1 パイル … 主結果はメーカー感度（パイルは照合のみ）
  - D2/d2 @ 400 cm … 黒鉛なし・線源〜検出器の直線距離 400 cm・Am-Be + PE
    → 熱中性子 φ(d) 公式は適用不可（PE 効果の相対比較用）
  - 現場の絶対 φ はメーカー整合の εS_wall。D2/d2 は地点間相対比較。

MCA はピーク積算モードのため dead time は較正判定・補正に使わない
（計数率は net/LIVE_TIME）。
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
from mca_common import analyze_roi, infer_serial, is_pf_d2_mca, parse_mca  # noqa: E402

SIM_ROOT = ROOT.parent / "04_PHITS_sim" / "equiv_concrete_sites"
sys.path.insert(0, str(SIM_ROOT))
from detector_specs import DETECTORS, he3_geometric_areas  # noqa: E402

MEAS_DIR = ROOT / "測定_20260818"
RAW = MEAS_DIR / "raw"
TABLES = MEAS_DIR / "tables"

# --- 文献・施設パラメータ ---
Q_AMBE = 2.26e6  # n/s（論文と同じ源）
PHI_OVER_Q = 9.44e-6  # n/(s·cm²·Q) at d_ref
D_REF_CM = 30.0
R_HALF_CM = 95.0  # 190 cm 幅の半幅
D2_PE_DISTANCE_CM = 400.0  # 線源〜検出器の直線距離（黒鉛なし・PE 効果確認）


@dataclass
class CountResult:
    filename: str
    detector: str
    serial: str
    dist_cm: float | None
    orientation: str  # horizontal | vertical | unknown
    graphite: bool | None  # None = unknown
    live_s: float
    dead_frac: float
    ch0_frac: float
    rate_total: float  # ch0 除外済みの場合あり
    rate_roi_net: float
    rate_roi_net_err: float
    overflow_ch0: bool
    saturated: bool
    notes: str


def detector_key(name: str, serial: str) -> str:
    low = name.lower()
    sn = str(serial)
    is_small = sn in ("2162", "2162")
    if "d2" in low or name.startswith("D2") or re.search(r"(^|_)D2($|_)", name):
        if sn in ("1715", "1715") or name.startswith("D2") or re.search(r"(^|_)D2($|_)", name):
            if re.search(r"(^|_)d2($|_)", name) or name.startswith("d2"):
                return "d2"
            return "D2"
        return "d2" if is_small else "D2"
    if re.search(r"(^|_)d2($|_)", name) or name.startswith("d2"):
        return "d2"
    if re.search(r"(^|_)D1($|_)", name) or name.startswith("D1"):
        return "D1"
    if re.search(r"(^|_)d1($|_)", name) or name.startswith("d1"):
        return "d1"
    if sn in ("2162",):
        return "d1"
    if sn in ("1715",):
        return "D1"
    return "?"


def parse_distance_cm(stem: str) -> float | None:
    m = re.search(r"(\d+)\s*cm", stem, re.I)
    return float(m.group(1)) if m else None


def geometry_meta(det: str, dist: float | None) -> tuple[str, bool | None]:
    """向き・黒鉛有無（ユーザー確認済み）。"""
    if det in ("d1", "D1") and dist in (30.0, 80.0):
        return "horizontal", True
    if det in ("d2", "D2") and (dist is None or dist == D2_PE_DISTANCE_CM):
        return "vertical", False  # 黒鉛なし・線源距離 400 cm・PE 効果確認
    return "unknown", None


def count_rates(path: Path) -> CountResult:
    m = parse_mca(path)
    c = np.asarray(m["counts"], dtype=float)
    live = float(m["LIVE_TIME"])
    real = float(m["REAL_TIME"])
    dead = max(0.0, 1.0 - live / real) if real > 0 else 0.0
    serial = infer_serial(path.name, str(m.get("serial") or ""))

    tot = float(c.sum())
    ch0_frac = float(c[0] / tot) if tot > 0 else 0.0
    overflow_ch0 = ch0_frac > 0.05  # 5% 超で ch0 溜まりありとみなす
    # MCA ピーク積算モードのため dead time では飽和判定しない（ch0 過多のみ）
    saturated = ch0_frac > 0.25

    if ch0_frac > 0.05:
        use = c[1:]
        tag = "ch1+"
    else:
        use = c
        tag = "all"

    rate_total = float(use.sum()) / live
    roi = analyze_roi(m["counts"], serial=serial)
    rate_roi = roi.net / live
    rate_roi_err = roi.err / live

    det = detector_key(path.stem, serial)
    dist = parse_distance_cm(path.stem)
    if det in ("D2", "d2") and dist is None:
        dist = D2_PE_DISTANCE_CM
    orient, graphite = geometry_meta(det, dist)

    notes = f"count={tag}; orient={orient}; graphite={'yes' if graphite else 'no' if graphite is False else '?'}"
    if overflow_ch0:
        notes += f"; ch0={ch0_frac*100:.1f}%"
    if saturated:
        notes += "; ch0過多 — 絶対較正はメーカー優先"

    return CountResult(
        filename=path.name,
        detector=det,
        serial=serial,
        dist_cm=dist,
        orientation=orient,
        graphite=graphite,
        live_s=live,
        dead_frac=dead,
        ch0_frac=ch0_frac,
        rate_total=rate_total,
        rate_roi_net=rate_roi,
        rate_roi_net_err=rate_roi_err,
        overflow_ch0=overflow_ch0,
        saturated=saturated,
        notes=notes,
    )


def dead_time_correct(rate: float, dead_frac: float) -> float:
    """計数率はすでに net/LIVE_TIME。MCA ピーク積算モードのため DT 補正はしない。"""
    return rate


def thermal_flux(d_cm: float, q: float = Q_AMBE, r_half: float = R_HALF_CM) -> float:
    """黒鉛表面から d_cm の熱中性子フラックス [n/cm²/s]（黒鉛ありの場合のみ）。"""
    scale = ((r_half + D_REF_CM) / (r_half + d_cm)) ** 2
    return PHI_OVER_Q * q * scale


def geometric_areas(det_key: str) -> dict[str, float]:
    """He-3 感知面積（detector_specs.he3_geometric_areas に委譲）。"""
    return he3_geometric_areas(det_key)


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser(description="He-3 検出器効率・フラックス推定")
    ap.add_argument("--q", type=float, default=Q_AMBE)
    ap.add_argument("--r-half", type=float, default=R_HALF_CM)
    ap.add_argument("--rate-mode", choices=("total", "roi"), default="total")
    args = ap.parse_args()

    files = sorted(RAW.glob("*熱中性子管理棟*.mca"))
    if not files:
        # 全角アンダースコア等のファイル名揺れに対応
        files = sorted(p for p in RAW.glob("*.mca") if "熱中性子管理棟" in p.name)
    cal_rows = [count_rates(f) for f in files]

    def pick_rate(r: CountResult) -> float:
        return r.rate_roi_net if args.rate_mode == "roi" else r.rate_total

    print("=" * 72)
    print("熱中性子管理棟 — 較正データ")
    print(f"  φ/Q = {PHI_OVER_Q:.3e}, Q = {args.q:.3e} n/s, R_half = {args.r_half} cm")
    print("  絶対較正: d1 @ 30/80 cm（水平・黒鉛あり）のみ")
    print("  D2/d2 @ 400 cm: 線源〜検出器直線距離・黒鉛なし → PE 相対比較のみ（ε×S なし）")
    print("  方針: 絶対 φ は d1（パイル）+ D1（メーカー感度スケール）/ D2・d2 は相対比較")
    print("=" * 72)

    for r in cal_rows:
        rc = dead_time_correct(pick_rate(r), r.dead_frac)
        if r.graphite and r.dist_cm is not None:
            phi = thermal_flux(r.dist_cm, args.q, args.r_half)
            eps_s = rc / phi if phi > 0 else float("nan")
            phi_s = f"{phi:8.3f}"
            eps_s_s = f"{eps_s:7.1f}"
        else:
            phi_s = "   n/a  "
            eps_s_s = "  n/a  "
        d_label = f"{r.dist_cm:g}" if r.dist_cm is not None else "-"
        print(
            f"{r.filename[:42]:42s} {r.detector:3s} d={d_label:>5s}cm "
            f"R={pick_rate(r):8.1f} R_corr={rc:8.1f} φ={phi_s} εS={eps_s_s}  {r.notes}"
        )

    # --- 絶対較正: d1 のみ ---
    eff: dict[str, dict] = {}
    d1_pair = [
        r
        for r in cal_rows
        if r.detector == "d1"
        and r.dist_cm in (30.0, 80.0)
        and r.graphite
        and not r.saturated
    ]
    if len(d1_pair) >= 2:
        mfr = DETECTORS["d1"].manufacturer_sensitivity_cps_nv
        ref = next(r for r in d1_pair if r.dist_cm == 30.0)
        f_roi = ref.rate_roi_net / ref.rate_total if ref.rate_total > 0 else float("nan")
        pile_eps = [
            dead_time_correct(pick_rate(r), r.dead_frac)
            / thermal_flux(r.dist_cm, args.q, args.r_half)  # type: ignore[arg-type]
            for r in d1_pair
        ]
        pile_mean = float(np.mean(pile_eps))
        pile_std = float(np.std(pile_eps))
        geom = geometric_areas("d1")
        s_iso = geom["S_he3_isotropic_cm2"]
        eff["d1"] = {
            "epsilon_S_cm2": mfr,
            "epsilon_S_std_cm2": 0.05 * mfr,
            "epsilon_S_ROI_cm2": mfr * f_roi,
            "f_roi_over_total": f_roi,
            "epsilon_end": mfr / geom["S_end_cm2"],
            "epsilon_side_norm": mfr / geom["S_side_cm2"],
            **geom,
            "note": (
                f"メーカー {mfr:.0f} cps/nv（±5%）· パイルは f_ROI={f_roi:.3f} のみ"
                f"（R/φ照合 {pile_mean:.1f}±{pile_std:.1f}）"
            ),
        }
        r30 = next(r for r in d1_pair if r.dist_cm == 30.0)
        r80 = next(r for r in d1_pair if r.dist_cm == 80.0)
        obs = dead_time_correct(pick_rate(r30), r30.dead_frac) / dead_time_correct(
            pick_rate(r80), r80.dead_frac
        )
        pred = thermal_flux(30.0, 1.0, args.r_half) / thermal_flux(80.0, 1.0, args.r_half)
        print(
            f"\n[d1] ε×S(total) = {mfr:.1f} cm²（メーカー ±5%）  "
            f"ε×S(ROI) = {mfr * f_roi:.1f} cm²  f_ROI={f_roi:.3f}"
        )
        print(
            f"     S_iso=S_surf/4 = {s_iso:.1f} cm²  ε_mfr={mfr/s_iso:.3f}"
        )
        print(
            f"     照合 パイル R/φ = {pile_mean:.1f} ± {pile_std:.1f} cm²"
            f"（点束×長い円筒のためメーカーとは比較しない）"
        )
        print(f"     R30/R80 観測={obs:.2f}  予測={pred:.2f}（水平・黒鉛あり）")
    else:
        print("\n[警告] d1 の 30/80 cm ペアが不足 — 絶対較正不可")

    # --- PE 効果（黒鉛なし・400 cm）相対比較 ---
    print("\n" + "-" * 72)
    print("PE 効果確認（線源〜検出器 400 cm・黒鉛なし・管軸垂直）— 絶対 φ は未定義")
    pe_rows = [r for r in cal_rows if r.detector in ("D2", "d2") and r.graphite is False]
    by_det = {r.detector: r for r in pe_rows}
    for det in ("D2", "d2"):
        r = by_det.get(det)
        if not r:
            print(f"  [{det}] データなし")
            continue
        rc = dead_time_correct(r.rate_total, r.dead_frac)
        print(
            f"  [{det}] R_total={r.rate_total:.2f} s⁻¹ (corr={rc:.2f})  "
            f"ROI={r.rate_roi_net:.2f}  dead={r.dead_frac*100:.1f}%  "
            f"ch0={r.ch0_frac*100:.1f}%  {'⚠ ch0溢' if r.overflow_ch0 else 'ch0 OK'}"
        )
    if "D2" in by_det and "d2" in by_det:
        rd = dead_time_correct(by_det["D2"].rate_total, by_det["D2"].dead_frac)
        rs = dead_time_correct(by_det["d2"].rate_total, by_det["d2"].dead_frac)
        print(f"  D2/d2 計数比 = {rd/rs:.2f}（幾何側面積比 ≈ 3.4 と比較用）")
        print("  ※ Am-Be 高速中性子 + PE 減速場。熱中性子 ε×S には使わない。")

    # D1 パイルは照合のみ（主結果はメーカー）
    d1_pile = [r for r in cal_rows if r.detector == "D1" and r.dist_cm in (30.0, 80.0)]
    if d1_pile:
        print("\n[D1] パイルは照合のみ（MCA ピーク積算のため DT は不問）")
        print("     → calc_D1_efficiency_transfer.py（メーカー 450 cps/nv × d1 窓比）")

    # 既存の転送較正 D1 / d2 / D2 行を保持（本スクリプト再実行で消さない）
    d1_transfer: dict[str, str] | None = None
    d2_transfer: dict[str, str] | None = None
    D2_transfer: dict[str, str] | None = None
    eff_existing = TABLES / "検出器効率_熱中性子校正版.csv"
    if eff_existing.exists():
        for r in csv.DictReader(eff_existing.open(encoding="utf-8")):
            det = r.get("検出器")
            if det == "D1" and (r.get("epsilon_S_ROI_cm2") or "").strip():
                d1_transfer = r
            if det == "d2" and (r.get("epsilon_S_ROI_cm2") or "").strip():
                d2_transfer = r
            if det == "D2" and (r.get("epsilon_S_ROI_cm2") or "").strip():
                D2_transfer = r

    # --- 現場フラックス（主窓 191–764 keV）---
    eff_wall_path = TABLES / "検出器効率_壁効果191_764keV.csv"
    eps_wall: dict[str, float] = {"d1": 109.5, "D1": 400.7}
    if eff_wall_path.exists():
        for r in csv.DictReader(eff_wall_path.open(encoding="utf-8")):
            det = (r.get("検出器") or "").strip()
            v = (r.get("epsilon_S_wall_cm2") or "").strip()
            if det in eps_wall and v:
                eps_wall[det] = float(v)

    record_csv = TABLES / "測定記録.csv"
    rows_out = []
    with record_csv.open(encoding="utf-8") as f:
        recs = list(csv.DictReader(f))

    # d2 / D2 wall 転送（build_flux_summary と同じ方針）
    def _wall_cps(recs_list, det: str, site_key: str) -> float | None:
        from build_flux_summary import detector_key as dk, site_label as sl, prefer_score as ps

        best = None
        best_score = -1.0
        for rec in recs_list:
            fn = rec.get("filename") or ""
            serial = str(rec.get("シリアル") or "")
            if dk(fn, serial) != det:
                continue
            place = rec.get("場所") or ""
            if sl(place, fn) != site_key:
                continue
            if str(rec.get("wall_net_valid", "1")) in ("0", "False", "false"):
                continue
            try:
                cps = float(rec["wall_net_cps"])
            except (KeyError, ValueError):
                continue
            if cps <= 0:
                continue
            live = float(rec.get("live_s") or 0)
            sc = ps(fn, live)
            if sc > best_score:
                best_score = sc
                best = cps
        return best

    d1_g = _wall_cps(recs, "D1", "地上")
    d2_g = _wall_cps(recs, "d2", "地上")
    if d1_g and d2_g and "D1" in eps_wall:
        eps_wall["d2"] = eps_wall["D1"] * d2_g / d1_g
    d1_l = _wall_cps(recs, "D1", "linac")
    d2_l = _wall_cps(recs, "D2", "linac")
    if d1_l and d2_l and "D1" in eps_wall:
        eps_wall["D2"] = eps_wall["D1"] * d2_l / d1_l

    for rec in recs:
        fn = rec.get("filename") or rec.get("ファイル名") or ""
        if is_pf_d2_mca(fn):
            continue
        serial = str(rec.get("シリアル") or "")
        det = detector_key(fn, serial)
        rate_wall = float(rec.get("wall_net_cps") or 0)
        rate_wall_err = float(rec.get("wall_net_cps_err") or 0)
        wall_valid = str(rec.get("wall_net_valid", "1")) not in ("0", "False", "false")
        rate_peak = float(rec.get("roi_net_cps") or 0)
        rate_peak_err = float(rec.get("roi_net_cps_err") or 0)

        eps = None
        note = ""
        if det == "d1" and "d1" in eff:
            eps = eps_wall.get("d1")
            note = "d1 熱中性子絶対較正（黒鉛 30/80 cm）· 191–764 keV"
        elif det == "D1" and d1_transfer:
            eps = eps_wall.get("D1")
            note = "D1 メーカー450 cps/nv × d1 wall/total · 191–764 keV"
        elif det == "d2" and eps_wall.get("d2"):
            eps = eps_wall["d2"]
            note = "d2 転送較正（地上 d2/D1×D1εS_wall）· 191–764 keV"
        elif det == "D2" and eps_wall.get("D2"):
            eps = eps_wall["D2"]
            note = "D2 転送較正（linac D2/D1×D1εS_wall；地上 wall NET≤0）· 191–764 keV"
        elif det in ("D1", "D2", "d2"):
            note = (
                "絶対効率未確定・相対比較のみ"
                + ("（D1: calc_D1_efficiency_transfer.py を実行）" if det == "D1" else "")
                + ("（d2: calc_d2_efficiency_transfer.py を実行）" if det == "d2" else "")
                + ("（D2: calc_D2_efficiency_transfer.py を実行）" if det == "D2" else "")
            )

        if eps and eps > 0 and wall_valid and rate_wall > 0:
            phi = rate_wall / eps
            phi_err = rate_wall_err / eps
        else:
            phi = phi_err = float("nan")

        rows_out.append(
            {
                "id": rec.get("id", ""),
                "場所": rec.get("場所", ""),
                "filename": fn,
                "検出器": det,
                "シリアル": serial,
                "NET_CPS_191_764keV": f"{rate_wall:.6g}" if wall_valid else "",
                "NET_CPS_191_764keV_err": f"{rate_wall_err:.6g}" if wall_valid else "",
                "peak_ROI_net_CPS": f"{rate_peak:.6g}",
                "peak_ROI_net_CPS_err": f"{rate_peak_err:.6g}",
                "epsilon_S_191_764_cm2": f"{eps:.4g}" if eps else "",
                "phi_191_764_n_cm2_s": f"{phi:.6g}" if not math.isnan(phi) else "",
                "phi_191_764_err": f"{phi_err:.6g}" if not math.isnan(phi_err) else "",
                "備考": note,
            }
        )

    out_eff = TABLES / "検出器効率_熱中性子校正版.csv"
    out_flux = TABLES / "フラックス_熱中性子校正版.csv"
    out_pe = TABLES / "PE効果確認_400cm_黒鉛なし.csv"

    with out_eff.open("w", newline="", encoding="utf-8") as f:
        fields = [
            "検出器",
            "epsilon_S_cm2",
            "epsilon_S_std_cm2",
            "epsilon_S_ROI_cm2",
            "f_roi_over_total",
            "r_he3_cm",
            "l_sensitive_cm",
            "S_he3_projected_cm2",
            "S_he3_lateral_cm2",
            "S_he3_end_cm2",
            "S_he3_horizontal_cm2",
            "S_end_cm2",
            "S_side_cm2",
            "Q_n_s",
            "R_half_cm",
            "phi_over_Q",
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
                    "epsilon_S_ROI_cm2": f"{e['epsilon_S_ROI_cm2']:.4g}",
                    "f_roi_over_total": f"{e['f_roi_over_total']:.4g}",
                    "r_he3_cm": f"{e.get('r_he3_cm', e.get('r_in_cm', '')):.3g}",
                    "l_sensitive_cm": f"{e.get('l_sensitive_cm', e.get('L_active_cm', '')):.3g}",
                    "S_he3_projected_cm2": f"{e.get('S_he3_projected_cm2', ''):.3g}",
                    "S_he3_lateral_cm2": f"{e.get('S_he3_lateral_cm2', e.get('S_side_cm2', '')):.3g}",
                    "S_he3_end_cm2": f"{e.get('S_he3_end_cm2', e.get('S_end_cm2', '')):.3g}",
                    "S_he3_horizontal_cm2": f"{e.get('S_he3_horizontal_cm2', ''):.3g}",
                    "S_end_cm2": f"{e['S_end_cm2']:.3g}",
                    "S_side_cm2": f"{e['S_side_cm2']:.3g}",
                    "Q_n_s": f"{args.q:.6g}",
                    "R_half_cm": f"{args.r_half:g}",
                    "phi_over_Q": f"{PHI_OVER_Q:.6g}",
                    "備考": e["note"],
                }
            )
        # D1: 転送較正があれば保持、なければ未較正メモ
        if d1_transfer:
            row = {k: d1_transfer.get(k, "") for k in fields}
            row["検出器"] = "D1"
            row["Q_n_s"] = f"{args.q:.6g}"
            row["R_half_cm"] = f"{args.r_half:g}"
            row["phi_over_Q"] = f"{PHI_OVER_Q:.6g}"
            w.writerow(row)
            d1_note_written = True
        else:
            d1_note_written = False
        if d2_transfer:
            row = {k: d2_transfer.get(k, "") for k in fields}
            row["検出器"] = "d2"
            row["Q_n_s"] = f"{args.q:.6g}"
            row["R_half_cm"] = f"{args.r_half:g}"
            row["phi_over_Q"] = f"{PHI_OVER_Q:.6g}"
            w.writerow(row)
            d2_note_written = True
        else:
            d2_note_written = False
        if D2_transfer:
            row = {k: D2_transfer.get(k, "") for k in fields}
            row["検出器"] = "D2"
            row["Q_n_s"] = f"{args.q:.6g}"
            row["R_half_cm"] = f"{args.r_half:g}"
            row["phi_over_Q"] = f"{PHI_OVER_Q:.6g}"
            w.writerow(row)
            D2_note_written = True
        else:
            D2_note_written = False
        for det, note in (
            (
                "D1",
                "未較正: 30/80cm 飽和 → calc_D1_efficiency_transfer.py を実行",
            ),
            ("D2", "未較正: 地上 D2/D1 転送 → calc_D2_efficiency_transfer.py を実行"),
            ("d2", "未較正: 地上 d2/D1 転送 → calc_d2_efficiency_transfer.py を実行"),
        ):
            if det == "D1" and d1_note_written:
                continue
            if det == "d2" and d2_note_written:
                continue
            if det == "D2" and D2_note_written:
                continue
            w.writerow(
                {
                    "検出器": det,
                    "epsilon_S_cm2": "",
                    "epsilon_S_std_cm2": "",
                    "epsilon_S_ROI_cm2": "",
                    "f_roi_over_total": "",
                    "S_end_cm2": "",
                    "S_side_cm2": "",
                    "Q_n_s": f"{args.q:.6g}",
                    "R_half_cm": f"{args.r_half:g}",
                    "phi_over_Q": f"{PHI_OVER_Q:.6g}",
                    "備考": note,
                }
            )

    with out_flux.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
        w.writeheader()
        w.writerows(rows_out)

    with out_pe.open("w", newline="", encoding="utf-8") as f:
        fields = [
            "検出器",
            "距離_cm",
            "黒鉛",
            "向き",
            "live_s",
            "dead_pct",
            "ch0_frac",
            "rate_total_cps",
            "rate_roi_cps",
            "備考",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for det in ("D2", "d2"):
            r = by_det.get(det)
            if not r:
                continue
            w.writerow(
                {
                    "検出器": det,
                    "距離_cm": D2_PE_DISTANCE_CM,
                    "黒鉛": "なし",
                    "向き": "vertical",
                    "live_s": f"{r.live_s:.3f}",
                    "dead_pct": f"{r.dead_frac*100:.2f}",
                    "ch0_frac": f"{r.ch0_frac:.4f}",
                    "rate_total_cps": f"{r.rate_total:.4f}",
                    "rate_roi_cps": f"{r.rate_roi_net:.4f}",
                    "備考": r.notes,
                }
            )

    print(f"\n出力: {out_eff}")
    print(f"出力: {out_flux}")
    print(f"出力: {out_pe}")


if __name__ == "__main__":
    main()
