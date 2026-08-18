#!/usr/bin/env python3
"""今年度 MCA スペクトルのグラフを 測定_20260818/figures/ に書き出す。"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "測定_20260818"
TABLES = DATA / "tables"
FIG = DATA / "figures"

BLUE, RED, GRAY = "#1F77B4", "#D62728", "#666666"

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


def load_spectrum() -> dict:
    ch, c0, c1, r0, r1 = [], [], [], [], []
    with (TABLES / "スペクトル.csv").open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ch.append(int(row["channel"]))
            c0.append(float(row["counts_kanri2f"]))
            c1.append(float(row["counts_linac"]))
            r0.append(float(row["cps_kanri2f"]))
            r1.append(float(row["cps_linac"]))
    rec = {}
    with (TABLES / "測定記録.csv").open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rec[row["場所"]] = row
    live0 = float(rec["管理棟2F"]["live_s"])
    live1 = float(rec["linac"]["live_s"])
    return {
        "ch": np.array(ch),
        "c0": np.array(c0),
        "c1": np.array(c1),
        "r0": np.array(r0),
        "r1": np.array(r1),
        "e0": np.sqrt(np.array(c0)) / live0,
        "e1": np.sqrt(np.array(c1)) / live1,
        "live0": live0,
        "live1": live1,
    }


def save(fig, name: str) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG / f"{name}.png")
    fig.savefig(FIG / f"{name}.pdf")
    plt.close(fig)


def fig_low_ch(d: dict) -> None:
    m = (d["ch"] >= 1) & (d["ch"] <= 80)
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.step(d["ch"][m], d["r0"][m], where="mid", color=BLUE, lw=1.6, label="管理棟2F")
    ax.step(d["ch"][m], d["r1"][m], where="mid", color=RED, lw=1.6, label="linac")
    ax.set_xlim(1, 80)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel("計数率 (cps / ch)")
    ax.set_title("低エネルギー域（ch 1–80、ch 0 除外）")
    ax.legend(frameon=False)
    save(fig, "01_低ch_線形")


def fig_full_log(d: dict) -> None:
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    y0 = np.where(d["r0"] > 0, d["r0"], np.nan)
    y1 = np.where(d["r1"] > 0, d["r1"], np.nan)
    ax.step(d["ch"], y0, where="mid", color=BLUE, lw=1.2, label="管理棟2F")
    ax.step(d["ch"], y1, where="mid", color=RED, lw=1.2, label="linac")
    ax.set_yscale("log")
    ax.set_xlim(0, 511)
    ax.set_ylim(3e-4, 50)
    ax.axvspan(150, 450, color="#FFF3BF", alpha=0.55, zorder=0, label="ROI (150–450)")
    ax.set_xlabel("チャンネル")
    ax.set_ylabel("計数率 (cps / ch)")
    ax.set_title("全チャンネル（対数、ゼロは非表示）")
    ax.legend(frameon=False, loc="upper right")
    save(fig, "02_全ch_対数")


def fig_roi(d: dict) -> None:
    m = (d["ch"] >= 150) & (d["ch"] <= 450)
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.errorbar(
        d["ch"][m],
        d["r0"][m],
        yerr=d["e0"][m],
        fmt="o",
        ms=2.4,
        lw=0.6,
        color=BLUE,
        label="管理棟2F",
        elinewidth=0.6,
        capsize=0,
    )
    ax.errorbar(
        d["ch"][m],
        d["r1"][m],
        yerr=d["e1"][m],
        fmt="o",
        ms=2.4,
        lw=0.6,
        color=RED,
        label="linac",
        elinewidth=0.6,
        capsize=0,
    )
    ax.set_xlim(150, 450)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel("計数率 (cps / ch)")
    ax.set_title("ROI（ch 150–450、誤差棒は √N / live）")
    ax.legend(frameon=False)
    save(fig, "03_ROI")


def fig_bands(d: dict) -> None:
    labels = ["ch 0", "ch 1–20", "ch 21–149", "ROI\n150–450", "ch 0 除く"]
    slices = [(0, 1), (1, 21), (21, 150), (150, 451), (1, 512)]
    v0, v1 = [], []
    for lo, hi in slices:
        v0.append(d["c0"][lo:hi].sum() / d["live0"])
        v1.append(d["c1"][lo:hi].sum() / d["live1"])
    x = np.arange(len(labels))
    w = 0.38
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.bar(x - w / 2, v0, w, color=BLUE, label="管理棟2F")
    ax.bar(x + w / 2, v1, w, color=RED, label="linac")
    ax.set_xticks(x, labels)
    ax.set_ylabel("計数率 (cps)")
    ax.set_title("チャンネル帯ごとの計数率")
    ax.legend(frameon=False)
    for i, (a, b) in enumerate(zip(v0, v1)):
        ax.text(i - w / 2, a, f"{a:.2f}", ha="center", va="bottom", fontsize=8, color=BLUE)
        ax.text(i + w / 2, b, f"{b:.2f}", ha="center", va="bottom", fontsize=8, color=RED)
    ymax = max(v0 + v1)
    ax.set_ylim(0, ymax * 1.18)
    save(fig, "04_帯域比較")


def fig_ratio(d: dict) -> None:
    m = (d["ch"] >= 1) & (d["ch"] <= 80) & (d["c0"] >= 20)
    ratio = d["r1"][m] / d["r0"][m]
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.axhline(1.0, color=GRAY, lw=1.0)
    ax.plot(d["ch"][m], ratio, "o", ms=4, color="#2CA02C")
    ax.set_xlim(1, 80)
    ax.set_ylim(0.7, 1.6)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel("計数率比（linac / 管理棟2F）")
    ax.set_title("形状比（ch 1–80、管理棟2F が 20 カウント以上）")
    save(fig, "05_比_低ch")


def fig_overview(d: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(10.6, 7.4), layout="constrained")
    fig.suptitle("今年度 MCA（2026-08-18）管理棟2F vs linac", fontsize=14)

    ax = axes[0, 0]
    m = (d["ch"] >= 1) & (d["ch"] <= 80)
    ax.step(d["ch"][m], d["r0"][m], where="mid", color=BLUE, lw=1.4, label="管理棟2F")
    ax.step(d["ch"][m], d["r1"][m], where="mid", color=RED, lw=1.4, label="linac")
    ax.set_xlim(1, 80)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel("計数率 (cps / ch)")
    ax.set_title("低ch（線形）")
    ax.legend(frameon=False, fontsize=9)

    ax = axes[0, 1]
    y0 = np.where(d["r0"] > 0, d["r0"], np.nan)
    y1 = np.where(d["r1"] > 0, d["r1"], np.nan)
    ax.step(d["ch"], y0, where="mid", color=BLUE, lw=1.0, label="管理棟2F")
    ax.step(d["ch"], y1, where="mid", color=RED, lw=1.0, label="linac")
    ax.set_yscale("log")
    ax.set_xlim(0, 511)
    ax.set_ylim(3e-4, 50)
    ax.axvspan(150, 450, color="#FFF3BF", alpha=0.5, zorder=0)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel("計数率 (cps / ch)")
    ax.set_title("全ch（対数）")

    ax = axes[1, 0]
    m = (d["ch"] >= 300) & (d["ch"] <= 380)
    ax.errorbar(d["ch"][m], d["r0"][m], yerr=d["e0"][m], fmt="o", ms=3, color=BLUE, label="管理棟2F", elinewidth=0.7)
    ax.errorbar(d["ch"][m], d["r1"][m], yerr=d["e1"][m], fmt="o", ms=3, color=RED, label="linac", elinewidth=0.7)
    ax.set_xlim(300, 380)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel("計数率 (cps / ch)")
    ax.set_title("ROI 内の山（ch 300–380）")
    ax.legend(frameon=False, fontsize=9)

    ax = axes[1, 1]
    labels = ["ch 0", "1–20", "21–149", "ROI", "ch0除く"]
    slices = [(0, 1), (1, 21), (21, 150), (150, 451), (1, 512)]
    v0 = [d["c0"][lo:hi].sum() / d["live0"] for lo, hi in slices]
    v1 = [d["c1"][lo:hi].sum() / d["live1"] for lo, hi in slices]
    x = np.arange(len(labels))
    w = 0.38
    ax.bar(x - w / 2, v0, w, color=BLUE, label="管理棟2F")
    ax.bar(x + w / 2, v1, w, color=RED, label="linac")
    ax.set_xticks(x, labels)
    ax.set_ylabel("計数率 (cps)")
    ax.set_title("帯域積分")
    ax.legend(frameon=False, fontsize=9)

    save(fig, "00_概要")


def main() -> None:
    d = load_spectrum()
    fig_overview(d)
    fig_low_ch(d)
    fig_full_log(d)
    fig_roi(d)
    fig_bands(d)
    fig_ratio(d)
    print(f"figures: {FIG}")
    for p in sorted(FIG.glob("*.png")):
        print(f"  {p.name}")


if __name__ == "__main__":
    main()
