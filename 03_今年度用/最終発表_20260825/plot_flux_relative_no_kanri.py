#!/usr/bin/env python3
"""図18相当: 相対フラックス（D1 地上 = 1）・管理棟除外・地上ラベルを枠内へ。

データ: 測定_20260818（peak764 / 図18 と同系統のフラックス_地点まとめ.csv）
出力: figures/18_全地点_フラックス_相対_検出器比較_片対数_管理棟除く.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator, MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import _plot_mca as pm  # noqa: E402
from theory_modufy_curves import legend_upper_right, plot_f123, thermal_components  # noqa: E402

OUT = Path(__file__).resolve().parent / "figures"
FLUX_CSV = (
    ROOT
    / "測定_20260818"
    / "denoised_runs"
    / "peak764_cut200"
    / "tables"
    / "フラックス_地点まとめ.csv"
)
OUT_STEM = "18_全地点_フラックス_相対_検出器比較_片対数_管理棟除く"


def _is_facility_point(point: dict) -> bool:
    """施設減衰比較用の点（管理棟・除外地点を落とす）。"""
    label = point.get("label") or ""
    site = point.get("site") or ""
    if label in pm.ANALYSIS_EXCLUDE_SITES or site in pm.ANALYSIS_EXCLUDE_SITES:
        return False
    if site in pm.FLUX_INDOOR_SITES or "管理棟" in site or "管理棟" in label:
        return False
    return label in pm.FACILITY_SITES or site == "地上"


def _annotate_site_names(ax, points: list[dict]) -> None:
    """地点名注釈。地上は枠内（点の右下）に置く。"""
    by_site: dict[str, list[dict]] = {}
    for p in points:
        by_site.setdefault(p["site"], []).append(p)

    # 左余白あり（xlim≈-20）前提。地上は点群の右下で曲線・凡例と重ならない位置
    offsets = {
        "地上": (22, -22, "left", "top"),
        "testhole": (14, -12, "left", "top"),
        "PF": (12, 14, "left", "bottom"),
        "Linac3": (14, -18, "left", "top"),
        "BT": (-14, 12, "right", "bottom"),
        "PS": (-14, -16, "right", "top"),
        "KEKB": (-14, 10, "right", "bottom"),
        "linac": (-14, 10, "right", "bottom"),
    }

    for site_pts in by_site.values():
        lab = site_pts[0]["label"]
        x = site_pts[0]["x"]
        ys = [p["y"] for p in site_pts if p["y"] > 0]
        if not ys:
            continue
        # 地上は基準点（y≈1）付近に付け、上端クリップを避ける
        if lab == "地上":
            y = min(ys, key=lambda v: abs(v - 1.0))
        else:
            y = max(ys)
        dx, dy, ha, va = offsets.get(lab, (10, 10, "left", "bottom"))
        ax.annotate(
            lab,
            (x, y),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=8,
            ha=ha,
            va=va,
            color="#222222",
            fontweight="bold",
            zorder=6,
            clip_on=False,
        )


def main() -> None:
    if not FLUX_CSV.exists():
        raise FileNotFoundError(FLUX_CSV)

    pm.FLUX_SUMMARY_CSV = FLUX_CSV
    flux = pm.load_flux_summary()

    plotted: list[str] = []
    for det in ("D1", "D2", "d1", "d2"):
        pts = [
            p
            for p in pm._build_flux_points_ground_norm(det, flux=flux)
            if _is_facility_point(p)
        ]
        if len(pts) < 2:
            print(f"skip {det}: 地点不足（{len(pts)}点）")
            continue
        plotted.append(det)

    if len(plotted) < 2:
        raise RuntimeError(f"重ねる検出器不足: {plotted}")

    x_max = pm._kek_axis_x_max()
    x_c = np.linspace(0, x_max, 900)
    f1, f2, f3 = thermal_components(x_c)
    norm = float(f1[0] + f2[0] + f3[0])
    f1, f2, f3 = f1 / norm, f2 / norm, f3 / norm

    fig, ax = plt.subplots(figsize=pm.EQUIV_FIGSIZE)
    fig.subplots_adjust(**pm.EQUIV_SUBPLOT)
    plot_f123(ax, x_c, f1, f2, f3)
    # 図11系と同じく地上(x=0)が左枠に張り付かない余白
    x_left = -20.0
    ax.axvline(0, color="#CCCCCC", lw=0.8, zorder=1)

    all_pts: list[dict] = []
    for det in plotted:
        pts = [
            p
            for p in pm._build_flux_points_ground_norm(det, flux=flux)
            if _is_facility_point(p)
        ]
        st = pm.DETECTOR_STYLE[det]
        ax.plot(
            [p["x"] for p in pts],
            [p["y"] for p in pts],
            linestyle="none",
            marker=st["marker"],
            color=st["color"],
            ms=st["ms"],
            zorder=3,
            label=st["label"],
        )
        all_pts.extend(pts)

    _annotate_site_names(ax, all_pts)

    ax.set_xlim(x_left, x_max)
    ax.set_xlabel(r"等価コンクリート厚さ [cm]（$t_{\mathrm{eq}}=X/\rho_c$）")
    ax.set_ylabel("相対フラックス（D1 地上 = 1）")
    ax.set_yscale("log")
    ax.set_ylim(1e-2, pm.EQUIV_Y_PAD_LOGY)
    ax.yaxis.set_major_locator(LogLocator(base=10.0))
    ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))
    ax.xaxis.set_major_locator(MultipleLocator(100))
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    ax.grid(True, which="major", alpha=0.35, linestyle="--")
    ax.grid(True, which="minor", alpha=0.18, linestyle=":")
    legend_upper_right(ax, fontsize=10.0)

    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{OUT_STEM}.png"
    fig.savefig(out, bbox_inches=None)
    plt.close(fig)
    print(f"saved {out}")
    print(f"  detectors={plotted}")
    print(f"  sites={sorted({p['label'] for p in all_pts})}")


if __name__ == "__main__":
    main()
