#!/usr/bin/env python3
"""D2 絶対効率の転送較正（400 cm・黒鉛なしの PE 確認データは熱 φ 公式に使わない）。

手順:
  1. D1 の ε×S_ROI は管理棟2階 D1/d1 転送で既知（calc_D1_efficiency_transfer.py）
  2. 同一地点（地上・低デッドタイム）で D2 / D1 の ROI NET CPS 比を取る
  3. ε×S_ROI(D2) = ε×S_ROI(D1) × (CPS_D2 / CPS_D1) @ 地上
"""

from __future__ import annotations

import csv
from pathlib import Path

from mca_common import analyze_roi, infer_serial, parse_mca

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "測定_20260818" / "raw"
TABLES = ROOT / "測定_20260818" / "tables"

F_ROI = 0.5614


def _roi_cps(path: Path) -> dict:
    m = parse_mca(path)
    c = __import__("numpy").asarray(m["counts"], dtype=float)
    live = float(m["LIVE_TIME"])
    real = float(m["REAL_TIME"])
    dead = max(0.0, 1.0 - live / real) if real > 0 else 0.0
    sn = infer_serial(path.name, str(m.get("serial") or ""))
    roi = analyze_roi(c, sn)
    net = float(roi.net)
    return {
        "file": path.name,
        "live_s": live,
        "dead_frac": dead,
        "roi_net_cps": net / live if live else float("nan"),
    }


def _load_eps_d1() -> float:
    eff_path = TABLES / "検出器効率_熱中性子校正版.csv"
    with eff_path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("検出器") == "D1" and (row.get("epsilon_S_ROI_cm2") or "").strip():
                return float(row["epsilon_S_ROI_cm2"])
    raise RuntimeError("D1 ε×S_ROI がありません。先に calc_D1_efficiency_transfer.py を実行してください。")


def main() -> None:
    eps_d1 = _load_eps_d1()
    d1_ground = _roi_cps(RAW / "D1_20260819_1530_地上.mca")
    d2_ground = _roi_cps(RAW / "D2_20260822_155048_地上.mca")

    ratio = d2_ground["roi_net_cps"] / d1_ground["roi_net_cps"]
    eps_roi = eps_d1 * ratio
    eps_tot = eps_roi / F_ROI

    print("=== 転送較正（地上・低レート）===")
    print(
        f"  D1  ROI CPS={d1_ground['roi_net_cps']:.5f}  dead={d1_ground['dead_frac']*100:.3f}%"
    )
    print(
        f"  D2  ROI CPS={d2_ground['roi_net_cps']:.5f}  dead={d2_ground['dead_frac']*100:.3f}%  "
        f"比={ratio:.4f}"
    )
    print(f"\n  ε×S_ROI(D1) = {eps_d1:.2f} cm²")
    print(f"  ε×S_ROI(D2) = {eps_d1:.2f} × {ratio:.4f} = {eps_roi:.2f} cm²")
    print(f"  ε×S_total(D2) ≈ {eps_tot:.2f} cm²  (f_ROI={F_ROI})")
    print(
        f"  地上 φ 整合: D1={d1_ground['roi_net_cps']/eps_d1:.4g}, "
        f"D2={d2_ground['roi_net_cps']/eps_roi:.4g} n/cm²/s"
    )

    eff_path = TABLES / "検出器効率_熱中性子校正版.csv"
    with eff_path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys())
    out = []
    for row in rows:
        if row["検出器"] == "D2":
            row = dict(row)
            row["epsilon_S_cm2"] = f"{eps_tot:.4g}"
            row["epsilon_S_std_cm2"] = ""
            row["epsilon_S_ROI_cm2"] = f"{eps_roi:.4g}"
            row["f_roi_over_total"] = f"{F_ROI:.4g}"
            row["S_end_cm2"] = "72.4"
            row["S_side_cm2"] = "1689"
            row["備考"] = (
                f"転送較正: 地上 D2/D1 ROI比={ratio:.4f}×D1εS_ROI; "
                f"400cm PE確認は熱φ公式不可・不使用"
            )
        out.append(row)
    with eff_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    print(f"\nupdated: {eff_path}")

    detail = TABLES / "D2効率_転送較正.csv"
    with detail.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "method",
                "epsilon_S_ROI_cm2",
                "D2_over_D1_ratio",
                "D1_epsilon_S_ROI_cm2",
                "note",
            ],
        )
        w.writeheader()
        w.writerow(
            {
                "method": "field_transfer_ground",
                "epsilon_S_ROI_cm2": f"{eps_roi:.4g}",
                "D2_over_D1_ratio": f"{ratio:.4g}",
                "D1_epsilon_S_ROI_cm2": f"{eps_d1:.4g}",
                "note": "主結果。D2/D1 @ 地上",
            }
        )
    print(f"wrote: {detail}")


if __name__ == "__main__":
    main()
