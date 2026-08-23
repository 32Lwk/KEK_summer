#!/usr/bin/env python3
"""ピーク ROI と壁効果窓（196–764 keV）の二系統解析を並べて出力する。

出力:
  tables/窓比較_計数率.csv
  tables/検出器効率_壁効果196_764keV.csv
  tables/フラックス_壁効果196_764keV.csv
  tables/D1効率_転送較正_壁効果.csv
"""

from __future__ import annotations

import csv
import math
import re
from pathlib import Path

import numpy as np

from mca_common import analyze_roi, analyze_wall_window, infer_serial, parse_mca

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "測定_20260818" / "raw"
TABLES = ROOT / "測定_20260818" / "tables"

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
    return "その他"


def analyze_file(path: Path) -> dict:
    m = parse_mca(path)
    c = np.asarray(m["counts"], dtype=float)
    live = float(m["LIVE_TIME"])
    real = float(m["REAL_TIME"])
    dead = max(0.0, 1.0 - live / real) if real > 0 else 0.0
    sn = infer_serial(path.name, str(m.get("serial") or ""))
    peak = analyze_roi(c, sn)
    wall = analyze_wall_window(c, sn)
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
        "wall_net_cps": wall.net / live if live else float("nan"),
        "wall_gross_cps": wall.gross / live if live else float("nan"),
        "wall_net_cps_err": wall.err / live if live else float("nan"),
        "wall_valid": int(wall.net_valid),
        "wall_bg_mode": wall.bg_mode,
        "ratio_wall_over_peak": (
            (wall.net / peak.net) if peak.net and peak.net > 0 else float("nan")
        ),
        "peak_warning": peak.warning,
        "wall_warning": wall.warning,
    }


def main() -> None:
    files = sorted(RAW.glob("*.mca"))
    rows = [analyze_file(p) for p in files]

    out_rates = TABLES / "窓比較_計数率.csv"
    fields = list(rows[0].keys())
    with out_rates.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {out_rates}")

    # --- d1 パイル絶対較正（壁効果窓）---
    d1_pile = [
        r
        for r in rows
        if r["検出器"] == "d1"
        and r["地点"] in ("熱中性子_30cm", "熱中性子_80cm")
        and r["wall_valid"]
        and r["dead_frac"] < 0.15
    ]
    eps_wall = []
    for r in d1_pile:
        d = 30.0 if "30" in r["地点"] else 80.0
        phi = thermal_flux(d)
        eps_wall.append(r["wall_net_cps"] / phi)
        print(
            f"  d1 wall @{d:.0f}cm: CPS={r['wall_net_cps']:.2f}  φ={phi:.3f}  "
            f"εS={r['wall_net_cps']/phi:.2f}  (peak CPS={r['peak_net_cps']:.2f})"
        )
    if len(eps_wall) >= 2:
        eps_mean = float(np.mean(eps_wall))
        eps_std = float(np.std(eps_wall))
    elif eps_wall:
        eps_mean = float(eps_wall[0])
        eps_std = float("nan")
    else:
        eps_mean = eps_std = float("nan")
        print("WARNING: d1 wall pile points missing")

    # ピーク側は既存表から読む
    peak_eps_d1 = 50.22
    peak_eps_D1 = 210.9
    eff_path = TABLES / "検出器効率_熱中性子校正版.csv"
    if eff_path.exists():
        for r in csv.DictReader(eff_path.open(encoding="utf-8")):
            if r.get("検出器") == "d1" and r.get("epsilon_S_ROI_cm2"):
                peak_eps_d1 = float(r["epsilon_S_ROI_cm2"])
            if r.get("検出器") == "D1" and r.get("epsilon_S_ROI_cm2"):
                peak_eps_D1 = float(r["epsilon_S_ROI_cm2"])

    # --- D1 転送（管理棟2階・壁効果）---
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

    wall_eps_D1 = float("nan")
    wall_ratio = float("nan")
    if d1_field and D1_night and eps_mean == eps_mean:
        wall_ratio = D1_night["wall_net_cps"] / d1_field["wall_net_cps"]
        wall_eps_D1 = eps_mean * wall_ratio
        print(
            f"\n  D1 wall transfer: ratio={wall_ratio:.3f}  "
            f"εS_wall(D1)={wall_eps_D1:.2f} cm²  (d1 εS_wall={eps_mean:.2f})"
        )
        if D1_short:
            r2 = D1_short["wall_net_cps"] / d1_field["wall_net_cps"]
            print(f"  check short D1: ratio={r2:.3f} → εS={eps_mean*r2:.2f}")

    # 効率表（壁効果）
    eff_wall = TABLES / "検出器効率_壁効果196_764keV.csv"
    with eff_wall.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "検出器",
                "epsilon_S_wall_cm2",
                "epsilon_S_wall_std_cm2",
                "epsilon_S_peakROI_cm2",
                "wall_over_peak_cal",
                "備考",
            ],
        )
        w.writeheader()
        w.writerow(
            {
                "検出器": "d1",
                "epsilon_S_wall_cm2": f"{eps_mean:.4g}" if eps_mean == eps_mean else "",
                "epsilon_S_wall_std_cm2": f"{eps_std:.4g}" if eps_std == eps_std else "",
                "epsilon_S_peakROI_cm2": f"{peak_eps_d1:.4g}",
                "wall_over_peak_cal": f"{eps_mean/peak_eps_d1:.4g}" if eps_mean == eps_mean else "",
                "備考": "黒鉛パイル30&80cm・水平・非飽和・窓196–764keV・右側帯背景",
            }
        )
        w.writerow(
            {
                "検出器": "D1",
                "epsilon_S_wall_cm2": f"{wall_eps_D1:.4g}" if wall_eps_D1 == wall_eps_D1 else "",
                "epsilon_S_wall_std_cm2": "",
                "epsilon_S_peakROI_cm2": f"{peak_eps_D1:.4g}",
                "wall_over_peak_cal": f"{wall_eps_D1/peak_eps_D1:.4g}" if wall_eps_D1 == wall_eps_D1 else "",
                "備考": f"転送: 管理棟2階 D1/d1 壁窓比={wall_ratio:.3f}×d1εS_wall" if wall_ratio == wall_ratio else "転送不可",
            }
        )
        for det in ("D2", "d2"):
            w.writerow(
                {
                    "検出器": det,
                    "epsilon_S_wall_cm2": "",
                    "epsilon_S_wall_std_cm2": "",
                    "epsilon_S_peakROI_cm2": "",
                    "wall_over_peak_cal": "",
                    "備考": "未較正（400cm・黒鉛なし）",
                }
            )
    print(f"wrote {eff_wall}")

    detail = TABLES / "D1効率_転送較正_壁効果.csv"
    with detail.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["method", "epsilon_S_wall_cm2", "D1_over_d1_ratio", "note"],
        )
        w.writeheader()
        if wall_eps_D1 == wall_eps_D1:
            w.writerow(
                {
                    "method": "field_transfer_wall_overnight",
                    "epsilon_S_wall_cm2": f"{wall_eps_D1:.4g}",
                    "D1_over_d1_ratio": f"{wall_ratio:.4g}",
                    "note": "管理棟2階・壁窓196–764keV",
                }
            )
        if D1_short and d1_field and eps_mean == eps_mean:
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

    # --- 現場フラックス比較（peak / wall）---
    flux_out = TABLES / "フラックス_窓比較.csv"
    skip_sites = {"熱中性子_30cm", "熱中性子_80cm", "熱中性子_gain調整", "熱中性子_その他", "その他"}
    flux_rows = []
    for r in rows:
        if r["地点"] in skip_sites:
            continue
        det = r["検出器"]
        peak_eps = peak_eps_d1 if det == "d1" else (peak_eps_D1 if det == "D1" else None)
        wall_eps = eps_mean if det == "d1" else (wall_eps_D1 if det == "D1" else None)
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
    if eps_mean == eps_mean:
        print(f"  wall 196–764  εS(d1)={eps_mean:.2f}±{eps_std:.2f}  εS(D1)={wall_eps_D1:.2f} cm²")
        print(f"  wall/peak 較正比 d1: {eps_mean/peak_eps_d1:.3f}")


if __name__ == "__main__":
    main()
