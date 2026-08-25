#!/usr/bin/env python3
"""Phase 0: 実測値の独立再現と旧理論からの乖離倍率の算出。

フラックス_地点まとめ.csv と equiv_shielding から、
- 各地点の t_eq（密度換算・組成補正）、X [g/cm²]、深さ [m.w.e.]
- 旧理論 φ_th = A0·exp(-t_eq/λ)（λ=39.2, 60 cm）
- 実測/理論 倍率（検出器別・窓別）
を再計算し tables/phase0_reproduction.csv に出す。
"""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # theory_research/
MEAS = HERE.parent                               # 測定_20260818/
TABLES = MEAS / "tables"
CODE = MEAS.parent                               # 03_今年度用/
sys.path.insert(0, str(CODE))

import equiv_shielding as esh  # noqa: E402
from flux_calibration import eps_wall_dict, load_wall_efficiencies_csv  # noqa: E402

A0_D1_GROUND = None  # フラックス表から取得
LAMBDAS = (esh.LAMBDA_CONCRETE_CM, 60.0)

# _plot_mca._site_layers() と同一の層厚（読了済みの値をここで独立再宣言）
SITE_LAYERS = {
    "地上": (0.0, 0.0, 0.0),
    "管理棟2階": (0.0, 0.0, 0.0),   # 屋内・遮蔽 0 扱い（現行解析と同じ）
    "管理棟1階": (0.0, 0.0, 0.0),
    "testhole": (57.0, 0.0, 0.0),  # linac テストホール（等価コンクリート 57 cm）
    "PF": (105.0, 0.0, 0.0),
    "linac150": (150.0, 0.0, 0.0),
    "linac": (300.0, 0.0, 0.0),      # フラックス表の "linac" = Linac3 (300 cm)
    "PS": (480.0, 0.0, 0.0),         # PS FEL（等価コンクリート 4.8 m）
    "放射線棟BT": (60.0, 220.0, 0.0),
    "KEKB": (80.0, 670.0, 0.0),
    "linac_IRON": (200.0, 100.0, 150.0),  # コンクリ200 + 土100 + 鉄150
}


def site_geometry(site: str) -> dict:
    tc, ts, tfe = SITE_LAYERS[site]
    r = esh.equiv_concrete(tc, ts, iron_cm=tfe)
    x_total = r.x_total_gcm2
    return {
        "concrete_cm": tc,
        "soil_cm": ts,
        "iron_cm": tfe,
        "X_gcm2": x_total,
        "mwe": x_total / 100.0,
        "t_eq_density_cm": r.t_eq_density_only_cm,  # 図11–18の横軸
        "t_eq_comp_cm": r.t_eq_cm,                   # 組成λ補正
        "tau": r.tau,
    }


def main() -> None:
    rows = list(csv.DictReader((TABLES / "フラックス_地点まとめ.csv").open(encoding="utf-8")))

    phi0 = None
    for r in rows:
        if r["検出器"] == "D1" and r["地点"] == "地上":
            phi0 = float(r["絶対phi_n_cm2_s"])
    assert phi0 is not None
    print(f"A0 (D1 地上 φ_wall) = {phi0:.4e} n/cm²/s")

    out = []
    print(f"{'det':4s} {'site':10s} {'t_eq':>6s} {'mwe':>5s} {'φ_wall':>9s} "
          f"{'φ/th(39.2)':>11s} {'φ/th(60)':>9s} {'peakCPS':>9s} {'wall/peak':>9s}")
    for r in rows:
        det, site = r["検出器"], r["地点"]
        g = site_geometry(site)
        t = g["t_eq_density_cm"]
        phi_s = (r.get("絶対phi_n_cm2_s") or "").strip()
        phi = float(phi_s) if phi_s else math.nan
        peak = float(r["peak_ROI_net_CPS"]) if r.get("peak_ROI_net_CPS") else math.nan
        wall = float(r["NET_CPS_191_764keV"]) if (r.get("NET_CPS_191_764keV") or "").strip() else math.nan
        ratios = []
        for lam in LAMBDAS:
            th = phi0 * math.exp(-t / lam)
            ratios.append(phi / th if not math.isnan(phi) else math.nan)
        wp = wall / peak if (not math.isnan(wall) and peak) else math.nan
        print(f"{det:4s} {site:10s} {t:6.1f} {g['mwe']:5.2f} "
              f"{phi:9.3e} {ratios[0]:11.3g} {ratios[1]:9.3g} {peak:9.4f} {wp:9.3g}")
        out.append({
            "検出器": det, "地点": site,
            "t_eq_density_cm": f"{t:.1f}",
            "t_eq_comp_cm": f"{g['t_eq_comp_cm']:.1f}",
            "X_gcm2": f"{g['X_gcm2']:.1f}",
            "mwe": f"{g['mwe']:.2f}",
            "phi_wall": f"{phi:.6g}" if not math.isnan(phi) else "",
            "phi_wall_err": r.get("絶対phi_err", ""),
            "peak_net_cps": f"{peak:.6g}",
            "wall_net_cps": f"{wall:.6g}" if not math.isnan(wall) else "",
            "wall_over_peak": f"{wp:.4g}" if not math.isnan(wp) else "",
            "meas_over_theory_39.2": f"{ratios[0]:.4g}" if not math.isnan(ratios[0]) else "",
            "meas_over_theory_60": f"{ratios[1]:.4g}" if not math.isnan(ratios[1]) else "",
            "filename": r.get("filename", ""),
        })

    # 窓比較 CSV から linac150 等の非採用ランも補完出力
    win = list(csv.DictReader((TABLES / "フラックス_窓比較.csv").open(encoding="utf-8")))
    eps_wall = eps_wall_dict(load_wall_efficiencies_csv(TABLES / "検出器効率_壁効果191_764keV.csv"))
    if len(eps_wall) < 4:
        eps_wall = {"d1": 109.5, "D1": 400.7, "d2": 147.1, "D2": 298.9}
    print("\n-- 非採用ラン（150cm linac 等・εS で φ 換算） --")
    for r in win:
        fn = r["filename"]
        if "_linac." in fn or "linac." in fn.replace("linacIRON", "").replace("Linac3", ""):
            det = r["検出器"]
            wall = float(r["wall_net_cps"])
            phi = wall / eps_wall.get(det, math.nan)
            g = site_geometry("linac150")
            th = phi0 * math.exp(-g["t_eq_density_cm"] / LAMBDAS[0])
            print(f"  {det:3s} linac150 {fn}: wall={wall:.4f} φ≈{phi:.3e} → 実測/理論(39.2)={phi/th:.3g}")
            out.append({
                "検出器": det, "地点": "linac150",
                "t_eq_density_cm": f"{g['t_eq_density_cm']:.1f}",
                "t_eq_comp_cm": f"{g['t_eq_comp_cm']:.1f}",
                "X_gcm2": f"{g['X_gcm2']:.1f}",
                "mwe": f"{g['mwe']:.2f}",
                "phi_wall": f"{phi:.6g}",
                "phi_wall_err": "",
                "peak_net_cps": r["peak_net_cps"],
                "wall_net_cps": f"{wall:.6g}",
                "wall_over_peak": r["ratio_wall_over_peak"],
                "meas_over_theory_39.2": f"{phi/th:.4g}",
                "meas_over_theory_60": "",
                "filename": fn + "（非採用・参考）",
            })

    dest = HERE / "tables" / "phase0_reproduction.csv"
    with dest.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    print(f"\nwrote {dest}")


if __name__ == "__main__":
    main()
