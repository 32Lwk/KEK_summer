#!/usr/bin/env python3
"""D1 絶対効率の転送較正（黒鉛パイル 30/80 cm は飽和のため直接較正不可）。

手順:
  1. d1 の ε×S_ROI は黒鉛パイル 30/80 cm（非飽和）から既知 = 50.22 cm²
  2. 現場の低計数率（管理棟2階）で D1 と d1 の ROI NET CPS 比を取る
     → デッドタイム ~0.1% なので飽和なし
  3. ε×S_ROI(D1) = ε×S_ROI(d1) × (CPS_D1 / CPS_d1)

黒鉛パイル raw の確認結果（参考・不採用）:
  D1@30cm: dead≈63%, ch0≈33%, R30/R80 が理論比から大きく外れる → 直接 ε×S 不可
  D1@80cm: dead≈33%, ch0≈35% → デッドタイム補正してもなお過小評価
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np

from mca_common import analyze_roi, infer_serial, parse_mca

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "測定_20260818" / "raw"
TABLES = ROOT / "測定_20260818" / "tables"

EPS_D1_ROI = 50.22  # cm²（検出器効率_熱中性子校正版.csv）
F_ROI_D1 = 0.5614  # d1 パイルでの ROI/total（D1 総効率の換算に同値を仮定）

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


def main() -> None:
    d1 = _roi_cps(RAW / "d1_20260819_1520_管理棟2階.mca")
    d1_night = _roi_cps(RAW / "D1_20260819_0832_管理棟2階.mca")
    d1_short = _roi_cps(RAW / "D1_20260818_1552_管理棟2階.mca")
    pile30 = _roi_cps(RAW / "D1_20260822_1633_熱中性子管理棟-30cm.mca")
    pile80 = _roi_cps(RAW / "D1_20260822_1644_熱中性子管理棟2-80cm.mca")

    r_night = d1_night["roi_net_cps"] / d1["roi_net_cps"]
    r_short = d1_short["roi_net_cps"] / d1["roi_net_cps"]
    ratio = r_night
    ratio_std = abs(r_night - r_short) / math.sqrt(2)

    eps_roi = EPS_D1_ROI * ratio
    eps_roi_std = EPS_D1_ROI * ratio_std
    eps_tot = eps_roi / F_ROI_D1
    eps_tot_std = eps_roi_std / F_ROI_D1

    geom_side_ratio = (2 * math.pi * 4.8 * 56.0) / (2 * math.pi * 2.54 * 31.03)
    eps_roi_geom = EPS_D1_ROI * geom_side_ratio
    pile80_eps = (pile80["roi_net_cps"] / (1.0 - pile80["dead_frac"])) / thermal_flux(80.0)

    print("=== 黒鉛パイル D1（直接較正は不可）===")
    print(
        f"  30cm: CPS={pile30['roi_net_cps']:.1f}  dead={pile30['dead_frac']*100:.1f}%  "
        f"ch0={pile30['ch0_frac']*100:.1f}%"
    )
    print(
        f"  80cm: CPS={pile80['roi_net_cps']:.1f}  dead={pile80['dead_frac']*100:.1f}%  "
        f"ch0={pile80['ch0_frac']*100:.1f}%  → dead補正のみのεS_ROI≈{pile80_eps:.1f}（過小・不採用）"
    )

    print("\n=== 転送較正（管理棟2階・低レート）===")
    print(f"  d1          ROI CPS={d1['roi_net_cps']:.5f}  dead={d1['dead_frac']*100:.3f}%")
    print(
        f"  D1 終夜     ROI CPS={d1_night['roi_net_cps']:.5f}  dead={d1_night['dead_frac']*100:.3f}%  "
        f"比={r_night:.3f}"
    )
    print(
        f"  D1 短時間   ROI CPS={d1_short['roi_net_cps']:.5f}  dead={d1_short['dead_frac']*100:.3f}%  "
        f"比={r_short:.3f}"
    )
    print(f"\n  ε×S_ROI(d1) = {EPS_D1_ROI:.2f} cm²")
    print(f"  ε×S_ROI(D1) = {EPS_D1_ROI:.2f} × {ratio:.3f} = {eps_roi:.2f} ± {eps_roi_std:.2f} cm²")
    print(f"  ε×S_total(D1) ≈ {eps_tot:.2f} ± {eps_tot_std:.2f} cm²  (f_ROI={F_ROI_D1} を d1 と同仮定)")
    print(f"  参考: 側面幾何比 {geom_side_ratio:.3f} → ε×S_ROI ≈ {eps_roi_geom:.1f} cm²")

    eff_path = TABLES / "検出器効率_熱中性子校正版.csv"
    with eff_path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
    out = []
    for row in rows:
        if row["検出器"] == "D1":
            row = dict(row)
            row["epsilon_S_cm2"] = f"{eps_tot:.4g}"
            row["epsilon_S_std_cm2"] = f"{eps_tot_std:.4g}"
            row["epsilon_S_ROI_cm2"] = f"{eps_roi:.4g}"
            row["f_roi_over_total"] = f"{F_ROI_D1:.4g}"
            row["S_end_cm2"] = "72.4"
            row["S_side_cm2"] = "1689"
            row["備考"] = (
                f"転送較正: 管理棟2階 D1/d1 ROI比={ratio:.3f}×d1εS_ROI; "
                f"パイル30/80cmは飽和(dead {pile30['dead_frac']*100:.0f}/{pile80['dead_frac']*100:.0f}%)不使用; "
                f"幾何側面比→{eps_roi_geom:.0f}cm²は参考"
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
                "method": "field_transfer_kanri2f_overnight",
                "epsilon_S_ROI_cm2": f"{eps_roi:.4g}",
                "epsilon_S_ROI_std_cm2": f"{eps_roi_std:.4g}",
                "epsilon_S_total_cm2": f"{eps_tot:.4g}",
                "D1_over_d1_ratio": f"{ratio:.4g}",
                "note": "主結果。終夜D1 / d1 @管理棟2階",
            }
        )
        w.writerow(
            {
                "method": "field_transfer_kanri2f_short",
                "epsilon_S_ROI_cm2": f"{EPS_D1_ROI * r_short:.4g}",
                "epsilon_S_ROI_std_cm2": "",
                "epsilon_S_total_cm2": f"{EPS_D1_ROI * r_short / F_ROI_D1:.4g}",
                "D1_over_d1_ratio": f"{r_short:.4g}",
                "note": "チェック用（短時間D1）",
            }
        )
        w.writerow(
            {
                "method": "geometry_side_area_scale",
                "epsilon_S_ROI_cm2": f"{eps_roi_geom:.4g}",
                "epsilon_S_ROI_std_cm2": "",
                "epsilon_S_total_cm2": f"{eps_roi_geom / F_ROI_D1:.4g}",
                "D1_over_d1_ratio": f"{geom_side_ratio:.4g}",
                "note": "参考。同一ε・側面支配を仮定",
            }
        )
        w.writerow(
            {
                "method": "pile_D1_80cm_deadtime_only_REJECTED",
                "epsilon_S_ROI_cm2": f"{pile80_eps:.4g}",
                "epsilon_S_ROI_std_cm2": "",
                "epsilon_S_total_cm2": "",
                "D1_over_d1_ratio": "",
                "note": "不採用。ch0溢れ残り・R30/R80異常",
            }
        )
    print(f"wrote: {detail}")


if __name__ == "__main__":
    main()
