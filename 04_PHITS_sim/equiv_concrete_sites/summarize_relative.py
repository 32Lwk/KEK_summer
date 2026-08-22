#!/usr/bin/env python3
"""各地点 PHITS He-3/SUS304 検出器応答を地上比でまとめ、図11と比較する。"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "03_今年度用"))
import equiv_shielding as esh

_FONT_CANDIDATES = [
    Path("/Library/Fonts/Arial Unicode.ttf"),
    Path("/System/Library/Fonts/Supplemental/AppleGothic.ttf"),
    Path("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"),
]
_JP_FONT = None
for _p in _FONT_CANDIDATES:
    if _p.is_file():
        font_manager.fontManager.addfont(str(_p))
        _JP_FONT = font_manager.FontProperties(fname=str(_p))
        break
if _JP_FONT is None:
    _JP_FONT = font_manager.FontProperties(family="Hiragino Sans")

plt.rcParams.update(
    {
        "font.family": _JP_FONT.get_name(),
        "font.sans-serif": [_JP_FONT.get_name(), "Hiragino Sans", "AppleGothic", "DejaVu Sans"],
        "axes.unicode_minus": False,
        "mathtext.fontset": "dejavusans",
        "axes.grid": True,
        "grid.alpha": 0.35,
        "grid.linestyle": "--",
    }
)

BASE = Path(__file__).resolve().parent
REPO = BASE.parents[1]
OUT_CSV = REPO / "03_今年度用" / "測定_20260818" / "tables" / "PHITS_等価コンクリート_相対.csv"
OUT_FIG = REPO / "03_今年度用" / "測定_20260818" / "figures" / "15_PHITS_等価コンクリート_比較.png"
OUT_FIG_LOG = (
    REPO / "03_今年度用" / "測定_20260818" / "figures" / "15_PHITS_等価コンクリート_比較_片対数.png"
)

_SITES_IN = [
    ("地上", "00_ground", 0.0, 0.0, 0.52514597),
    ("PF", "01_PF", 105.0, 0.0, 0.25108616),
    ("linac", "02_linac", 150.0, 0.0, 0.06478913),
    ("BT", "03_BT", 60.0, 220.0, 0.11475671),
    ("KEKB", "04_KEKB", 80.0, 670.0, 0.0399324),
]
SITES = []
for _label, _dir, _tc, _ts, _cps in _SITES_IN:
    _r = esh.equiv_concrete(_tc, _ts, profile=esh.DEFAULT_PROFILE)
    SITES.append(
        {
            "label": _label,
            "dir": _dir,
            "concrete_cm": _tc,
            "soil_cm": _ts,
            "teq_cm": _r.t_eq_cm,
            "cps": _cps,
        }
    )

LAMBDA_CM = esh.LAMBDA_CONCRETE_CM
# He-3(n,p)T 典型ピーク窓（既存 de2.out と同じ）
DE_PEAK_LO = 0.191
DE_PEAK_HI = 0.850


def parse_spectrum(path: Path) -> list[tuple[float, float, float, float]]:
    rows: list[tuple[float, float, float, float]] = []
    if not path.is_file():
        return rows
    with path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.split()
            if len(parts) < 4:
                continue
            try:
                lo, hi, y, err = map(float, parts[:4])
            except ValueError:
                continue
            rows.append((lo, hi, y, err))
    return rows


def sum_y(rows: list[tuple[float, float, float, float]]) -> float:
    return float(sum(y for _, _, y, _ in rows))


def sum_peak(rows: list[tuple[float, float, float, float]]) -> float:
    return float(
        sum(y for lo, hi, y, _ in rows if lo >= DE_PEAK_LO and hi <= DE_PEAK_HI)
    )


def theory_rel(teq_cm: float) -> float:
    return float(np.exp(-teq_cm / LAMBDA_CM))


def main() -> None:
    results = []
    for site in SITES:
        d = BASE / site["dir"]
        de = parse_spectrum(d / "de.out")
        he = parse_spectrum(d / "neutron_he3.out")
        results.append(
            {
                **site,
                "deposit": sum_y(de),
                "deposit_peak": sum_peak(de),
                "he3_flux": sum_y(he),
            }
        )

    # 主比較量: He-3 T-Deposit（検出器応答）。地上=0 なら He-3 フラックスにフォールバックしない
    # （物理量が違うため）。地上 deposit が極小でもそのまま相対化する。
    d0 = results[0]["deposit"]
    f0 = results[0]["he3_flux"]
    if d0 <= 0 and f0 <= 0:
        raise SystemExit("ground He-3 response is zero — cannot normalize")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "地点",
        "コンクリート_cm",
        "土_cm",
        "等価コンクリート_cm",
        "PHITS_He3_Deposit",
        "PHITS_He3_DepositPeak",
        "PHITS_Deposit_相対_地上1",
        "PHITS_He3_フラックス",
        "PHITS_He3Flux_相対_地上1",
        "理論_A0exp_相対",
        "測定_相対_地上1",
        "測定_CPS",
        "備考",
    ]
    rows_out = []
    for r in results:
        notes = []
        if r["deposit"] <= 0:
            notes.append("Deposit統計ゼロ（厚い遮蔽 or ヒストリ不足）")
        if d0 > 0 and r["deposit"] > d0 * 1.5:
            notes.append("Depositが地上より大きい（熱化でHe-3感度上昇の可能性）")
        rel_de = (r["deposit"] / d0) if d0 > 0 else float("nan")
        rel_fl = (r["he3_flux"] / f0) if f0 > 0 else float("nan")
        rows_out.append(
            {
                "地点": r["label"],
                "コンクリート_cm": f"{r['concrete_cm']:.1f}",
                "土_cm": f"{r['soil_cm']:.1f}",
                "等価コンクリート_cm": f"{r['teq_cm']:.1f}",
                "PHITS_He3_Deposit": f"{r['deposit']:.6g}",
                "PHITS_He3_DepositPeak": f"{r['deposit_peak']:.6g}",
                "PHITS_Deposit_相対_地上1": f"{rel_de:.6g}",
                "PHITS_He3_フラックス": f"{r['he3_flux']:.6g}",
                "PHITS_He3Flux_相対_地上1": f"{rel_fl:.6g}",
                "理論_A0exp_相対": f"{theory_rel(r['teq_cm']):.6f}",
                "測定_相対_地上1": f"{r['cps'] / results[0]['cps']:.6f}",
                "測定_CPS": f"{r['cps']:.8f}",
                "備考": "；".join(notes),
            }
        )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows_out)
    print(f"wrote {OUT_CSV}")

    x = np.array([r["teq_cm"] for r in results])
    y_de = np.array([(r["deposit"] / d0) if d0 > 0 else np.nan for r in results])
    y_fl = np.array([(r["he3_flux"] / f0) if f0 > 0 else np.nan for r in results])
    y_meas = np.array([r["cps"] / results[0]["cps"] for r in results])
    x_th = np.linspace(0, max(520.0, float(x.max()) + 20), 400)
    y_th = np.exp(-x_th / LAMBDA_CM)

    for logy, path in ((False, OUT_FIG), (True, OUT_FIG_LOG)):
        fig, ax = plt.subplots(figsize=(8.6, 5.2))
        ax.plot(
            x_th,
            y_th,
            color="#888888",
            lw=2.0,
            label=f"理論  exp(-x/{LAMBDA_CM:.1f} cm)",
        )
        ax.plot(x, y_meas, "o", ms=9, color="#C0392B", label="測定 CPS (地上=1)", zorder=3)
        ax.plot(
            x,
            y_de,
            "s",
            ms=8,
            color="#2471A3",
            label="PHITS He-3 Deposit (地上=1)",
            zorder=3,
        )
        ax.plot(
            x,
            y_fl,
            "^",
            ms=8,
            color="#1E8449",
            label="PHITS He-3 内フラックス (地上=1)",
            zorder=3,
        )
        for r, yp in zip(results, y_fl):
            ax.annotate(
                r["label"],
                (r["teq_cm"], yp if yp > 0 else 1e-4),
                textcoords="offset points",
                xytext=(6, 4),
                fontsize=9,
                fontproperties=_JP_FONT,
            )
        ax.set_xlabel("等価コンクリート厚さ [cm]", fontproperties=_JP_FONT)
        ax.set_ylabel("相対値 (地上 = 1)", fontproperties=_JP_FONT)
        title = "図11比較: 測定 / 理論 / PHITS (He-3+SUS304)"
        if logy:
            ax.set_yscale("log")
            ax.set_ylim(1e-5, max(2.0, float(np.nanmax(y_de)) * 1.3))
            title += " (片対数)"
        else:
            ymax = max(1.15, float(np.nanmax(np.concatenate([y_de, y_fl, y_meas]))) * 1.15)
            ax.set_ylim(0, ymax)
        ax.set_xlim(-10, 540)
        ax.set_title(title, fontproperties=_JP_FONT)
        ax.legend(frameon=False, loc="upper right", prop=_JP_FONT, fontsize=8)
        for t in ax.get_xticklabels() + ax.get_yticklabels():
            t.set_fontproperties(_JP_FONT)
        fig.tight_layout()
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=200, bbox_inches="tight")
        plt.close(fig)
        print(f"wrote {path}")

    print("\nsummary:")
    for row in rows_out:
        print(
            f"  {row['地点']:6s}  Deposit相対={row['PHITS_Deposit_相対_地上1']:>10s}  "
            f"Flux相対={row['PHITS_He3Flux_相対_地上1']:>10s}  "
            f"theory={row['理論_A0exp_相対']:>8s}  meas={row['測定_相対_地上1']:>8s}  "
            f"{row['備考']}"
        )


if __name__ == "__main__":
    main()
