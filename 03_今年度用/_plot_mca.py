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
    if "kanri2f" in sl and "0819" in sl:
        return GREEN
    if "kanri2f" in sl or ("kanri" in sl and "1f" not in sl):
        return BLUE
    if "hoshasen" in sl or "0819_d1" in sl:
        return PALETTE[6]
    if "ground" in sl or sl.startswith("d1"):
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


def save(fig, name: str, folder: Path | None = None) -> None:
    dest = folder if folder is not None else FIG
    dest.mkdir(parents=True, exist_ok=True)
    fig.savefig(dest / f"{name}.png")
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


def fig_linac_ground() -> None:
    """指定値: linac 0.0647（コンクリート 150 cm）、地上 0.525。対数縦軸を上下逆向き。"""
    labels = ["linac\n(コンクリート 150 cm)", "地上"]
    y = [0.0647, 0.525]
    x = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    ax.plot(x, y, "-o", color=RED, ms=10, lw=2.0, label="CPS_NET")
    for xi, yi in zip(x, y):
        ax.annotate(
            f"{yi:.4f}",
            (xi, yi),
            textcoords="offset points",
            xytext=(0, 12),
            ha="center",
            fontsize=11,
        )
    ax.set_xticks(x, labels)
    ax.set_xlim(-0.4, 1.4)
    ax.set_yscale("log")
    ax.set_ylim(0.04, 0.8)
    ax.invert_yaxis()
    ax.set_xlabel("地点")
    ax.set_ylabel("CPS_NET [1/s]")
    ax.legend(frameon=False)
    save(fig, "09_linac_地上")


def cleanup_old_figures(valid_folders: set[str]) -> None:
    stale = [
        "03_ROI_150-450.png",
        "08_ピーク窓_300-380.png",
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
    fig_linac_ground()
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
