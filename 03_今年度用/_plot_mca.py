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

import equiv_shielding as esh

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


# 等価コンクリート換算（教材の質量厚さ X=ρt + 元素混合則）
# 理論: A = A0 * exp(-x / λ_c)、x・λ_c とも等価コンクリート厚 [cm]
# λ_c は equiv_shielding の詳細計算（Λ_i=37·A^0.3, 1/Λ=Σw_i/Λ_i）
# 土層プロファイル既定: tsukuba（ローム3.5 m → 常総2.0 m → 下総）
SOIL_PROFILE = esh.DEFAULT_PROFILE
RHO_CONCRETE = esh.RHO_CONCRETE
RHO_LOAM = esh.RHO_LOAM
RHO_JOSO = esh.RHO_JOSO
LOAM_MAX_CM = esh.LOAM_MAX_CM
LAMBDA_CONCRETE_GCM2 = esh.LAMBDA_CONCRETE_GCM2
LAMBDA_SOIL_GCM2 = esh.LAMBDA_SOIL_GCM2
LAMBDA_CM = esh.LAMBDA_CONCRETE_CM  # ≈39.2 cm（旧77 cmは誤り）
LAMBDA_M = esh.LAMBDA_CONCRETE_M    # ≈0.392 m（旧0.77 mは誤り）

# Book5 / ユーザー表の CPS。相対値は地上で規格化。
USER_CPS = {
    "地上": 0.52514597,
    "linac": 0.06478913,
    "BT": 0.11475671,
    "KEKB": 0.0399324,
    "PF": 0.25108616,
}

# d2: 分子/分母（ユーザー指定）。PF・地上はなし。
# BT 144/9541.27, KEKB 336/39042.15, linac 568/42626.85
USER_CPS_D2 = {
    "linac": 568 / 42626.85,
    "BT": 144 / 9541.27,
    "KEKB": 336 / 39042.15,
}


def _soil_mass_thickness(soil_cm: float, profile: str = SOIL_PROFILE) -> float:
    return esh.soil_mass_thickness_gcm2(soil_cm, profile=profile)


def _mass_thickness(concrete_cm: float, soil_cm: float, profile: str = SOIL_PROFILE) -> float:
    return concrete_cm * RHO_CONCRETE + _soil_mass_thickness(soil_cm, profile=profile)


def _equiv_concrete_cm_from_x(x_gcm2: float) -> float:
    return x_gcm2 / RHO_CONCRETE


def _optical_depth(x_c: float, x_s: float) -> float:
    """組成を反映した光学的厚さ τ = X_c/λ_c + X_s/λ_s（無次元）。"""
    return x_c / LAMBDA_CONCRETE_GCM2 + x_s / LAMBDA_SOIL_GCM2


def _equiv_concrete_cm_composition(x_c: float, x_s: float) -> float:
    """組成補正した等価コンクリート厚 [cm]。純コンクリートでは t_eq = t_c。"""
    return _optical_depth(x_c, x_s) * LAMBDA_CONCRETE_GCM2 / RHO_CONCRETE


def _equiv_from_layers(concrete_cm: float, soil_cm: float, profile: str = SOIL_PROFILE):
    """土+コンクリート厚から等価コンクリート（自動換算）。"""
    return esh.equiv_concrete(concrete_cm, soil_cm, profile=profile)


def _theory_rel(x_eq_cm, a0: float = 1.0):
    """A = A0 * exp(-x/λ_c)。x・λ_c とも等価コンクリート [cm]。"""
    return esh.theory_attenuation(x_eq_cm, a0=a0)


def _site_layers() -> list[dict]:
    """地点ごとの遮蔽層厚（検出器共通）。"""
    return [
        {"label": "地上", "concrete_cm": 0.0, "soil_cm": 0.0, "note": "基準（屋外）"},
        {"label": "PF", "concrete_cm": 105.0, "soil_cm": 0.0, "note": ""},
        {"label": "linac", "concrete_cm": 150.0, "soil_cm": 0.0, "note": ""},
        {"label": "BT", "concrete_cm": 60.0, "soil_cm": 220.0, "note": "土はロームのみ（220 cm < 3.5 m）"},
        {
            "label": "KEKB",
            "concrete_cm": 80.0,
            "soil_cm": 670.0,
            "note": "ローム3.5 m + 常総2.0 m + 下総1.2 m + コンクリ80 cm（Book5の117.25は桁誤り）",
        },
    ]


def _site_shielding(cps_map: dict[str, float]) -> list[dict]:
    """層厚から X を算出し、CPS と組み合わせる（密度のみ）。"""
    sites = []
    for base in _site_layers():
        if base["label"] not in cps_map:
            continue
        site = dict(base)
        site["X"] = _mass_thickness(site["concrete_cm"], site["soil_cm"])
        site["cps"] = float(cps_map[site["label"]])
        if not site["note"]:
            site["note"] = f"X={site['X']:.2f}"
        sites.append(site)
    return sites


def _site_shielding_d1() -> list[dict]:
    """図11/12用（D1・Book5 CPS）。"""
    return _site_shielding(USER_CPS)


def load_d2_cps() -> dict[str, float]:
    """d2 のユーザー CPS（分子/分母）。PF・地上は含まない。"""
    return dict(USER_CPS_D2)


def _site_shielding_composition() -> list[dict]:
    """組成補正付き X・t_eq（図13/14）。土層は SOIL_PROFILE で自動換算。"""
    sites = []
    for base in _site_shielding_d1():
        site = dict(base)
        r = _equiv_from_layers(site["concrete_cm"], site["soil_cm"])
        site["X_c"] = r.x_concrete_gcm2
        site["X_s"] = r.x_soil_gcm2
        site["X"] = r.x_total_gcm2
        site["tau"] = r.tau
        site["t_eq"] = r.t_eq_cm
        if site["soil_cm"] > 0:
            site["note"] = site["note"].rstrip("。") + f"・組成λ補正({r.profile})"
        sites.append(site)
    return sites




def fig_all_sites_equiv_concrete(
    d: dict | None = None,
    absolute: bool = False,
    logy: bool = False,
    *,
    cps_map: dict[str, float] | None = None,
    ref_label: str = "地上",
    name_suffix: str = "",
    csv_name: str = "等価コンクリート_減衰.csv",
    measure_label: str | None = None,
    detector: str = "D1",
) -> None:
    """層厚換算 X + CPS。理論 A0·exp(-x/λ_c)。

    absolute=False: 相対（ref_label=1）、図11
    absolute=True:  実測 CPS [1/s]、図12
    logy=True: 片対数（Y対数）。図11/12の片対数版を別ファイルに保存。
    detector: 凡例に出す検出器名（D1 / d2）。
    """
    from matplotlib.ticker import LogLocator, MultipleLocator

    cps = cps_map if cps_map is not None else USER_CPS
    sites = _site_shielding(cps)
    if ref_label not in cps:
        raise KeyError(f"基準地点 {ref_label!r} が CPS にありません: {list(cps)}")
    cps_ref = float(cps[ref_label])
    ref_site = next(s for s in sites if s["label"] == ref_label)
    x_ref = _equiv_concrete_cm_from_x(ref_site["X"])
    theory_at_ref = float(np.asarray(_theory_rel(x_ref, 1.0)).reshape(-1)[0])
    # 基準が地上(x=0)ならそのまま。それ以外は理論減衰で x=0 へ外挿した A0 を使う。
    # 表示（軸・凡例）は図11/12と同じく常に「地上」。
    if ref_label == "地上" or x_ref <= 0:
        cps0 = cps_ref
    else:
        cps0 = cps_ref / theory_at_ref if theory_at_ref > 0 else cps_ref
    rel_tag = "地上"
    a0 = cps0 if absolute else 1.0
    lam_air = 1475.0 * 100.0
    rel_key = "相対_地上1"

    rows = []
    points = []
    for site in sites:
        x_eq = _equiv_concrete_cm_from_x(site["X"])
        y_rel = site["cps"] / cps0
        y = site["cps"] if absolute else y_rel
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
                rel_key: f"{y_rel:.6f}",
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

    out_csv = TABLES / csv_name
    if not absolute and not logy:
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    x_max = max(p["x"] for p in points) * 1.04
    x_air = np.linspace(-20, 0, 200)
    x_c = np.linspace(0, x_max, 900)
    y_air_level = a0
    y_theory = _theory_rel(x_c, a0)

    fig, ax = plt.subplots(figsize=(8.8, 5.2))
    fig.subplots_adjust(left=0.20, right=0.96, top=0.90, bottom=0.16)

    if not logy:
        ax.plot(
            x_air,
            y_air_level * np.exp(x_air / lam_air),
            color=BLUE,
            lw=1.6,
            label=r"空気  $\lambda=1475$ m",
        )
    ax.plot(
        x_c,
        y_theory,
        color=GRAY,
        lw=2.0,
        label=(
            rf"$A_0\,e^{{-x/\lambda_c}}$  （$\lambda_c={LAMBDA_CM:.1f}\,\mathrm{{cm}}$, $A_0={a0:.4f}$）"
            if absolute
            else rf"$A_0\,e^{{-x/\lambda_c}}$  （$\lambda_c={LAMBDA_CM:.1f}\,\mathrm{{cm}}$, $A_0=1$）"
        ),
    )
    if not logy:
        ax.axvline(0, color="#CCCCCC", lw=0.8, zorder=1)

    if measure_label is None:
        measure_label = (
            f"測定 {detector}（実測CPS）"
            if absolute
            else f"測定 {detector}（{rel_tag}=1）"
        )
    ax.plot(
        [p["x"] for p in points],
        [p["y"] for p in points],
        "o",
        color=RED,
        ms=9,
        zorder=3,
        label=measure_label,
    )

    if logy:
        offsets = {
            "地上": (10, -22),
            "PF": (8, 8),
            "linac": (8, -28),
            "BT": (8, 8),
            "KEKB": (-8, 10),
        }
    else:
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

    # 片対数は x<0 の空気領域を省き、左側の空きをなくす
    ax.set_xlim(0 if logy else -20, x_max)
    if absolute:
        ax.set_ylabel("実測 CPS [1/s]")
        out_name = "12_全地点_等価コンクリート_実測CPS"
    else:
        ax.set_ylabel(f"相対 CPS（{rel_tag} = 1）")
        out_name = "11_全地点_等価コンクリート"
    if name_suffix:
        out_name = f"{out_name}{name_suffix}"

    y_data_max = max(p["y"] for p in points)
    y_th_max = float(np.max(y_theory))
    y_data_min = min(p["y"] for p in points)
    y_th_min = float(np.min(y_theory[y_theory > 0]))

    if logy:
        out_name = f"{out_name}_片対数"
        y_min = min(y_data_min, y_th_min) * 0.5
        y_max = max(y_data_max, y_th_max, a0) * 2.0
        ax.set_yscale("log")
        ax.set_ylim(y_min, y_max)
        ax.yaxis.set_major_locator(LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))
        ax.grid(True, which="major", alpha=0.35, linestyle="--")
        ax.grid(True, which="minor", axis="y", alpha=0.12, linestyle=":")
        ax.grid(True, which="minor", axis="x", alpha=0.18, linestyle=":")
    else:
        # 図11/12 と同じく A0（地上相当）まで見せる
        y_top = max(y_data_max, a0) * 1.12
        ax.set_ylim(0, y_top)
        if absolute:
            ax.yaxis.set_major_locator(MultipleLocator(0.05))
            ax.yaxis.set_minor_locator(MultipleLocator(0.01))
        else:
            ax.yaxis.set_major_locator(MultipleLocator(0.1))
            ax.yaxis.set_minor_locator(MultipleLocator(0.02))
        ax.grid(True, which="major", alpha=0.35, linestyle="--")
        ax.grid(True, which="minor", alpha=0.18, linestyle=":")

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    ax.tick_params(which="major", direction="out", length=5)
    ax.tick_params(which="minor", direction="out", length=3)
    ax.set_xlabel(r"等価コンクリート厚さ [cm]（$t_{\mathrm{eq}}=X/\rho_c$）")
    ax.legend(frameon=False, loc="upper right", fontsize=9)
    save(fig, out_name, bbox_inches="none")
    print(f"figure: {out_name}.png")
    if not absolute and not logy:
        print(f"equiv table: {out_csv}")
    print(
        f"  理論 A0·exp(-x/λ_c)  λ_c={LAMBDA_CM:.2f} cm  A0={a0:.6f}  "
        f"absolute={absolute}  logy={logy}  ref={ref_label}→{rel_tag}"
    )
    for p in points:
        th = float(np.asarray(_theory_rel(p["x"], a0)).reshape(-1)[0])
        print(
            f"  {p['label']}: x={p['x']:.1f} cm  "
            f"{'CPS' if absolute else '相対'}={p['y']:.4f}  理論={th:.4f}"
        )


def fig_all_sites_equiv_concrete_cps(d: dict | None = None) -> None:
    """実測 CPS 版（図12）。"""
    fig_all_sites_equiv_concrete(d, absolute=True)


def fig_all_sites_equiv_concrete_semilog(d: dict | None = None) -> None:
    """図11の片対数版。"""
    fig_all_sites_equiv_concrete(d, absolute=False, logy=True)


def fig_all_sites_equiv_concrete_cps_semilog(d: dict | None = None) -> None:
    """図12の片対数版。"""
    fig_all_sites_equiv_concrete(d, absolute=True, logy=True)


def fig_all_sites_equiv_concrete_d2(
    absolute: bool = False, logy: bool = False
) -> None:
    """d2 検出器版の図11/12。地上・PF なしのため linac から地上 CPS を外挿。"""
    cps = load_d2_cps()
    fig_all_sites_equiv_concrete(
        absolute=absolute,
        logy=logy,
        cps_map=cps,
        ref_label="linac",
        name_suffix="_d2",
        csv_name="等価コンクリート_減衰_d2.csv",
        detector="d2",
    )


def fig_all_sites_equiv_concrete_d2_cps() -> None:
    fig_all_sites_equiv_concrete_d2(absolute=True)


def fig_all_sites_equiv_concrete_d2_semilog() -> None:
    fig_all_sites_equiv_concrete_d2(absolute=False, logy=True)


def fig_all_sites_equiv_concrete_d2_cps_semilog() -> None:
    fig_all_sites_equiv_concrete_d2(absolute=True, logy=True)


def fig_all_sites_equiv_concrete_composition(
    d: dict | None = None, absolute: bool = False
) -> None:
    """組成補正版。図11/12は上書きせず、図13/14として新規保存。"""
    from matplotlib.ticker import MultipleLocator

    cps0 = USER_CPS["地上"]
    a0 = cps0 if absolute else 1.0
    lam_air = 1475.0 * 100.0

    rows = []
    points = []
    for site in _site_shielding_composition():
        x_eq = site["t_eq"]
        y_rel = site["cps"] / cps0
        y = site["cps"] if absolute else y_rel
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
                "X_コンクリート": f"{site['X_c']:.2f}",
                "X_土": f"{site['X_s']:.2f}",
                "質量厚さ_X": f"{site['X']:.2f}",
                "光学厚さ_tau": f"{site['tau']:.6f}",
                "等価コンクリート_cm": f"{x_eq:.1f}",
                "等価コンクリート_m": f"{x_eq / 100.0:.4f}",
                "密度のみ等価_cm": f"{site['X'] / RHO_CONCRETE:.1f}",
                "理論_A0exp_相対": f"{float(np.asarray(_theory_rel(x_eq, 1.0)).reshape(-1)[0]):.6f}",
                "理論_A0exp_CPS": f"{float(np.asarray(_theory_rel(x_eq, cps0)).reshape(-1)[0]):.6f}",
                "備考": site["note"],
            }
        )

    out_csv = TABLES / "等価コンクリート_減衰_組成補正.csv"
    if not absolute:
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    x_max = max(p["x"] for p in points) * 1.04
    x_air = np.linspace(-20, 0, 200)
    x_c = np.linspace(0, x_max, 900)
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
            rf"$A_0\,e^{{-x/\lambda_c}}$  （$\lambda_c={LAMBDA_CM:.1f}\,\mathrm{{cm}}$, $A_0={a0:.4f}$）"
            if absolute
            else rf"$A_0\,e^{{-x/\lambda_c}}$  （$\lambda_c={LAMBDA_CM:.1f}\,\mathrm{{cm}}$, $A_0=1$）"
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
        label="測定（実測CPS）" if absolute else "測定（地上=1）",
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
        out_name = "14_全地点_等価コンクリート_組成補正_実測CPS"
    else:
        ax.set_ylim(0, 1.12)
        ax.yaxis.set_major_locator(MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(MultipleLocator(0.02))
        ax.set_ylabel("相対 CPS（地上 = 1）")
        out_name = "13_全地点_等価コンクリート_組成補正"

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    ax.tick_params(which="major", direction="out", length=5)
    ax.tick_params(which="minor", direction="out", length=3)
    ax.grid(True, which="major", alpha=0.35, linestyle="--")
    ax.grid(True, which="minor", alpha=0.18, linestyle=":")
    ax.set_xlabel(
        r"等価コンクリート厚さ [cm]"
        r"（$t_{\mathrm{eq}}=(X_c/\lambda_c+X_s/\lambda_s)\,\lambda_c/\rho_c$）"
    )
    ax.legend(frameon=False, loc="upper right", fontsize=9)
    save(fig, out_name, bbox_inches="none")
    print(f"figure: {out_name}.png")
    if not absolute:
        print(f"equiv table: {out_csv}")
    print(
        f"  組成補正 A0·exp(-x/λ_c)  λ_c={LAMBDA_CM:.2f} cm  A0={a0:.6f}  "
        f"λ_c={LAMBDA_CONCRETE_GCM2} λ_s={LAMBDA_SOIL_GCM2}"
    )
    for p in points:
        th = float(np.asarray(_theory_rel(p["x"], a0)).reshape(-1)[0])
        s = p["site"]
        print(
            f"  {p['label']}: t_eq={p['x']:.1f} cm（密度のみ{s['X']/RHO_CONCRETE:.1f}）  "
            f"{'CPS' if absolute else '相対'}={p['y']:.4f}  理論={th:.4f}"
        )


def fig_all_sites_equiv_concrete_composition_cps(d: dict | None = None) -> None:
    """組成補正・実測 CPS 版（図14）。"""
    fig_all_sites_equiv_concrete_composition(d, absolute=True)



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
    fig_all_sites_equiv_concrete_semilog(d)
    fig_all_sites_equiv_concrete_cps_semilog(d)
    fig_all_sites_equiv_concrete_d2()
    fig_all_sites_equiv_concrete_d2_cps()
    fig_all_sites_equiv_concrete_d2_semilog()
    fig_all_sites_equiv_concrete_d2_cps_semilog()
    fig_all_sites_equiv_concrete_composition(d)
    fig_all_sites_equiv_concrete_composition_cps(d)
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
