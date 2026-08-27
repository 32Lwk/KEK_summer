#!/usr/bin/env python3
"""図18 分割（熱 D1/d1・MeV D2/d2）: f₁,f₂,f₃ 成分曲線。

出力:
  figures/18_全地点_フラックス_絶対_熱中性子_D1d1_λ60.png
  figures/18_全地点_フラックス_絶対_MeV_D2d2_λ60.png
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
from theory_modufy_curves import components_for, plot_f123  # noqa: E402

OUT = Path(__file__).resolve().parent / "figures"
FLUX_CSV = (
    ROOT
    / "測定_20260818"
    / "denoised_runs"
    / "peak764_cut200"
    / "tables"
    / "フラックス_地点まとめ.csv"
)

GROUPS = (
    {
        "detectors": ("D1", "d1"),
        "title": "熱中性子（D1, d1）",
        "stem": "18_全地点_フラックス_絶対_熱中性子_D1d1_λ60",
        "labels": {
            "D1": "D1（熱・大径・SN1715）",
            "d1": "d1（熱・小径・SN2162）",
        },
        "kind": "thermal",
    },
    {
        "detectors": ("D2", "d2"),
        "title": "MeV 中性子（D2, d2）",
        "stem": "18_全地点_フラックス_絶対_MeV_D2d2_λ60",
        "labels": {
            "D2": "D2（MeV・大径・SN1715）",
            "d2": "d2（MeV・小径・SN2162）",
        },
        "kind": "mev",
    },
)

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


def _is_facility_point(point: dict) -> bool:
    label = point.get("label") or ""
    site = point.get("site") or ""
    if label in pm.ANALYSIS_EXCLUDE_SITES or site in pm.ANALYSIS_EXCLUDE_SITES:
        return False
    if site in pm.FLUX_INDOOR_SITES or "管理棟" in site or "管理棟" in label:
        return False
    return label in pm.FACILITY_SITES or site == "地上"


def _annotate_sites(ax, points: list[dict]) -> None:
    offsets = {
        "地上": (10, 10, "left", "bottom"),
        "testhole": (10, -12, "left", "top"),
        "PF": (10, 12, "left", "bottom"),
        "Linac3": (10, -14, "left", "top"),
        "BT": (-10, 12, "right", "bottom"),
        "PS": (10, 14, "left", "bottom"),
        "K2KBL": (-10, 10, "right", "bottom"),
        "KEKB": (-10, -16, "right", "top"),
    }
    best: dict[str, dict] = {}
    for pt in points:
        lab = pt.get("label") or pt.get("site", "")
        if lab not in best or pt["y"] > best[lab]["y"]:
            best[lab] = pt
    for lab, pt in best.items():
        dx, dy, ha, va = offsets.get(lab, (8, 8, "left", "bottom"))
        ax.annotate(
            lab,
            (pt["x"], pt["y"]),
            xytext=(dx, dy),
            textcoords="offset points",
            fontsize=8,
            ha=ha,
            va=va,
            color="#333333",
            zorder=6,
        )


def _plot_group(flux: dict, group: dict) -> Path:
    detectors = group["detectors"]
    all_pts: list[dict] = []
    by_det: dict[str, list[dict]] = {}
    for det in detectors:
        pts = [
            p
            for p in pm._build_flux_points(det, absolute=True, flux=flux)
            if _is_facility_point(p)
        ]
        if not pts:
            continue
        by_det[det] = pts
        all_pts.extend(pts)

    if len(all_pts) < 2:
        raise RuntimeError(f"{group['title']}: 測定点不足")

    x_max = pm._kek_axis_x_max()
    x_c = np.linspace(0.0, x_max, 500)
    f1, f2, f3 = components_for(group["kind"], x_c)

    fig, ax = plt.subplots(figsize=(10.6, 6.4))
    fig.subplots_adjust(left=0.11, right=0.97, top=0.90, bottom=0.12)

    plot_f123(ax, x_c, f1, f2, f3)

    for det, pts in by_det.items():
        st = pm.DETECTOR_STYLE[det]
        ax.errorbar(
            [p["x"] for p in pts],
            [p["y"] for p in pts],
            xerr=[p["x_err"] for p in pts],
            yerr=[p["y_err"] for p in pts],
            fmt=st["marker"],
            color=st["color"],
            ms=st["ms"] - 1,
            linestyle="none",
            capsize=2.5,
            elinewidth=0.8,
            zorder=4,
            label=group["labels"].get(det, st["label"]),
        )

    y_vals = [p["y"] for p in all_pts if p["y"] > 0]
    y_vals.extend(f1[f1 > 0].tolist())
    y_vals.extend(f2[f2 > 0].tolist())
    y_vals.extend(f3[f3 > 0].tolist())
    y_lo = max(1e-5, min(y_vals) * 0.25)
    y_hi = max(y_vals) * 3.0
    ax.set_yscale("log")
    ax.set_ylim(y_lo, y_hi)
    ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=8))
    ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=(0.2, 0.5, 2, 5)))

    ax.set_xlim(-20.0, x_max)
    ax.axvline(0, color="#DDDDDD", lw=0.6, zorder=0)
    ax.xaxis.set_major_locator(MultipleLocator(100))
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]（$X/\rho_c$）")
    ax.set_ylabel(r"中性子フラックス $\phi$ [n/cm$^2$/s]")
    ax.set_title(group["title"], fontsize=12, pad=8)
    _annotate_sites(ax, all_pts)
    ax.legend(
        frameon=True,
        framealpha=0.92,
        fontsize=10.0,
        loc="upper right",
        borderaxespad=0.8,
        handlelength=2.0,
        labelspacing=0.45,
    )

    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{group['stem']}.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    if not FLUX_CSV.exists():
        raise FileNotFoundError(FLUX_CSV)
    pm.FLUX_SUMMARY_CSV = FLUX_CSV
    flux = pm.load_flux_summary()

    for group in GROUPS:
        out = _plot_group(flux, group)
        print(f"saved {out}")


if __name__ == "__main__":
    main()
