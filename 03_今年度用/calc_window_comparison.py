#!/usr/bin/env python3
"""ピーク ROI と壁効果窓（191–764 keV）の二系統解析を並べて出力する。

出力:
  tables/窓比較_計数率.csv
  tables/検出器効率_壁効果191_764keV.csv
  tables/フラックス_窓比較.csv
  tables/D1効率_転送較正_壁効果.csv
"""

from __future__ import annotations

import csv
import math
import re
from pathlib import Path

import numpy as np

from flux_calibration import compute_wall_efficiencies, write_wall_efficiencies_csv
from mca_common import (
    analyze_roi,
    analyze_wall_window,
    analyze_wall_window_linear,
    infer_serial,
    is_pf_d2_mca,
    parse_mca_for_analysis,
)

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "測定_20260818" / "raw"
TABLES = ROOT / "測定_20260818" / "tables"
SIM_ROOT = ROOT.parent / "04_PHITS_sim" / "equiv_concrete_sites"
import sys

sys.path.insert(0, str(SIM_ROOT))
from detector_specs import DETECTORS, he3_geometric_areas  # noqa: E402

Q_AMBE = 2.26e6
PHI_OVER_Q = 9.44e-6
D_REF = 30.0
R_HALF = 95.0
F_ROI_D1 = 0.5614  # ピーク窓の ROI/total（total 換算用・壁窓には使わない）


def thermal_phi(d_cm: float) -> float:
    scale = ((R_HALF + D_REF) / (R_HALF + d_cm)) ** 2
    return PHI_OVER_Q * Q_AMBE * scale


def detector_key(name: str) -> str:
    stem = Path(name).stem
    if re.search(r"(^|_)D2($|_)", stem) or stem.startswith("D2"):
        return "D2"
    if re.search(r"(^|_)d2($|_)", stem) or stem.startswith("d2"):
        return "d2"
    if re.search(r"(^|_)D1($|_)", stem) or stem.startswith("D1"):
        return "D1"
    if re.search(r"(^|_)d1($|_)", stem) or stem.startswith("d1"):
        return "d1"
    return "?"


def site_label(name: str) -> str:
    s = name
    if "熱中性子" in s:
        if "30cm" in s:
            return "熱中性子_30cm"
        if "80cm" in s:
            return "熱中性子_80cm"
        if "gain" in s.lower() or "corse" in s.lower() or "coarse" in s.lower():
            return "熱中性子_gain調整"
        return "熱中性子_その他"
    if "地上" in s:
        return "地上"
    if "管理棟2" in s:
        return "管理棟2階"
    if "管理棟1" in s:
        return "管理棟1階"
    if "IRON" in s or "iron" in s.lower():
        return "linac_IRON"
    if "linac" in s.lower():
        return "linac"
    if re.search(r"(^|_)PF($|_)", s) or "_PF" in s:
        return "PF"
    if "BT" in s or "放射線" in s:
        return "放射線棟BT"
    if "KEKB" in s:
        return "KEKB"
    if "ep1" in s.lower() or "k2k" in s.lower():
        return "K2KBL"
    return "その他"


def analyze_file(path: Path) -> dict:
    m = parse_mca_for_analysis(path)
    c = np.asarray(m["counts"], dtype=float)
    live = float(m["LIVE_TIME"])
    real = float(m["REAL_TIME"])
    dead = max(0.0, 1.0 - live / real) if real > 0 else 0.0
    sn = infer_serial(path.name, str(m.get("serial") or ""))
    peak = analyze_roi(c, sn)
    wall = analyze_wall_window(c, sn)
    wall_lin = analyze_wall_window_linear(c, sn)
    wall_cps = wall.net / live if live else float("nan")
    wall_lin_cps = wall_lin.net / live if live else float("nan")
    return {
        "filename": path.name,
        "検出器": detector_key(path.name),
        "地点": site_label(path.name),
        "シリアル": sn,
        "live_s": live,
        "dead_frac": dead,
        "peak_lo": peak.roi_lo,
        "peak_hi": peak.roi_hi,
        "peak_ch": peak.roi_peak,
        "peak_net_cps": peak.net / live if live else float("nan"),
        "peak_net_cps_err": peak.err / live if live else float("nan"),
        "peak_valid": int(peak.net_valid),
        "wall_lo": wall.roi_lo,
        "wall_hi": wall.roi_hi,
        "wall_e_lo_kev": wall.e_lo_kev,
        "wall_e_hi_kev": wall.e_hi_kev,
        "wall_sb_lo_lo": wall_lin.sb_lo_lo,
        "wall_sb_lo_hi": wall_lin.sb_lo_hi,
        "wall_sb_hi_lo": wall.sb_hi_lo,
        "wall_sb_hi_hi": wall.sb_hi_hi,
        "wall_net_cps": wall_cps,
        "wall_net_cps_linear": wall_lin_cps,
        "wall_gross_cps": wall.gross / live if live else float("nan"),
        "wall_net_cps_err": wall.err / live if live else float("nan"),
        "wall_valid": int(wall.net_valid),
        "wall_valid_linear": int(wall_lin.net_valid),
        "wall_bg_mode": wall.bg_mode,
        "wall_bg_mode_linear": wall_lin.bg_mode,
        "ratio_wall_over_peak": (
            (wall.net / peak.net) if peak.net and peak.net > 0 else float("nan")
        ),
        "ratio_linear_over_right": (
            (wall_lin.net / wall.net) if wall.net and wall.net > 0 else float("nan")
        ),
        "peak_warning": peak.warning,
        "wall_warning": wall.warning,
        "total_cps": float(c.sum()) / live if live else float("nan"),
    }


def main() -> None:
    files = [p for p in sorted(RAW.glob("*.mca")) if not is_pf_d2_mca(p.name)]
    rows = [analyze_file(p) for p in files]

    out_rates = TABLES / "窓比較_計数率.csv"
    fields = list(rows[0].keys())
    with out_rates.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {out_rates}")

    # --- 背景方式比較（直線 vs 右のみ）---
    cmp_out = TABLES / "背景比較_wall窓.csv"
    cmp_fields = [
        "filename", "検出器", "地点",
        "wall_lo", "wall_sb_lo", "wall_sb_hi",
        "wall_bg_mode_linear",
        "wall_net_cps", "wall_net_cps_linear", "peak_net_cps",
        "wall_valid", "wall_valid_linear",
        "ratio_linear_over_right", "delta_cps",
    ]
    cmp_rows = []
    for r in rows:
        rt = r["wall_net_cps"]
        lin = r["wall_net_cps_linear"]
        delta = lin - rt if lin == lin and rt == rt else float("nan")
        cmp_rows.append({
            "filename": r["filename"],
            "検出器": r["検出器"],
            "地点": r["地点"],
            "wall_lo": r["wall_lo"],
            "wall_sb_lo": f"{r['wall_sb_lo_lo']}–{r['wall_sb_lo_hi']}" if r["wall_sb_lo_hi"] else "",
            "wall_sb_hi": f"{r['wall_sb_hi_lo']}–{r['wall_sb_hi_hi']}" if r["wall_sb_hi_hi"] else "",
            "wall_bg_mode_linear": r["wall_bg_mode_linear"],
            "wall_net_cps": f"{rt:.6g}" if rt == rt else "",
            "wall_net_cps_linear": f"{lin:.6g}" if lin == lin else "",
            "peak_net_cps": f"{r['peak_net_cps']:.6g}",
            "wall_valid": r["wall_valid"],
            "wall_valid_linear": r["wall_valid_linear"],
            "ratio_linear_over_right": f"{r['ratio_linear_over_right']:.4g}" if r["ratio_linear_over_right"] == r["ratio_linear_over_right"] else "",
            "delta_cps": f"{delta:.6g}" if delta == delta else "",
        })
    with cmp_out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cmp_fields)
        w.writeheader()
        w.writerows(cmp_rows)
    print(f"wrote {cmp_out}")

    key_sites = {"地上", "管理棟2階", "linac", "放射線棟BT", "PF", "KEKB"}
    print("\n--- 背景比較（施設測定・右のみ=主 / 直線=比較）---")
    for r in rows:
        if r["地点"] not in key_sites or r["検出器"] not in ("D1", "D2", "d1", "d2"):
            continue
        if "熱中性子" in r["filename"]:
            continue
        flag = ""
        if r["wall_valid"] and not r["wall_valid_linear"]:
            flag = " ★直線のみ NET≤0"
        elif not r["wall_valid"] and r["wall_valid_linear"]:
            flag = " ★右のみ NET≤0・直線は正"
        elif not r["wall_valid"] and not r["wall_valid_linear"]:
            flag = " ★両方 NET≤0"
        print(
            f"  {r['検出器']:2s} {r['地点']:10s}  "
            f"right={r['wall_net_cps']:.4g}  linear={r['wall_net_cps_linear']:.4g}  "
            f"peak={r['peak_net_cps']:.4g}  lin/right={r['ratio_linear_over_right']:.3g}{flag}"
        )

    # --- d1 パイル絶対較正（壁効果窓）---
    d1_pile = [
        r
        for r in rows
        if r["検出器"] == "d1"
        and r["地点"] in ("熱中性子_30cm", "熱中性子_80cm")
        and r["wall_valid"]
    ]
    for r in d1_pile:
        d = 30.0 if "30" in r["地点"] else 80.0
        phi = thermal_phi(d)
        tot = float(r.get("total_cps") or 0)
        f_w = r["wall_net_cps"] / tot if tot else float("nan")
        print(
            f"  d1 wall @{d:.0f}cm: CPS={r['wall_net_cps']:.2f}  total={tot:.2f}  "
            f"f_wall={f_w:.3f}  φ照合={phi:.3f}  R/φ={r['wall_net_cps']/phi:.2f}"
        )

    wall_eff = compute_wall_efficiencies(rows)
    peak_eps_d1 = wall_eff["d1"].epsilon_S_peakROI_cm2 or 50.22
    peak_eps_D1 = wall_eff["D1"].epsilon_S_peakROI_cm2 or 210.9
    eps_mean = wall_eff["d1"].epsilon_S_wall_cm2
    eps_std = wall_eff["d1"].epsilon_S_wall_std_cm2 or float("nan")
    wall_eps_D1 = wall_eff["D1"].epsilon_S_wall_cm2

    print("\n--- wall ε×S（4 検出器）---")
    for det in ("d1", "D1", "d2", "D2"):
        e = wall_eff[det]
        std_s = f"±{e.epsilon_S_wall_std_cm2:.2f}" if e.epsilon_S_wall_std_cm2 else ""
        print(f"  {det}: εS_wall={e.epsilon_S_wall_cm2:.2f}{std_s} cm²  ({e.note})")

    eff_wall = write_wall_efficiencies_csv(wall_eff)
    print(f"wrote {eff_wall}")

    d1_field = next(
        (r for r in rows if r["検出器"] == "d1" and r["地点"] == "管理棟2階" and r["wall_valid"]),
        None,
    )
    D1_night = next(
        (
            r
            for r in rows
            if r["検出器"] == "D1"
            and r["地点"] == "管理棟2階"
            and "0832" in r["filename"]
            and r["wall_valid"]
        ),
        None,
    )
    D1_short = next(
        (
            r
            for r in rows
            if r["検出器"] == "D1"
            and r["地点"] == "管理棟2階"
            and "1552" in r["filename"]
            and r["wall_valid"]
        ),
        None,
    )
    wall_ratio = (
        D1_night["wall_net_cps"] / d1_field["wall_net_cps"]
        if d1_field and D1_night
        else float("nan")
    )

    detail = TABLES / "D1効率_転送較正_壁効果.csv"
    with detail.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["method", "epsilon_S_wall_cm2", "D1_over_d1_ratio", "note"],
        )
        w.writeheader()
        w.writerow(
            {
                "method": "field_transfer_wall_overnight",
                "epsilon_S_wall_cm2": f"{wall_eps_D1:.4g}",
                "D1_over_d1_ratio": f"{wall_ratio:.4g}",
                "note": "メーカー450×d1 wall/total（熱中性子）",
            }
        )
        if D1_short and d1_field:
            r2 = D1_short["wall_net_cps"] / d1_field["wall_net_cps"]
            w.writerow(
                {
                    "method": "field_transfer_wall_short",
                    "epsilon_S_wall_cm2": f"{eps_mean * r2:.4g}",
                    "D1_over_d1_ratio": f"{r2:.4g}",
                    "note": "チェック用",
                }
            )
    print(f"wrote {detail}")

    for label, det in (("d2", "d2"), ("D2", "D2")):
        tr_path = TABLES / f"{label}効率_転送較正_壁効果.csv"
        e = wall_eff[det]
        ratio = e.epsilon_S_wall_cm2 / wall_eps_D1
        with tr_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(
                f,
                fieldnames=[
                    "method",
                    "epsilon_S_wall_cm2",
                    f"{det}_over_D1_ratio",
                    "D1_epsilon_S_wall_cm2",
                    "note",
                ],
            )
            w.writeheader()
            w.writerow(
                {
                    "method": f"field_transfer_{det.lower()}_wall",
                    "epsilon_S_wall_cm2": f"{e.epsilon_S_wall_cm2:.4g}",
                    f"{det}_over_D1_ratio": f"{ratio:.4g}",
                    "D1_epsilon_S_wall_cm2": f"{wall_eps_D1:.4g}",
                    "note": e.note,
                }
            )
        print(f"wrote {tr_path}")

    # --- 現場フラックス比較（peak / wall）---
    flux_out = TABLES / "フラックス_窓比較.csv"
    skip_sites = {"熱中性子_30cm", "熱中性子_80cm", "熱中性子_gain調整", "熱中性子_その他", "その他"}
    flux_rows = []
    for r in rows:
        if r["地点"] in skip_sites:
            continue
        det = r["検出器"]
        peak_eps = wall_eff[det].epsilon_S_peakROI_cm2 if det in wall_eff else None
        wall_eps = wall_eff[det].epsilon_S_wall_cm2 if det in wall_eff else None
        row = {
            "検出器": det,
            "地点": r["地点"],
            "filename": r["filename"],
            "peak_net_cps": f"{r['peak_net_cps']:.6g}",
            "wall_net_cps": f"{r['wall_net_cps']:.6g}",
            "ratio_wall_over_peak": f"{r['ratio_wall_over_peak']:.4g}",
            "phi_peak": "",
            "phi_wall": "",
            "備考": "",
        }
        notes = []
        if peak_eps and r["peak_valid"] and r["peak_net_cps"] > 0:
            row["phi_peak"] = f"{r['peak_net_cps']/peak_eps:.6g}"
            notes.append(f"peak εS={peak_eps:.4g}")
        if wall_eps and wall_eps == wall_eps and r["wall_valid"] and r["wall_net_cps"] > 0:
            row["phi_wall"] = f"{r['wall_net_cps']/wall_eps:.6g}"
            notes.append(f"wall εS={wall_eps:.4g}")
        if not notes:
            notes.append("絶対φなし")
        row["備考"] = "; ".join(notes)
        flux_rows.append(row)

    with flux_out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(flux_rows[0].keys()) if flux_rows else [])
        if flux_rows:
            w.writeheader()
            w.writerows(flux_rows)
    print(f"wrote {flux_out}")

    print("\n=== まとめ ===")
    print(f"  peak ROI  εS(d1)={peak_eps_d1:.2f}  εS(D1)={peak_eps_D1:.2f} cm²")
    print(
        f"  wall 191–764  "
        + "  ".join(
            f"εS({d})={wall_eff[d].epsilon_S_wall_cm2:.2f}" for d in ("d1", "D1", "d2", "D2")
        )
        + " cm²"
    )
    print(f"  wall/peak 較正比 d1: {eps_mean/peak_eps_d1:.3f}")

    print("\n--- He-3 感知面積（メーカー cps/nv の S は等方 S_surf/4。2rL は平行ビーム）---")
    for det in ("d1", "D1", "d2", "D2"):
        g = he3_geometric_areas(det)
        spec = DETECTORS[det]
        model = f" [{spec.rs_model}]" if spec.rs_model else ""
        mfr = spec.manufacturer_sensitivity_cps_nv
        e = wall_eff.get(det)
        f_s = f"  f_wall={e.f_wall:.3f}" if e and e.f_wall is not None else ""
        print(
            f"  {det}{model}: r_he3={g['r_he3_cm']:.2f} cm  L_sens={g['l_sensitive_cm']:.1f} cm  "
            f"S_iso={g['S_he3_isotropic_cm2']:.1f} cm²  "
            f"メーカー={mfr:.0f} cps/nv  ε_mfr={g['epsilon_mfr']:.3f}"
            f"{f_s}"
        )


if __name__ == "__main__":
    main()
