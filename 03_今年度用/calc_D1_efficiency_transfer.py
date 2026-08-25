#!/usr/bin/env python3
"""D1 絶対効率（ピーク ROI）— メーカー感度スケール。

d1 / D1 の ε×S_total はメーカー感度（123 / 450 cps/nv、公称 ±5%）。
パイルは窓比のみ（calc_detector_efficiency / flux_calibration が算出）。

  εS_window(D1) = 450 × (εS_window(d1) / 123)

使わない:
  - 管理棟2階 D1/d1 比（宇宙線スペクトル。熱中性子 εS には不適）
照合:
  - D1 パイル 30/80 cm の live 計数率 / φ（主結果はメーカー。DT は不問）
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

from mca_common import analyze_roi, infer_serial, parse_mca

ROOT = Path(__file__).resolve().parent
SIM_ROOT = ROOT.parent / "04_PHITS_sim" / "equiv_concrete_sites"
import sys

sys.path.insert(0, str(SIM_ROOT))
from detector_specs import (  # noqa: E402
    LARGE_SENSITIVITY_CPS_NV,
    RS_P4_1613_203_SENSITIVITY_CPS_NV,
    he3_geometric_areas,
)

RAW = ROOT / "測定_20260818" / "raw"
TABLES = ROOT / "測定_20260818" / "tables"

PHI_OVER_Q = 9.44e-6
Q_AMBE = 2.26e6
R_HALF = 95.0
D_REF = 30.0


def thermal_flux(d_cm: float) -> float:
    scale = ((R_HALF + D_REF) / (R_HALF + d_cm)) ** 2
    return PHI_OVER_Q * Q_AMBE * scale


def _roi_cps(path: Path) -> dict:
    m = parse_mca(path)
    c = np.asarray(m["counts"], dtype=float)
    live = float(m["LIVE_TIME"])
    real = float(m["REAL_TIME"])
    dead = max(0.0, 1.0 - live / real) if real > 0 else 0.0
    sn = infer_serial(path.name, str(m.get("serial") or ""))
    roi = analyze_roi(c, sn)
    tot = float(c.sum())
    ch0 = float(c[0]) if tot else 0.0
    net = float(roi.net)
    return {
        "file": path.name,
        "live_s": live,
        "dead_frac": dead,
        "ch0_frac": ch0 / tot if tot else 0.0,
        "roi_net_cps": net / live if live else float("nan"),
        "peak": roi.roi_peak,
    }


def _load_d1_roi() -> tuple[float, float]:
    """d1 の εS_ROI と εS_total（パイル）。"""
    path = TABLES / "検出器効率_熱中性子校正版.csv"
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("検出器") == "d1":
                roi = float(row["epsilon_S_ROI_cm2"])
                tot = float(row["epsilon_S_cm2"])
                return roi, tot
    raise RuntimeError("d1 効率がありません。先に calc_detector_efficiency.py を実行してください。")


def main() -> None:
    eps_d1_roi, eps_d1_tot = _load_d1_roi()
    mfr_d1 = RS_P4_1613_203_SENSITIVITY_CPS_NV
    mfr_D1 = LARGE_SENSITIVITY_CPS_NV
    f_roi = eps_d1_roi / mfr_d1
    f_tot = eps_d1_tot / mfr_d1

    eps_roi = mfr_D1 * f_roi
    eps_tot = mfr_D1 * f_tot

    d1 = _roi_cps(RAW / "d1_20260819_1520_管理棟2階.mca")
    d1_night = _roi_cps(RAW / "D1_20260819_0832_管理棟2階.mca")
    d1_short = _roi_cps(RAW / "D1_20260818_1552_管理棟2階.mca")
    pile30 = _roi_cps(RAW / "D1_20260822_1633_熱中性子管理棟-30cm.mca")
    pile80 = _roi_cps(RAW / "D1_20260822_1644_熱中性子管理棟2-80cm.mca")

    r_night = d1_night["roi_net_cps"] / d1["roi_net_cps"]
    r_short = d1_short["roi_net_cps"] / d1["roi_net_cps"]
    field_eps_roi = eps_d1_roi * r_night

    geom_d1 = he3_geometric_areas("d1")
    geom_D1 = he3_geometric_areas("D1")
    geom_iso_ratio = geom_D1["S_he3_isotropic_cm2"] / geom_d1["S_he3_isotropic_cm2"]
    pile80_eps = pile80["roi_net_cps"] / thermal_flux(80.0)

    print("=== 黒鉛パイル D1（照合・主結果はメーカー）===")
    print(
        f"  30cm: CPS={pile30['roi_net_cps']:.1f}  "
        f"ch0={pile30['ch0_frac']*100:.1f}%  "
        f"εS_ROI≈{pile30['roi_net_cps']/thermal_flux(30.0):.1f}"
    )
    print(
        f"  80cm: CPS={pile80['roi_net_cps']:.1f}  "
        f"ch0={pile80['ch0_frac']*100:.1f}%  "
        f"εS_ROI≈{pile80_eps:.1f}"
    )

    print("\n=== メーカー感度スケール（主結果）===")
    print(f"  d1 メーカー {mfr_d1:.0f} cps/nv  ε_mfr={geom_d1['epsilon_mfr']:.3f}  "
          f"パイル εS_total={eps_d1_tot:.2f}  εS_ROI={eps_d1_roi:.2f}")
    print(f"  D1 メーカー {mfr_D1:.0f} cps/nv  ε_mfr={geom_D1['epsilon_mfr']:.3f}")
    print(f"  ROI/メーカー(d1) = {f_roi:.3f}")
    print(f"  ε×S_ROI(D1) = {mfr_D1:.0f} × {f_roi:.3f} = {eps_roi:.2f} cm²")
    print(f"  ε×S_total(D1) = {mfr_D1:.0f} × {f_tot:.3f} = {eps_tot:.2f} cm²")
    print(
        f"  S_iso 比 D1/d1 = {geom_iso_ratio:.3f}  "
        f"メーカー比 = {mfr_D1/mfr_d1:.3f}"
    )

    print("\n=== 参考: 管理棟2階現場比（宇宙線・熱 εS には不使用）===")
    print(f"  D1/d1 終夜 ROI 比={r_night:.3f} → εS_ROI≈{field_eps_roi:.1f} cm²")
    print(f"  D1/d1 短時間 ROI 比={r_short:.3f}")

    eff_path = TABLES / "検出器効率_熱中性子校正版.csv"
    with eff_path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
    out = []
    for row in rows:
        if row["検出器"] == "D1":
            row = dict(row)
            row["epsilon_S_cm2"] = f"{eps_tot:.4g}"
            row["epsilon_S_std_cm2"] = ""
            row["epsilon_S_ROI_cm2"] = f"{eps_roi:.4g}"
            row["f_roi_over_total"] = f"{eps_roi/eps_tot:.4g}"
            row["S_end_cm2"] = f"{geom_D1['S_he3_end_cm2']:.3g}"
            row["S_side_cm2"] = f"{geom_D1['S_he3_lateral_cm2']:.3g}"
            if "S_he3_projected_cm2" in fields:
                row["S_he3_projected_cm2"] = f"{geom_D1['S_he3_projected_cm2']:.3g}"
            if "r_he3_cm" in fields:
                row["r_he3_cm"] = f"{geom_D1['r_he3_cm']:.3g}"
            if "l_sensitive_cm" in fields:
                row["l_sensitive_cm"] = f"{geom_D1['l_sensitive_cm']:.3g}"
            if "S_he3_lateral_cm2" in fields:
                row["S_he3_lateral_cm2"] = f"{geom_D1['S_he3_lateral_cm2']:.3g}"
            if "S_he3_end_cm2" in fields:
                row["S_he3_end_cm2"] = f"{geom_D1['S_he3_end_cm2']:.3g}"
            if "S_he3_horizontal_cm2" in fields:
                row["S_he3_horizontal_cm2"] = f"{geom_D1['S_he3_horizontal_cm2']:.3g}"
            row["備考"] = (
                f"メーカー{mfr_D1:.0f}×d1 ROI/メーカー={f_roi:.3f}; "
                f"パイル照合 30cm εS_ROI={pile30['roi_net_cps']/thermal_flux(30.0):.0f}, "
                f"80cm εS_ROI={pile80_eps:.0f}"
            )
        out.append(row)
    with eff_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    print(f"\nupdated: {eff_path}")

    detail = TABLES / "D1効率_転送較正.csv"
    with detail.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "method",
                "epsilon_S_ROI_cm2",
                "epsilon_S_ROI_std_cm2",
                "epsilon_S_total_cm2",
                "D1_over_d1_ratio",
                "note",
            ],
        )
        w.writeheader()
        w.writerow(
            {
                "method": "manufacturer_scale_450",
                "epsilon_S_ROI_cm2": f"{eps_roi:.4g}",
                "epsilon_S_ROI_std_cm2": "",
                "epsilon_S_total_cm2": f"{eps_tot:.4g}",
                "D1_over_d1_ratio": f"{mfr_D1/mfr_d1:.4g}",
                "note": "主結果。450 × (d1窓/123)",
            }
        )
        w.writerow(
            {
                "method": "field_transfer_kanri2f_overnight_REF_ONLY",
                "epsilon_S_ROI_cm2": f"{field_eps_roi:.4g}",
                "epsilon_S_ROI_std_cm2": "",
                "epsilon_S_total_cm2": f"{field_eps_roi / (eps_d1_roi/eps_d1_tot):.4g}",
                "D1_over_d1_ratio": f"{r_night:.4g}",
                "note": "参考。宇宙線場の実効比。熱中性子εSには不使用",
            }
        )
        w.writerow(
            {
                "method": "geometry_projected_area_scale",
                "epsilon_S_ROI_cm2": f"{eps_d1_roi * geom_iso_ratio:.4g}",
                "epsilon_S_ROI_std_cm2": "",
                "epsilon_S_total_cm2": f"{eps_d1_tot * geom_iso_ratio:.4g}",
                "D1_over_d1_ratio": f"{geom_iso_ratio:.4g}",
                "note": "参考。同一ε・等方面積 S_iso",
            }
        )
        w.writerow(
            {
                "method": "pile_D1_80cm_live_CROSSCHECK",
                "epsilon_S_ROI_cm2": f"{pile80_eps:.4g}",
                "epsilon_S_ROI_std_cm2": "",
                "epsilon_S_total_cm2": "",
                "D1_over_d1_ratio": "",
                "note": "照合。net/live ÷ φ(80cm)。主結果はメーカー（DT 不問）",
            }
        )
    print(f"wrote: {detail}")


if __name__ == "__main__":
    main()
