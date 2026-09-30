#!/usr/bin/env python3
"""最終レポート用の図（fig04, fig05, fig08）を作る。

fig04: 熱中性子 D1/d1 の実測と単純指数減衰（λ=60 cm）
fig05: MeV 中性子 D2/d2 の実測と単純指数減衰（λ=60 cm）
fig08: MeV 中性子 D2/d2 の実測と多成分モデル f1+f2+f3（誤差棒は統計と置き場所の系統 4.75% の二乗和）

実行: python3 make_figures.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator, MultipleLocator

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "最終発表_20260825"))

import _plot_mca as pm  # noqa: E402
from theory_modufy_curves import components_for, plot_f123  # noqa: E402

OUT = HERE / "figures"
FLUX_CSV = ROOT / "測定_20260818" / "denoised_runs" / "peak764_cut200" / "tables" / "フラックス_地点まとめ.csv"
LAMBDA_CM = 60.0
FLUX_SYS_FRAC = 0.0475
TOTAL_COLOR = "#7B3294"

plt.rcParams.update(
    {
        "font.family": "Hiragino Sans",
        "axes.unicode_minus": False,
        "figure.dpi": 120,
        "savefig.dpi": 180,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "grid.linestyle": "--",
    }
)

LABELS = {
    "D1": "D1（熱・大径）",
    "d1": "d1（熱・小径）",
    "D2": "D2（MeV・大径）",
    "d2": "d2（MeV・小径）",
}

SITE_OFFSETS = {
    "地上": (10, 8, "left", "bottom"),
    "testhole": (0, -12, "center", "top"),
    "PF": (10, -6, "left", "top"),
    "BT": (-10, 12, "right", "bottom"),
    "Linac3": (10, -14, "left", "top"),
    "K2KBL": (-10, -14, "right", "top"),
    "PS": (-12, -12, "right", "top"),
    "KEKB": (10, 12, "left", "bottom"),
}
SITE_NAMES = {"testhole": "テストホール", "K2KBL": "K2K"}


def _is_facility_point(point: dict) -> bool:
    label = point.get("label") or ""
    site = point.get("site") or ""
    if label in pm.ANALYSIS_EXCLUDE_SITES or site in pm.ANALYSIS_EXCLUDE_SITES:
        return False
    if site in pm.FLUX_INDOOR_SITES or "管理棟" in site or "管理棟" in label:
        return False
    return label in pm.FACILITY_SITES or site == "地上"


def _points(flux: dict, detectors: tuple[str, ...]) -> dict[str, list[dict]]:
    out = {}
    for det in detectors:
        pts = [p for p in pm._build_flux_points(det, absolute=True, flux=flux) if _is_facility_point(p)]
        if pts:
            out[det] = pts
    return out


def _annotate(ax, by_det: dict[str, list[dict]]) -> None:
    best: dict[str, dict] = {}
    for pts in by_det.values():
        for pt in pts:
            lab = pt.get("label") or pt.get("site", "")
            if lab not in best or pt["y"] > best[lab]["y"]:
                best[lab] = pt
    for lab, pt in best.items():
        dx, dy, ha, va = SITE_OFFSETS.get(lab, (8, 8, "left", "bottom"))
        ax.annotate(
            SITE_NAMES.get(lab, lab),
            (pt["x"], pt["y"]),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=9,
            ha=ha,
            va=va,
            color="#333333",
            zorder=6,
        )


def _errorbars(ax, by_det: dict[str, list[dict]], *, with_sys: bool) -> None:
    for det, pts in by_det.items():
        st = pm.DETECTOR_STYLE[det]
        y = np.array([p["y"] for p in pts])
        yerr = np.array([p["y_err"] for p in pts])
        if with_sys:
            yerr = np.hypot(yerr, FLUX_SYS_FRAC * y)
        ax.errorbar(
            [p["x"] for p in pts],
            y,
            xerr=[p["x_err"] for p in pts],
            yerr=yerr,
            fmt=st["marker"],
            color=st["color"],
            ms=st["ms"] - 1,
            linestyle="none",
            capsize=2.5,
            elinewidth=0.8,
            zorder=4,
            label=LABELS[det],
        )


def _axes(ax, title: str, ylabel: str, y_lo: float, y_hi: float, x_max: float) -> None:
    ax.set_yscale("log")
    ax.set_ylim(y_lo, y_hi)
    ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=8))
    ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=(0.2, 0.5, 2, 5)))
    ax.set_xlim(-20.0, x_max)
    ax.axvline(0, color="#DDDDDD", lw=0.6, zorder=0)
    ax.xaxis.set_major_locator(MultipleLocator(100))
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]")
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontsize=12, pad=8)


def plot_simple(flux: dict, detectors: tuple[str, ...], title: str, stem: str, ref_det: str) -> Path:
    by_det = _points(flux, detectors)
    ground = [p for p in by_det[ref_det] if p.get("label") == "地上" or p.get("site") == "地上"]
    a0 = ground[0]["y"]
    x_max = pm._kek_axis_x_max()
    x_c = np.linspace(0.0, x_max, 500)

    fig, ax = plt.subplots(figsize=(10.0, 5.8))
    ax.plot(x_c, a0 * np.exp(-x_c / LAMBDA_CM), color="#555555", lw=2.0,
            label=rf"単純指数減衰 $A_0e^{{-t/\lambda}}$（$\lambda={LAMBDA_CM:.0f}$ cm）", zorder=2)
    _errorbars(ax, by_det, with_sys=False)
    ys = [p["y"] for pts in by_det.values() for p in pts]
    _axes(ax, title, r"中性子フラックス $\phi$ [cm$^{-2}$ s$^{-1}$]", min(ys) * 0.25, max(ys) * 3.0, x_max)
    _annotate(ax, by_det)
    ax.legend(frameon=True, framealpha=0.92, fontsize=10, loc="upper right")
    out = OUT / f"{stem}.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def plot_model(flux: dict) -> Path:
    by_det = _points(flux, ("D2", "d2"))
    x_max = pm._kek_axis_x_max()
    x_c = np.linspace(0.0, x_max, 500)
    f1, f2, f3 = components_for("mev", x_c)

    fig, ax = plt.subplots(figsize=(10.0, 5.8))
    plot_f123(ax, x_c, f1, f2, f3)
    ax.plot(x_c, f1 + f2 + f3, color=TOTAL_COLOR, lw=2.4, label=r"モデル $f_1+f_2+f_3$", zorder=3)
    _errorbars(ax, by_det, with_sys=True)
    _axes(ax, "MeV 中性子（D2, d2）", r"中性子フラックス $\phi$ [cm$^{-2}$ s$^{-1}$]", 1e-6, 6e-3, x_max)
    _annotate(ax, by_det)
    ax.legend(frameon=True, framealpha=0.92, fontsize=9.5, loc="upper right")
    out = OUT / "fig08_mev_theory.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    pm.FLUX_SUMMARY_CSV = FLUX_CSV
    flux = pm.load_flux_summary()
    OUT.mkdir(parents=True, exist_ok=True)
    print(plot_simple(flux, ("D1", "d1"), "熱中性子（D1, d1）", "fig04_thermal_abs", "D1"))
    print(plot_simple(flux, ("D2", "d2"), "MeV 中性子（D2, d2）", "fig05_mev_abs", "D2"))
    print(plot_model(flux))


if __name__ == "__main__":
    main()
