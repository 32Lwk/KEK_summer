#!/usr/bin/env python3
"""強ノイズ small_d 4 件の ch≥300 割合補正（確認用）。

前提:
  - 入力 `raw/` はすでに方式 B（側帯フロア引き）済み
  - 熱中性子 d1 30cm/80cm の平均形状比に基づき、
    怪しいデータは wall 窓のうち ch≥300 だけを積分し 1/f で
    元の wall 窓相当へ換算する（窓定義自体は変えない）

出力（本解析 tables/figures は触らない）:
  - raw_denoised/                          … 補正 MCA
  - figures/地点別_denoised/<stem>/         … スペクトル
  - figures/地点別_denoised/theory_16_19/   … fig16–19
  - denoised_review/tables/                … 再集計表
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from mca_common import (  # noqa: E402
    PEAK_HALF_WIDTH,
    he3_wall_channels,
    high_ch_peak,
    infer_serial,
    parse_mca,
    peak_clip as roi_peak_clip,
    resolve_he3_energy_cal,
)

MEAS = ROOT / "測定_20260818"
RAW = MEAS / "raw"
RAW_DENOISED = MEAS / "raw_denoised"
REVIEW = MEAS / "denoised_review"
REVIEW_RAW = REVIEW / "raw"
REVIEW_TABLES = REVIEW / "tables"
SITE_FIG = MEAS / "figures" / "地点別_denoised"
THEORY_FIG = SITE_FIG / "theory_16_19"

# 強ノイズ 4 件（方式 B 後の raw/ を入力）
STRONG_NOISE = (
    "d1_20260823_1509_linac_testhole.mca",
    "d2_20260821_080725_linac.mca",
    "d1_20260823_1509_PS.mca",
    "d2_20260822_155046_地上.mca",
)

# 熱中性子テンプレ（両方の平均で f を検証。補正には指定値を使用）
THERMAL_REFS = (
    "d1_20260822_1705_熱中性子管理棟-30cm.mca",
    "d1_20260822_1702_熱中性子管理棟-80cm.mca",
)

CUT_CH = 300
# ユーザー指定。再計算平均は ~0.775（README に併記）
F_PARTIAL = 0.769

COPY_TABLE_GLOBS = (
    "検出器効率_壁効果191_764keV.csv",
    "等価コンクリート_*.csv",
    "PHITS_*.csv",
    "深さ_等価コンクリート_*.csv",
    "施設3D_*.csv",
    "施設3D_*.json",
    "測定地点マスタ.csv",
    "遮蔽換算_推奨パラメータ.csv",
    "フラックス_窓比較.csv",
)


def _place_from_stem(stem: str) -> str:
    parts = stem.split("_")
    return "_".join(parts[3:]) if len(parts) >= 4 else stem


def wall_bounds(counts: np.ndarray, serial: str, place: str) -> tuple[int, int, int]:
    """wall_lo, wall_hi, peak_ch。"""
    n = len(counts)
    roi_peak = high_ch_peak(counts, serial)
    cal = resolve_he3_energy_cal(serial, roi_peak, place)
    peak_ch = cal.peak_ch if cal else roi_peak
    wall = he3_wall_channels(serial, roi_peak, place, n=n)
    if wall is None:
        raise RuntimeError(f"壁窓を決められません: serial={serial} peak={roi_peak}")
    wlo, whi = wall
    return int(wlo), int(whi), int(peak_ch)


def thermal_partial_fraction(cut: int = CUT_CH) -> tuple[float, list[dict]]:
    """熱中性子 d1 2 本の f = N(ch≥cut ∩ wall) / N(wall)。"""
    rows: list[dict] = []
    for name in THERMAL_REFS:
        src = RAW / name
        meta = parse_mca(src, apply_gain_correction=False)
        counts = np.asarray(meta["counts"], dtype=float)
        serial = infer_serial(src.name, meta.get("serial") or "")
        place = _place_from_stem(src.stem)
        wlo, whi, peak_ch = wall_bounds(counts, serial, place)
        full = float(counts[wlo : whi + 1].sum())
        lo = max(wlo, cut)
        part = float(counts[lo : whi + 1].sum()) if lo <= whi else 0.0
        f = part / full if full > 0 else float("nan")
        rows.append(
            {
                "file": name,
                "wall": f"{wlo}-{whi}",
                "peak_ch": peak_ch,
                "N_full": full,
                "N_ge_cut": part,
                "f": f,
            }
        )
    mean_f = float(np.mean([r["f"] for r in rows]))
    return mean_f, rows


def apply_partial_correction(
    counts: np.ndarray,
    *,
    wlo: int,
    whi: int,
    cut: int = CUT_CH,
    f: float = F_PARTIAL,
) -> tuple[np.ndarray, dict]:
    """wall 内 ch<cut を 0、ch≥cut を 1/f 倍。窓外・側帯はそのまま。

    こうすると analyze_wall_window の GROSS ≈ N(≥cut)/f = 補正後 NET
    （方式 B 後は側帯≈0 のため）。
    """
    if f <= 0:
        raise ValueError(f"f must be positive, got {f}")
    out = np.asarray(counts, dtype=float).copy()
    lo = max(wlo, cut)
    n_full = float(counts[wlo : whi + 1].sum())
    n_part = float(counts[lo : whi + 1].sum()) if lo <= whi else 0.0
    # wall 内・cut 未満を落とす
    if wlo < cut:
        out[wlo:cut] = 0.0
    # cut〜wall_hi をスケール
    if lo <= whi:
        out[lo : whi + 1] *= 1.0 / f
    cleaned = np.rint(np.maximum(out, 0.0)).astype(int)
    info = {
        "wlo": wlo,
        "whi": whi,
        "cut": cut,
        "f": f,
        "N_full_before": n_full,
        "N_ge_cut_before": n_part,
        "N_wall_after": float(cleaned[wlo : whi + 1].sum()),
        "ratio_ge_cut": (n_part / n_full) if n_full > 0 else float("nan"),
    }
    return cleaned, info


def write_denoised_mca(src: Path, dst: Path, cleaned: np.ndarray) -> None:
    """DATA を置換し、Slow Count を新合計に合わせる。"""
    text = src.read_text(encoding="utf-8", errors="replace")
    data_block = "\n".join(str(int(x)) for x in cleaned)
    text2, n = re.subn(
        r"<<DATA>>\n[\s\S]*?\n<<END>>",
        f"<<DATA>>\n{data_block}\n<<END>>",
        text,
        count=1,
    )
    if n != 1:
        raise RuntimeError(f"DATA 置換失敗: {src.name}")
    total = int(cleaned.sum())
    text2, n2 = re.subn(
        r"(Slow Count:\s*)\d+",
        rf"\g<1>{total}",
        text2,
        count=1,
        flags=re.IGNORECASE,
    )
    if n2 != 1:
        text2, n2 = re.subn(
            r"Slow Count\s*[:：]\s*\d+",
            f"Slow Count: {total}",
            text2,
            count=1,
            flags=re.IGNORECASE,
        )
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text2, encoding="utf-8")


def make_corrected_mcas() -> list[dict]:
    RAW_DENOISED.mkdir(parents=True, exist_ok=True)
    mean_f, thermal_rows = thermal_partial_fraction()
    print(
        f"thermal mean f={mean_f:.6f}  (using F_PARTIAL={F_PARTIAL} for correction)"
    )
    for tr in thermal_rows:
        print(
            f"  {tr['file']}: wall={tr['wall']}  "
            f"N_full={tr['N_full']:.0f}  N≥{CUT_CH}={tr['N_ge_cut']:.0f}  f={tr['f']:.6f}"
        )

    reports: list[dict] = []
    for name in STRONG_NOISE:
        src = RAW / name
        if not src.exists():
            raise FileNotFoundError(src)
        meta = parse_mca(src, apply_gain_correction=False)
        counts = np.asarray(meta["counts"], dtype=float)
        serial = infer_serial(src.name, meta.get("serial") or "")
        place = _place_from_stem(src.stem)
        wlo, whi, peak_ch = wall_bounds(counts, serial, place)
        cleaned, info = apply_partial_correction(
            counts, wlo=wlo, whi=whi, cut=CUT_CH, f=F_PARTIAL
        )
        dst = RAW_DENOISED / name
        write_denoised_mca(src, dst, cleaned)
        live = float(meta["LIVE_TIME"])
        cps_before = info["N_full_before"] / live if live else float("nan")
        cps_after = info["N_wall_after"] / live if live else float("nan")
        rep = {
            "file": name,
            "serial": serial,
            "peak_ch": peak_ch,
            "wall": f"{wlo}-{whi}",
            "cut": CUT_CH,
            "f": F_PARTIAL,
            "N_full_before": info["N_full_before"],
            "N_ge_cut_before": info["N_ge_cut_before"],
            "ratio_ge_cut": info["ratio_ge_cut"],
            "N_wall_after": info["N_wall_after"],
            "cps_before": cps_before,
            "cps_after": cps_after,
            "thermal_mean_f": mean_f,
            "dst": str(dst),
        }
        reports.append(rep)
        print(
            f"  {name}: wall {wlo}-{whi}  "
            f"gross {info['N_full_before']:.0f} → {info['N_wall_after']:.0f}  "
            f"cps {cps_before:.6g} → {cps_after:.6g}  "
            f"(part/full={info['ratio_ge_cut']:.3f})"
        )

    readme = RAW_DENOISED / "README.md"
    lines = [
        "# raw_denoised（ch≥300 割合補正・確認用）",
        "",
        f"入力は方式 B 済みの `raw/`。対象 4 件について wall 内 ch<{CUT_CH} を 0、",
        f"ch≥{CUT_CH} を 1/{F_PARTIAL} 倍し、wall 積分が N(≥{CUT_CH})/{F_PARTIAL} になるようにした。",
        "",
        f"- 補正係数 f = {F_PARTIAL}（指定値）",
        f"- 熱中性子 d1 30/80cm 再計算平均 f = {mean_f:.6f}",
        "",
        "| ファイル | wall | N_full | N≥300 | part/full | N_wall補正後 |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for r in reports:
        lines.append(
            f"| `{r['file']}` | {r['wall']} | {r['N_full_before']:.0f} | "
            f"{r['N_ge_cut_before']:.0f} | {r['ratio_ge_cut']:.3f} | "
            f"{r['N_wall_after']:.0f} |"
        )
    readme.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return reports


def prepare_review_raw() -> None:
    """全 raw をコピーし、強ノイズ 4 件だけ補正 MCA で上書き。"""
    if REVIEW_RAW.exists():
        shutil.rmtree(REVIEW_RAW)
    REVIEW_RAW.mkdir(parents=True)
    for p in RAW.glob("*.mca"):
        shutil.copy2(p, REVIEW_RAW / p.name)
    for name in STRONG_NOISE:
        shutil.copy2(RAW_DENOISED / name, REVIEW_RAW / name)
    print(f"review raw: {REVIEW_RAW} ({len(list(REVIEW_RAW.glob('*.mca')))} mca)")


def copy_static_tables() -> None:
    REVIEW_TABLES.mkdir(parents=True, exist_ok=True)
    src_tables = MEAS / "tables"
    copied = 0
    for pattern in COPY_TABLE_GLOBS:
        for p in src_tables.glob(pattern):
            if p.is_file():
                shutil.copy2(p, REVIEW_TABLES / p.name)
                copied += 1
    detail = src_tables / "施設3D_施設詳細"
    if detail.is_dir():
        dst = REVIEW_TABLES / "施設3D_施設詳細"
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(detail, dst)
        copied += 1
    print(f"copied static tables: {copied}")


def rebuild_review_tables() -> None:
    import _build_mca_xlsx as bx
    import build_flux_summary as bfs
    import flux_calibration as fc

    bx.RAW = REVIEW_RAW
    bx.TABLES = REVIEW_TABLES
    bx.OUT = MEAS

    files = sorted(REVIEW_RAW.glob("*.mca"))
    rows = bx.load_runs(files)
    bx.write_tables(rows)
    print(f"wrote review tables → {REVIEW_TABLES}")

    bfs.TABLES = REVIEW_TABLES
    bfs.RECORD = REVIEW_TABLES / "測定記録.csv"
    bfs.OUT_LONG = REVIEW_TABLES / "フラックス_地点まとめ.csv"
    bfs.OUT_WIDE = REVIEW_TABLES / "フラックス_検出器別相対.csv"

    _orig = fc.load_wall_efficiencies_csv

    def _load_eff(path=None):
        return _orig(path or (REVIEW_TABLES / "検出器効率_壁効果191_764keV.csv"))

    fc.load_wall_efficiencies_csv = _load_eff  # type: ignore
    bfs.load_wall_efficiencies_csv = _load_eff  # type: ignore
    try:
        bfs.main()
    finally:
        fc.load_wall_efficiencies_csv = _orig  # type: ignore


def _series_from_mca(path: Path, color: str = "#D62728") -> tuple[np.ndarray, dict]:
    import _plot_mca as pm
    from mca_common import analyze_roi, analyze_wall_window

    meta = parse_mca(path, apply_gain_correction=True)
    counts = np.asarray(meta["counts"], dtype=float)
    live = float(meta["LIVE_TIME"])
    serial = infer_serial(path.name, meta.get("serial") or "")
    place = path.stem
    roi = analyze_roi(counts, serial)
    wall_r = analyze_wall_window(counts, serial)
    wall = he3_wall_channels(
        serial, roi.roi_peak, _place_from_stem(path.stem), n=len(counts)
    )
    wlo, whi = wall if wall else (None, None)
    cal = resolve_he3_energy_cal(serial, roi.roi_peak, _place_from_stem(path.stem))
    peak_ch = cal.peak_ch if cal else roi.roi_peak
    n = len(counts)
    if wall is not None and peak_ch > 0:
        sb_lo = min(n - 1, max(whi, peak_ch + PEAK_HALF_WIDTH) + 1)
        sb_hi = n - 1
    else:
        sb_lo, sb_hi = 0, 0
    cps = counts / live
    lo, hi = roi.roi_lo, roi.roi_hi
    clip = roi_peak_clip(
        cps,
        lo,
        hi,
        pad=max(pm.CLIP_PAD, 0.1 * float(np.max(cps[lo : hi + 1]) if hi >= lo else 0)),
    )
    s = {
        "id": path.stem,
        "場所": place,
        "シリアル": serial,
        "c": cps,
        "e": np.sqrt(np.maximum(counts, 0.0)) / live,
        "live": live,
        "lab": place,
        "color": color,
        "roi_lo": lo,
        "roi_hi": hi,
        "roi_peak": roi.roi_peak,
        "wall_lo": wlo,
        "wall_hi": whi,
        "wall_sb_hi_lo": sb_lo,
        "wall_sb_hi_hi": sb_hi,
        "roi_net_cps": wall_r.net / live if live else float("nan"),
        "roi_warning": wall_r.warning or "",
        "sb_lo_lo": wall_r.sb_lo_lo,
        "sb_lo_hi": wall_r.sb_lo_hi,
        "sb_hi_lo": wall_r.sb_hi_lo,
        "sb_hi_hi": wall_r.sb_hi_hi,
        "clip": clip,
    }
    ch = np.arange(n)
    return ch, s


def _annotate_partial_correction(ax, s: dict, *, logy: bool = False) -> None:
    """cut・捨てた帯・換算の説明を図に載せる。"""
    wlo = s.get("wall_lo")
    whi = s.get("wall_hi")
    ax.axvline(CUT_CH, color="#222222", ls="--", lw=1.2, zorder=4)
    if wlo is not None and whi is not None and wlo < CUT_CH:
        ax.axvspan(
            wlo,
            min(CUT_CH, whi + 1),
            color="#BBBBBB",
            alpha=0.35,
            zorder=0,
            label=f"捨てた帯 (wall内 ch<{CUT_CH})",
        )
    ymin, ymax = ax.get_ylim()
    y_txt = ymax * (0.08 if logy else 0.92)
    ax.text(
        CUT_CH + 2,
        y_txt,
        f"cut={CUT_CH}",
        va="bottom" if logy else "top",
        ha="left",
        fontsize=8,
        color="#222222",
        zorder=5,
    )
    note = (
        f"壁窓(緑)の定義は従来どおり 191–764 keV\n"
        f"・灰帯: wall内 ch<{CUT_CH} は捨てる（低chノイズ疑い）\n"
        f"・ch>={CUT_CH}: 実測 × (1/{F_PARTIAL}) で wall全体相当へ換算\n"
        f"・壁窓外の低chは表示のみ（積分に使わない）"
    )
    ax.text(
        0.98,
        0.98 if not logy else 0.02,
        note,
        transform=ax.transAxes,
        ha="right",
        va="top" if not logy else "bottom",
        fontsize=7.5,
        linespacing=1.35,
        bbox=dict(
            boxstyle="round,pad=0.35",
            facecolor="white",
            edgecolor="#888888",
            alpha=0.92,
        ),
        zorder=6,
    )


def _site_title(kind: str) -> str:
    return f"{kind}｜割合補正確認（cut={CUT_CH}, f={F_PARTIAL}）"


def plot_site_denoised() -> None:
    import _plot_mca as pm

    SITE_FIG.mkdir(parents=True, exist_ok=True)
    colors = ["#D62728", "#FF7F0E", "#2CA02C", "#1F77B4"]
    for i, name in enumerate(STRONG_NOISE):
        path = RAW_DENOISED / name
        ch, s = _series_from_mca(path, color=colors[i % len(colors)])
        out = SITE_FIG / path.stem
        out.mkdir(parents=True, exist_ok=True)

        c = s["c"]
        color = s["color"]
        clip = s["clip"]
        ctitle = pm.clip_title(clip)

        fig, ax = plt.subplots(figsize=(9.0, 5.0))
        ax.step(ch, c, where="mid", color=color, lw=1.4, label="補正後スペクトル")
        _annotate_partial_correction(ax, s)
        ax.set_xlim(0, 511)
        ax.set_ylim(0, None)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title("全ch 線形"))
        pm.place_legend(ax)
        pm.save(fig, "全ch_線形", out)

        fig, ax = plt.subplots(figsize=(9.0, 5.0))
        pm.step_spectrum(ax, ch, c, color, clip=clip)
        _annotate_partial_correction(ax, s)
        ax.set_xlim(0, 511)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title(f"全ch {ctitle}"))
        pm.place_legend(ax)
        pm.save(fig, "全ch_線形_クリップ", out)

        m = ch >= 1
        fig, ax = plt.subplots(figsize=(9.0, 5.0))
        ax.step(ch[m], c[m], where="mid", color=color, lw=1.4, label="補正後スペクトル")
        pm._decorate_he3_window(ax, s)
        _annotate_partial_correction(ax, s)
        ax.set_xlim(1, 511)
        ax.set_ylim(0, None)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title("全ch 線形（ch0除く）"))
        pm.place_legend(ax)
        pm.save(fig, "全ch_線形_ch0除く", out)

        fig, ax = plt.subplots(figsize=(9.0, 5.0))
        pm.step_spectrum(ax, ch[m], c[m], color, clip=clip)
        pm._decorate_he3_window(ax, s, show_energy_marks=True)
        _annotate_partial_correction(ax, s)
        ax.set_xlim(1, 511)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title(f"全ch {ctitle}（ch0除く）"))
        pm.place_legend(ax)
        pm.save(fig, "全ch_線形_ch0除く_クリップ", out)

        fig, ax = plt.subplots(figsize=(9.0, 5.0))
        ax.step(
            ch,
            pm.cps_for_log(c, live=s.get("live")),
            where="mid",
            color=color,
            lw=1.3,
            label="補正後スペクトル",
        )
        ax.set_yscale("log")
        pm._decorate_he3_window(ax, s, show_energy_marks=True)
        _annotate_partial_correction(ax, s, logy=True)
        ax.set_xlim(0, 511)
        ax.set_ylim(pm.LOG_Y_FLOOR, pm.LOG_Y_MAX)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title("対数"))
        pm.place_legend(ax)
        pm.save(fig, "全ch_対数", out)

        print(f"  site figs → {out.relative_to(MEAS)}")

    _write_site_fig_readme()


def _write_site_fig_readme() -> None:
    """地点別_denoised の見方。"""
    path = SITE_FIG / "README.md"
    lines = [
        "# 地点別_denoised（割合補正の確認用スペクトル）",
        "",
        "本解析の `figures/地点別/` とは別。**確認用**です。",
        "",
        "## 図の読み方（例: PS）",
        "",
        "![説明](d1_20260823_1509_PS/全ch_線形_ch0除く_クリップ.png)",
        "",
        "| 要素 | 意味 |",
        "|------|------|",
        "| **緑の帯** | wall窓（191–764 keV）。**定義は従来どおり** |",
        f"| **灰の帯** | wall内で **ch<{CUT_CH}**。低chノイズ疑いのため **積分から捨てた** |",
        f"| **黒破線 cut={CUT_CH}** | これより右だけを使う境界 |",
        f"| **cutより右の山** | 実測カウントを **×(1/{F_PARTIAL})** した形。"
        " wall全体相当の NET になるよう振幅を上げている |",
        "| **青の帯** | 764 keV より右の側帯（方式B後はほぼ0） |",
        "| **壁窓より左の高い山** | 壁窓の外。**フラックス計算には使わない**（表示のみ） |",
        "",
        "## 補正の式",
        "",
        f"`R_corr = N(ch>={CUT_CH} ∩ wall) / {F_PARTIAL}`",
        "",
        f"- `{F_PARTIAL}` は熱中性子 d1（30cm・80cm）の形状比（指定値）",
        "- 対象は強ノイズ small_d **4件のみ**",
        "",
        "## 対象フォルダ",
        "",
    ]
    for name in STRONG_NOISE:
        lines.append(f"- `{Path(name).stem}/`")
    lines += [
        "",
        "## fig16–19",
        "",
        f"`theory_16_19/` … 補正後のフラックス点を載せた確認用図",
        "",
        "## 本解析への反映",
        "",
        "確認OKなら次を実行（または「本解析にマージして」と指示）:",
        "",
        "```bash",
        "python3 03_今年度用/build_denoised_review.py --merge",
        "```",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def plot_theory_review() -> None:
    import _plot_mca as pm

    theory_dir = MEAS / "theory_research"
    if str(theory_dir) not in sys.path:
        sys.path.insert(0, str(theory_dir))
    import build_complete_theory as bct  # noqa: E402
    import plot_fig16_17_18_comparison as pfig  # noqa: E402

    THEORY_FIG.mkdir(parents=True, exist_ok=True)

    pm.TABLES = REVIEW_TABLES
    pm.FLUX_SUMMARY_CSV = REVIEW_TABLES / "フラックス_地点まとめ.csv"
    bct.TABLES_IN = MEAS / "tables"

    pfig.FIG_DIR = THEORY_FIG

    p = bct.load_transport_params()
    print(
        f"theory review: F0={p.F0_fast:.4g}, Λh={p.Lambda_h:.1f} → {THEORY_FIG}"
    )

    for det in pfig.FIG16_DETECTORS:
        pfig.fig16_cps(p, absolute=False, detector=det)
        pfig.fig16_cps(p, absolute=True, detector=det)
    for det in pfig.FIG17_DETECTORS:
        pfig.fig17_flux(p, detector=det)
    pfig.fig18_relative(p)
    pfig.fig18_compare(p, absolute=True)
    pfig.fig19_deep_compare(p, absolute=False)
    pfig.fig19_deep_compare(p, absolute=True)
    pfig.fig19_deep_compare_continuous(p, absolute=False)
    pfig.fig19_deep_compare_continuous(p, absolute=True)

    kept = sorted(THEORY_FIG.glob("1[6789]_*.png"))
    print(f"theory figs: {len(kept)}")
    for f in kept:
        print(f"  {f.name}")


def write_review_readme(reports: list[dict]) -> None:
    REVIEW.mkdir(parents=True, exist_ok=True)
    mean_f = reports[0]["thermal_mean_f"] if reports else float("nan")
    path = REVIEW / "README.md"
    lines = [
        "# denoised 確認用成果物（ch≥300 割合補正）",
        "",
        "本解析（`tables/`・`figures/`）は**未変更**（`--merge` するまで）。",
        "",
        "## 方式",
        "",
        "1. 入力: 方式 B（側帯フロア引き）済みの `raw/`",
        f"2. 対象 4 件のみ: wall 窓内で ch<{CUT_CH} を捨て、ch>={CUT_CH} を `1/f` 倍",
        f"3. f = {F_PARTIAL}（指定）。熱中性子 d1 30/80cm 再計算平均 = {mean_f:.6f}",
        "4. wall 窓の定義（191–764 keV）自体は変えない",
        "",
        "## 図の見方",
        "",
        f"→ `{SITE_FIG.relative_to(MEAS)}/README.md`",
        "",
        "## 出力場所",
        "",
        f"- MCA: `{RAW_DENOISED.relative_to(MEAS)}/`",
        f"- 地点別スペクトル: `{SITE_FIG.relative_to(MEAS)}/<stem>/`",
        f"- fig16–19: `{THEORY_FIG.relative_to(MEAS)}/`",
        f"- 再集計表: `{REVIEW_TABLES.relative_to(MEAS)}/`",
        "",
        "## 対象ファイル",
        "",
        f"| ファイル | wall | N_full | N>={CUT_CH} | part/full | cps前 | cps後 |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for r in reports:
        lines.append(
            f"| `{r['file']}` | {r['wall']} | {r['N_full_before']:.0f} | "
            f"{r['N_ge_cut_before']:.0f} | {r['ratio_ge_cut']:.3f} | "
            f"{r['cps_before']:.6g} | {r['cps_after']:.6g} |"
        )
    lines += [
        "",
        "## 本解析への反映",
        "",
        "```bash",
        "python3 03_今年度用/build_denoised_review.py --merge",
        "```",
        "",
        f"- 現在の `raw/`（方式B済み）4件は `raw_pre_partial_corr/` に退避",
        f"- `raw_denoised/` の補正 MCA を `raw/` に同名配置",
        "- tables / figures / theory を再計算",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def print_net_delta() -> None:
    """本番表 vs 確認用表の wall_net_cps 差分（対象 4 件）。"""
    import csv

    main_rec = MEAS / "tables" / "測定記録.csv"
    rev_rec = REVIEW_TABLES / "測定記録.csv"
    if not rev_rec.exists():
        return
    main = {
        r["filename"]: r
        for r in csv.DictReader(main_rec.open(encoding="utf-8"))
    }
    print("\nwall_net_cps 差分（本番 → ch≥300 補正 review）:")
    for name in STRONG_NOISE:
        a = main.get(name)
        b = next(
            (
                r
                for r in csv.DictReader(rev_rec.open(encoding="utf-8"))
                if r.get("filename") == name
            ),
            None,
        )
        if not a or not b:
            print(f"  {name}: missing")
            continue
        va, vb = float(a["wall_net_cps"]), float(b["wall_net_cps"])
        print(
            f"  {name}: {va:.6g} → {vb:.6g}  "
            f"(Δ={vb - va:+.4g}, ×{vb / va if va else float('nan'):.3f})"
        )


BACKUP_PARTIAL = MEAS / "raw_pre_partial_corr"


def merge_to_main() -> None:
    """補正 MCA を本解析 raw/ に入れ、tables・figures・theory を再計算。"""
    import csv
    import subprocess

    # 補正 MCA が無ければ先に作る
    missing = [n for n in STRONG_NOISE if not (RAW_DENOISED / n).exists()]
    if missing:
        print("raw_denoised が無いので先に補正 MCA を作成します…")
        make_corrected_mcas()

    BACKUP_PARTIAL.mkdir(parents=True, exist_ok=True)
    for name in STRONG_NOISE:
        src = RAW / name
        den = RAW_DENOISED / name
        if not den.exists():
            raise FileNotFoundError(den)
        if not src.exists():
            raise FileNotFoundError(src)
        bak = BACKUP_PARTIAL / name
        if not bak.exists():
            shutil.copy2(src, bak)
            csv0 = RAW / name.replace(".mca", ".csv")
            if csv0.exists():
                shutil.copy2(csv0, BACKUP_PARTIAL / csv0.name)
            print(f"backup: {name}")
        else:
            print(f"backup exists: {name}")
        shutil.copy2(den, src)
        print(f"installed corrected: {name}")

    (BACKUP_PARTIAL / "README.md").write_text(
        "\n".join(
            [
                "# raw_pre_partial_corr",
                "",
                "割合補正（ch≥300 / f）を本解析へ入れる直前の `raw/`（方式 B 済み）。",
                "",
                "復元: ここから同名ファイルを `raw/` へ戻し、",
                "`_build_mca_xlsx.py` → `calc_window_comparison.py` → "
                "`build_flux_summary.py` → `_plot_mca.py` → "
                "`theory_research/plot_fig16_17_18_comparison.py` を再実行。",
                "",
            ]
        ),
        encoding="utf-8",
    )

    steps = [
        ["python3", "_build_mca_xlsx.py", "--no-usb", "--no-plot"],
        ["python3", "calc_window_comparison.py"],
        ["python3", "build_flux_summary.py"],
        ["python3", "_plot_mca.py"],
        ["python3", "plot_fig16_17_18_comparison.py"],
    ]
    for cmd in steps:
        cwd = ROOT if cmd[1] != "plot_fig16_17_18_comparison.py" else (
            MEAS / "theory_research"
        )
        print(f"\n>>> {' '.join(cmd)}  (cwd={cwd.name})")
        subprocess.run(cmd, cwd=cwd, check=True)

    rows = {
        r["filename"]: r
        for r in csv.DictReader((MEAS / "tables" / "測定記録.csv").open(encoding="utf-8"))
    }
    print("\n本解析 wall_net_cps（マージ後）:")
    for name in STRONG_NOISE:
        r = rows[name]
        print(f"  {name}: {r['wall_net_cps']}")

    (RAW_DENOISED / "README.md").write_text(
        "\n".join(
            [
                "# raw_denoised",
                "",
                f"ch>={CUT_CH} 割合補正 MCA（f={F_PARTIAL}）。",
                "",
                "**本解析に反映済み**（`raw/` を置換。直前の方式B済みは "
                "`raw_pre_partial_corr/`）。",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"\nmerge done. backup={BACKUP_PARTIAL}")


def build_review() -> None:
    print("=== 1) ch≥300 割合補正 MCA ===")
    reports = make_corrected_mcas()

    print("\n=== 2) review raw + tables ===")
    prepare_review_raw()
    copy_static_tables()
    rebuild_review_tables()
    print_net_delta()

    print("\n=== 3) site figures ===")
    plot_site_denoised()

    print("\n=== 4) theory fig16–19 ===")
    plot_theory_review()

    write_review_readme(reports)
    print(f"\ndone. see {REVIEW / 'README.md'}")
    print(f"図の見方: {SITE_FIG / 'README.md'}")
    print("本解析反映: python3 build_denoised_review.py --merge")


def main(argv: list[str] | None = None) -> None:
    import argparse

    p = argparse.ArgumentParser(
        description="small_d 強ノイズ4件の ch≥300 割合補正（確認用 / 本解析マージ）"
    )
    p.add_argument(
        "--merge",
        action="store_true",
        help="補正 MCA を raw/ に入れ、本解析 tables・figures・theory を再計算",
    )
    p.add_argument(
        "--plots-only",
        action="store_true",
        help="既存 raw_denoised から地点別図だけ再生成",
    )
    args = p.parse_args(argv)

    if args.merge:
        merge_to_main()
    elif args.plots_only:
        plot_site_denoised()
    else:
        build_review()


if __name__ == "__main__":
    main()
