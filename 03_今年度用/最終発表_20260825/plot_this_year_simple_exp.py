#!/usr/bin/env python3
"""今年度計測：単純 e^{-x/λ}（λ=39.2 cm）と実測 3 点の比較。

上段: 理論曲線 + 実測プロット（絶対フラックス）
下段: 乖離倍率（実測/理論）の棒グラフ（上段と同一横軸で対応）

地点: 地上 / PF / Linac3（等価コンクリート厚 0 / 105 / 300 cm）
データ: 測定_20260818（D1 wall 窓、相対_D1地上 → Φ₀ で絶対化）
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator, MultipleLocator

OUT = Path(__file__).resolve().parent / "figures"
LAM_CONC_CM = 39.2  # 教材混合則（equiv_shielding 推奨値）
# D1 wall 窓の地上絶対フラックス [n/cm²/s]（相対×Φ₀ で絶対化）
PHI0 = 0.00131715

SITES = [
    {"label": "地上", "t_eq_cm": 0.0, "rel": 1.0000, "err": 0.0234},
    {"label": "PF", "t_eq_cm": 105.0, "rel": 0.4343, "err": 0.00535},
    {"label": "Linac3", "t_eq_cm": 300.0, "rel": 0.2106, "err": 0.00495},
]

BLUE, RED, ORANGE, GRAY = "#4C78A8", "#E45756", "#F58518", "#666666"

plt.rcParams.update(
    {
        "font.family": "Hiragino Sans",
        "axes.unicode_minus": False,
        "mathtext.fontset": "dejavusans",
        "figure.dpi": 140,
        "savefig.dpi": 200,
        "axes.grid": True,
        "grid.alpha": 0.35,
        "grid.linestyle": "--",
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "legend.fontsize": 9.5,
    }
)


def _theory_rel(t_cm: np.ndarray | float) -> np.ndarray | float:
    return np.exp(-np.asarray(t_cm, dtype=float) / LAM_CONC_CM)


def _format_ratio(ratio: float) -> str:
    if ratio >= 10:
        return f"{ratio:.0f}×"
    if ratio >= 2:
        return f"{ratio:.1f}×"
    return f"{ratio:.2f}×"


def _plot(*, logy: bool, out_stem: str) -> None:
    t = np.array([s["t_eq_cm"] for s in SITES], dtype=float)
    y_meas = np.array([s["rel"] for s in SITES], dtype=float) * PHI0
    yerr = np.array([s["err"] for s in SITES], dtype=float) * PHI0
    y_th = _theory_rel(t) * PHI0
    ratios = y_meas / y_th

    t_fit = np.linspace(0.0, 340.0, 400)
    y_fit = _theory_rel(t_fit) * PHI0

    fig, (ax_flux, ax_ratio) = plt.subplots(
        2,
        1,
        figsize=(8.4, 6.8),
        sharex=True,
        gridspec_kw={"height_ratios": [1.45, 1.0], "hspace": 0.06},
    )
    fig.subplots_adjust(left=0.14, right=0.97, top=0.96, bottom=0.10)

    # --- 上段: 理論曲線 + 実測 ---
    ax_flux.plot(
        t_fit,
        y_fit,
        color=BLUE,
        lw=2.0,
        label="理論値",
        zorder=2,
    )
    ax_flux.errorbar(
        t,
        y_meas,
        yerr=yerr,
        fmt="o",
        color=RED,
        ms=10,
        capsize=4,
        capthick=1.4,
        elinewidth=1.4,
        zorder=4,
        label="実測",
    )
    # 理論上の対応点（曲線上）も小さく示す（凡例には出さない）
    ax_flux.plot(t, y_th, "s", color=BLUE, ms=7, zorder=3)

    for s, ti, yi in zip(SITES, t, y_meas):
        dy = 10 if s["label"] != "Linac3" else -18
        ax_flux.annotate(
            s["label"],
            (ti, yi),
            textcoords="offset points",
            xytext=(8, dy),
            fontsize=9,
            color=RED,
        )

    # 上→下の対応を示す縦線
    for ti in t:
        ax_flux.axvline(ti, color="#CCCCCC", lw=0.9, ls=":", zorder=1)
        ax_ratio.axvline(ti, color="#CCCCCC", lw=0.9, ls=":", zorder=1)

    ylab = r"フラックス $\Phi$ [cm$^{-2}$ s$^{-1}$]"
    ax_flux.set_ylabel(ylab + ("（片対数）" if logy else ""))
    ax_flux.legend(frameon=False, loc="upper right")

    if logy:
        ax_flux.set_yscale("log")
        ax_flux.set_ylim(min(float(y_th.min()), float(y_meas.min())) * 0.35, PHI0 * 1.8)
        ax_flux.yaxis.set_major_locator(LogLocator(base=10.0))
    else:
        ax_flux.set_ylim(0, PHI0 * 1.15)

    # --- 下段: 乖離倍率（上段と同位置の棒）---
    bar_w = 28.0
    bars = ax_ratio.bar(
        t,
        ratios,
        width=bar_w,
        color=ORANGE,
        alpha=0.9,
        edgecolor="white",
        linewidth=0.8,
        zorder=2,
        align="center",
    )
    ax_ratio.axhline(1.0, color=GRAY, lw=1.2, ls="--", zorder=1, label="一致（1×）")

    for bar, ratio in zip(bars, ratios):
        ax_ratio.text(
            bar.get_x() + bar.get_width() / 2,
            ratio * 1.18,
            _format_ratio(float(ratio)),
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
            color="#B35C00",
        )

    ax_ratio.set_ylabel("乖離倍率（実測 / 理論）")
    ax_ratio.set_xlabel("等価コンクリート厚 $t_\\mathrm{eq}$ [cm]")
    ax_ratio.set_yscale("log")
    ax_ratio.set_ylim(0.45, float(ratios.max()) * 2.8)
    ax_ratio.yaxis.set_major_locator(LogLocator(base=10.0))
    ax_ratio.set_xlim(-15, 340)
    ax_ratio.xaxis.set_major_locator(MultipleLocator(50))
    ax_ratio.xaxis.set_minor_locator(MultipleLocator(10))

    suffix = "_片対数" if logy else ""
    out = OUT / f"{out_stem}{suffix}.png"
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight", pad_inches=0.10)
    plt.close(fig)
    print(f"saved {out}")


def main() -> None:
    for logy in (False, True):
        _plot(logy=logy, out_stem="03_今年_単純指数_3点_乖離")


if __name__ == "__main__":
    main()
