#!/usr/bin/env python3
"""図18 完全理論版（絶対の.csv + modufy 理論式 f₁+f₂+f₃）。

元の fig18（λ=60 のみ）は plot_fig18_thermal_mev_lam60.py が出力する別ファイル。
本スクリプトは上書きせず、完全理論付きの新規 PNG を出力する。

出力:
  figures/18_全地点_フラックス_絶対_熱中性子_D1d1_完全理論.png
  figures/18_全地点_フラックス_絶対_MeV_D2d2_完全理論.png
  figures/18_全地点_フラックス_絶対_熱中性子_D1d1_完全理論_系統475.png
  figures/18_全地点_フラックス_絶対_MeV_D2d2_完全理論_系統475.png
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator, MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import _plot_mca as pm  # noqa: E402
from theory_modufy_curves import (  # noqa: E402
    components_for,
    mev_complete_theory,
    plot_f123,
    thermal_complete_theory,
)

OUT = Path(__file__).resolve().parent / "figures"
FLUX_CSV = (
    ROOT
    / "測定_20260818"
    / "figures"
    / "地点別_denoised"
    / "stages"
    / "03_peak764_cut200"
    / "theory_16_19"
    / "絶対の.csv"
)

COMPLETE_COLOR = "#7B3294"
COMPLETE_LW = 2.4
FLUX_SYS_FRAC = 0.0475  # フラックス系統誤差（各観測点の φ に対する相対値）

GROUPS = (
    {
        "detectors": ("D1", "d1"),
        "title": "熱中性子（D1, d1）",
        "stem": "18_全地点_フラックス_絶対_熱中性子_D1d1_完全理論",
        "labels": {
            "D1": "D1（熱・大径・SN1715）",
            "d1": "d1（熱・小径・SN2162）",
        },
        "theory_fn": thermal_complete_theory,
        "kind": "thermal",
    },
    {
        "detectors": ("D2", "d2"),
        "title": "MeV 中性子（D2, d2）",
        "stem": "18_全地点_フラックス_絶対_MeV_D2d2_完全理論",
        "labels": {
            "D2": "D2（MeV・大径・SN1715）",
            "d2": "d2（MeV・小径・SN2162）",
        },
        "theory_fn": mev_complete_theory,
        "kind": "mev",
    },
)

EXCLUDE_DETECTORS = frozenset({"literature"})
EXCLUDE_SITES = frozenset({"神岡"})

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


def _load_abs_csv(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            det = (row.get("detector") or "").strip()
            site = (row.get("site") or "").strip()
            if det in EXCLUDE_DETECTORS or site in EXCLUDE_SITES:
                continue
            rows.append(
                {
                    "detector": det,
                    "site": site,
                    "label": site,
                    "x": float(row["x"]),
                    "y": float(row["y"]),
                    "x_err": float(row["x_err"] or 0.0),
                    "y_err": float(row["y_err"] or 0.0),
                }
            )
    return rows


def _total_y_err(y: float, y_stat: float) -> float:
    """統計誤差と系統誤差（4.75%×φ）を二乗和で合成。"""
    y_sys = FLUX_SYS_FRAC * y
    return float(np.hypot(y_stat, y_sys))


def _apply_flux_sys_err(rows: list[dict]) -> list[dict]:
    out: list[dict] = []
    for row in rows:
        r = dict(row)
        r["y_err"] = _total_y_err(r["y"], r["y_err"])
        out.append(r)
    return out


def _flux_ylabel(*, include_sys_note: bool) -> str:
    base = r"中性子フラックス $\phi$ [n/cm$^2$/s]"
    if include_sys_note:
        return base + "\n（誤差棒: 統計＋系統 4.75%）"
    return base


def _plot_theory_layers(
    ax,
    x_c: np.ndarray,
    *,
    y_complete: np.ndarray,
    f1: np.ndarray,
    f2: np.ndarray,
    f3: np.ndarray,
) -> None:
    plot_f123(ax, x_c, f1, f2, f3)
    ax.plot(
        x_c,
        y_complete,
        color=COMPLETE_COLOR,
        lw=COMPLETE_LW,
        zorder=2.5,
        label=r"理論式（$f_1+f_2+f_3$）",
    )


def _apply_log_y(ax, y_vals: list[float]) -> None:
    y_lo = max(1e-6, min(y_vals) * 0.25)
    y_hi = max(y_vals) * 3.0
    ax.set_yscale("log")
    ax.set_ylim(y_lo, y_hi)
    ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=8))
    ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=(0.2, 0.5, 2, 5)))


def _legend_upper_right(ax) -> None:
    ax.legend(
        frameon=True,
        framealpha=0.92,
        fontsize=10.0,
        loc="upper right",
        borderaxespad=0.8,
        handlelength=2.0,
        labelspacing=0.45,
    )


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


def _plot_group(all_rows: list[dict], group: dict, *, include_sys_note: bool = False) -> Path:
    detectors = group["detectors"]
    by_det: dict[str, list[dict]] = {}
    all_pts: list[dict] = []
    for det in detectors:
        pts = [r for r in all_rows if r["detector"] == det]
        if not pts:
            continue
        by_det[det] = pts
        all_pts.extend(pts)

    if len(all_pts) < 2:
        raise RuntimeError(f"{group['title']}: 測定点不足")

    x_max = pm._kek_axis_x_max()
    x_c = np.linspace(0.0, x_max, 500)
    y_complete = group["theory_fn"](x_c)
    f1, f2, f3 = components_for(group["kind"], x_c)

    fig, ax = plt.subplots(figsize=(10.6, 6.4))
    fig.subplots_adjust(left=0.11, right=0.97, top=0.90, bottom=0.12)

    _plot_theory_layers(
        ax,
        x_c,
        y_complete=y_complete,
        f1=f1,
        f2=f2,
        f3=f3,
    )

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
    y_vals.extend(y_complete[y_complete > 0].tolist())
    y_vals.extend(f1[f1 > 0].tolist())
    y_vals.extend(f2[f2 > 0].tolist())
    y_vals.extend(f3[f3 > 0].tolist())
    _apply_log_y(ax, y_vals)

    ax.set_xlim(-20.0, x_max)
    ax.axvline(0, color="#DDDDDD", lw=0.6, zorder=0)
    ax.xaxis.set_major_locator(MultipleLocator(100))
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]（$X/\rho_c$）")
    ax.set_ylabel(_flux_ylabel(include_sys_note=include_sys_note))
    ax.set_title(group["title"], fontsize=12, pad=8)
    _annotate_sites(ax, all_pts)
    _legend_upper_right(ax)

    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{group['stem']}.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    if not FLUX_CSV.exists():
        raise FileNotFoundError(FLUX_CSV)
    rows = _load_abs_csv(FLUX_CSV)
    rows_sys = _apply_flux_sys_err(rows)

    for group in GROUPS:
        out = _plot_group(rows, group, include_sys_note=False)
        print(f"saved {out}")

        group_sys = {**group, "stem": f"{group['stem']}_系統475"}
        out_sys = _plot_group(rows_sys, group_sys, include_sys_note=True)
        print(f"saved {out_sys}")


if __name__ == "__main__":
    main()
