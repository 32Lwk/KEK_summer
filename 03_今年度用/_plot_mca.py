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

from mca_common import (
    HE3_MARK_KEV,
    detector_fs_suffix,
    equiv_decay_csv_name,
    peak_clip as roi_peak_clip,
    resolve_he3_energy_cal,
)

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
# 対数軸では 0 を描けない。NaN にすると step が切れるので、
# 半カウント相当（0.5/live）を床として連続線にする。
LOG_Y_FLOOR = 1e-5
LOG_Y_MAX = 80.0


def cps_for_log(c, live: float | None = None) -> np.ndarray:
    """対数プロット用: 非正値を床値に置き、線が切れないようにする。"""
    floor = LOG_Y_FLOOR
    if live is not None and live > 0:
        floor = max(floor, 0.5 / float(live))
    return np.maximum(np.asarray(c, dtype=float), floor)

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
                "シリアル": str(rec.get("シリアル") or ""),
                "c": cps,
                "e": np.sqrt(np.maximum(c, 0.0)) / live,
                "live": live,
                "lab": f"{rec['場所']}（{tlab}）",
                "color": color_for(sid, i),
                "roi_lo": lo,
                "roi_hi": hi,
                "roi_peak": int(float(rec.get("roi_peak") or 0)),
                "roi_net_cps": float(rec["roi_net_cps"]),
                "roi_warning": rec.get("roi_warning") or "",
                "sb_lo_lo": int(float(rec["sb_lo_lo"])) if rec.get("sb_lo_lo") not in (None, "") else 0,
                "sb_lo_hi": int(float(rec["sb_lo_hi"])) if rec.get("sb_lo_hi") not in (None, "") else 0,
                "sb_hi_lo": int(float(rec["sb_hi_lo"])) if rec.get("sb_hi_lo") not in (None, "") else 0,
                "sb_hi_hi": int(float(rec["sb_hi_hi"])) if rec.get("sb_hi_hi") not in (None, "") else 0,
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
            ax.step(
                x,
                cps_for_log(c, live=s.get("live")),
                where="mid",
                color=s["color"],
                lw=lw,
                label=s["lab"],
            )
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
    ax.axvspan(lo, hi, color="#F4C7C3", alpha=0.45, zorder=0, label=label or f"共通ROI {lo}–{hi}")


def shade_sidebands(ax, s: dict) -> None:
    """側帯を塗る（凡例には出さない）。"""
    sb0 = (int(s.get("sb_lo_lo") or 0), int(s.get("sb_lo_hi") or 0))
    sb1 = (int(s.get("sb_hi_lo") or 0), int(s.get("sb_hi_hi") or 0))
    if sb0[1] >= sb0[0] > 0:
        ax.axvspan(sb0[0], sb0[1], color="#9EC9E2", alpha=0.35, zorder=0)
    if sb1[1] >= sb1[0] > 0 and sb1 != sb0:
        ax.axvspan(sb1[0], sb1[1], color="#9EC9E2", alpha=0.35, zorder=0)


# ³He エネルギー目印（較正は mca_common.resolve_he3_energy_cal: SN×ゲイン群別）。
HE3_MARK_COLOR = {764.0: "#D62728", 573.0: "#FF7F0E", 191.0: "#2CA02C"}


def mark_he3_energies(ax, s: dict) -> None:
    """シリアル×ゲイン群で決めた 764 keV 基準から縦線を引く。"""
    cal = resolve_he3_energy_cal(
        str(s.get("シリアル") or ""),
        int(s.get("roi_peak") or 0),
        str(s.get("場所") or ""),
    )
    if cal is None or cal.peak_ch <= 0:
        return
    for e_kev in HE3_MARK_KEV:
        ch_e = cal.channel_of(e_kev)
        color = HE3_MARK_COLOR.get(float(e_kev), "#555555")
        ax.axvline(ch_e, color=color, ls="--", lw=1.0, alpha=0.9, zorder=3)
        ax.text(
            ch_e,
            0.97,
            f"{e_kev:.0f} keV",
            transform=ax.get_xaxis_transform(),
            rotation=90,
            va="top",
            ha="right",
            fontsize=7,
            color=color,
            clip_on=False,
        )
    # 左下に較正モード（D/d・フォールバックの区別）
    tag = f"SN{cal.serial}/{cal.mode}"
    if cal.source == "peak_ref":
        tag += f" ref={cal.peak_ch}"
    ax.text(
        0.01,
        0.02,
        tag,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=7,
        color=GRAY,
    )


def place_legend(ax, fontsize: float = 9, ncol: int = 1) -> None:
    """凡例を図内右上に固定（loc=best だと地点・スケールで位置がぶれる）。"""
    handles, labels = ax.get_legend_handles_labels()
    if not handles:
        return
    ax.legend(
        handles,
        labels,
        frameon=False,
        loc="upper right",
        fontsize=fontsize,
        ncol=ncol,
        borderaxespad=0.3,
    )


def step_spectrum(ax, ch, c, color, label=None, clip=None, annotate=True) -> None:
    y = np.minimum(c, clip) if clip is not None else c
    ax.step(ch, y, where="mid", color=color, lw=1.4, label=label)
    if clip is not None:
        ax.set_ylim(0, clip)
        if annotate:
            n_hi = int(np.sum(c > clip))
            if n_hi:
                # 軸の上外側に置き、図内右上の凡例と重ならないようにする
                ax.text(
                    0.99,
                    1.02,
                    f"{n_hi} ch が {clip:.3f} 超",
                    transform=ax.transAxes,
                    ha="right",
                    va="bottom",
                    fontsize=8,
                    color=GRAY,
                    clip_on=False,
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
    place_legend(ax, fontsize=8, ncol=2)
    save(fig, "06_全ch_線形")

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, clip=overlay_clip(d))
    ax.set_xlim(0, 511)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"全ch {clip_title(overlay_clip(d))}")
    place_legend(ax, fontsize=8, ncol=2)
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
    place_legend(ax, fontsize=8, ncol=2)
    save(fig, "07_全ch_線形_ch0除く")

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, mask=m, clip=overlay_clip(d))
    shade_roi(ax, lo, hi)
    ax.set_xlim(1, 511)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"全ch {clip_title(overlay_clip(d))}（ch0除く）")
    place_legend(ax, fontsize=8, ncol=2)
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
    place_legend(ax, fontsize=8, ncol=2)
    save(fig, "01_低ch_線形")

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, mask=m, clip=low_clip(d), lw=1.6)
    ax.set_xlim(1, 80)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"低ch {clip_title(low_clip(d))}")
    place_legend(ax, fontsize=8, ncol=2)
    save(fig, "01b_低ch_線形_クリップ")


def fig_full_log(d: dict) -> None:
    lo, hi = union_roi(d["series"])
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    overlay_step(ax, d, log=True, lw=1.2)
    ax.set_yscale("log")
    ax.set_xlim(0, 511)
    ax.set_ylim(LOG_Y_FLOOR, LOG_Y_MAX)
    shade_roi(ax, lo, hi)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("対数")
    place_legend(ax, fontsize=8, ncol=2)
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
    place_legend(ax, fontsize=8, ncol=2)
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
    place_legend(ax, fontsize=8, ncol=2)
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
    place_legend(ax, fontsize=8, ncol=2)
    save(fig, "05_比_低ch")


def _one_site(d: dict, s: dict) -> None:
    out = FIG / "地点別" / folder_name(s["場所"])
    out.mkdir(parents=True, exist_ok=True)
    ch, c, e = d["ch"], s["c"], s["e"]
    color = s["color"]
    clip = s["clip"]
    lo, hi = s["roi_lo"], s["roi_hi"]
    ctitle = clip_title(clip)
    roi_title = f"共通ROI {lo}–{hi}"
    if s.get("roi_warning"):
        roi_title += f"  ⚠ {s['roi_warning']}"

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
    shade_sidebands(ax, s)
    ax.set_xlim(1, 511)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("全ch 線形（ch0除く）")
    place_legend(ax)
    save(fig, "全ch_線形_ch0除く", out)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    step_spectrum(ax, ch[m], c[m], color, clip=clip)
    shade_roi(ax, lo, hi)
    shade_sidebands(ax, s)
    mark_he3_energies(ax, s)
    ax.set_xlim(1, 511)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"全ch {ctitle}（ch0除く）")
    place_legend(ax)
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
    ax.step(ch, cps_for_log(c, live=s.get("live")), where="mid", color=color, lw=1.3)
    ax.set_yscale("log")
    ax.set_xlim(0, 511)
    ax.set_ylim(LOG_Y_FLOOR, LOG_Y_MAX)
    shade_roi(ax, lo, hi)
    shade_sidebands(ax, s)
    mark_he3_energies(ax, s)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title("対数")
    place_legend(ax)
    save(fig, "全ch_対数", out)

    mroi = (ch >= lo) & (ch <= hi)
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.errorbar(ch[mroi], c[mroi], yerr=e[mroi], fmt="o", ms=3.5, color=color, elinewidth=0.8)
    ax.set_xlim(lo, hi)
    ax.set_ylim(0, None)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(roi_title)
    save(fig, "ROI", out)

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.errorbar(ch[mroi], np.minimum(c[mroi], clip), yerr=e[mroi], fmt="o", ms=3.5, color=color, elinewidth=0.8)
    ax.set_xlim(lo, hi)
    ax.set_ylim(0, clip)
    ax.set_xlabel("チャンネル")
    ax.set_ylabel(YLABEL)
    ax.set_title(f"{roi_title} {ctitle}")
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
    place_legend(ax, fontsize=7, ncol=2)

    ax = axes[0, 1]
    overlay_step(ax, d, log=True, lw=1.0)
    ax.set_yscale("log")
    ax.set_xlim(0, 511)
    ax.set_ylim(LOG_Y_FLOOR, LOG_Y_MAX)
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
    place_legend(ax, fontsize=7, ncol=2)

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
    place_legend(ax, fontsize=7, ncol=2)

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
RHO_IRON = esh.RHO_IRON
LOAM_MAX_CM = esh.LOAM_MAX_CM
LAMBDA_CONCRETE_GCM2 = esh.LAMBDA_CONCRETE_GCM2
LAMBDA_SOIL_GCM2 = esh.LAMBDA_SOIL_GCM2
LAMBDA_IRON_GCM2 = esh.LAMBDA_IRON_GCM2
LAMBDA_CM = esh.LAMBDA_CONCRETE_CM  # ≈39.2 cm（旧77 cmは誤り）
LAMBDA_M = esh.LAMBDA_CONCRETE_M    # ≈0.392 m（旧0.77 mは誤り）

# 図11/12系の余白（凡例は左下・注釈用に上余白を確保）
EQUIV_FIGSIZE = (8.8, 6.0)
EQUIV_SUBPLOT = dict(left=0.18, right=0.96, top=0.92, bottom=0.12)
EQUIV_Y_PAD_LINEAR = 1.32  # ylim 上端 = max(data, A0) × この値
EQUIV_Y_PAD_LOGY = 4.0  # log ylim 上端 = max(data, A0) × この値


def _equiv_legend(ax, fontsize: float = 9) -> None:
    """凡例をグラフ内左下に置く（データ点・注釈との重なりを避ける）。"""
    ax.legend(
        frameon=False,
        loc="lower left",
        fontsize=fontsize,
        borderaxespad=0.8,
    )

# 施設地点比較に使う場所ラベル（等価コンクリート図の横軸）
FACILITY_SITES = ("地上", "PF", "linac", "BT", "KEKB", "linacIRON")

# 検出器別のマーカー／色（4パターン比較用）
DETECTOR_STYLE = {
    "D1": {"color": "#C0392B", "marker": "o", "ms": 9, "label": "D1（大径・SN1715）"},
    "D2": {"color": "#2471A3", "marker": "s", "ms": 8, "label": "D2（大径・SN1715）"},
    "d1": {"color": "#1E8449", "marker": "^", "ms": 8, "label": "d1（小径・SN2162）"},
    "d2": {"color": "#E67E22", "marker": "D", "ms": 7, "label": "d2（小径・SN2162）"},
}


def _detector_from_place(place: str) -> str | None:
    """場所名（raw ファイル名）から D1/D2/d1/d2 を判定。大文字・小文字を区別。"""
    if re.search(r"(^|[_＿])D1($|[_＿])", place) or place.startswith("D1"):
        return "D1"
    if re.search(r"(^|[_＿])D2($|[_＿])", place) or place.startswith("D2"):
        return "D2"
    if re.search(r"(^|[_＿])d1($|[_＿])", place) or place.startswith("d1"):
        return "d1"
    if (
        re.search(r"(^|[_＿])d2($|[_＿])", place)
        or place.startswith("d2")
        or place.startswith("smalld2")
    ):
        return "d2"
    return None


def _facility_site_from_place(place: str) -> str | None:
    """遮蔽減衰比較用の地点。熱中性子・管理棟は除外。"""
    if "熱中性子" in place or "gain" in place.lower():
        return None
    if "管理棟" in place or "kanri" in place.lower():
        return None
    # linacIRON は linac より先に判定（名前が linac を含むため）
    if "linacIRON" in place or "linaciron" in place.lower():
        return "linacIRON"
    if "地上" in place or "ground" in place.lower():
        return "地上"
    if re.search(r"(^|[_＿])PF($|[_＿])", place) or place.endswith("_PF") or "_PF_" in place:
        return "PF"
    if "KEKB" in place:
        return "KEKB"
    if "BT" in place or "hoshasen" in place.lower():
        return "BT"
    if "linac" in place.lower():
        return "linac"
    return None


def load_facility_cps_by_detector(
    path: Path | None = None,
) -> dict[str, dict[str, float]]:
    """ROI_NET_CPS.csv から検出器別・地点別の側帯 NET CPS を読む。

    raw のファイル名規則に従い D1/D2/d1/d2 を混同しない。
    同一 (検出器, 地点) が複数ある場合は無警告・長い live_s を優先。
    """
    csv_path = path or (TABLES / "ROI_NET_CPS.csv")
    # score, live, cps, cps_err, place
    best: dict[tuple[str, str], tuple[int, float, float, float, str]] = {}
    with csv_path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if str(row.get("roi_net_valid", "1")) not in ("1", "True", "true"):
                continue
            place = row.get("場所") or ""
            det = _detector_from_place(place)
            site = _facility_site_from_place(place)
            if not det or not site:
                continue
            try:
                cps = float(row["roi_net_cps"])
                live = float(row.get("live_s") or 0.0)
                cps_err = float(row.get("roi_net_cps_err") or 0.0)
            except (KeyError, ValueError, TypeError):
                continue
            if cps <= 0:
                continue
            warn = (row.get("roi_warning") or "").strip()
            score = (0 if warn else 1, live)
            key = (det, site)
            prev = best.get(key)
            if prev is None or score > (prev[0], prev[1]):
                best[key] = (score[0], live, cps, cps_err, place)

    out: dict[str, dict[str, float]] = {k: {} for k in ("D1", "D2", "d1", "d2")}
    errs: dict[str, dict[str, float]] = {k: {} for k in out}
    sources: dict[str, dict[str, str]] = {k: {} for k in out}
    for (det, site), (_, _, cps, cps_err, place) in best.items():
        out[det][site] = cps
        errs[det][site] = cps_err
        sources[det][site] = place
    load_facility_cps_by_detector._sources = sources  # type: ignore[attr-defined]
    load_facility_cps_by_detector._errs = errs  # type: ignore[attr-defined]
    return out


def facility_cps_sources() -> dict[str, dict[str, str]]:
    """load_facility_cps_by_detector が選んだ測定ファイル名。"""
    load_facility_cps_by_detector()
    return getattr(load_facility_cps_by_detector, "_sources", {})


def facility_cps_errs() -> dict[str, dict[str, float]]:
    """検出器別・地点別の ROI NET CPS 統計誤差 [1/s]。"""
    load_facility_cps_by_detector()
    return getattr(load_facility_cps_by_detector, "_errs", {})


def load_detector_cps(detector: str) -> dict[str, float]:
    """指定検出器の施設地点 CPS（実測がある地点のみ）。"""
    return dict(load_facility_cps_by_detector().get(detector, {}))


def load_detector_cps_err(detector: str) -> dict[str, float]:
    """指定検出器の施設地点 CPS 統計誤差。"""
    return dict(facility_cps_errs().get(detector, {}))


# 図13/14・旧呼び出し用（D1 実測）
USER_CPS = load_detector_cps("D1")

# ---------------------------------------------------------------------------
# 系統誤差（厚さ + 密度を二乗和）→ 横軸 δt_eq
# X = ρ_c·t_c + X_s、t_eq = X/ρ_c
# 各層: δX/X = √((δt/t)² + (δρ/ρ)²)、δt_eq = √(δX_c²+δX_s²)/ρ_c
# ---------------------------------------------------------------------------
SYS_DT_CONCRETE_ABS_CM = 5.0  # コンクリート厚の絶対不確かさ [cm]
SYS_DT_CONCRETE_FRAC = 0.05  # コンクリート厚の相対不確かさ
SYS_DT_SOIL_FRAC = 0.10  # 土厚の相対不確かさ
SYS_DT_IRON_ABS_CM = 5.0  # 鉄厚の絶対不確かさ [cm]
SYS_DT_IRON_FRAC = 0.05  # 鉄厚の相対不確かさ
SYS_DRHO_CONCRETE = 0.10  # ρ_c = 2.3 ± 0.1 [g/cm³]
SYS_DRHO_SOIL_FRAC = 0.15  # 土密度の相対不確かさ（施設表 1.3–1.6）
SYS_DRHO_IRON = 0.30  # ρ_Fe = 7.2 ± 0.3 [g/cm³]


def _teq_systematic_err_cm(
    concrete_cm: float,
    soil_cm: float,
    iron_cm: float = 0.0,
    *,
    profile: str = SOIL_PROFILE,
) -> dict[str, float]:
    """等価コンクリート厚の系統誤差 [cm]（厚さ・密度を二乗和）。

    各層の質量厚さ不確かさ δX/X = √((δt/t)²+(δρ/ρ)²) を合成し、
    δt_eq = √(δX_c²+δX_s²+δX_fe²)/ρ_c とする。
    """
    t_c = max(float(concrete_cm), 0.0)
    t_s = max(float(soil_cm), 0.0)
    t_fe = max(float(iron_cm), 0.0)
    x_s = _soil_mass_thickness(t_s, profile=profile) if t_s > 0 else 0.0
    x_c = RHO_CONCRETE * t_c
    x_fe = RHO_IRON * t_fe
    t_eq = (x_c + x_s + x_fe) / RHO_CONCRETE

    dx_c_t = dx_c_r = 0.0
    if t_c > 0:
        dt_c = max(SYS_DT_CONCRETE_ABS_CM, SYS_DT_CONCRETE_FRAC * t_c)
        drho_c_rel = SYS_DRHO_CONCRETE / RHO_CONCRETE
        dx_c_t = x_c * (dt_c / t_c)
        dx_c_r = x_c * drho_c_rel

    dx_s_t = dx_s_r = 0.0
    if t_s > 0 and x_s > 0:
        dt_s = SYS_DT_SOIL_FRAC * t_s
        dx_s_t = x_s * (dt_s / t_s)
        dx_s_r = x_s * SYS_DRHO_SOIL_FRAC

    dx_fe_t = dx_fe_r = 0.0
    if t_fe > 0 and x_fe > 0:
        dt_fe = max(SYS_DT_IRON_ABS_CM, SYS_DT_IRON_FRAC * t_fe)
        drho_fe_rel = SYS_DRHO_IRON / RHO_IRON
        dx_fe_t = x_fe * (dt_fe / t_fe)
        dx_fe_r = x_fe * drho_fe_rel

    dx_c = float(np.hypot(dx_c_t, dx_c_r))
    dx_s = float(np.hypot(dx_s_t, dx_s_r))
    dx_fe = float(np.hypot(dx_fe_t, dx_fe_r))
    dteq_thick = float(np.hypot(np.hypot(dx_c_t, dx_s_t), dx_fe_t)) / RHO_CONCRETE
    dteq_dens = float(np.hypot(np.hypot(dx_c_r, dx_s_r), dx_fe_r)) / RHO_CONCRETE
    dteq = float(np.hypot(np.hypot(dx_c, dx_s), dx_fe)) / RHO_CONCRETE

    return {
        "t_eq_cm": t_eq,
        "dteq_cm": dteq,
        "dteq_thickness_cm": dteq_thick,
        "dteq_density_cm": dteq_dens,
        "dx_concrete": dx_c,
        "dx_soil": dx_s,
        "dx_iron": dx_fe,
    }


def _soil_mass_thickness(soil_cm: float, profile: str = SOIL_PROFILE) -> float:
    return esh.soil_mass_thickness_gcm2(soil_cm, profile=profile)


def _iron_mass_thickness(iron_cm: float) -> float:
    return max(float(iron_cm), 0.0) * RHO_IRON


def _mass_thickness(
    concrete_cm: float,
    soil_cm: float,
    iron_cm: float = 0.0,
    profile: str = SOIL_PROFILE,
) -> float:
    return (
        concrete_cm * RHO_CONCRETE
        + _soil_mass_thickness(soil_cm, profile=profile)
        + _iron_mass_thickness(iron_cm)
    )


def _equiv_concrete_cm_from_x(x_gcm2: float) -> float:
    return x_gcm2 / RHO_CONCRETE


def _optical_depth(x_c: float, x_s: float, x_fe: float = 0.0) -> float:
    """組成を反映した光学的厚さ τ = X_c/λ_c + X_s/λ_s + X_fe/λ_fe（無次元）。"""
    tau = x_c / LAMBDA_CONCRETE_GCM2 + x_s / LAMBDA_SOIL_GCM2
    if x_fe > 0:
        tau += x_fe / LAMBDA_IRON_GCM2
    return tau


def _equiv_concrete_cm_composition(x_c: float, x_s: float, x_fe: float = 0.0) -> float:
    """組成補正した等価コンクリート厚 [cm]。純コンクリートでは t_eq = t_c。"""
    return _optical_depth(x_c, x_s, x_fe) * LAMBDA_CONCRETE_GCM2 / RHO_CONCRETE


def _equiv_from_layers(
    concrete_cm: float,
    soil_cm: float,
    iron_cm: float = 0.0,
    profile: str = SOIL_PROFILE,
):
    """土+コンクリート+鉄厚から等価コンクリート（自動換算）。"""
    return esh.equiv_concrete(
        concrete_cm, soil_cm, iron_cm=iron_cm, profile=profile
    )


def _theory_rel(x_eq_cm, a0: float = 1.0):
    """A = A0 * exp(-x/λ_c)。x・λ_c とも等価コンクリート [cm]。"""
    return esh.theory_attenuation(x_eq_cm, a0=a0)


def _site_layers() -> list[dict]:
    """地点ごとの遮蔽層厚（検出器共通）。"""
    return [
        {"label": "地上", "concrete_cm": 0.0, "soil_cm": 0.0, "iron_cm": 0.0, "note": "基準（屋外）"},
        {"label": "PF", "concrete_cm": 105.0, "soil_cm": 0.0, "iron_cm": 0.0, "note": ""},
        {"label": "linac", "concrete_cm": 150.0, "soil_cm": 0.0, "iron_cm": 0.0, "note": ""},
        {
            "label": "BT",
            "concrete_cm": 60.0,
            "soil_cm": 220.0,
            "iron_cm": 0.0,
            "note": "土はロームのみ（220 cm < 3.5 m）",
        },
        {
            "label": "KEKB",
            "concrete_cm": 80.0,
            "soil_cm": 670.0,
            "iron_cm": 0.0,
            "note": "ローム3.5 m + 常総2.0 m + 下総1.2 m + コンクリ80 cm（Book5の117.25は桁誤り）",
        },
        {
            "label": "linacIRON",
            "concrete_cm": 200.0,
            "soil_cm": 100.0,
            "iron_cm": 150.0,
            "note": "土100 cm + コンクリート200 cm + 鉄150 cm（ρ_Fe=7.2）",
        },
    ]


def _site_shielding(cps_map: dict[str, float]) -> list[dict]:
    """層厚から X を算出し、CPS と組み合わせる（密度のみ）。"""
    sites = []
    for base in _site_layers():
        if base["label"] not in cps_map:
            continue
        site = dict(base)
        site["X"] = _mass_thickness(
            site["concrete_cm"], site["soil_cm"], site.get("iron_cm", 0.0)
        )
        site["cps"] = float(cps_map[site["label"]])
        if not site["note"]:
            site["note"] = f"X={site['X']:.2f}"
        sites.append(site)
    return sites


def _site_shielding_d1() -> list[dict]:
    """図11/12用（D1・側帯 NET CPS）。"""
    return _site_shielding(load_detector_cps("D1"))


def load_d2_cps() -> dict[str, float]:
    """小径 d2 の側帯 NET CPS（SN 2162、raw 実測のみ）。"""
    return load_detector_cps("d2")


def load_d1_cps() -> dict[str, float]:
    """小径 d1 の側帯 NET CPS（SN 2162、raw 実測のみ）。"""
    return load_detector_cps("d1")


def load_D2_cps() -> dict[str, float]:
    """大径 D2 の側帯 NET CPS（SN 1715、raw 実測のみ）。"""
    return load_detector_cps("D2")


def _equiv_concrete_for_detector(
    detector: str,
    *,
    absolute: bool = False,
    logy: bool = False,
) -> None:
    """検出器別の図11/12。raw に無い地点は載せない。接尾辞は small_d2 / large_D2 等。"""
    cps = load_detector_cps(detector)
    if "地上" not in cps:
        src = facility_cps_sources().get(detector, {})
        print(
            f"skip {detector}: 地上測定なし（施設地点={list(cps) or 'なし'} "
            f"sources={src}）。他検出器の値は流用しない。"
        )
        return
    if len(cps) < 2:
        print(f"skip {detector}: 比較地点が不足（{cps}）")
        return
    if not absolute and not logy:
        for site, place in sorted(facility_cps_sources().get(detector, {}).items()):
            print(f"  {detector} {site}: {place}  CPS={cps[site]:.6g}")
    fig_all_sites_equiv_concrete(
        absolute=absolute,
        logy=logy,
        cps_map=cps,
        ref_label="地上",
        name_suffix=detector_fs_suffix(detector),
        csv_name=equiv_decay_csv_name(detector),
        detector=detector,
    )


def _site_shielding_composition() -> list[dict]:
    """組成補正付き X・t_eq（図13/14）。土層は SOIL_PROFILE で自動換算。"""
    sites = []
    for base in _site_shielding_d1():
        site = dict(base)
        iron_cm = site.get("iron_cm", 0.0)
        r = _equiv_from_layers(site["concrete_cm"], site["soil_cm"], iron_cm)
        site["X_c"] = r.x_concrete_gcm2
        site["X_s"] = r.x_soil_gcm2
        site["X_fe"] = r.x_iron_gcm2
        site["X"] = r.x_total_gcm2
        site["tau"] = r.tau
        site["t_eq"] = r.t_eq_cm
        extras = []
        if site["soil_cm"] > 0:
            extras.append(f"組成λ補正({r.profile})")
        if iron_cm > 0:
            extras.append(f"鉄{iron_cm:.0f}cm")
        if extras:
            site["note"] = site["note"].rstrip("。") + "・" + "・".join(extras)
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

    cps = cps_map if cps_map is not None else load_detector_cps("D1")
    if not cps:
        print(f"skip {detector}: CPS が空")
        return
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
                "鉄_cm": f"{site.get('iron_cm', 0.0):.1f}",
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

    fig, ax = plt.subplots(figsize=EQUIV_FIGSIZE)
    fig.subplots_adjust(**EQUIV_SUBPLOT)

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
            "linacIRON": (8, -22),
        }
    else:
        offsets = {
            "地上": (8, -28),
            "PF": (8, 6),
            "linac": (8, -28),
            "BT": (8, 6),
            "KEKB": (-10, 6),
            "linacIRON": (8, -28),
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
        y_max = max(y_data_max, y_th_max, a0) * EQUIV_Y_PAD_LOGY
        ax.set_yscale("log")
        ax.set_ylim(y_min, y_max)
        ax.yaxis.set_major_locator(LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))
        ax.grid(True, which="major", alpha=0.35, linestyle="--")
        ax.grid(True, which="minor", axis="y", alpha=0.12, linestyle=":")
        ax.grid(True, which="minor", axis="x", alpha=0.18, linestyle=":")
    else:
        # 図11/12 と同じく A0（地上相当）まで見せる（凡例・注釈用に上余白）
        y_top = max(y_data_max, a0) * EQUIV_Y_PAD_LINEAR
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
    _equiv_legend(ax, fontsize=9)
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
    """小径 d2 検出器版の図11/12（SN 2162）。"""
    _equiv_concrete_for_detector("d2", absolute=absolute, logy=logy)


def fig_all_sites_equiv_concrete_d1(
    absolute: bool = False, logy: bool = False
) -> None:
    """小径 d1 検出器版の図11/12（SN 2162）。"""
    _equiv_concrete_for_detector("d1", absolute=absolute, logy=logy)


def fig_all_sites_equiv_concrete_D2(
    absolute: bool = False, logy: bool = False
) -> None:
    """大径 D2 検出器版の図11/12（SN 1715）。BT・KEKB 未測定。linacIRON あり。"""
    _equiv_concrete_for_detector("D2", absolute=absolute, logy=logy)


def fig_all_sites_equiv_concrete_d2_cps() -> None:
    fig_all_sites_equiv_concrete_d2(absolute=True)


def fig_all_sites_equiv_concrete_d2_semilog() -> None:
    fig_all_sites_equiv_concrete_d2(absolute=False, logy=True)


def fig_all_sites_equiv_concrete_d2_cps_semilog() -> None:
    fig_all_sites_equiv_concrete_d2(absolute=True, logy=True)


def fig_all_sites_equiv_concrete_d1_cps() -> None:
    fig_all_sites_equiv_concrete_d1(absolute=True)


def fig_all_sites_equiv_concrete_d1_semilog() -> None:
    fig_all_sites_equiv_concrete_d1(absolute=False, logy=True)


def fig_all_sites_equiv_concrete_d1_cps_semilog() -> None:
    fig_all_sites_equiv_concrete_d1(absolute=True, logy=True)


def fig_all_sites_equiv_concrete_D2_cps() -> None:
    fig_all_sites_equiv_concrete_D2(absolute=True)


def fig_all_sites_equiv_concrete_D2_semilog() -> None:
    fig_all_sites_equiv_concrete_D2(absolute=False, logy=True)


def fig_all_sites_equiv_concrete_D2_cps_semilog() -> None:
    fig_all_sites_equiv_concrete_D2(absolute=True, logy=True)


def _rel_cps_err(cps: float, cps_err: float, cps0: float, cps0_err: float) -> float:
    """相対 CPS = cps/cps0 の統計誤差（独立測定の伝播）。"""
    if cps <= 0 or cps0 <= 0:
        return 0.0
    return float(cps / cps0) * float(
        np.hypot(cps_err / cps if cps > 0 else 0.0, cps0_err / cps0 if cps0 > 0 else 0.0)
    )


def fig_all_sites_equiv_concrete_errorbars(
    *,
    absolute: bool = False,
    logy: bool = False,
    cps_map: dict[str, float] | None = None,
    cps_err_map: dict[str, float] | None = None,
    ref_label: str = "地上",
    name_suffix: str = "",
    csv_name: str = "等価コンクリート_減衰_誤差棒.csv",
    detector: str = "D1",
) -> None:
    """図11/12と同軸の新規図。縦=統計誤差、横=系統誤差（厚さ+密度の二乗和）。"""
    from matplotlib.ticker import LogLocator, MultipleLocator

    cps = cps_map if cps_map is not None else load_detector_cps("D1")
    cps_err = cps_err_map if cps_err_map is not None else load_detector_cps_err(detector)
    if not cps:
        print(f"skip errorbars {detector}: CPS が空")
        return
    sites = _site_shielding(cps)
    if ref_label not in cps:
        raise KeyError(f"基準地点 {ref_label!r} が CPS にありません: {list(cps)}")
    cps0 = float(cps[ref_label])
    cps0_err = float(cps_err.get(ref_label, 0.0))
    a0 = cps0 if absolute else 1.0
    lam_air = 1475.0 * 100.0
    rel_key = "相対_地上1"

    rows = []
    points = []
    for site in sites:
        x_eq = _equiv_concrete_cm_from_x(site["X"])
        sys = _teq_systematic_err_cm(
            site["concrete_cm"], site["soil_cm"], site.get("iron_cm", 0.0)
        )
        y_rel = site["cps"] / cps0
        y = site["cps"] if absolute else y_rel
        e_cps = float(cps_err.get(site["label"], 0.0))
        y_err = e_cps if absolute else _rel_cps_err(site["cps"], e_cps, cps0, cps0_err)
        x_err = float(sys["dteq_cm"])
        points.append(
            {
                "label": site["label"],
                "x": x_eq,
                "y": y,
                "x_err": x_err,
                "y_err": y_err,
                "cps": site["cps"],
                "cps_err": e_cps,
                "y_rel": y_rel,
                "site": site,
                "sys": sys,
            }
        )
        rows.append(
            {
                "地点": site["label"],
                "CPS": f"{site['cps']:.8f}",
                "CPS_統計誤差": f"{e_cps:.8f}",
                rel_key: f"{y_rel:.6f}",
                "相対_統計誤差": f"{_rel_cps_err(site['cps'], e_cps, cps0, cps0_err):.6f}",
                "土_cm": f"{site['soil_cm']:.1f}",
                "コンクリート_cm": f"{site['concrete_cm']:.1f}",
                "鉄_cm": f"{site.get('iron_cm', 0.0):.1f}",
                "質量厚さ_X": f"{site['X']:.2f}",
                "等価コンクリート_cm": f"{x_eq:.1f}",
                "等価コンクリート_系統誤差_cm": f"{x_err:.2f}",
                "系統_厚さ寄与_cm": f"{sys['dteq_thickness_cm']:.2f}",
                "系統_密度寄与_cm": f"{sys['dteq_density_cm']:.2f}",
                "理論_A0exp_相対": f"{float(np.asarray(_theory_rel(x_eq, 1.0)).reshape(-1)[0]):.6f}",
                "理論_A0exp_CPS": f"{float(np.asarray(_theory_rel(x_eq, cps0)).reshape(-1)[0]):.6f}",
                "備考": (
                    f"{site['note']}; "
                    f"系統=√(厚さ²+密度²) "
                    f"δt_c=max({SYS_DT_CONCRETE_ABS_CM}cm,{SYS_DT_CONCRETE_FRAC:.0%}t) "
                    f"δt_s={SYS_DT_SOIL_FRAC:.0%} "
                    f"δt_fe=max({SYS_DT_IRON_ABS_CM}cm,{SYS_DT_IRON_FRAC:.0%}t) "
                    f"δρ_c={SYS_DRHO_CONCRETE} δρ_s={SYS_DRHO_SOIL_FRAC:.0%} "
                    f"δρ_fe={SYS_DRHO_IRON}"
                ),
            }
        )

    out_csv = TABLES / csv_name
    if not absolute and not logy:
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    x_max = max(p["x"] + p["x_err"] for p in points) * 1.04
    # 地上(x=0)が左枠に張り付かない程度の余白（図11と同程度）
    x_left = -20.0
    x_air = np.linspace(x_left, 0, 200)
    x_c = np.linspace(0, x_max, 900)
    y_theory = _theory_rel(x_c, a0)

    fig, ax = plt.subplots(figsize=EQUIV_FIGSIZE)
    fig.subplots_adjust(**EQUIV_SUBPLOT)

    if not logy:
        ax.plot(
            x_air,
            a0 * np.exp(x_air / lam_air),
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

    measure_label = f"測定 {detector}" if absolute else f"測定 {detector}（地上=1）"
    ax.errorbar(
        [p["x"] for p in points],
        [p["y"] for p in points],
        xerr=[p["x_err"] for p in points],
        yerr=[p["y_err"] for p in points],
        fmt="o",
        color=RED,
        ms=8,
        zorder=3,
        elinewidth=1.0,
        capsize=2.5,
        label=measure_label,
    )

    if absolute:
        ax.set_ylabel("実測 CPS [1/s]")
        out_name = "16_全地点_等価コンクリート_実測CPS_誤差棒"
    else:
        ax.set_ylabel("相対 CPS（地上 = 1）")
        out_name = "16_全地点_等価コンクリート_誤差棒"
    if name_suffix:
        out_name = f"{out_name}{name_suffix}"

    y_data_max = max(p["y"] + p["y_err"] for p in points)
    y_th_max = float(np.max(y_theory))
    y_data_min = min(max(p["y"] - p["y_err"], 1e-12) for p in points)
    y_th_min = float(np.min(y_theory[y_theory > 0]))

    # 片対数でも左余白を残し、地上点が枠に乗らないようにする
    ax.set_xlim(x_left, x_max)
    if logy:
        out_name = f"{out_name}_片対数"
        # 図11と同じく、横軸全幅で理論曲線が枠内に収まるよう y を取る
        y_min = min(y_data_min, y_th_min) * 0.5
        y_max = max(y_data_max, y_th_max, a0) * EQUIV_Y_PAD_LOGY
        ax.set_yscale("log")
        ax.set_ylim(y_min, y_max)
        ax.yaxis.set_major_locator(LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))
        ax.grid(True, which="major", alpha=0.35, linestyle="--")
        ax.grid(True, which="minor", axis="y", alpha=0.12, linestyle=":")
        ax.grid(True, which="minor", axis="x", alpha=0.18, linestyle=":")
        offsets = {
            "地上": (12, -16),
            "PF": (8, 8),
            "linac": (8, -20),
            "BT": (-12, 10),
            "KEKB": (-10, 10),
            "linacIRON": (8, -18),
        }
    else:
        y_top = max(y_data_max, a0) * EQUIV_Y_PAD_LINEAR
        ax.set_ylim(0, y_top)
        if absolute:
            ax.yaxis.set_major_locator(MultipleLocator(0.05))
            ax.yaxis.set_minor_locator(MultipleLocator(0.01))
        else:
            ax.yaxis.set_major_locator(MultipleLocator(0.1))
            ax.yaxis.set_minor_locator(MultipleLocator(0.02))
        ax.grid(True, which="major", alpha=0.35, linestyle="--")
        ax.grid(True, which="minor", alpha=0.18, linestyle=":")
        offsets = {
            "地上": (10, -18),
            "PF": (8, 6),
            "linac": (8, -20),
            "BT": (-10, 8),
            "KEKB": (-10, 6),
            "linacIRON": (8, -18),
        }

    # 図11と同じ短い注釈（引出線なし・1行）
    for p in points:
        dx, dy = offsets.get(p["label"], (8, 8))
        if absolute:
            txt = f'{p["label"]}  {p["cps"]:.4f}±{p["cps_err"]:.4f}'
        else:
            txt = f'{p["label"]}  {p["y_rel"]:.3f}±{p["y_err"]:.3f}'
        ax.annotate(
            txt,
            (p["x"], p["y"]),
            textcoords="offset points",
            xytext=(dx, dy),
            fontsize=8,
            ha="left" if dx >= 0 else "right",
            va="center",
        )

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    ax.tick_params(which="major", direction="out", length=5)
    ax.tick_params(which="minor", direction="out", length=3)
    ax.set_xlabel(r"等価コンクリート厚さ [cm]（$t_{\mathrm{eq}}=X/\rho_c$）")
    _equiv_legend(ax, fontsize=9)
    save(fig, out_name, bbox_inches="none")
    print(f"figure: {out_name}.png")
    if not absolute and not logy:
        print(f"equiv errorbar table: {out_csv}")
    for p in points:
        print(
            f"  {p['label']}: x={p['x']:.1f}±{p['x_err']:.1f} cm  "
            f"y={p['y']:.4f}±{p['y_err']:.4f}  "
            f"(厚{p['sys']['dteq_thickness_cm']:.1f}+密{p['sys']['dteq_density_cm']:.1f})"
        )


def _equiv_concrete_errorbars_for_detector(
    detector: str,
    *,
    absolute: bool = False,
    logy: bool = False,
) -> None:
    cps = load_detector_cps(detector)
    if "地上" not in cps or len(cps) < 2:
        print(f"skip errorbars {detector}: 地点不足（{list(cps)}）")
        return
    fig_all_sites_equiv_concrete_errorbars(
        absolute=absolute,
        logy=logy,
        cps_map=cps,
        cps_err_map=load_detector_cps_err(detector),
        ref_label="地上",
        name_suffix=detector_fs_suffix(detector),
        csv_name=equiv_decay_csv_name(detector).replace(".csv", "_誤差棒.csv"),
        detector=detector,
    )


def fig_all_sites_equiv_concrete_errorbars_all() -> None:
    """D1 / D2 / d2 の誤差棒図（相対・実測 × 線形・片対数）を一括生成。"""
    for det in ("D1", "D2", "d2"):
        for absolute in (False, True):
            for logy in (False, True):
                _equiv_concrete_errorbars_for_detector(
                    det, absolute=absolute, logy=logy
                )


def fig_all_sites_equiv_concrete_detectors_compare(logy: bool = False) -> None:
    """4検出器（D1/D2/d1/d2）の相対 CPS を同一軸に重ねる。実測地点のみ。"""
    from matplotlib.ticker import LogLocator, MultipleLocator

    by_det = load_facility_cps_by_detector()
    sources = facility_cps_sources()
    plotted = []
    for det in ("D1", "D2", "d1", "d2"):
        cps = by_det.get(det) or {}
        if "地上" not in cps or len(cps) < 2:
            print(
                f"compare skip {det}: 地上なし or 地点不足 "
                f"({list(cps)}; {sources.get(det, {})})"
            )
            continue
        plotted.append(det)
        for site, place in sorted(sources.get(det, {}).items()):
            print(f"  compare {det} {site}: {place}  CPS={cps[site]:.6g}")

    if not plotted:
        print("compare skip: 重ねる検出器なし")
        return

    x_max = 0.0
    for base in _site_layers():
        if any(base["label"] in (by_det.get(d) or {}) for d in plotted):
            x_max = max(
                x_max,
                _equiv_concrete_cm_from_x(
                    _mass_thickness(
                        base["concrete_cm"],
                        base["soil_cm"],
                        base.get("iron_cm", 0.0),
                    )
                ),
            )
    x_max = max(x_max, 1.0) * 1.04
    x_c = np.linspace(0, x_max, 900)
    y_theory = _theory_rel(x_c, 1.0)

    fig, ax = plt.subplots(figsize=EQUIV_FIGSIZE)
    fig.subplots_adjust(**EQUIV_SUBPLOT)
    ax.plot(
        x_c,
        y_theory,
        color=GRAY,
        lw=2.0,
        label=rf"$A_0\,e^{{-x/\lambda_c}}$  （$\lambda_c={LAMBDA_CM:.1f}\,\mathrm{{cm}}$, $A_0=1$）",
    )
    ax.axvline(0, color="#CCCCCC", lw=0.8, zorder=1)

    for det in plotted:
        cps = by_det[det]
        cps0 = cps["地上"]
        style = DETECTOR_STYLE[det]
        xs, ys = [], []
        for base in _site_layers():
            lab = base["label"]
            if lab not in cps:
                continue
            x_eq = _equiv_concrete_cm_from_x(
                _mass_thickness(
                    base["concrete_cm"],
                    base["soil_cm"],
                    base.get("iron_cm", 0.0),
                )
            )
            xs.append(x_eq)
            ys.append(cps[lab] / cps0)
        ax.plot(
            xs,
            ys,
            linestyle="none",
            marker=style["marker"],
            color=style["color"],
            ms=style["ms"],
            zorder=3,
            label=style["label"],
        )

    ax.set_xlim(0 if logy else -20, x_max)
    ax.set_ylabel("相対 CPS（各地点の地上 = 1）")
    ax.set_xlabel(r"等価コンクリート厚さ [cm]（$t_{\mathrm{eq}}=X/\rho_c$）")
    out_name = "11_全地点_等価コンクリート_検出器比較"
    if logy:
        out_name += "_片対数"
        ax.set_yscale("log")
        ax.set_ylim(1e-6, EQUIV_Y_PAD_LOGY)
        ax.yaxis.set_major_locator(LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))
        ax.grid(True, which="major", alpha=0.35, linestyle="--")
        ax.grid(True, which="minor", axis="y", alpha=0.12, linestyle=":")
    else:
        ax.set_ylim(0, EQUIV_Y_PAD_LINEAR)
        ax.yaxis.set_major_locator(MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(MultipleLocator(0.02))
        ax.grid(True, which="major", alpha=0.35, linestyle="--")
        ax.grid(True, which="minor", alpha=0.18, linestyle=":")
    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    _equiv_legend(ax, fontsize=8)
    save(fig, out_name, bbox_inches="none")
    print(f"figure: {out_name}.png")


def fig_all_sites_equiv_concrete_composition(
    d: dict | None = None, absolute: bool = False
) -> None:
    """組成補正版。図11/12は上書きせず、図13/14として新規保存。"""
    from matplotlib.ticker import MultipleLocator

    cps0 = load_detector_cps("D1")["地上"]
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
                "鉄_cm": f"{site.get('iron_cm', 0.0):.1f}",
                "X_コンクリート": f"{site['X_c']:.2f}",
                "X_土": f"{site['X_s']:.2f}",
                "X_鉄": f"{site.get('X_fe', 0.0):.2f}",
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

    fig, ax = plt.subplots(figsize=EQUIV_FIGSIZE)
    fig.subplots_adjust(**EQUIV_SUBPLOT)

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
        ax.set_ylim(0, cps0 * EQUIV_Y_PAD_LINEAR)
        ax.yaxis.set_major_locator(MultipleLocator(0.05))
        ax.yaxis.set_minor_locator(MultipleLocator(0.01))
        ax.set_ylabel("実測 CPS [1/s]")
        out_name = "14_全地点_等価コンクリート_組成補正_実測CPS"
    else:
        ax.set_ylim(0, EQUIV_Y_PAD_LINEAR)
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
    _equiv_legend(ax, fontsize=9)
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



def cleanup_unsafe_detector_artifacts() -> None:
    """macOS で _d2/_D2 等が衝突する旧ファイル名を削除。

    d1 は施設地点（地上等）が raw に無いため、誤って d2 流用で作った図も消す。
    """
    unsafe_stems = [
        "11_全地点_等価コンクリート_d1",
        "11_全地点_等価コンクリート_d2",
        "11_全地点_等価コンクリート_D2",
        "12_全地点_等価コンクリート_実測CPS_d1",
        "12_全地点_等価コンクリート_実測CPS_d2",
        "12_全地点_等価コンクリート_実測CPS_D2",
    ]
    # d1 施設減衰図は raw に地上が無い限り無効
    if "地上" not in load_detector_cps("d1"):
        unsafe_stems.extend(
            [
                "11_全地点_等価コンクリート_small_d1",
                "12_全地点_等価コンクリート_実測CPS_small_d1",
            ]
        )
    for stem in unsafe_stems:
        for suffix in ("", "_片対数"):
            p = FIG / f"{stem}{suffix}.png"
            if p.exists():
                p.unlink()
    for name in (
        "等価コンクリート_減衰_d1.csv",
        "等価コンクリート_減衰_d2.csv",
        "等価コンクリート_減衰_D2.csv",
        "等価コンクリート_減衰_small_d1.csv",
    ):
        if "地上" in load_detector_cps("d1") and name.endswith("small_d1.csv"):
            continue
        p = TABLES / name
        if p.exists() and (
            not name.endswith("small_d1.csv") or "地上" not in load_detector_cps("d1")
        ):
            p.unlink()


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
    fig_all_sites_equiv_concrete_d1()
    fig_all_sites_equiv_concrete_d1_cps()
    fig_all_sites_equiv_concrete_d1_semilog()
    fig_all_sites_equiv_concrete_d1_cps_semilog()
    fig_all_sites_equiv_concrete_D2()
    fig_all_sites_equiv_concrete_D2_cps()
    fig_all_sites_equiv_concrete_D2_semilog()
    fig_all_sites_equiv_concrete_D2_cps_semilog()
    fig_all_sites_equiv_concrete_detectors_compare(logy=False)
    fig_all_sites_equiv_concrete_detectors_compare(logy=True)
    fig_all_sites_equiv_concrete_errorbars_all()
    cleanup_unsafe_detector_artifacts()
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
