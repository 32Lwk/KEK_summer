#!/usr/bin/env python3
"""割合補正の確認用パイプライン（run ごとにフォルダを追加）。

出力は上書き共有ではなく、常に:

  測定_20260818/denoised_runs/<run_id>/
    raw/                 … 補正 MCA
    review_raw/          … 全 raw + 補正上書き（再集計用）
    tables/              … 再集計表
    figures/地点別/      … スペクトル
    figures/地点別/theory_16_19/
    README.md

確認用の統合ビュー（時系列）:

  測定_20260818/figures/地点別_denoised/
    stages/ … 各 run へのリンク
    timeline/ … 測定時刻順の統合ギャラリー

既定 run: large_d_cut200（d1/d2/D1/D2 統合・cut=200）。
  - D1/D2: f = D1熱中性子 30/80cm 平均
  - d1/d2: f = d1熱中性子 30/80cm 平均
確認用のみ（--merge するまで本解析は触らない）。
"""

from __future__ import annotations

import os
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
    analyze_roi,
    he3_wall_channels,
    high_ch_peak,
    infer_serial,
    parse_mca,
    peak_clip as roi_peak_clip,
    resolve_he3_energy_cal,
    roi_net_sideband,
)

MEAS = ROOT / "測定_20260818"
RAW = MEAS / "raw"
RUNS_ROOT = MEAS / "denoised_runs"
GALLERY = MEAS / "figures" / "地点別_denoised"
DEFAULT_RUN_ID = "large_d_cut200"

# configure_run() で設定
RUN_ID = DEFAULT_RUN_ID
RUN_DIR = RUNS_ROOT / DEFAULT_RUN_ID
RAW_DENOISED = RUN_DIR / "raw"
REVIEW = RUN_DIR
REVIEW_RAW = RUN_DIR / "review_raw"
REVIEW_TABLES = RUN_DIR / "tables"
SITE_FIG = RUN_DIR / "figures" / "地点別"
THEORY_FIG = SITE_FIG / "theory_16_19"
SCOPE = "all"  # all | large_d | small_d

# D1 熱中性子（large-D の f 基準）
THERMAL_REFS_LARGE = (
    "D1_20260822_1633_熱中性子管理棟-30cm.mca",
    "D1_20260822_1644_熱中性子管理棟2-80cm.mca",
)
# d1 熱中性子（small_d の f 基準）
THERMAL_REFS_SMALL = (
    "d1_20260822_1705_熱中性子管理棟-30cm.mca",
    "d1_20260822_1702_熱中性子管理棟-80cm.mca",
)
THERMAL_REFS = THERMAL_REFS_LARGE

CUT_CH = 200
# make_corrected_mcas() で更新（検出器族ごと）
F_PARTIAL = 0.0
F_LARGE = 0.0
F_SMALL = 0.0
FIXED_F: float | None = None

# 適応補正（large_d_cut200 / scope=all）
ADAPTIVE = False
# wall 窓補正 | peak764 ピーク ROI 補正
CORRECTION_MODE = "wall"  # wall | peak_roi
CUT_HIGH = 300  # C4: 左漏れが強いとき
F_AT_CUT: dict[tuple[str, int], float] = {}  # ('large'|'small', cut) -> f
F_AT_CUT_WALL: dict[tuple[str, int], float] = {}  # peak764: F5 用 wall gross f
THERMAL_PROFILE: dict[str, np.ndarray] = {}  # family -> mean counts (512,)
DIRT_R1_MARGIN = 0.03  # legacy（f 基準・未使用）
CLEAN_R1 = 0.84  # S2: これ以上かつ左漏れ弱ければ skip
DIRTY_R1 = 0.75  # S2: これ未満は補正
DIRT_R2_CUT300 = 0.45  # C4: 左漏れ強 → cut=300
DIRT_R2_MIN = 0.35  # S2: 左漏れ疑い
CUT300_DELTA = 0.06  # 参考（C4 では r2 優先）

# 強ノイズ hybrid: d1/d2 だけ legacy F2、同地点 D1/D2 は skip（01 実績）
LEGACY_CUT = 300
LEGACY_F = 0.769
LEGACY_SMALL_FILES = frozenset(
    {
        "d1_20260823_1509_PS.mca",
        "d1_20260823_1509_linac_testhole.mca",
        "d2_20260821_080725_linac.mca",
        "d2_20260822_155046_地上.mca",
    }
)
HYBRID_LARGE_SKIP_PLACES = frozenset({"PS", "testhole", "linac_testhole"})

# 01 と同様本番維持（過補正を避ける）
PROD_PRESERVE_PLACES = frozenset({"PF", "linac"})


def _is_testhole_place(place: str) -> bool:
    return place.endswith("testhole") or place == "testhole"


def _resolve_correction_mode(name: str, place: str) -> str:
    """地点別モード: skip | legacy_f2 | adaptive_f5 | skip_preserve | skip_hybrid。"""
    if _prod_preserve(place):
        return "skip_preserve"

    # peak764: 全件 peak ROI 部分補正（01/02 と同型、窓だけ peak ROI）
    if CORRECTION_MODE == "peak_roi":
        return "peak_partial"

    # Linac3: d2 は本番維持、他は適応 F5（大管を下げ d2 とのバランス改善）
    if place == "Linac3":
        return "skip" if name.startswith("d2_") else "adaptive_f5"

    # BT: D1 のみ適応 F5、d2 は本番（D1/d2 比 ~1.74）
    if place == "放射線棟BT":
        return "skip" if _is_small_name(name) else "adaptive_f5"

    # testhole: 大小とも legacy F2（|log(D1/d1)| ~0.26）
    if _is_testhole_place(place):
        return "legacy_f2"

    # PS 等: hybrid（大 skip + 小 legacy）
    if not _is_small_name(name) and _hybrid_large_skip(place):
        return "skip_hybrid"
    if _hybrid_small_legacy(name, place):
        return "legacy_f2"

    return "adaptive_f5"


def _prod_preserve(place: str) -> bool:
    return place in PROD_PRESERVE_PLACES


def _hybrid_large_skip(place: str) -> bool:
    """同地点 hybrid: 大検出器は skip。"""
    if place in HYBRID_LARGE_SKIP_PLACES:
        return True
    return place.endswith("testhole")


def _hybrid_small_legacy(name: str, place: str) -> bool:
    """強ノイズ d 系: legacy F2 cut300/f0.769。"""
    if name in LEGACY_SMALL_FILES:
        return True
    if _is_small_name(name) and _hybrid_large_skip(place):
        return True
    return False

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


def configure_run(
    run_id: str,
    *,
    cut: int | None = None,
    scope: str | None = None,
    fixed_f: float | None = None,
) -> None:
    """出力先を denoised_runs/<run_id>/ に切り替える（他 run は触らない）。"""
    global RUN_ID, RUN_DIR, RAW_DENOISED, REVIEW, REVIEW_RAW, REVIEW_TABLES
    global SITE_FIG, THEORY_FIG, CUT_CH, SCOPE, THERMAL_REFS, FIXED_F, F_PARTIAL
    RUN_ID = run_id.strip().strip("/")
    if not RUN_ID:
        raise ValueError("run_id が空です")
    if cut is not None:
        CUT_CH = int(cut)
    if scope is not None:
        SCOPE = scope.strip().lower()
    elif RUN_ID == "large_d_cut200" or RUN_ID.startswith("all_"):
        SCOPE = "all"
    elif "small_d" in RUN_ID:
        SCOPE = "small_d"
    elif "large_d" in RUN_ID:
        SCOPE = "large_d"
    if SCOPE not in {"all", "large_d", "small_d"}:
        raise ValueError(f"未知の scope: {SCOPE}")
    THERMAL_REFS = THERMAL_REFS_SMALL if SCOPE == "small_d" else THERMAL_REFS_LARGE
    FIXED_F = float(fixed_f) if fixed_f is not None else None
    if FIXED_F is not None:
        F_PARTIAL = float(FIXED_F)
    RUN_DIR = RUNS_ROOT / RUN_ID
    RAW_DENOISED = RUN_DIR / "raw"
    REVIEW = RUN_DIR
    REVIEW_RAW = RUN_DIR / "review_raw"
    REVIEW_TABLES = RUN_DIR / "tables"
    SITE_FIG = RUN_DIR / "figures" / "地点別"
    THEORY_FIG = SITE_FIG / "theory_16_19"
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    global ADAPTIVE, F_AT_CUT, F_AT_CUT_WALL, THERMAL_PROFILE, CORRECTION_MODE
    ADAPTIVE = RUN_ID == "large_d_cut200"
    CORRECTION_MODE = "peak_roi" if "peak764" in RUN_ID.lower() else "wall"
    if CORRECTION_MODE == "peak_roi":
        ADAPTIVE = True  # 02 と同じ地点別 skip/legacy/F5、 f だけ peak ROI 側帯 NET
        SCOPE = "all"
    F_AT_CUT = {}
    F_AT_CUT_WALL = {}
    THERMAL_PROFILE = {}


def update_runs_index() -> None:
    """denoised_runs/README.md に run 一覧を書く。"""
    RUNS_ROOT.mkdir(parents=True, exist_ok=True)
    lines = [
        "# denoised_runs（確認用・追記型）",
        "",
        "条件を変えるたびに **新しいフォルダ** を追加する。既存 run は上書きしない運用。",
        "",
        "| run_id | 説明 |",
        "|--------|------|",
    ]
    for d in sorted(p for p in RUNS_ROOT.iterdir() if p.is_dir()):
        note = ""
        readme = d / "README.md"
        if readme.exists():
            first = next(
                (ln.strip() for ln in readme.read_text(encoding="utf-8").splitlines() if ln.strip()),
                "",
            )
            note = first.lstrip("# ").strip()
        lines.append(f"| `{d.name}` | {note} |")
    lines += [
        "",
        "例:",
        "",
        "```bash",
        "python3 03_今年度用/build_denoised_review.py --run-id large_d_cut200",
        "python3 03_今年度用/build_denoised_review.py --run-id large_d_cut200 --merge",
        "```",
        "",
    ]
    (RUNS_ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")



def _is_small_name(name: str) -> bool:
    return name.startswith("d1_") or name.startswith("d2_")


def _skip_target(name: str) -> bool:
    """熱中性子・gain・D1 PF・_error を除外。"""
    if not name.startswith(("D1_", "D2_", "d1_", "d2_")):
        return True
    if "熱中性子" in name:
        return True
    low = name.lower()
    if "gain" in low or "corse" in low:
        return True
    if "_error" in name:
        return True
    if name.startswith("D1_") and "_PF" in name:
        return True
    if name == "d2_20260820_0807_PF.mca":
        return True
    return False


def list_targets() -> list[str]:
    if SCOPE == "small_d":
        return sorted(p.name for p in RAW.glob("d*.mca") if not _skip_target(p.name))
    if SCOPE == "large_d":
        return sorted(p.name for p in RAW.glob("D*.mca") if not _skip_target(p.name))
    # all: d1/d2/D1/D2
    return sorted(
        p.name
        for p in RAW.glob("*.mca")
        if p.name.startswith(("D1_", "D2_", "d1_", "d2_")) and not _skip_target(p.name)
    )


# 後方互換（旧 STRONG_NOISE 参照箇所用）。build 時に list_targets() で埋める
STRONG_NOISE: tuple[str, ...] = ()


def _refresh_targets() -> tuple[str, ...]:
    global STRONG_NOISE
    STRONG_NOISE = tuple(list_targets())
    return STRONG_NOISE


def f_for_file(name: str) -> float:
    """検出器族ごとの f。FIXED_F があれば全員同じ。"""
    if FIXED_F is not None:
        return float(FIXED_F)
    if _is_small_name(name):
        return float(F_SMALL if F_SMALL > 0 else F_PARTIAL)
    return float(F_LARGE if F_LARGE > 0 else F_PARTIAL)


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


def peak_roi_cut_eff(roi_lo: int, peak_ch: int, cut: int = CUT_CH) -> int:
    """peak ROI 内の effective cut。

    roi_lo > cut のとき peak ROI は wall より高 ch にあるため、
    01/02 と同型の「左側を捨てる」に相当する境界を peak−half とする。
    """
    if roi_lo > cut:
        return max(roi_lo, peak_ch - PEAK_HALF_WIDTH)
    return cut


def peak_roi_bounds(counts: np.ndarray, serial: str) -> tuple[int, int, int, int]:
    """peak ROI lo/hi, peak_ch, cut_eff（analyze_roi 窓）。"""
    roi = analyze_roi(np.asarray(counts, dtype=float), serial)
    cut_eff = peak_roi_cut_eff(roi.roi_lo, roi.roi_peak, CUT_CH)
    return int(roi.roi_lo), int(roi.roi_hi), int(roi.roi_peak), int(cut_eff)


def peak_roi_net_fraction(
    counts: np.ndarray, serial: str, cut: int = CUT_CH
) -> tuple[float, float, float, int, int, int]:
    """peak ROI の側帯 NET 比 f = NET(ch≥cut_eff) / NET(peak ROI)。"""
    c = np.asarray(counts, dtype=float)
    roi = analyze_roi(c, serial)
    lo, hi, peak = int(roi.roi_lo), int(roi.roi_hi), int(roi.roi_peak)
    cut_eff = peak_roi_cut_eff(lo, peak, cut)
    _, _, net_full, _, _, _, _ = roi_net_sideband(c, lo, hi, peak)
    lo2 = max(lo, cut_eff)
    if lo2 > hi or net_full <= 0:
        return float("nan"), net_full, 0.0, cut_eff, lo, hi
    _, _, net_part, _, _, _, _ = roi_net_sideband(c, lo2, hi, peak)
    f = net_part / net_full if net_full > 0 else float("nan")
    return f, net_full, net_part, cut_eff, lo, hi


def thermal_partial_fraction_peak(
    cut: int = CUT_CH, refs: tuple[str, ...] | None = None
) -> tuple[float, list[dict]]:
    """熱中性子 refs の f = NET(ch≥cut_eff ∩ peak ROI) / NET(peak ROI) の平均（側帯背景）。"""
    use = refs if refs is not None else THERMAL_REFS
    rows: list[dict] = []
    for name in use:
        src = RAW / name
        meta = parse_mca(src, apply_gain_correction=False)
        counts = np.asarray(meta["counts"], dtype=float)
        serial = infer_serial(src.name, meta.get("serial") or "")
        f, net_full, net_part, cut_eff, roi_lo, roi_hi = peak_roi_net_fraction(
            counts, serial, cut
        )
        rows.append(
            {
                "file": name,
                "peak_roi": f"{roi_lo}-{roi_hi}",
                "peak_ch": analyze_roi(counts, serial).roi_peak,
                "cut_eff": cut_eff,
                "N_full": net_full,
                "N_ge_cut": net_part,
                "f": f,
            }
        )
    mean_f = float(np.mean([r["f"] for r in rows]))
    return mean_f, rows


def thermal_partial_fraction(
    cut: int = CUT_CH, refs: tuple[str, ...] | None = None
) -> tuple[float, list[dict]]:
    """熱中性子 refs の f = N(ch≥cut ∩ wall) / N(wall) の平均。"""
    use = refs if refs is not None else THERMAL_REFS
    rows: list[dict] = []
    for name in use:
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


def apply_peak_roi_partial_correction(
    counts: np.ndarray,
    *,
    serial: str,
    cut: int = CUT_CH,
    f: float = F_PARTIAL,
) -> tuple[np.ndarray, dict]:
    """peak ROI 内 ch<cut_eff を 0、ch≥cut_eff を 1/f 倍。窓外・側帯はそのまま。

    f は熱中性子 peak ROI 側帯 NET 比（thermal_partial_fraction_peak）。
    補正後 peak NET ≈ NET(ch≥cut_eff)/f。
    """
    if f <= 0:
        raise ValueError(f"f must be positive, got {f}")
    c = np.asarray(counts, dtype=float)
    roi = analyze_roi(c, serial)
    lo, hi, peak = int(roi.roi_lo), int(roi.roi_hi), int(roi.roi_peak)
    cut_eff = peak_roi_cut_eff(lo, peak, cut)
    out = c.copy()
    lo2 = max(lo, cut_eff)
    n_full = float(c[lo : hi + 1].sum())
    n_part = float(c[lo2 : hi + 1].sum()) if lo2 <= hi else 0.0
    if lo < cut_eff:
        out[lo:cut_eff] = 0.0
    if lo2 <= hi:
        out[lo2 : hi + 1] *= 1.0 / f
    cleaned = np.rint(np.maximum(out, 0.0)).astype(int)
    _, _, net_before, _, _, _, _ = roi_net_sideband(c, lo, hi, peak)
    _, _, net_after, _, _, _, bg_mode = roi_net_sideband(
        cleaned.astype(float), lo, hi, peak
    )
    return cleaned, {
        "peak_roi": f"{lo}-{hi}",
        "cut_eff": cut_eff,
        "cut": cut,
        "f": f,
        "wlo": lo,
        "whi": hi,
        "N_full_before": n_full,
        "N_ge_cut_before": n_part,
        "N_wall_after": float(cleaned[lo : hi + 1].sum()),
        "ratio_ge_cut": (n_part / n_full) if n_full > 0 else float("nan"),
        "peak_net_before": net_before,
        "peak_net_after": net_after,
        "bg_mode": bg_mode,
        "skipped": False,
        "r2": None,
        "mode": "peak_partial",
    }


def _family_key(name: str) -> str:
    return "small" if _is_small_name(name) else "large"


def _ensure_f_at_cuts() -> None:
    """T1: 族×cut ごとの f をキャッシュ。"""
    global F_AT_CUT, F_LARGE, F_SMALL
    frac_fn = (
        thermal_partial_fraction_peak
        if CORRECTION_MODE == "peak_roi"
        else thermal_partial_fraction
    )
    for fam, refs in (
        ("large", THERMAL_REFS_LARGE),
        ("small", THERMAL_REFS_SMALL),
    ):
        for cut in (CUT_CH, CUT_HIGH):
            key = (fam, cut)
            if key not in F_AT_CUT:
                f, _ = frac_fn(cut, refs)
                F_AT_CUT[key] = float(f)
    F_LARGE = F_AT_CUT.get(("large", CUT_CH), F_LARGE)
    F_SMALL = F_AT_CUT.get(("small", CUT_CH), F_SMALL)


def _ensure_thermal_profiles() -> None:
    """F5: 族ごとの熱中性子平均スペクトル（512ch）。"""
    global THERMAL_PROFILE
    if THERMAL_PROFILE:
        return
    for fam, refs in (
        ("large", THERMAL_REFS_LARGE),
        ("small", THERMAL_REFS_SMALL),
    ):
        acc: np.ndarray | None = None
        n = 0
        for name in refs:
            meta = parse_mca(RAW / name, apply_gain_correction=False)
            c = np.asarray(meta["counts"], dtype=float)
            if acc is None:
                acc = np.zeros_like(c)
            acc += c
            n += 1
        if acc is not None and n:
            THERMAL_PROFILE[fam] = acc / n


def dirtiness_metrics(
    counts: np.ndarray,
    *,
    wlo: int,
    whi: int,
    peak_ch: int,
    cut: int,
    f_ref: float,
) -> dict:
    """R1=part/full, R2=wall低ch/ピーク帯。"""
    wall = counts[wlo : whi + 1]
    n_full = float(wall.sum())
    lo = max(wlo, cut)
    n_ge = float(counts[lo : whi + 1].sum()) if lo <= whi else 0.0
    r1 = n_ge / n_full if n_full > 0 else float("nan")
    lo300 = max(wlo, CUT_HIGH)
    n_ge300 = float(counts[lo300 : whi + 1].sum()) if lo300 <= whi else 0.0
    r300 = n_ge300 / n_full if n_full > 0 else float("nan")
    plo = max(wlo, peak_ch - 30)
    phi = min(whi, peak_ch + 30)
    peak_band = float(counts[plo : phi + 1].sum())
    hi_low = min(whi, cut - 1)
    n_low = float(counts[wlo : hi_low + 1].sum()) if wlo <= hi_low else 0.0
    r2 = n_low / peak_band if peak_band > 0 else 0.0
    return {
        "r1": r1,
        "r300": r300,
        "r2": r2,
        "r1_deficit": f_ref - r1 if np.isfinite(r1) else float("nan"),
        "r200_minus_r300": r1 - r300 if np.isfinite(r1) and np.isfinite(r300) else 0.0,
    }


def needs_adaptive_correction(metrics: dict, f_ref: float) -> bool:
    """S2: きれいな点は触らない（r1 絶対閾値 + 左漏れ）。"""
    r1 = metrics["r1"]
    r2 = metrics["r2"]
    if not np.isfinite(r1):
        return False
    if r1 >= CLEAN_R1 and r2 < DIRT_R2_MIN:
        return False
    if r1 < DIRTY_R1:
        return True
    if r2 >= DIRT_R2_MIN:
        return True
    return False


def choose_adaptive_cut(metrics: dict) -> int:
    """C4: 左漏れが強いときだけ cut=300。"""
    if metrics["r2"] >= DIRT_R2_CUT300:
        return CUT_HIGH
    return CUT_CH


def f_for_family_at_cut(name: str, cut: int) -> float:
    if FIXED_F is not None:
        return float(FIXED_F)
    fam = _family_key(name)
    _ensure_f_at_cuts()
    return F_AT_CUT.get((fam, cut), f_for_file(name))


def apply_adaptive_correction(
    counts: np.ndarray,
    *,
    wlo: int,
    whi: int,
    peak_ch: int,
    name: str,
) -> tuple[np.ndarray, dict]:
    """F5+部分積分: ch>=cut は観測、ch<cut は熱中性子テンプレで (1-f) 分を補完。"""
    fam = _family_key(name)
    f200 = f_for_family_at_cut(name, CUT_CH)
    m200 = dirtiness_metrics(
        counts, wlo=wlo, whi=whi, peak_ch=peak_ch, cut=CUT_CH, f_ref=f200
    )
    if not needs_adaptive_correction(m200, f200):
        n_full = float(counts[wlo : whi + 1].sum())
        return np.asarray(counts, dtype=float).copy().astype(int), {
            "skipped": True,
            "cut": CUT_CH,
            "f": f200,
            "wlo": wlo,
            "whi": whi,
            "N_full_before": n_full,
            "N_ge_cut_before": float(m200["r1"] * n_full) if n_full else 0.0,
            "N_wall_after": n_full,
            "ratio_ge_cut": m200["r1"],
            "r2": m200["r2"],
            "mode": "skip",
        }

    cut = choose_adaptive_cut(m200)
    f_ref = f_for_family_at_cut(name, cut)
    m = dirtiness_metrics(
        counts, wlo=wlo, whi=whi, peak_ch=peak_ch, cut=cut, f_ref=f_ref
    )
    _ensure_thermal_profiles()
    tmpl = THERMAL_PROFILE.get(fam)
    if tmpl is None:
        raise RuntimeError(f"thermal profile missing: {fam}")

    out = np.asarray(counts, dtype=float).copy()
    lo = max(wlo, cut)
    n_full = float(counts[wlo : whi + 1].sum())
    n_ge = float(counts[lo : whi + 1].sum()) if lo <= whi else 0.0
    n_wall_target = n_ge / f_ref if f_ref > 0 else n_full
    n_low_target = max(0.0, n_wall_target * (1.0 - f_ref))
    n_high_target = n_wall_target - n_low_target  # ≈ n_ge

    # F5: 低 ch 帯を熱中性子テンプレで埋める
    if wlo < cut:
        seg = tmpl[wlo:cut].astype(float)
        s = seg.sum()
        if s > 0 and n_low_target > 0:
            out[wlo:cut] = seg / s * n_low_target
        else:
            out[wlo:cut] = 0.0

    # ch>=cut: 観測を維持し、合計が n_high_target になるようスケール
    if lo <= whi:
        obs_hi = counts[lo : whi + 1].astype(float)
        obs_sum = float(obs_hi.sum())
        if obs_sum > 0 and n_high_target > 0:
            out[lo : whi + 1] = obs_hi * (n_high_target / obs_sum)
        else:
            out[lo : whi + 1] = 0.0

    cleaned = np.rint(np.maximum(out, 0.0)).astype(int)
    info = {
        "skipped": False,
        "cut": cut,
        "f": f_ref,
        "wlo": wlo,
        "whi": whi,
        "N_full_before": n_full,
        "N_ge_cut_before": n_ge,
        "N_wall_after": float(cleaned[wlo : whi + 1].sum()),
        "ratio_ge_cut": m["r1"],
        "r2": m["r2"],
        "mode": "adaptive_f5",
        "n_low_fill": n_low_target,
        "n_high_target": n_high_target,
    }
    return cleaned, info


def _skip_copy(
    counts: np.ndarray, *, wlo: int, whi: int, cut: int, f: float, mode: str
) -> tuple[np.ndarray, dict]:
    """観測スペクトルをそのまま返す（hybrid large / S2 skip）。"""
    n_full = float(counts[wlo : whi + 1].sum())
    lo = max(wlo, cut)
    n_ge = float(counts[lo : whi + 1].sum()) if lo <= whi else 0.0
    return np.asarray(counts, dtype=float).copy().astype(int), {
        "skipped": True,
        "cut": cut,
        "f": f,
        "wlo": wlo,
        "whi": whi,
        "N_full_before": n_full,
        "N_ge_cut_before": n_ge,
        "N_wall_after": n_full,
        "ratio_ge_cut": n_ge / n_full if n_full else float("nan"),
        "r2": None,
        "mode": mode,
    }


def apply_file_correction(
    counts: np.ndarray,
    *,
    wlo: int,
    whi: int,
    peak_ch: int,
    name: str,
    f_default: float,
    serial: str = "",
) -> tuple[np.ndarray, dict]:
    """large_d_cut200: 地点別 hybrid / legacy / 適応型 F5。"""
    place = _place_from_stem(Path(name).stem)
    mode = _resolve_correction_mode(name, place)

    if mode == "skip_preserve":
        return _skip_copy(
            counts, wlo=wlo, whi=whi, cut=CUT_CH, f=f_default, mode="skip_preserve"
        )
    if mode == "skip_hybrid":
        return _skip_copy(
            counts, wlo=wlo, whi=whi, cut=CUT_CH, f=f_default, mode="skip_hybrid"
        )
    if mode == "skip":
        return _skip_copy(
            counts, wlo=wlo, whi=whi, cut=CUT_CH, f=f_default, mode="skip_site"
        )
    if mode == "peak_partial":
        metrics = dirtiness_metrics(
            counts,
            wlo=wlo,
            whi=whi,
            peak_ch=peak_ch,
            cut=CUT_CH,
            f_ref=f_default,
        )
        if not needs_adaptive_correction(metrics, f_default):
            skipped, info = _skip_copy(
                counts,
                wlo=wlo,
                whi=whi,
                cut=CUT_CH,
                f=f_default,
                mode="peak_skip_clean",
            )
            info["peak_roi"] = info.get("peak_roi") or f"{wlo}-{whi}"
            return skipped, info
        cut_use = choose_adaptive_cut(metrics)
        f_use = f_for_family_at_cut(name, cut_use)
        cleaned, info = apply_peak_roi_partial_correction(
            counts, serial=serial, cut=cut_use, f=f_use
        )
        info["r2"] = metrics["r2"]
        return cleaned, info
    if mode == "legacy_f2":
        cleaned, info = apply_partial_correction(
            counts, wlo=wlo, whi=whi, cut=LEGACY_CUT, f=LEGACY_F
        )
        info["mode"] = "legacy_f2"
        info["skipped"] = False
        m = dirtiness_metrics(
            counts, wlo=wlo, whi=whi, peak_ch=peak_ch, cut=LEGACY_CUT, f_ref=LEGACY_F
        )
        info["r2"] = m["r2"]
        return cleaned, info
    return apply_adaptive_correction(
        counts, wlo=wlo, whi=whi, peak_ch=peak_ch, name=name
    )


def print_adaptive_evaluation() -> None:
    """E1+E2+E4: 同地点 D/d 差・きれい地点の変化・問題地点。"""
    import csv
    import math

    path = REVIEW_TABLES / "フラックス_地点まとめ.csv"
    prod = MEAS / "tables" / "フラックス_地点まとめ.csv"
    if not path.exists():
        return
    rev = {
        (r["検出器"], r["地点"]): float(r["絶対phi_n_cm2_s"])
        for r in csv.DictReader(path.open(encoding="utf-8"))
    }
    main = {
        (r["検出器"], r["地点"]): float(r["絶対phi_n_cm2_s"])
        for r in csv.DictReader(prod.open(encoding="utf-8"))
    }
    pairs = [
        ("D1", "d1"),
        ("D2", "d2"),
    ]
    watch = {"KEKB", "放射線棟BT", "PS", "testhole", "Linac3", "linac", "地上", "管理棟2階"}

    print("\n=== E1: 同地点 |log(D/d)|（小さいほど良い）===")
    gaps: list[tuple[str, str, float, float]] = []
    for place in sorted({k[1] for k in rev}):
        for Ld, sd in pairs:
            if (Ld, place) not in rev or (sd, place) not in rev:
                continue
            pL, ps = rev[(Ld, place)], rev[(sd, place)]
            if pL <= 0 or ps <= 0:
                continue
            gap = abs(math.log10(pL / ps))
            gaps.append((place, f"{Ld}/{sd}", gap, pL / ps))
    for place, pr, gap, ratio in sorted(gaps, key=lambda x: -x[2]):
        mark = " *" if place in watch else ""
        print(f"  {place:12} {pr:8} |logL/s|={gap:.3f}  L/s={ratio:.3f}{mark}")

    print("\n=== E2: きれい地点の φ 変化率（|1-比| が小さいほど良い）===")
    for det, place in [("D1", "管理棟2階"), ("D1", "地上"), ("d1", "管理棟2階"), ("D2", "地上")]:
        k = (det, place)
        if k in rev and k in main and main[k] > 0:
            chg = rev[k] / main[k]
            print(f"  {det} {place}: {main[k]:.4g} → {rev[k]:.4g}  ×{chg:.4f}")

    print("\n=== E4: 問題地点（φ と D/d 比）===")
    watch_pairs = [
        ("KEKB", "D1", "d2"),
        ("放射線棟BT", "D1", "d2"),
        ("PS", "D1", "d1"),
        ("testhole", "D1", "d1"),
        ("Linac3", "D1", "d1"),
        ("linac", "D1", "d1"),
        ("地上", "D2", "d2"),
    ]
    for place, Ld, sd in watch_pairs:
        kL, ks = (Ld, place), (sd, place)
        if kL not in rev:
            continue
        pL = rev[kL]
        mL = main.get(kL, float("nan"))
        if ks in rev and rev[ks] > 0:
            ratio = pL / rev[ks]
            gap = abs(math.log10(ratio))
            ps = rev[ks]
            ms = main.get(ks, float("nan"))
            print(
                f"  {place:10} {Ld}/{sd}: φ {mL:.4g}/{ms:.4g} → {pL:.4g}/{ps:.4g}  "
                f"L/s={ratio:.3f} |log|={gap:.3f}"
            )
        else:
            print(f"  {place:10} {Ld}: φ {mL:.4g} → {pL:.4g}  ({sd} なし)")

    out = RUN_DIR / "evaluation_adaptive.csv"
    lines = ["place,pair,abs_log_ratio,L_over_s"]
    for place, pr, gap, ratio in gaps:
        lines.append(f"{place},{pr},{gap:.6f},{ratio:.6f}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n  saved → {out.relative_to(MEAS)}")


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
    global F_PARTIAL, F_LARGE, F_SMALL
    targets = _refresh_targets()
    RAW_DENOISED.mkdir(parents=True, exist_ok=True)

    keep = set(targets)
    for old in RAW_DENOISED.glob("*.mca"):
        if old.name not in keep:
            old.unlink()
            print(f"  [{RUN_ID}] removed stale in-run: {old.name}")

    need_large = any(not _is_small_name(n) for n in targets)
    need_small = any(_is_small_name(n) for n in targets)

    thermal_rows_large: list[dict] = []
    thermal_rows_small: list[dict] = []
    frac_fn = thermal_partial_fraction_peak if CORRECTION_MODE == "peak_roi" else thermal_partial_fraction
    if FIXED_F is not None:
        F_LARGE = F_SMALL = F_PARTIAL = float(FIXED_F)
        print(f"[{RUN_ID}] fixed f={F_PARTIAL:.6f}  (cut={CUT_CH}, n={len(targets)})")
    else:
        if need_large or SCOPE in {"all", "large_d"}:
            F_LARGE, thermal_rows_large = frac_fn(CUT_CH, THERMAL_REFS_LARGE)
            fam_label = "D1 peak ROI" if CORRECTION_MODE == "peak_roi" else "D1 thermal"
            print(f"[{RUN_ID}] {fam_label} mean f_large={F_LARGE:.6f}  (cut={CUT_CH})")
            for tr in thermal_rows_large:
                if CORRECTION_MODE == "peak_roi":
                    print(
                        f"  {tr['file']}: peak_roi={tr['peak_roi']} cut_eff={tr['cut_eff']}  "
                        f"N_full={tr['N_full']:.0f}  N>={tr['cut_eff']}={tr['N_ge_cut']:.0f}  "
                        f"f={tr['f']:.6f}"
                    )
                else:
                    print(
                        f"  {tr['file']}: wall={tr['wall']}  "
                        f"N_full={tr['N_full']:.0f}  N>={CUT_CH}={tr['N_ge_cut']:.0f}  "
                        f"f={tr['f']:.6f}"
                    )
        if need_small or SCOPE in {"all", "small_d"}:
            F_SMALL, thermal_rows_small = frac_fn(CUT_CH, THERMAL_REFS_SMALL)
            fam_label = "d1 peak ROI" if CORRECTION_MODE == "peak_roi" else "d1 thermal"
            print(f"[{RUN_ID}] {fam_label} mean f_small={F_SMALL:.6f}  (cut={CUT_CH})")
            for tr in thermal_rows_small:
                if CORRECTION_MODE == "peak_roi":
                    print(
                        f"  {tr['file']}: peak_roi={tr['peak_roi']} cut_eff={tr['cut_eff']}  "
                        f"N_full={tr['N_full']:.0f}  N>={tr['cut_eff']}={tr['N_ge_cut']:.0f}  "
                        f"f={tr['f']:.6f}"
                    )
                else:
                    print(
                        f"  {tr['file']}: wall={tr['wall']}  "
                        f"N_full={tr['N_full']:.0f}  N>={CUT_CH}={tr['N_ge_cut']:.0f}  "
                        f"f={tr['f']:.6f}"
                    )
        # 注釈用の代表値
        F_PARTIAL = F_LARGE if F_LARGE > 0 else F_SMALL
        if ADAPTIVE:
            _ensure_f_at_cuts()
            _ensure_thermal_profiles()
            print(
                f"[{RUN_ID}] adaptive: f@200 L/S={F_AT_CUT.get(('large', CUT_CH), 0):.4f}/"
                f"{F_AT_CUT.get(('small', CUT_CH), 0):.4f}  "
                f"f@300 L/S={F_AT_CUT.get(('large', CUT_HIGH), 0):.4f}/"
                f"{F_AT_CUT.get(('small', CUT_HIGH), 0):.4f}"
            )

    reports: list[dict] = []
    for name in targets:
        src = RAW / name
        if not src.exists():
            raise FileNotFoundError(src)
        f_use = f_for_file(name)
        meta = parse_mca(src, apply_gain_correction=False)
        counts = np.asarray(meta["counts"], dtype=float)
        serial = infer_serial(src.name, meta.get("serial") or "")
        place = _place_from_stem(src.stem)
        peak_ch = 0
        wlo, whi, peak_ch = wall_bounds(counts, serial, place)
        if CORRECTION_MODE == "peak_roi" or ADAPTIVE:
            cleaned, info = apply_file_correction(
                counts,
                wlo=wlo,
                whi=whi,
                peak_ch=peak_ch,
                name=name,
                f_default=f_use,
                serial=serial,
            )
            bounds_label = info.get("peak_roi") or f"{info['wlo']}-{info['whi']}"
        else:
            cleaned, info = apply_partial_correction(
                counts, wlo=wlo, whi=whi, cut=CUT_CH, f=f_use
            )
            bounds_label = f"{wlo}-{whi}"
        dst = RAW_DENOISED / name
        write_denoised_mca(src, dst, cleaned)
        live = float(meta["LIVE_TIME"])
        cps_before = info["N_full_before"] / live if live else float("nan")
        cps_after = info["N_wall_after"] / live if live else float("nan")
        fam = "small_d" if _is_small_name(name) else "large_D"
        cut_used = info.get("cut", CUT_CH)
        f_used = info.get("f", f_use)
        mode = info.get("mode", "partial")
        bounds_key = "wall"
        rep = {
            "file": name,
            "family": fam,
            "serial": serial,
            "peak_ch": peak_ch,
            "wall": bounds_label,
            "cut": cut_used,
            "f": f_used,
            "N_full_before": info["N_full_before"],
            "N_ge_cut_before": info["N_ge_cut_before"],
            "ratio_ge_cut": info["ratio_ge_cut"],
            "N_wall_after": info["N_wall_after"],
            "cps_before": cps_before,
            "cps_after": cps_after,
            "thermal_mean_f": f_used,
            "skipped": info.get("skipped", False),
            "r2": info.get("r2"),
            "mode": mode,
            "dst": str(dst),
        }
        reports.append(rep)
        r2v = info.get("r2")
        r2s = f"{r2v:.3f}" if r2v is not None else "-"
        skip_mark = " [skip]" if info.get("skipped") else ""
        bounds_desc = bounds_label
        print(
            f"  {name}: [{fam}] {mode} cut={cut_used} f={f_used:.4f}  "
            f"wall {bounds_desc}  "
            f"gross {info['N_full_before']:.0f} → {info['N_wall_after']:.0f}  "
            f"cps {cps_before:.6g} → {cps_after:.6g}  "
            f"(part/full={info['ratio_ge_cut']:.3f}, r2={r2s})"
            f"{skip_mark}"
        )

    n_s = sum(1 for r in reports if r["family"] == "small_d")
    n_l = sum(1 for r in reports if r["family"] == "large_D")
    n_skip = sum(1 for r in reports if r.get("skipped"))
    n_adapt = sum(
        1 for r in reports if r.get("mode") in ("adaptive_f5", "legacy_f2")
    )
    readme = RUN_DIR / "README.md"
    if ADAPTIVE:
        title = (
            f"# {RUN_ID}（peak ROI 側帯 NET f · 02 地点別ロジック）"
            if CORRECTION_MODE == "peak_roi"
            else f"# {RUN_ID}（適応型補正・d/D 統合・確認用）"
        )
        f_note = (
            "- **T1**: f = D1/d1 熱中性子 **peak ROI 側帯 NET 比**（4ファイル平均）"
            if CORRECTION_MODE == "peak_roi"
            else "- **T1**: f_large = D1熱中性子、f_small = d1熱中性子（cut ごと）"
        )
        lines = [
            title,
            "",
            f"親ディレクトリ: `denoised_runs/{RUN_ID}/`（他 run とは独立）",
            "",
            "入力はいまの `raw/`（方式B済み4件含む）。",
            f"対象 {len(targets)} 件（small_d {n_s} + large_D {n_l}）。",
            "",
            "## 方針",
            "",
            "- **S2**: part/full ≥ 0.84 かつ左漏れ弱い地点は**未補正**",
            f"- **C4**: 左漏れ r2≥{DIRT_R2_CUT300} のとき cut={CUT_HIGH}、それ以外 cut={CUT_CH}",
            "- **F5**: ch<cut を熱中性子テンプレ、ch≥cut は観測維持で wall 合計 = N_ge/f",
            f_note,
            "",
            f"- f_large @ {CUT_CH} = {F_LARGE:.6f}",
            f"- f_small @ {CUT_CH} = {F_SMALL:.6f}",
            f"- 適用 {n_adapt} 件 / skip {n_skip} 件",
            f"- **hybrid**: PS → D skip + d legacy F2 (cut={LEGACY_CUT}, f={LEGACY_F})",
            f"- **testhole**: 大小とも legacy F2",
            f"- **BT**: D1 適応 F5、d2 本番",
            f"- **Linac3**: d2 本番、他適応 F5",
            f"- **preserve**: PF, linac（トンネル linac 系）→ 本番維持",
            "- 除外: 熱中性子・gain・D1/d2 PF・`_error`",
            "- 本解析は未変更（`--merge` するまで）",
            "",
            "## 中身",
            "",
            "- `raw/` … 補正 MCA",
            "- `review_raw/` … 再集計用",
            "- `tables/`",
            "- `figures/地点別/`",
            "- `evaluation_adaptive.csv` … 同地点 D/d 評価",
            "",
            "| ファイル | 族 | mode | cut | wall | part/full | r2 | f | N_wall補正後 |",
            "|---|---|---|---:|---|---:|---:|---:|---:|",
        ]
        for r in reports:
            r2s = f"{r['r2']:.3f}" if r.get("r2") is not None else "-"
            wall_col = r.get("wall") or r.get("peak_roi") or "-"
            lines.append(
                f"| `{r['file']}` | {r['family']} | {r.get('mode', '-')} | {r['cut']} | "
                f"{wall_col} | {r['ratio_ge_cut']:.3f} | {r2s} | {r['f']:.4f} | "
                f"{r['N_wall_after']:.0f} |"
            )
    else:
        lines = [
            f"# {RUN_ID}（d/D 統合・ch>={CUT_CH} 割合補正・確認用）",
            "",
            f"親ディレクトリ: `denoised_runs/{RUN_ID}/`（他 run とは独立）",
            "",
            f"入力はいまの `raw/`。対象 {len(targets)} 件（small_d {n_s} + large_D {n_l}）について",
            f"wall 内 ch<{CUT_CH} を 0、ch>={CUT_CH} を 1/f 倍。",
            "",
            f"- cut = {CUT_CH}",
            f"- f_large (D1/D2) = {F_LARGE:.6f}（D1 熱中性子 30cm/80cm 平均）"
            if F_LARGE > 0
            else f"- f_large = (未使用)",
            f"- f_small (d1/d2) = {F_SMALL:.6f}（d1 熱中性子 30cm/80cm 平均）"
            if F_SMALL > 0
            else f"- f_small = (未使用)",
            "- 除外: 熱中性子・gain・D1 PF・`_error`",
            "- 本解析は未変更（`--merge` するまで）",
            "",
            "## 中身",
            "",
            "- `raw/` … 補正 MCA",
            "- `review_raw/` … 再集計用（全 raw + 補正上書き）",
            "- `tables/`",
            "- `figures/地点別/`",
            "",
            f"| ファイル | 族 | wall | N_full | N>={CUT_CH} | part/full | f | N_wall補正後 |",
            "|---|---|---|---:|---:|---:|---:|---:|",
        ]
        for r in reports:
            lines.append(
                f"| `{r['file']}` | {r['family']} | {r.get('wall', '-')} | "
                f"{r['N_full_before']:.0f} | {r['N_ge_cut_before']:.0f} | "
                f"{r['ratio_ge_cut']:.3f} | {r['f']:.4f} | {r['N_wall_after']:.0f} |"
            )
    readme.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (RAW_DENOISED / "README.md").write_text(
        f"# {RUN_ID} 補正 MCA\n\n詳細は `../README.md`。\n",
        encoding="utf-8",
    )
    return reports


# 他 run（例: small_d_cut300）の地点別フォルダを残すための stem 集合
OVERLAY_SITE_STEMS: set[str] = set()


def prepare_review_raw(*, overlay_run_ids: list[str] | None = None) -> None:
    """全 raw をコピーし、本 run 補正 MCA で上書き。必要なら他 run も重ねる。"""
    targets = STRONG_NOISE or _refresh_targets()
    if REVIEW_RAW.exists():
        shutil.rmtree(REVIEW_RAW)
    REVIEW_RAW.mkdir(parents=True)
    for p in RAW.glob("*.mca"):
        shutil.copy2(p, REVIEW_RAW / p.name)
    for name in targets:
        src = RAW_DENOISED / name
        if not src.exists():
            raise FileNotFoundError(src)
        shutil.copy2(src, REVIEW_RAW / name)
    overlaid: list[str] = []
    for rid in overlay_run_ids or []:
        other = RUNS_ROOT / rid / "raw"
        if not other.is_dir():
            raise FileNotFoundError(f"overlay run raw がありません: {other}")
        for p in sorted(other.glob("*.mca")):
            shutil.copy2(p, REVIEW_RAW / p.name)
            overlaid.append(f"{rid}:{p.name}")
            print(f"  overlay MCA ← {rid}/{p.name}")
    print(
        f"review raw: {REVIEW_RAW} "
        f"({len(list(REVIEW_RAW.glob('*.mca')))} mca, overlay={len(overlaid)})"
    )


def overlay_run_site_figures(run_id: str) -> list[str]:
    """他 run の地点別スペクトル図を本 run の figures/地点別 に取り込む。"""
    global OVERLAY_SITE_STEMS
    src_root = RUNS_ROOT / run_id / "figures" / "地点別"
    if not src_root.is_dir():
        raise FileNotFoundError(src_root)
    SITE_FIG.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for d in sorted(p for p in src_root.iterdir() if p.is_dir()):
        if d.name == "theory_16_19":
            continue
        dst = SITE_FIG / d.name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(d, dst)
        OVERLAY_SITE_STEMS.add(d.name)
        copied.append(d.name)
        print(f"  overlay site fig ← {run_id}/{d.name}")
    return copied


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
    prev_flux = bfs.FLUX_WINDOW
    if CORRECTION_MODE == "peak_roi":
        bfs.FLUX_WINDOW = "peak"
        print("  FLUX_WINDOW=peak（764 keV peak ROI · εS_peak）")

    _orig = fc.load_wall_efficiencies_csv

    def _load_eff(path=None):
        return _orig(path or (REVIEW_TABLES / "検出器効率_壁効果191_764keV.csv"))

    fc.load_wall_efficiencies_csv = _load_eff  # type: ignore
    bfs.load_wall_efficiencies_csv = _load_eff  # type: ignore
    try:
        bfs.main()
    finally:
        fc.load_wall_efficiencies_csv = _orig  # type: ignore
        bfs.FLUX_WINDOW = prev_flux


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
    cut_eff = peak_roi_cut_eff(lo, int(roi.roi_peak), CUT_CH)
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
        "cut_eff": cut_eff,
        "wall_lo": wlo,
        "wall_hi": whi,
        "wall_sb_hi_lo": sb_lo,
        "wall_sb_hi_hi": sb_hi,
        "roi_net_cps": wall_r.net / live if live else float("nan"),
        "roi_warning": wall_r.warning or "",
        # peak ROI 側帯（analyze_roi）
        "peak_sb_lo_lo": roi.sb_lo_lo,
        "peak_sb_lo_hi": roi.sb_lo_hi,
        "peak_sb_hi_lo": roi.sb_hi_lo,
        "peak_sb_hi_hi": roi.sb_hi_hi,
        # wall 側帯（参考・01/02 用）
        "sb_lo_lo": wall_r.sb_lo_lo,
        "sb_lo_hi": wall_r.sb_lo_hi,
        "sb_hi_lo": wall_r.sb_hi_lo,
        "sb_hi_hi": wall_r.sb_hi_hi,
        "clip": clip,
    }
    ch = np.arange(n)
    return ch, s


def _decorate_site_windows(ax, s: dict, *, show_energy_marks: bool = False) -> None:
    """地点別図の主窓。peak764 は peak ROI、それ以外は wall 窓。"""
    import _plot_mca as pm

    if CORRECTION_MODE == "peak_roi":
        lo, hi = s.get("roi_lo"), s.get("roi_hi")
        c_arr = s.get("c")
        nch = int(np.asarray(c_arr).size) if c_arr is not None else 0
        # 512ch MCA は表示上 512 まで（データ最終 ch は 511）
        ch_hi = 512 if nch == 512 else max(nch - 1, 0)
        if lo is not None and hi is not None:
            ax.axvspan(
                int(lo),
                int(hi),
                color="#F4C7C3",
                alpha=0.45,
                zorder=0,
                label=f"peak ROI {int(lo)}–{int(hi)}",
            )
            # 青帯: peak ROI より右（hi+1 … 最終 ch）
            sb_lo = int(hi) + 1
            if sb_lo <= ch_hi:
                ax.axvspan(
                    sb_lo,
                    ch_hi,
                    color="#9EC9E2",
                    alpha=0.35,
                    zorder=0,
                    label=f"peak右 {sb_lo}–{ch_hi}",
                )
        # wall は参考のみ（凡例に出さない）
        wlo, whi = s.get("wall_lo"), s.get("wall_hi")
        if wlo is not None and whi is not None:
            ax.axvspan(
                int(wlo),
                int(whi),
                color="#C8E6C9",
                alpha=0.12,
                zorder=0,
            )
        if show_energy_marks:
            pm.mark_he3_energies(ax, s, show_cal_tag=False)
        return
    pm._decorate_he3_window(ax, s, show_energy_marks=show_energy_marks)


def _annotate_partial_correction(ax, s: dict, *, logy: bool = False) -> None:
    """cut 線と積分除外帯を載せる（長文コメントは出さない）。"""
    del logy  # 互換のため残す
    # peak764: 積分除外は図に出さず、peak ROI として一体表示
    if CORRECTION_MODE == "peak_roi":
        return

    wlo = s.get("wall_lo")
    whi = s.get("wall_hi")
    cut_eff = CUT_CH
    ax.axvline(
        cut_eff,
        color="#222222",
        ls="--",
        lw=1.2,
        zorder=4,
        label=f"cut={CUT_CH}",
    )
    if wlo is not None and whi is not None and wlo < cut_eff:
        ax.axvspan(
            wlo,
            min(cut_eff, whi + 1),
            color="#BBBBBB",
            alpha=0.35,
            zorder=0,
            label=f"積分除外帯 (ch<{cut_eff})",
        )


def _site_title(kind: str, f: float | None = None) -> str:
    ff = F_PARTIAL if f is None else f
    if CORRECTION_MODE == "peak_roi":
        return f"{kind}｜peak ROI, ×1/{ff:.4f}"
    return f"{kind}｜cut={CUT_CH}, ×1/{ff}"


def _ensure_fs() -> None:
    """注釈・プロット用に F_LARGE / F_SMALL を用意。"""
    global F_PARTIAL, F_LARGE, F_SMALL
    if FIXED_F is not None:
        F_LARGE = F_SMALL = F_PARTIAL = float(FIXED_F)
        return
    frac_fn = thermal_partial_fraction_peak if CORRECTION_MODE == "peak_roi" else thermal_partial_fraction
    if F_LARGE <= 0 and SCOPE in {"all", "large_d"}:
        F_LARGE, _ = frac_fn(CUT_CH, THERMAL_REFS_LARGE)
    if F_SMALL <= 0 and SCOPE in {"all", "small_d"}:
        F_SMALL, _ = frac_fn(CUT_CH, THERMAL_REFS_SMALL)
    if F_PARTIAL <= 0:
        F_PARTIAL = F_LARGE if F_LARGE > 0 else F_SMALL


def plot_site_denoised() -> None:
    import _plot_mca as pm

    targets = STRONG_NOISE or _refresh_targets()
    _ensure_fs()

    SITE_FIG.mkdir(parents=True, exist_ok=True)
    keep_dirs = {Path(n).stem for n in targets} | {"theory_16_19"} | set(OVERLAY_SITE_STEMS)
    for d in list(SITE_FIG.iterdir()):
        if d.is_dir() and d.name not in keep_dirs:
            shutil.rmtree(d)
            print(f"  [{RUN_ID}] removed stale site dir: {d.name}")

    colors = ["#D62728", "#FF7F0E", "#2CA02C", "#1F77B4", "#9467BD", "#8C564B"]
    for i, name in enumerate(targets):
        path = RAW_DENOISED / name
        if not path.exists():
            raise FileNotFoundError(path)
        f_use = f_for_file(name)
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
        ax.set_title(_site_title("全ch 線形", f_use))
        pm.place_legend(ax)
        pm.save(fig, "全ch_線形", out)

        fig, ax = plt.subplots(figsize=(9.0, 5.0))
        pm.step_spectrum(ax, ch, c, color, clip=clip)
        _annotate_partial_correction(ax, s)
        ax.set_xlim(0, 511)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title(f"全ch {ctitle}", f_use))
        pm.place_legend(ax)
        pm.save(fig, "全ch_線形_クリップ", out)

        m = ch >= 1
        fig, ax = plt.subplots(figsize=(9.0, 5.0))
        ax.step(ch[m], c[m], where="mid", color=color, lw=1.4, label="補正後スペクトル")
        _decorate_site_windows(ax, s)
        _annotate_partial_correction(ax, s)
        ax.set_xlim(1, 511)
        ax.set_ylim(0, None)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title("全ch 線形（ch0除く）", f_use))
        pm.place_legend(ax)
        pm.save(fig, "全ch_線形_ch0除く", out)

        fig, ax = plt.subplots(figsize=(9.0, 5.0))
        pm.step_spectrum(ax, ch[m], c[m], color, clip=clip)
        _decorate_site_windows(ax, s, show_energy_marks=True)
        _annotate_partial_correction(ax, s)
        ax.set_xlim(1, 511)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title(f"全ch {ctitle}（ch0除く）", f_use))
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
        _decorate_site_windows(ax, s, show_energy_marks=True)
        _annotate_partial_correction(ax, s, logy=True)
        ax.set_xlim(0, 511)
        ax.set_ylim(pm.LOG_Y_FLOOR, pm.LOG_Y_MAX)
        ax.set_xlabel("チャンネル")
        ax.set_ylabel(pm.YLABEL)
        ax.set_title(_site_title("対数", f_use))
        pm.place_legend(ax)
        pm.save(fig, "全ch_対数", out)

        print(f"  site figs → {out.relative_to(MEAS)}")

    _write_site_fig_readme()


def _write_site_fig_readme() -> None:
    """地点別図の見方。"""
    targets = STRONG_NOISE or _refresh_targets()
    _ensure_fs()
    path = SITE_FIG / "README.md"
    if SCOPE == "all":
        scope_label = "d1/d2/D1/D2（除外のみ）"
    elif SCOPE == "small_d":
        scope_label = "small-d（d1/d2）"
    else:
        scope_label = "large-D（D1/D2）"
    lines = [
        f"# 地点別（{RUN_ID}・割合補正の確認用）",
        "",
        "本解析の `figures/地点別/` とは別。**確認用**です。",
        "",
        "## 図の読み方",
        "",
    ]
    if CORRECTION_MODE == "peak_roi":
        lines += [
            "| 要素 | 意味 |",
            "|------|------|",
            "| **赤みの帯** | **peak ROI**（`analyze_roi`・764 keV 付近）。**φ の積分窓** |",
            "| **青の帯** | peak ROI より右（hi+1 … 最終 ch）。表示用 |",
            "| **薄緑** | wall窓（191–764 keV）の参考表示のみ。φ には使わない |",
            f"| **係数 f** | D系 {F_LARGE:.4f} / d系 {F_SMALL:.4f}（熱中性子 peak ROI 側帯 NET） |",
            "| **フラックス** | φ = peak NET / εS_peak |",
            "| **補正** | peak ROI 内で ×(1/f)（S2: きれいな点は skip）。図上は peak ROI を一体表示 |",
            "",
            "## 補正の式",
            "",
            "`φ = NET_peak / εS_peak`（側帯背景つき peak ROI）",
            "",
            f"- f_large (D1/D2) = {F_LARGE:.6f}  f_small (d1/d2) = {F_SMALL:.6f}",
            f"- 対象: **{scope_label}** · **peak_partial**（S2: きれいな点は skip）",
            "",
        ]
    else:
        lines += [
            "| 要素 | 意味 |",
            "|------|------|",
            "| **緑の帯** | wall窓（191–764 keV）。**定義は従来どおり** |",
            f"| **灰の帯** | wall内で **ch<{CUT_CH}**。低chノイズ疑いのため **積分除外** |",
            f"| **黒破線 cut={CUT_CH}** | これより右だけを使う境界 |",
            f"| **cutより右の山** | 実測 ×(1/f)。D系 f={F_LARGE:.4f} / d系 f={F_SMALL:.4f} |",
            "| **青の帯** | 764 keV より右の側帯 |",
            "| **壁窓より左** | 表示のみ（積分に使わない） |",
            "",
            "## 補正の式",
            "",
            f"`R_corr = N(ch>={CUT_CH} ∩ wall) / f`",
            "",
            f"- f_large (D1/D2) = {F_LARGE:.6f}",
            f"- f_small (d1/d2) = {F_SMALL:.6f}",
            f"- 対象: **{scope_label}**",
            "",
        ]
    lines += [
        "## 対象フォルダ",
        "",
    ]
    for name in targets:
        lines.append(f"- `{Path(name).stem}/`")
    lines += [
        "",
        "## fig16–19",
        "",
        "`theory_16_19/` … 補正後のフラックス点を載せた確認用図",
        "",
        "## 本解析への反映",
        "",
        "```bash",
        f"python3 03_今年度用/build_denoised_review.py --run-id {RUN_ID} --merge",
        "```",
        "",
        "## 時系列統合ビュー",
        "",
        "`figures/地点別_denoised/` … 全 run を測定時刻順にまとめたギャラリー",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


_STEM_TS = re.compile(
    r"^(?P<det>[Dd]\d+)_(?P<ymd>\d{8})_(?P<hm>\d{3,6})_(?P<place>.+)$"
)


def _parse_stem_time(stem: str) -> tuple[str, str, str, str]:
    """stem → (ymd, hm, det, place)。パース失敗時は辞書順キー。"""
    m = _STEM_TS.match(stem)
    if not m:
        return ("99999999", "999999", stem[:2], stem)
    hm = m.group("hm")
    if len(hm) == 3:
        hm = hm.zfill(4)
    elif len(hm) == 5:
        hm = hm.zfill(6)
    return (m.group("ymd"), hm, m.group("det"), m.group("place"))


def _stage_order(run_id: str) -> int:
    low = run_id.lower()
    if "small_d" in low:
        return 1
    if "large_d" in low:
        return 2
    if "peak764" in low:
        return 3
    return 9


def build_timeline_gallery() -> Path:
    """figures/地点別_denoised を時系列統合ギャラリーとして再構築。"""
    # 旧 symlink や中身を置き換え
    if GALLERY.is_symlink() or GALLERY.exists():
        if GALLERY.is_symlink() or GALLERY.is_file():
            GALLERY.unlink()
        else:
            shutil.rmtree(GALLERY)
    stages_dir = GALLERY / "stages"
    timeline_dir = GALLERY / "timeline"
    stages_dir.mkdir(parents=True, exist_ok=True)
    timeline_dir.mkdir(parents=True, exist_ok=True)

    runs = sorted(
        (p for p in RUNS_ROOT.iterdir() if p.is_dir() and (p / "figures" / "地点別").is_dir()),
        key=lambda p: (_stage_order(p.name), p.name),
    )
    if not runs:
        (GALLERY / "README.md").write_text(
            "# 地点別_denoised\n\nまだ denoised_runs に図がありません。\n",
            encoding="utf-8",
        )
        return GALLERY

    # stages: 番号付き symlink
    entries: list[dict] = []
    for i, run in enumerate(runs, start=1):
        site = run / "figures" / "地点別"
        link = stages_dir / f"{i:02d}_{run.name}"
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(os_relpath(site, stages_dir))
        # 他 run からコピーした overlay 図は timeline では二重計上しない
        own_stems = {p.stem for p in (run / "raw").glob("*.mca")}
        for d in sorted(p for p in site.iterdir() if p.is_dir() and p.name != "theory_16_19"):
            if own_stems and d.name not in own_stems:
                continue
            ymd, hm, det, place = _parse_stem_time(d.name)
            clip = d / "全ch_線形_ch0除く_クリップ.png"
            entries.append(
                {
                    "run": run.name,
                    "stage_i": i,
                    "stem": d.name,
                    "ymd": ymd,
                    "hm": hm,
                    "det": det,
                    "place": place,
                    "src_dir": d,
                    "clip": clip if clip.exists() else None,
                }
            )

    entries.sort(key=lambda e: (e["ymd"], e["hm"], e["det"].lower(), e["stage_i"], e["stem"]))

    # timeline: 測定時刻順に番号付きフォルダ + 主要PNGの symlink
    key_pngs = (
        "全ch_線形_ch0除く_クリップ.png",
        "全ch_対数.png",
        "全ch_線形.png",
    )
    index_rows: list[str] = []
    for n, e in enumerate(entries, start=1):
        folder = (
            f"{n:03d}_{e['ymd']}_{e['hm']}_{e['det']}_{e['place']}"
            f"__{e['run']}"
        )
        # パスに危険文字があれば簡易置換
        folder = folder.replace("/", "_").replace(" ", "_")
        out = timeline_dir / folder
        out.mkdir(parents=True, exist_ok=True)
        (out / "SOURCE.txt").write_text(
            f"run={e['run']}\nstem={e['stem']}\npath={e['src_dir']}\n",
            encoding="utf-8",
        )
        for name in key_pngs:
            src = e["src_dir"] / name
            if not src.exists():
                continue
            dst = out / name
            if dst.exists() or dst.is_symlink():
                dst.unlink()
            dst.symlink_to(os_relpath(src, out))
        index_rows.append(
            f"| {n:03d} | {e['ymd']} {e['hm']} | `{e['det']}` | {e['place']} "
            f"| `{e['run']}` | `{folder}/` |"
        )

    # 統合コンタクトシート（測定時刻順）
    _write_timeline_contact_sheet(entries, GALLERY / "timeline_contact.png")

    readme = [
        "# 地点別_denoised（時系列統合）",
        "",
        "denoised 確認用の図を **測定時刻順** にまとめたビューです。",
        "各 run の原本は `denoised_runs/<run_id>/figures/地点別/` に残しています。",
        "",
        "## 構成",
        "",
        "| パス | 内容 |",
        "|------|------|",
        "| `stages/` | 補正ステージ別（01_small_d → 02_large_d …） |",
        "| `timeline/` | **測定時刻順**の統合フォルダ（主要PNGへのリンク） |",
        "| `timeline_contact.png` | クリップ図の時系列コンタクトシート |",
        "",
        "## ステージ順",
        "",
    ]
    for i, run in enumerate(runs, start=1):
        readme.append(f"{i}. `{run.name}` → `stages/{i:02d}_{run.name}/`")
    readme += [
        "",
        "## タイムライン一覧",
        "",
        "| # | 測定 | 検出器 | 地点 | run | フォルダ |",
        "|---|------|--------|------|-----|----------|",
        *index_rows,
        "",
        "再生成:",
        "",
        "```bash",
        "python3 03_今年度用/build_denoised_review.py --timeline-only",
        "```",
        "",
    ]
    (GALLERY / "README.md").write_text("\n".join(readme), encoding="utf-8")
    print(f"timeline gallery → {GALLERY}  ({len(entries)} entries)")
    return GALLERY


def os_relpath(target: Path, start: Path) -> Path:
    return Path(os.path.relpath(target, start))


def _write_timeline_contact_sheet(entries: list[dict], out: Path) -> None:
    """クリップPNGを測定時刻順に並べたコンタクトシート。"""
    clips = [e for e in entries if e.get("clip") and e["clip"].exists()]
    if not clips:
        return
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        # Pillow が無い場合は matplotlib で簡易版
        n = len(clips)
        cols = 3
        rows = (n + cols - 1) // cols
        fig, axes = plt.subplots(rows, cols, figsize=(4.2 * cols, 3.2 * rows))
        axes_flat = np.atleast_1d(axes).ravel()
        for ax in axes_flat:
            ax.axis("off")
        for i, e in enumerate(clips):
            ax = axes_flat[i]
            img = plt.imread(str(e["clip"]))
            ax.imshow(img)
            ax.set_title(
                f"{e['ymd']} {e['hm']} {e['det']}\n{e['place']} [{e['run']}]",
                fontsize=7,
            )
            ax.axis("off")
        fig.tight_layout()
        fig.savefig(out, dpi=120)
        plt.close(fig)
        print(f"  contact sheet → {out.relative_to(MEAS)}")
        return

    imgs = []
    labels = []
    for e in clips:
        im = Image.open(e["clip"]).convert("RGB")
        imgs.append(im)
        labels.append(f"{e['ymd']} {e['hm']} {e['det']} {e['place']}\n[{e['run']}]")

    cell_w, cell_h = 480, 300
    cols = 3
    rows = (len(imgs) + cols - 1) // cols
    title_h = 36
    sheet = Image.new("RGB", (cols * cell_w, rows * (cell_h + title_h)), (255, 255, 255))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for i, (im, lab) in enumerate(zip(imgs, labels)):
        r, c = divmod(i, cols)
        x0 = c * cell_w
        y0 = r * (cell_h + title_h)
        im2 = im.copy()
        im2.thumbnail((cell_w - 8, cell_h - 8))
        ox = x0 + (cell_w - im2.width) // 2
        oy = y0 + title_h + (cell_h - im2.height) // 2
        sheet.paste(im2, (ox, oy))
        draw.text((x0 + 4, y0 + 4), lab, fill=(20, 20, 20), font=font)

    sheet.save(out)
    print(f"  contact sheet → {out.relative_to(MEAS)}")


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
    pfig.fig19_same_type_continuous(p, absolute=True)

    kept = sorted(THEORY_FIG.glob("1[6789]_*.png"))
    print(f"theory figs: {len(kept)}")
    for f in kept:
        print(f"  {f.name}")


def write_review_readme(reports: list[dict]) -> None:
    REVIEW.mkdir(parents=True, exist_ok=True)
    path = REVIEW / "README.md"
    n_s = sum(1 for r in reports if r.get("family") == "small_d")
    n_l = sum(1 for r in reports if r.get("family") == "large_D")
    n_skip = sum(1 for r in reports if r.get("skipped"))
    n_adapt = sum(
        1 for r in reports if r.get("mode") in ("adaptive_f5", "legacy_f2")
    )
    if ADAPTIVE and CORRECTION_MODE == "peak_roi":
        lines = [
            f"# {RUN_ID}（764 keV peak ROI フラックス・確認用）",
            "",
            "本解析の `tables/`・`figures/` は**未変更**（`--merge` するまで）。",
            f"この成果は `denoised_runs/{RUN_ID}/` にあり、他 run とは独立。",
            "",
            "## 方針",
            "",
            "1. 入力: いまの `raw/`",
            f"2. 対象: d1/d2/D1/D2 計 {len(reports)} 件（small {n_s} + large {n_l}）",
            "3. **フラックス**: φ = peak ROI NET / εS_peak（側帯背景）",
            "4. **スペクトル補正**: peak ROI 部分補正（S2: part/full≥0.84 かつ左漏れ弱 → skip）",
            "5. **Linac3**: wall F5 を使わず peak 部分補正のみ",
            "6. 除外: 熱中性子・gain・D1/d2 PF・`_error`",
            "",
            f"- f_large（参考・peak ROI 側帯 NET）@ {CUT_CH} = {F_LARGE:.6f}",
            f"- f_small（参考）@ {CUT_CH} = {F_SMALL:.6f}",
            "",
            "## 評価",
            "",
            f"- `evaluation_adaptive.csv` … 同地点 D/d |log比|（E1）",
            "",
            "## 図の見方",
            "",
            f"→ `{SITE_FIG.relative_to(MEAS)}/README.md`",
            f"→ 時系列: `figures/地点別_denoised/stages/03_{RUN_ID}/`",
            "",
            "## 出力場所",
            "",
            f"- MCA: `{RAW_DENOISED.relative_to(MEAS)}/`",
            f"- 地点別: `{SITE_FIG.relative_to(MEAS)}/<stem>/`",
            f"- fig16–19: `{THEORY_FIG.relative_to(MEAS)}/`",
            f"- 再集計表: `{REVIEW_TABLES.relative_to(MEAS)}/`",
            "",
            "## 対象ファイル",
            "",
            "| ファイル | 族 | mode | cut | wall | part/full | r2 | f | cps前 | cps後 |",
            "|---|---|---|---:|---|---:|---:|---:|---:|---:|",
        ]
        for r in reports:
            r2s = f"{r['r2']:.3f}" if r.get("r2") is not None else "-"
            lines.append(
                f"| `{r['file']}` | {r.get('family','')} | {r.get('mode','-')} | {r['cut']} | "
                f"{r.get('wall','-')} | {r['ratio_ge_cut']:.3f} | {r2s} | {r['f']:.4f} | "
                f"{r['cps_before']:.6g} | {r['cps_after']:.6g} |"
            )
    elif ADAPTIVE:
        lines = [
            f"# {RUN_ID}（適応型補正・d/D 統合・確認用）",
            "",
            "本解析の `tables/`・`figures/` は**未変更**（`--merge` するまで）。",
            f"この成果は `denoised_runs/{RUN_ID}/` にあり、他 run とは独立。",
            "",
            "## 方針",
            "",
            "1. 入力: いまの `raw/`（方式B済み4件含む）",
            f"2. 対象: d1/d2/D1/D2 計 {len(reports)} 件（small {n_s} + large {n_l}）",
            f"3. **S2**: part/full ≥ {CLEAN_R1} かつ左漏れ弱 → **未補正**",
            f"4. **C4**: 左漏れ r2≥{DIRT_R2_CUT300} → cut={CUT_HIGH}、それ以外 cut={CUT_CH}",
            "5. **F5**: ch<cut を熱中性子テンプレ、ch≥cut は観測維持（wall 合計 = N_ge/f）",
            "6. **T1**: f_large = D1熱中性子、f_small = d1熱中性子（cut ごと）",
            f"7. 適用 {n_adapt} 件 / skip {n_skip} 件",
            f"8. **hybrid**: PS → D skip + d legacy F2",
            "9. **testhole**: 大小 legacy F2 / **BT**: D1 adapt + d2 skip / **Linac3**: d2 skip + 他 adapt",
            f"10. **preserve**: PF, linac",
            "11. 除外: 熱中性子・gain・D1/d2 PF(0807)・`_error`",
            "",
            f"- f_large @ {CUT_CH} = {F_LARGE:.6f}",
            f"- f_small @ {CUT_CH} = {F_SMALL:.6f}",
            "",
            "## 評価",
            "",
            f"- `evaluation_adaptive.csv` … 同地点 D/d |log比|（E1）",
            "",
            "## 図の見方",
            "",
            f"→ `{SITE_FIG.relative_to(MEAS)}/README.md`",
            f"→ 時系列: `figures/地点別_denoised/stages/02_{RUN_ID}/`",
            "",
            "## 出力場所",
            "",
            f"- MCA: `{RAW_DENOISED.relative_to(MEAS)}/`",
            f"- 地点別: `{SITE_FIG.relative_to(MEAS)}/<stem>/`",
            f"- fig16–19: `{THEORY_FIG.relative_to(MEAS)}/`",
            f"- 再集計表: `{REVIEW_TABLES.relative_to(MEAS)}/`",
            "",
            "## 対象ファイル",
            "",
            "| ファイル | 族 | mode | cut | wall | part/full | r2 | f | cps前 | cps後 |",
            "|---|---|---|---:|---|---:|---:|---:|---:|---:|",
        ]
        for r in reports:
            r2s = f"{r['r2']:.3f}" if r.get("r2") is not None else "-"
            lines.append(
                f"| `{r['file']}` | {r.get('family','')} | {r.get('mode','-')} | {r['cut']} | "
                f"{r['wall']} | {r['ratio_ge_cut']:.3f} | {r2s} | {r['f']:.4f} | "
                f"{r['cps_before']:.6g} | {r['cps_after']:.6g} |"
            )
    else:
        if CORRECTION_MODE == "peak_roi":
            lines = [
                f"# {RUN_ID}（764 keV peak ROI 割合補正・d/D 統合・確認用）",
                "",
                "本解析の `tables/`・`figures/` は**未変更**（`--merge` するまで）。",
                f"この成果は `denoised_runs/{RUN_ID}/` にあり、他 run とは独立。",
                "",
                "## 方式",
                "",
                "1. 入力: いまの `raw/`（方式B済み4件含む）",
                f"2. 対象: d1/d2/D1/D2 計 {len(reports)} 件（small {n_s} + large {n_l}）",
                "3. **764 keV peak ROI**（`analyze_roi`）内で part/full 補正 · **全件一律**",
                f"4. cut_eff = peak−{PEAK_HALF_WIDTH}（roi_lo>{CUT_CH} のとき）",
                f"5. f_large (D1/D2) = {F_LARGE:.6f}（D1 熱中性子 peak ROI 平均）",
                f"6. f_small (d1/d2) = {F_SMALL:.6f}（d1 熱中性子 peak ROI 平均）",
                "7. 除外: 熱中性子・gain・D1/d2 PF・`_error`",
                "",
                "## 図の見方",
                "",
                f"→ `{SITE_FIG.relative_to(MEAS)}/README.md`",
                f"→ 時系列: `figures/地点別_denoised/stages/03_{RUN_ID}/`",
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
                "| ファイル | 族 | peak ROI | cut | part/full | f | cps前 | cps後 |",
                "|---|---|---|---:|---:|---:|---:|---:|",
            ]
            for r in reports:
                fam = r.get("family", "")
                lines.append(
                    f"| `{r['file']}` | {fam} | {r.get('peak_roi', '-')} | "
                    f"{r['cut']} | {r['ratio_ge_cut']:.3f} | {r['f']:.4f} | "
                    f"{r['cps_before']:.6g} | {r['cps_after']:.6g} |"
                )
        else:
            lines = [
                f"# {RUN_ID}（d/D 統合・ch>={CUT_CH} 割合補正・確認用）",
                "",
                "本解析の `tables/`・`figures/` は**未変更**（`--merge` するまで）。",
                f"この成果は `denoised_runs/{RUN_ID}/` にあり、他 run とは独立。",
                "",
                "## 方式",
                "",
                "1. 入力: いまの `raw/`（small_d 強ノイズ4件は方式B済み、他は未B）",
                f"2. 対象: d1/d2/D1/D2 計 {len(reports)} 件（small {n_s} + large {n_l}）。"
                f" wall 内 ch<{CUT_CH} を捨て、ch>={CUT_CH} を `1/f` 倍",
                f"3. f_large (D1/D2) = {F_LARGE:.6f}（D1 熱中性子 30cm/80cm 平均）",
                f"4. f_small (d1/d2) = {F_SMALL:.6f}（d1 熱中性子 30cm/80cm 平均）",
                "5. 除外: 熱中性子・gain・D1 PF・`_error`",
                "6. wall 窓の定義（191–764 keV）自体は変えない",
                "",
                "## 図の見方",
                "",
                f"→ `{SITE_FIG.relative_to(MEAS)}/README.md`",
                f"→ 時系列: `figures/地点別_denoised/`",
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
                f"| ファイル | 族 | wall | N_full | N>={CUT_CH} | part/full | f | cps前 | cps後 |",
                "|---|---|---|---:|---:|---:|---:|---:|---:|",
            ]
            for r in reports:
                fam = r.get("family", "")
                lines.append(
                    f"| `{r['file']}` | {fam} | {r['wall']} | "
                    f"{r['N_full_before']:.0f} | {r['N_ge_cut_before']:.0f} | "
                    f"{r['ratio_ge_cut']:.3f} | {r['f']:.4f} | "
                    f"{r['cps_before']:.6g} | {r['cps_after']:.6g} |"
                )
    lines += [
        "",
        "## 本解析への反映",
        "",
        "```bash",
        f"python3 03_今年度用/build_denoised_review.py --run-id {RUN_ID} --merge",
        "```",
        "",
        f"- 対象ファイルは `raw_pre_partial_corr/{RUN_ID}/` に退避してから `raw/` を置換",
        "- tables / figures / theory を再計算",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def print_net_delta() -> None:
    """本番表 vs 確認用表の wall_net_cps 差分（large-D 対象）。"""
    import csv

    targets = STRONG_NOISE or _refresh_targets()
    main_rec = MEAS / "tables" / "測定記録.csv"
    rev_rec = REVIEW_TABLES / "測定記録.csv"
    if not rev_rec.exists():
        return
    main = {
        r["filename"]: r
        for r in csv.DictReader(main_rec.open(encoding="utf-8"))
    }
    print(f"\nwall_net_cps 差分（本番 → large-D ch>={CUT_CH} 補正 review）:")
    for name in targets:
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


BACKUP_PARTIAL = MEAS / "raw_pre_partial_corr"  # 下に run_id サブフォルダ


def merge_to_main() -> None:
    """補正 MCA を本解析 raw/ に入れ、tables・figures・theory を再計算。"""
    import csv
    import subprocess

    global F_PARTIAL
    targets = _refresh_targets()
    if F_PARTIAL <= 0:
        if CORRECTION_MODE == "peak_roi":
            F_PARTIAL, _ = thermal_partial_fraction_peak()
        else:
            F_PARTIAL, _ = thermal_partial_fraction()

    missing = [n for n in targets if not (RAW_DENOISED / n).exists()]
    if missing:
        print("raw_denoised が無いので先に補正 MCA を作成します…")
        make_corrected_mcas()
        targets = STRONG_NOISE

    bak_dir = BACKUP_PARTIAL / RUN_ID
    bak_dir.mkdir(parents=True, exist_ok=True)
    for name in targets:
        src = RAW / name
        den = RAW_DENOISED / name
        if not den.exists():
            raise FileNotFoundError(den)
        if not src.exists():
            raise FileNotFoundError(src)
        bak = bak_dir / name
        if not bak.exists():
            shutil.copy2(src, bak)
            csv0 = RAW / name.replace(".mca", ".csv")
            if csv0.exists():
                shutil.copy2(csv0, bak_dir / csv0.name)
            print(f"backup: {name}")
        else:
            print(f"backup exists: {name}")
        shutil.copy2(den, src)
        print(f"installed corrected: {name}")

    (bak_dir / "README.md").write_text(
        "\n".join(
            [
                "# raw_pre_partial_corr",
                "",
                f"large-D 割合補正（ch>={CUT_CH} / f）を本解析へ入れる直前の `raw/`。",
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
    # peak764 採用時は φ = peak ROI NET / εS_peak
    env = None
    if CORRECTION_MODE == "peak_roi":
        env = {**os.environ, "FLUX_WINDOW": "peak"}
        print("merge: FLUX_WINDOW=peak（764 keV peak ROI）")
    for cmd in steps:
        cwd = ROOT if cmd[1] != "plot_fig16_17_18_comparison.py" else (
            MEAS / "theory_research"
        )
        print(f"\n>>> {' '.join(cmd)}  (cwd={cwd.name})")
        if cmd[1] == "build_flux_summary.py" and CORRECTION_MODE == "peak_roi":
            # 環境変数だけでは足りないので一時的に peak を強制
            subprocess.run(
                [
                    "python3",
                    "-c",
                    (
                        "import build_flux_summary as bfs; "
                        "bfs.FLUX_WINDOW='peak'; "
                        "bfs.main()"
                    ),
                ],
                cwd=ROOT,
                check=True,
                env=env,
            )
            continue
        subprocess.run(cmd, cwd=cwd, check=True, env=env)

    rows = {
        r["filename"]: r
        for r in csv.DictReader((MEAS / "tables" / "測定記録.csv").open(encoding="utf-8"))
    }
    print("\n本解析 wall_net_cps（マージ後）:")
    for name in targets:
        r = rows.get(name)
        if r:
            print(f"  {name}: {r['wall_net_cps']}")

    (RAW_DENOISED / "README.md").write_text(
        "\n".join(
            [
                "# raw_denoised",
                "",
                f"large-D ch>={CUT_CH} 割合補正 MCA（f={F_PARTIAL:.6f}）。",
                "",
                "**本解析に反映済み**（`raw/` を置換。直前版は "
                "`raw_pre_partial_corr/`）。",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"\nmerge done. backup={bak_dir}")


def default_overlay_run_ids() -> list[str]:
    """統合 run (all) では重ね不要。旧 large_d のみのとき small_d を自動重ね。"""
    if SCOPE == "all":
        return []
    if SCOPE != "large_d":
        return []
    cand = RUNS_ROOT / "small_d_cut300" / "raw"
    if cand.is_dir() and any(cand.glob("*.mca")):
        return ["small_d_cut300"]
    return []


def refresh_review(
    *, overlay_run_ids: list[str] | None = None, remake_mca: bool = True
) -> list[dict]:
    """review_raw / tables / 地点別 / theory を（再）構築。"""
    global OVERLAY_SITE_STEMS, F_PARTIAL
    overlays = (
        list(overlay_run_ids)
        if overlay_run_ids is not None
        else default_overlay_run_ids()
    )
    OVERLAY_SITE_STEMS = set()

    reports: list[dict] = []
    if remake_mca:
        title = "適応型補正 MCA" if ADAPTIVE else f"{SCOPE} ch>={CUT_CH} 割合補正 MCA"
        print(f"=== 1) {title} ===")
        reports = make_corrected_mcas()
    else:
        print(f"=== 1) skip MCA（既存 {RAW_DENOISED} を使用）===")
        _ensure_fs()
        print(
            f"  f_large={F_LARGE:.6f}  f_small={F_SMALL:.6f} (annotation用)"
        )

    print("\n=== 2) review raw + tables ===")
    if overlays:
        print(f"  overlays: {overlays}")
    prepare_review_raw(overlay_run_ids=overlays)
    copy_static_tables()
    rebuild_review_tables()
    print_net_delta()

    print("\n=== 3) site figures ===")
    plot_site_denoised()
    for rid in overlays:
        print(f"=== 3b) overlay site figures from {rid} ===")
        overlay_run_site_figures(rid)

    print("\n=== 4) theory fig16–19（overlay 反映後の tables）===")
    plot_theory_review()

    if ADAPTIVE:
        print_adaptive_evaluation()

    if reports:
        write_review_readme(reports)
    _write_combined_readme(overlays)
    return reports


def _write_combined_readme(overlays: list[str]) -> None:
    """large_d に small_d を重ねた旨を README に追記。"""
    if not overlays:
        return
    note = [
        "",
        "## 他 run の反映",
        "",
        "本 run の確認用 `review_raw` / `tables` / `theory_16_19` には、次の補正 MCA も重ねています。",
        "",
    ]
    for rid in overlays:
        note.append(f"- `{rid}` → `denoised_runs/{rid}/raw/*.mca`")
    note += [
        "",
        "地点別スペクトルにも同 run の図フォルダをコピー済み（cut/f は元 run の注記のまま）。",
        "",
    ]
    path = RUN_DIR / "README.md"
    text = path.read_text(encoding="utf-8") if path.exists() else f"# {RUN_ID}\n"
    if "## 他 run の反映" not in text:
        path.write_text(text.rstrip() + "\n" + "\n".join(note), encoding="utf-8")

    site_readme = SITE_FIG / "README.md"
    if site_readme.exists():
        st = site_readme.read_text(encoding="utf-8")
        if "## 他 run の反映" not in st:
            site_readme.write_text(st.rstrip() + "\n" + "\n".join(note), encoding="utf-8")


def build_review(*, overlay_run_ids: list[str] | None = None) -> None:
    refresh_review(overlay_run_ids=overlay_run_ids, remake_mca=True)
    print(f"\ndone. see {RUN_DIR / 'README.md'}")
    print(f"図の見方: {SITE_FIG / 'README.md'}")
    print(f"本解析反映: python3 build_denoised_review.py --run-id {RUN_ID} --merge")
    print(f"一覧: {RUNS_ROOT / 'README.md'}")


def main(argv: list[str] | None = None) -> None:
    import argparse

    global F_PARTIAL

    p = argparse.ArgumentParser(
        description="割合補正確認用（denoised_runs/<run_id>/ に追記）"
    )
    p.add_argument(
        "--run-id",
        default=DEFAULT_RUN_ID,
        help=f"出力フォルダ名（既定: {DEFAULT_RUN_ID}）。既存 run は触らず新規追加可",
    )
    p.add_argument(
        "--cut",
        type=int,
        default=None,
        help="cut チャンネル（省略時は run-id 末尾 cutNNN または既定）",
    )
    p.add_argument(
        "--scope",
        choices=("all", "large_d", "small_d"),
        default=None,
        help="対象スコープ（省略時: large_d_cut200→all、他は run-id から推定）",
    )
    p.add_argument(
        "--f",
        type=float,
        default=None,
        help="補正係数 f を全員固定。省略時は D系=D1熱中性子 / d系=d1熱中性子",
    )
    p.add_argument(
        "--merge",
        action="store_true",
        help="指定 run の補正 MCA を raw/ に入れ、本解析を再計算",
    )
    p.add_argument(
        "--plots-only",
        action="store_true",
        help="指定 run の地点別図 + theory だけ再生成（既存 MCA/tables を使用）",
    )
    p.add_argument(
        "--refresh-review",
        action="store_true",
        help="MCA は触らず review_raw/tables/地点別/theory を再構築（--include-run 可）",
    )
    p.add_argument(
        "--include-run",
        action="append",
        default=None,
        help="他 run の補正 MCA/地点別図を重ねる（例: --include-run small_d_cut300）。"
        " large_d では省略時に small_d_cut300 を自動適用",
    )
    p.add_argument(
        "--no-overlay",
        action="store_true",
        help="他 run の自動重ね込みをしない",
    )
    p.add_argument(
        "--timeline-only",
        action="store_true",
        help="figures/地点別_denoised の時系列統合ギャラリーだけ再構築",
    )
    args = p.parse_args(argv)

    if args.timeline_only:
        build_timeline_gallery()
        update_runs_index()
        return

    cut = args.cut
    if cut is None and "cut" in args.run_id:
        m = re.search(r"cut(\d+)$", args.run_id)
        if m:
            cut = int(m.group(1))
    # 旧 small_d_cut300 だけ cut=300 / f=0.769 の互換
    is_legacy_small300 = (
        args.run_id == "small_d_cut300"
        or (args.scope == "small_d" and "cut300" in (args.run_id or ""))
    )
    if cut is None and is_legacy_small300:
        cut = 300
    fixed_f = args.f
    if fixed_f is None and is_legacy_small300:
        fixed_f = 0.769

    configure_run(args.run_id, cut=cut, scope=args.scope, fixed_f=fixed_f)
    print(
        f"run_id={RUN_ID}  out={RUN_DIR}  cut={CUT_CH}  "
        f"scope={SCOPE}  f={F_PARTIAL if F_PARTIAL > 0 else '(per-family thermal)'}"
    )

    if args.include_run is not None:
        overlays: list[str] | None = list(args.include_run)
    elif args.no_overlay or SCOPE == "all":
        overlays = []
    else:
        overlays = None

    if args.merge:
        merge_to_main()
    elif args.refresh_review:
        refresh_review(overlay_run_ids=overlays, remake_mca=False)
    elif args.plots_only:
        _refresh_targets()
        _ensure_fs()
        plot_site_denoised()
        if overlays is None:
            overlays = default_overlay_run_ids()
        for rid in overlays:
            overlay_run_site_figures(rid)
        plot_theory_review()
        _write_combined_readme(overlays)
    else:
        build_review(overlay_run_ids=overlays)
    update_runs_index()
    build_timeline_gallery()


if __name__ == "__main__":
    main()
