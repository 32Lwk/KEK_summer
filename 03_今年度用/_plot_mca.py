#!/usr/bin/env python3
"""今年度 MCA スペクトルのグラフを 測定_20260818/figures/ に書き出す。

重ね書きは live time [s] で割った CPS（比較可能）。ROI NET は表を参照。
"""

from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from mca_common import peak_clip as roi_peak_clip

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "測定_20260818"
TABLES = DATA / "tables"
FIG = DATA / "figures"

BLUE, RED, GREEN, GRAY = "#1F77B4", "#D62728", "#2CA02C", "#666666"
PALETTE = [BLUE, RED, GREEN, "#9467BD", "#8C564B", "#E377C2", "#17BECF"]
YLABEL = "計数率 [1/s / ch]"
YLABEL_SUM = "計数率 [1/s]"
CLIP_PAD = 0.002

plt.rcParams.update(
    {
        "font.family": "Hiragino Sans",
        "axes.unicode_minus": False,
        "mathtext.fontset": "dejavusans",
        "figure.dpi": 140,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "axes.grid": True,
        "grid.alpha": 0.35,
        "grid.linestyle": "--",
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "legend.fontsize": 10,
    }
)


def color_for(sid: str, i: int) -> str:
    sl = sid.lower()
    if "linac" in sl:
        return RED
    if "kanri1f" in sl:
        return PALETTE[3]
    if "kanri2f" in sid and sid.endswith("_d1"):
        return PALETTE[6]
    if "kanri2f" in sl and "0832" in sl:
        return GREEN
    if "kanri2f" in sl or ("kanri" in sl and "1f" not in sl):
        return BLUE
    if "hoshasen" in sl and sid.endswith("_d2"):
        return "#FF7F0E"
    if "hoshasen" in sl:
        return PALETTE[5]
    if "ground" in sl:
        return PALETTE[4]
    return PALETTE[i % len(PALETTE)]


def folder_name(場所: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", 場所)


def clip_title(clip: float) -> str:
    return f"クリップ {clip:.3f} /s"


def union_roi(series: list[dict]) -> tuple[int, int]:
    return min(s["roi_lo"] for s in series), max(s["roi_hi"] for s in series)


def load_spectrum() -> dict:
    with (TABLES / "測定記録.csv").open(encoding="utf-8") as f:
        recs = list(csv.DictReader(f))
    with (TABLES / "スペクトル.csv").open(encoding="utf-8") as f:
        spec = list(csv.DictReader(f))
    ch = np.array([int(r["channel"]) for r in spec])
    series = []
    for i, rec in enumerate(recs):
        sid = rec["id"]
        c = np.array([float(r[f"counts_{sid}"]) for r in spec])
        live = float(rec["live_s"])
        cps = c / live
        hours = live / 3600.0
        tlab = f"{hours:.1f} h" if live >= 3600 else f"{live/60:.1f} min"
        lo, hi = int(float(rec["roi_lo"])), int(float(rec["roi_hi"]))
        series.append(
            {
                "id": sid,
                "場所": rec["場所"],
                "c": cps,
                "e": np.sqrt(np.maximum(c, 0.0)) / live,
                "live": live,
                "lab": f"{rec['場所']}（{tlab}）",
                "color": color_for(sid, i),
                "roi_lo": lo,
                "roi_hi": hi,
                "roi_peak": int(float(rec.get("roi_peak") or 0)),
                "roi_net_cps": float(rec["roi_net_cps"]),
                "clip": roi_peak_clip(cps, lo, hi, pad=max(CLIP_PAD, 0.1 * float(np.max(cps[lo : hi + 1]) if hi >= lo else 0))),
            }
        )
    return {"ch": ch, "series": series}


def overlay_clip(d: dict) -> float:
    return max(s["clip"] for s in d["series"])


def low_clip(d: dict) -> float:
    m = (d["ch"] >= 1) & (d["ch"] <= 80)
    return max(float(np.max(s["c"][m])) for s in d["series"]) * 1.05


def overlay_step(ax, d: dict, mask=None, clip=None, log=False, lw=1.3) -> None:
    x = d["ch"] if mask is None else d["ch"][mask]
    for s in d["series"]:
        c = s["c"] if mask is None else s["c"][mask]
        if log:
            y = np.where(c > 0, c, np.nan)
            ax.step(x, y, where="mid", color=s["color"], lw=lw, label=s["lab"])
        else:
            step_spectrum(ax, x, c, s["color"], s["lab"], clip=clip, annotate=False)


def overlay_err(ax, d: dict, mask, ms=2.6) -> None:
    x = d["ch"][mask]
    for s in d["series"]:
        ax.errorbar(
            x, s["c"][mask], yerr=s["e"][mask],
            fmt="o", ms=ms, color=s["color"], label=s["lab"], elinewidth=0.6,
        )


def save(
    fig,
    name: str,
    folder: Path | None = None,
    pad_inches: float | None = None,
    bbox_inches: str | None = None,
) -> None:
    dest = folder if folder is not None else FIG
    dest.mkdir(parents=True, exist_ok=True)
    kw: dict = {}
    if pad_inches is not None:
        kw["pad_inches"] = pad_inches
    if bbox_inches == "none":
        kw["bbox_inches"] = None
    elif bbox_inches is not None:
        kw["bbox_inches"] = bbox_inches
    fig.savefig(dest / f"{name}.png", **kw)
    plt.close(fig)


def shade_roi(ax, lo: int, hi: int, label: str | None = None) -> None:
    ax.axvspan(lo, hi, color="#F4C7C3", alpha=0.45, zorder=0, label=label or f"ROI {lo}–{hi}")


def step_spectrum(ax, ch, c, color, label=None, clip=None, annotate=True) -> None:
    y = np.minimum(c, clip) if clip is not None else c
    ax.step(ch, y, where="mid", color=color, lw=1.4, label=label)
    if clip is not None:
        ax.set_ylim(0, clip)
        if annotate:
            n_hi = int(np.sum(c > clip))
            if n_hi:
                ax.text(
                    0.99,
                    0.97,
                    f"{n_hi} ch が {clip:.3f} 超",
                    transform=ax.transAxes,
                    ha="right",
                    va="top",
                    fontsize=8,
                    color=GRAY,
                )


def fig_full_linear(d: dict) -> None:
    lo, hi = union_roi(d["series"])
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d)
    ax.set_xlim(0, 511)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("全ch 線形")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "06_全ch_線形")

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, clip=overlay_clip(d))
    ax.set_xlim(0, 511)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"全ch {clip_title(overlay_clip(d))}")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "06b_全ch_線形_クリップ")

    m = d["ch"] >= 1
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, mask=m)
    shade_roi(ax, lo, hi)
    ax.set_xlim(1, 511)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("全ch 線形（ch0除く）")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "07_全ch_線形_ch0除く")

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, mask=m, clip=overlay_clip(d))
    shade_roi(ax, lo, hi)
    ax.set_xlim(1, 511)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"全ch {clip_title(overlay_clip(d))}（ch0除く）")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "07b_全ch_線形_ch0除く_クリップ")


def fig_low_ch(d: dict) -> None:
    m = (d["ch"] >= 1) & (d["ch"] <= 80)
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, mask=m, lw=1.6)
    ax.set_xlim(1, 80)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("低ch")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "01_低ch_線形")

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, mask=m, clip=low_clip(d), lw=1.6)
    ax.set_xlim(1, 80)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"低ch {clip_title(low_clip(d))}")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "01b_低ch_線形_クリップ")


def fig_full_log(d: dict) -> None:
    lo, hi = union_roi(d["series"])
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, log=True, lw=1.2)
    ax.set_yscale("log")
    ax.set_xlim(0, 511)
    ax.set_ylim(1e-5, 80)
    shade_roi(ax, lo, hi)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("対数")
    ax.legend(frameon=False, loc="upper right", fontsize=8)
    save(fig, "02_全ch_対数")


def fig_roi(d: dict) -> None:
    lo, hi = union_roi(d["series"])
    m = (d["ch"] >= lo) & (d["ch"] <= hi)
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_err(ax, d, m, ms=3.5)
    ax.set_xlim(lo, hi)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"ROI {lo}–{hi}")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "03_ROI")


def fig_bands(d: dict) -> None:
    labels = ["ch 0", "ch 1–20", "ch 21–149", "ROI", "ch 0 除く"]
    n = len(d["series"])
    x = np.arange(len(labels))
    w = 0.8 / n
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    ymax = 0
    for i, s in enumerate(d["series"]):
        slices = [
            (0, 1),
            (1, 21),
            (21, 150),
            (s["roi_lo"], s["roi_hi"] + 1),
            (1, 512),
        ]
        vals = [s["c"][lo:hi].sum() for lo, hi in slices]
        ymax = max(ymax, max(vals))
        ax.bar(x + (i - (n - 1) / 2) * w, vals, w, color=s["color"], label=s["lab"])
    ax.set_xticks(x, labels)
    ax.set_ylabel(YLABEL_SUM)
    ax.set_title("帯域")
    ax.legend(frameon=False, fontsize=8)
    ax.set_ylim(0, ymax * 1.18)
    save(fig, "04_帯域比較")


def fig_ratio(d: dict) -> None:
    if len(d["series"]) < 2:
        return
    ref = min(d["series"], key=lambda s: s["live"])
    m = (d["ch"] >= 1) & (d["ch"] <= 80) & (ref["c"] >= 20)
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    for s in d["series"]:
        if s["id"] == ref["id"]:
            continue
        t_ratio = s["live"] / ref["live"]
        ax.axhline(t_ratio, color=s["color"], lw=1.0, ls="--", label=f"時間比 {s['場所']} {t_ratio:.2f}")
        ax.plot(d["ch"][m], s["c"][m] / ref["c"][m], "o", ms=4, color=s["color"], label=f"カウント比 {s['場所']}")
    ax.set_xlim(1, 80)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(f"カウント比（対 {ref['場所']}）")
    ax.set_title("比（低ch）")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "05_比_低ch")


def _one_site(d: dict, s: dict) -> None:
    out = FIG / "地点別" / folder_name(s["場所"])
    out.mkdir(parents=True, exist_ok=True)
    ch, c, e = d["ch"], s["c"], s["e"]
    color = s["color"]
    clip = s["clip"]
    lo, hi = s["roi_lo"], s["roi_hi"]
    ctitle = clip_title(clip)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.step(ch, c, where="mid", color=color, lw=1.4)
    ax.set_xlim(0, 511)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("全ch 線形")
    save(fig, "全ch_線形", out)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    step_spectrum(ax, ch, c, color, clip=clip)
    ax.set_xlim(0, 511)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"全ch {ctitle}")
    save(fig, "全ch_線形_クリップ", out)

    m = ch >= 1
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.step(ch[m], c[m], where="mid", color=color, lw=1.4)
    shade_roi(ax, lo, hi)
    ax.set_xlim(1, 511)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("全ch 線形（ch0除く）")
    ax.legend(frameon=False)
    save(fig, "全ch_線形_ch0除く", out)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    step_spectrum(ax, ch[m], c[m], color, clip=clip)
    shade_roi(ax, lo, hi)
    ax.set_xlim(1, 511)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"全ch {ctitle}（ch0除く）")
    ax.legend(frameon=False)
    save(fig, "全ch_線形_ch0除く_クリップ", out)

    m80 = (ch >= 1) & (ch <= 80)
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.step(ch[m80], c[m80], where="mid", color=color, lw=1.4)
    ax.set_xlim(1, 80)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("低ch")
    save(fig, "低ch_線形", out)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    step_spectrum(ax, ch[m80], c[m80], color, clip=float(np.max(c[m80]) * 1.05))
    ax.set_xlim(1, 80)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("低ch クリップ")
    save(fig, "低ch_線形_クリップ", out)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    y = np.where(c > 0, c, np.nan)
    ax.step(ch, y, where="mid", color=color, lw=1.3)
    ax.set_yscale("log")
    ax.set_xlim(0, 511)
    ax.set_ylim(1e-5, 80)
    shade_roi(ax, lo, hi)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("対数")
    ax.legend(frameon=False, loc="upper right")
    save(fig, "全ch_対数", out)

    mroi = (ch >= lo) & (ch <= hi)
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.errorbar(ch[mroi], c[mroi], yerr=e[mroi], fmt="o", ms=3.5, color=color, elinewidth=0.8)
    ax.set_xlim(lo, hi)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"ROI {lo}–{hi}")
    save(fig, "ROI", out)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.errorbar(ch[mroi], np.minimum(c[mroi], clip), yerr=e[mroi], fmt="o", ms=3.5, color=color, elinewidth=0.8)
    ax.set_xlim(lo, hi)
    ax.set_ylim(0, clip)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"ROI {ctitle}")
    save(fig, "ROI_クリップ", out)


def fig_overview(d: dict) -> None:
    lo, hi = union_roi(d["series"])
    fig, axes = plt.subplots(2, 2, figsize=(10.6, 7.4), layout="constrained")
    fig.suptitle(f"MCA {len(d['series'])}測定", fontsize=14)

    ax = axes[0, 0]
    m = (d["ch"] >= 1) & (d["ch"] <= 80)
    overlay_step(ax, d, mask=m, lw=1.4)
    ax.set_xlim(1, 80)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("低ch")
    ax.legend(frameon=False, fontsize=7)

    ax = axes[0, 1]
    overlay_step(ax, d, log=True, lw=1.0)
    ax.set_yscale("log")
    ax.set_xlim(0, 511)
    ax.set_ylim(1e-5, 80)
    shade_roi(ax, lo, hi, label=None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("対数")

    ax = axes[1, 0]
    m = (d["ch"] >= lo) & (d["ch"] <= hi)
    overlay_err(ax, d, m, ms=3)
    ax.set_xlim(lo, hi)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"ROI {lo}–{hi}")
    ax.legend(frameon=False, fontsize=7)

    ax = axes[1, 1]
    labels = ["ch 0", "1–20", "21–149", "ROI", "ch0除く"]
    n = len(d["series"])
    x = np.arange(len(labels))
    w = 0.8 / n
    for i, s in enumerate(d["series"]):
        slices = [(0, 1), (1, 21), (21, 150), (s["roi_lo"], s["roi_hi"] + 1), (1, 512)]
        vals = [s["c"][a:b].sum() for a, b in slices]
        ax.bar(x + (i - (n - 1) / 2) * w, vals, w, color=s["color"], label=s["lab"])
    ax.set_xticks(x, labels)
    ax.set_ylabel(YLABEL_SUM)
    ax.set_title("帯域")
    ax.legend(frameon=False, fontsize=7)

    save(fig, "00_概要")


def _roi_net(d: dict, key: str) -> float:
    for s in d["series"]:
        if key in s["id"].lower():
            return s["roi_net_cps"]
    raise KeyError(key)


def fig_linac_ground(d: dict) -> None:
    """地上を左、縦軸上端を 1（地上で規格化）。"""
    i0, i1 = _roi_net(d, "ground"), _roi_net(d, "linac")
    labels = ["地上", "linac\n(コンクリート 150 cm)"]
    y = [1.0, i1 / i0]
    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    fig.subplots_adjust(left=0.22)
    ax.plot(x, y, "-o", color=RED, ms=10, lw=2.0, label="測定（地上=1）")
    for xi, yi in zip(x, y):
        ax.annotate(
            f"{yi:.4f}",
            (xi, yi),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=11,
        )
    ax.set_xticks(x, labels)
    ax.set_xlim(-0.4, 1.4)
    ax.set_ylim(0, 1.08)
    ax.set_xlabel("地点")
    ax.set_ylabel("相対 CPS_NET（地上 = 1）", labelpad=14)
    ax.legend(frameon=False)
    save(fig, "09_linac_地上", pad_inches=0.45)


def fig_linac_ground_theory(d: dict) -> None:
    """x<0 は空気、x>0 はコンクリートの指数減衰。空気の λ は昨年（熱中性子）。"""
    i0, i1 = _roi_net(d, "ground"), _roi_net(d, "linac")
    x_linac = 150.0
    y_linac = i1 / i0
    lam_c = x_linac / np.log(i0 / i1)
    lam_air = 1475.0 * 100.0  # 昨年: 管理棟1階→白根山・熱中性子 1475 m

    x_air = np.linspace(-40, 0, 200)
    y_air = np.exp(x_air / lam_air)
    x_c = np.linspace(0, 180, 400)
    y_c = np.exp(-x_c / lam_c)

    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    fig.subplots_adjust(left=0.26, right=0.90, top=0.86, bottom=0.18)
    ax.plot(
        x_air,
        y_air,
        color=BLUE,
        lw=1.8,
        label=rf"空気  $\lambda={lam_air/100:.0f}$ m",
    )
    ax.plot(
        x_c,
        y_c,
        color=GRAY,
        lw=1.8,
        label=rf"コンクリート  $\lambda={lam_c:.1f}$ cm",
    )
    ax.axvline(0, color="#BBBBBB", lw=0.8, zorder=1)
    ax.plot(
        [0, x_linac],
        [1.0, y_linac],
        "o",
        color=RED,
        ms=10,
        zorder=3,
        label="測定（地上=1）",
    )
    ax.annotate("地上  1.000", (0, 1.0), textcoords="offset points", xytext=(10, -14), fontsize=10)
    ax.annotate(
        f"linac  {y_linac:.4f}",
        (x_linac, y_linac),
        textcoords="offset points",
        xytext=(-72, 10),
        fontsize=10,
    )
    ax.set_xlim(-40, 180)
    ax.set_ylim(0, 1.18)
    ax.set_xlabel("厚さ [cm]（左: 空気、右: コンクリート）")
    ax.set_ylabel("相対 CPS_NET（地上 = 1）", labelpad=12)
    ax.legend(frameon=False)
    save(fig, "10_linac_地上_理論フィット", bbox_inches="none")


# 等価コンクリート換算（教材の質量厚さ X=ρt）
# 理論: A = A0 * exp(-x / 0.77)、x は等価コンクリート厚 [m]
# 土: 関東ローム ≤4 m (ρ=1.35)、以深は常総粘土 (ρ=1.65)
RHO_CONCRETE = 2.3
RHO_LOAM = 1.35
RHO_JOSO = 1.65
LOAM_MAX_CM = 400.0
LAMBDA_M = 0.77

# Book5 / ユーザー表の CPS。相対値は地上で規格化。
USER_CPS = {
    "地上": 0.52514597,
    "linac": 0.06478913,
    "BT": 0.11475671,
    "KEKB": 0.0399324,
    "PF": 0.25108616,
}


def _soil_mass_thickness(soil_cm: float) -> float:
    loam = min(max(soil_cm, 0.0), LOAM_MAX_CM)
    joso = max(0.0, soil_cm - LOAM_MAX_CM)
    return loam * RHO_LOAM + joso * RHO_JOSO


def _mass_thickness(concrete_cm: float, soil_cm: float) -> float:
    return concrete_cm * RHO_CONCRETE + _soil_mass_thickness(soil_cm)


def _equiv_concrete_cm_from_x(x_gcm2: float) -> float:
    return x_gcm2 / RHO_CONCRETE


def _theory_rel(x_eq_cm, a0: float = 1.0):
    """A = A0 * exp(-x/0.77)。x は等価コンクリート [m]。"""
    return a0 * np.exp(-(np.asarray(x_eq_cm, dtype=float) / 100.0) / LAMBDA_M)


def _site_shielding_d1() -> list[dict]:
    """層厚から X を算出し、ユーザー CPS と組み合わせる。"""
    sites = [
        {"label": "地上", "concrete_cm": 0.0, "soil_cm": 0.0, "note": "基準（屋外）"},
        {"label": "PF", "concrete_cm": 105.0, "soil_cm": 0.0, "note": ""},
        {"label": "linac", "concrete_cm": 150.0, "soil_cm": 0.0, "note": ""},
        {"label": "BT", "concrete_cm": 60.0, "soil_cm": 220.0, "note": "土はロームのみ（220 cm < 4 m）"},
        {
            "label": "KEKB",
            "concrete_cm": 80.0,
            "soil_cm": 670.0,
            "note": "ローム4 m + 常総2.7 m + コンクリ80 cm（Book5の117.25は桁誤り）",
        },
    ]
    for site in sites:
        site["X"] = _mass_thickness(site["concrete_cm"], site["soil_cm"])
        site["cps"] = USER_CPS[site["label"]]
        if not site["note"]:
            site["note"] = f"X={site['X']:.2f}"
    return sites


def fig_all_sites_equiv_concrete(d: dict | None = None, absolute: bool = False) -> None:
    """層厚換算 X + ユーザー CPS。理論 A0·exp(-x/0.77)。

    absolute=False: 相対（地上=1）、図11
    absolute=True:  実測 CPS [1/s]、図12
    """
    from matplotlib.ticker import MultipleLocator

    cps0 = USER_CPS["地上"]
    a0 = cps0 if absolute else 1.0
    lam_air = 1475.0 * 100.0

    rows = []
    points = []
    for site in _site_shielding_d1():
        x_eq = _equiv_concrete_cm_from_x(site["X"])
        y_rel = site["cps"] / cps0
        y = site["cps"] if absolute else y_rel
        y_th = float(np.asarray(_theory_rel(x_eq, a0)).reshape(-1)[0])
        points.append(
            {
                "label": site["label"],
                "x": x_eq,
                "y": y,
                "cps": site["cps"],
                "y_rel": y_rel,
                "site": site,
            }
        )
        rows.append(
            {
                "地点": site["label"],
                "CPS": f"{site['cps']:.8f}",
                "相対_地上1": f"{y_rel:.6f}",
                "土_cm": f"{site['soil_cm']:.1f}",
                "コンクリート_cm": f"{site['concrete_cm']:.1f}",
                "質量厚さ_X": f"{site['X']:.2f}",
                "等価コンクリート_cm": f"{x_eq:.1f}",
                "等価コンクリート_m": f"{x_eq / 100.0:.4f}",
                "理論_A0exp_相対": f"{float(np.asarray(_theory_rel(x_eq, 1.0)).reshape(-1)[0]):.6f}",
                "理論_A0exp_CPS": f"{float(np.asarray(_theory_rel(x_eq, cps0)).reshape(-1)[0]):.6f}",
                "備考": site["note"],
            }
        )

    out_csv = TABLES / "等価コンクリート_減衰.csv"
    if not absolute:
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    x_max = max(p["x"] for p in points) * 1.04
    x_air = np.linspace(-20, 0, 200)
    x_c = np.linspace(0, x_max, 900)
    # 空気側: 相対なら y=1、実測なら地上 CPS
    y_air_level = a0

    fig, ax = plt.subplots(figsize=(8.8, 5.2))
    fig.subplots_adjust(left=0.20, right=0.96, top=0.90, bottom=0.16)

    ax.plot(
        x_air,
        y_air_level * np.exp(x_air / lam_air),
        color=BLUE,
        lw=1.6,
        label=r"空気  $\lambda=1475$ m",
    )
    ax.plot(
        x_c,
        _theory_rel(x_c, a0),
        color=GRAY,
        lw=2.0,
        label=(
            rf"$A_0\,e^{{-x/{LAMBDA_M}}}$  （$A_0={a0:.4f}$, $x$ [m]）"
            if absolute
            else rf"$A_0\,e^{{-x/{LAMBDA_M}}}$  （$A_0=1$, $x$ [m]）"
        ),
    )
    ax.axvline(0, color="#CCCCCC", lw=0.8, zorder=1)

    ax.plot(
        [p["x"] for p in points],
        [p["y"] for p in points],
        "o",
        color=RED,
        ms=9,
        zorder=3,
        label="測定（実測CPS）" if absolute else "測定（ユーザーCPS・地上=1）",
    )

    offsets = {
        "地上": (8, -28),
        "PF": (8, 6),
        "linac": (8, -28),
        "BT": (8, 6),
        "KEKB": (-10, 6),
    }
    for p in points:
        dx, dy = offsets.get(p["label"], (8, 8))
        if absolute:
            txt = f'{p["label"]}  {p["cps"]:.4f}\n（相対 {p["y_rel"]:.3f}）'
        else:
            txt = f'{p["label"]}  相対{p["y_rel"]:.3f}\n（実測CPS {p["cps"]:.4f}）'
        ax.annotate(
            txt,
            (p["x"], p["y"]),
            textcoords="offset points",
            xytext=(dx, dy),
            fontsize=8,
            ha="left" if dx >= 0 else "right",
            linespacing=1.15,
        )

    ax.set_xlim(-20, x_max)
    if absolute:
        ax.set_ylim(0, cps0 * 1.12)
        ax.yaxis.set_major_locator(MultipleLocator(0.05))
        ax.yaxis.set_minor_locator(MultipleLocator(0.01))
        ax.set_ylabel("実測 CPS [1/s]")
        out_name = "12_全地点_等価コンクリート_実測CPS"
    else:
        ax.set_ylim(0, 1.12)
        ax.yaxis.set_major_locator(MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(MultipleLocator(0.02))
        ax.set_ylabel("相対 CPS（地上 = 1）")
        out_name = "11_全地点_等価コンクリート"

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    ax.tick_params(which="major", direction="out", length=5)
    ax.tick_params(which="minor", direction="out", length=3)
    ax.grid(True, which="major", alpha=0.35, linestyle="--")
    ax.grid(True, which="minor", alpha=0.18, linestyle=":")
    ax.set_xlabel(r"等価コンクリート厚さ [cm]（$t_{\mathrm{eq}}=X/\rho_c$）")
    ax.legend(frameon=False, loc="upper right", fontsize=9)
    save(fig, out_name, bbox_inches="none")
    print(f"figure: {out_name}.png")
    if not absolute:
        print(f"equiv table: {out_csv}")
    print(f"  理論 A0·exp(-x/{LAMBDA_M})  A0={a0:.6f}  absolute={absolute}")
    for p in points:
        th = float(np.asarray(_theory_rel(p["x"], a0)).reshape(-1)[0])
        s = p["site"]
        print(
            f"  {p['label']}: x={p['x']:.1f} cm  "
            f"{'CPS' if absolute else '相対'}={p['y']:.4f}  理論={th:.4f}"
        )


def fig_all_sites_equiv_concrete_cps(d: dict | None = None) -> None:
    """実測 CPS 版（図12）。"""
    fig_all_sites_equiv_concrete(d, absolute=True)



def cleanup_old_figures(valid_folders: set[str]) -> None:
    stale = [
        "03_ROI_150-450.png",
        "08_ピーク窓_300-380.png",
        "11_検出器稼働帯.png",
    ]
    for name in stale:
        p = FIG / name
        if p.exists():
            p.unlink()
    site = FIG / "地点別"
    if not site.exists():
        return
    for p in site.iterdir():
        if p.is_dir() and p.name not in valid_folders:
            shutil.rmtree(p)
    for p in site.rglob("*.png"):
        if p.name.startswith("ROI_150-450") or p.name.startswith("ピーク窓"):
            p.unlink()


def main() -> None:
    d = load_spectrum()
    fig_overview(d)
    fig_low_ch(d)
    fig_full_log(d)
    fig_roi(d)
    fig_full_linear(d)
    fig_bands(d)
    fig_ratio(d)
    fig_linac_ground(d)
    fig_linac_ground_theory(d)
    fig_all_sites_equiv_concrete(d)
    fig_all_sites_equiv_concrete_cps(d)
    valid = set()
    for s in d["series"]:
        _one_site(d, s)
        valid.add(folder_name(s["場所"]))
    cleanup_old_figures(valid)
    print(f"figures: {FIG}")
    for p in sorted(FIG.rglob("*.png")):
        print(f"  {p.relative_to(FIG)}")


if __name__ == "__main__":
    main()
