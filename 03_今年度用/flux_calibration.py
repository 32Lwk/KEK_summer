#!/usr/bin/env python3
"""191–764 keV 壁効果窓の ε×S 較正（フラックス φ = R_wall / εS_wall の単一定義）。

方式（d1 と D1 で同一）:
  εS_total = メーカー感度 [cps/nv]
  S_iso    = S_surf/4 = π r (L+r)/2
             d1/d2: L=He-3 長 39.53 cm（外形全長 50 cm）, 直径=5.08 cm
             D1/D2: L=全長−信管=56 cm（外形全長 66 cm）, r=He-3 内半径
  ε_mfr    = εS_total / S_iso
  f_wall   = パイル（d1 30&80 cm）の R_wall / R_total
  εS_wall  = εS_total × f_wall

MCA はピークを正しく積算するモードのため dead time は較正判定に使わない
（計数率は net/LIVE_TIME。追加の 1/(1−DT) はしない）。

データの持ち方:
  幾何・メーカー定数 … `detector_specs.DETECTORS`（メモリ上の dataclass）
  較正の計算          … 本モジュールの関数（`bare_tube_efficiency`, `compute_wall_efficiencies`）
  較正の永続化        … `tables/検出器効率_壁効果191_764keV.csv`
  実行時の読み出し    … `load_wall_efficiencies_csv()` → `eps_wall_dict()`
  フラックス          … `build_flux_summary.py` が CSV を唯一の εS ソースにする
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
SIM_ROOT = ROOT.parent / "04_PHITS_sim" / "equiv_concrete_sites"
sys.path.insert(0, str(SIM_ROOT))
from detector_specs import (  # noqa: E402
    DETECTORS,
    LARGE_SENSITIVITY_CPS_NV,
    RS_P4_1613_203_SENSITIVITY_CPS_NV,
    he3_geometric_areas,
)

Q_AMBE = 2.26e6
PHI_OVER_Q = 9.44e-6
D_REF_CM = 30.0
R_HALF_CM = 95.0

MFR_SENSITIVITY_CPS_NV = {
    "d1": RS_P4_1613_203_SENSITIVITY_CPS_NV,
    "d2": RS_P4_1613_203_SENSITIVITY_CPS_NV,
    "D1": LARGE_SENSITIVITY_CPS_NV,
    "D2": LARGE_SENSITIVITY_CPS_NV,
}

D1_OVERNIGHT_SUBSTR = "0832"
D2_TRANSFER_SITE = "linac"
D2_TRANSFER_SUBSTR = "0835"
D1_LINAC_SUBSTR = "1510"

TABLES = ROOT / "測定_20260818" / "tables"
EFF_WALL_CSV = TABLES / "検出器効率_壁効果191_764keV.csv"
MFR_CMP_CSV = TABLES / "メーカー感度比較.csv"


@dataclass(frozen=True)
class WallEfficiency:
    detector: str
    epsilon_S_wall_cm2: float
    epsilon_S_wall_std_cm2: float | None
    epsilon_S_peakROI_cm2: float | None
    note: str
    f_wall: float | None = None
    epsilon_S_total_cm2: float | None = None


def thermal_phi(d_cm: float, q: float = Q_AMBE, r_half: float = R_HALF_CM) -> float:
    scale = ((r_half + D_REF_CM) / (r_half + d_cm)) ** 2
    return PHI_OVER_Q * q * scale


def _pick_row(
    rows: list[dict],
    detector: str,
    site: str,
    *,
    filename_contains: str = "",
) -> dict | None:
    hits = [
        r
        for r in rows
        if r.get("検出器") == detector
        and r.get("地点") == site
        and r.get("wall_valid")
        and float(r.get("wall_net_cps") or 0) > 0
    ]
    if filename_contains:
        pref = [r for r in hits if filename_contains in r.get("filename", "")]
        if pref:
            hits = pref
    return hits[0] if hits else None


def _total_cps(row: dict) -> float:
    v = row.get("total_cps")
    if v not in (None, ""):
        return float(v)
    raise RuntimeError(
        f"total_cps がありません（{row.get('filename','')}）。"
        "calc_window_comparison.py を再実行してください。"
    )


def manufacturer_eps_s(det: str) -> float:
    """裸管の εS_total [cm²] = メーカー cps/nv。"""
    return MFR_SENSITIVITY_CPS_NV[det]


def epsilon_mfr(det: str) -> float:
    """ε_mfr = メーカー / S_iso。S_iso は全長−信管の等方面積。"""
    return float(he3_geometric_areas(det)["epsilon_mfr"])


def pile_window_fractions(rows: list[dict]) -> tuple[float, float | None, float | None]:
    """d1 パイル 30&80 cm から (f_wall, f_wall_std, f_peak)。

    MCA ピーク積算モードのため dead time では除外しない。
    """
    d1_pile = [
        r
        for r in rows
        if r.get("検出器") == "d1"
        and r.get("地点") in ("熱中性子_30cm", "熱中性子_80cm")
        and r.get("wall_valid")
    ]
    f_wall_pile: list[float] = []
    f_peak_pile: list[float] = []
    for r in d1_pile:
        tot = _total_cps(r)
        if tot <= 0:
            continue
        f_wall_pile.append(float(r["wall_net_cps"]) / tot)
        peak = float(r.get("peak_net_cps") or 0)
        if peak > 0:
            f_peak_pile.append(peak / tot)
    if not f_wall_pile:
        raise RuntimeError("d1 黒鉛パイル wall 較正点がありません")
    f_wall = float(np.mean(f_wall_pile))
    f_wall_std = float(np.std(f_wall_pile)) if len(f_wall_pile) >= 2 else None
    f_peak = float(np.mean(f_peak_pile)) if f_peak_pile else None
    return f_wall, f_wall_std, f_peak


def bare_tube_efficiency(
    det: str,
    f_wall: float,
    *,
    f_peak: float | None = None,
    f_wall_std: float | None = None,
    note_extra: str = "",
) -> WallEfficiency:
    """d1 / D1 共通: εS_total=メーカー, εS_wall=メーカー×f_wall。"""
    if det not in ("d1", "D1"):
        raise ValueError(f"裸管較正は d1/D1 のみ: {det}")
    mfr = manufacturer_eps_s(det)
    spec = DETECTORS[det]
    r_iso, L_iso = spec._s_iso_cylinder()
    note = (
        f"メーカー {mfr:.0f} cps/nv × f_wall={f_wall:.3f}"
        f"（S_iso: L={L_iso:.2f} cm, 直径={2*r_iso:.2f} cm, ε_mfr={spec.epsilon_mfr:.3f}）"
        f"{note_extra}"
    )
    return WallEfficiency(
        det,
        mfr * f_wall,
        (mfr * f_wall_std) if f_wall_std is not None else None,
        (mfr * f_peak) if f_peak else None,
        note,
        f_wall=f_wall,
        epsilon_S_total_cm2=mfr,
    )


def compute_wall_efficiencies(rows: list[dict]) -> dict[str, WallEfficiency]:
    """窓比較_計数率.csv 相当の行リストから 4 検出器の wall ε×S を求める。

    裸管 d1/D1 は `bare_tube_efficiency`（メーカー × パイル f_wall）。
    d2/D2 は現場 wall CPS 比で D1 から転送。
    """
    out: dict[str, WallEfficiency] = {}
    f_wall, f_wall_std, f_peak = pile_window_fractions(rows)
    out["d1"] = bare_tube_efficiency(
        "d1", f_wall, f_peak=f_peak, f_wall_std=f_wall_std, note_extra="・パイル30&80cm"
    )

    pile80 = _pick_row(rows, "D1", "熱中性子_80cm")
    pile80_note = ""
    if pile80:
        phi80 = thermal_phi(80.0)
        eps80 = float(pile80["wall_net_cps"]) / phi80
        pile80_note = f"；照合 D1@80cm R/φ={eps80:.1f}（参考・主結果はメーカー）"
    out["D1"] = bare_tube_efficiency(
        "D1", f_wall, f_peak=f_peak, note_extra=pile80_note
    )
    eps_d1_large = out["D1"].epsilon_S_wall_cm2
    eps_d1_large_peak = out["D1"].epsilon_S_peakROI_cm2

    d1_g = _pick_row(rows, "D1", "地上")
    d2_small_g = _pick_row(rows, "d2", "地上")
    if not d1_g or not d2_small_g:
        raise RuntimeError("d2 地上 wall 転送データがありません")
    ratio_d2 = float(d2_small_g["wall_net_cps"]) / float(d1_g["wall_net_cps"])
    peak_d1_g = float(d1_g.get("peak_net_cps") or 0)
    peak_d2_g = float(d2_small_g.get("peak_net_cps") or 0)
    eps_d2_peak = None
    if eps_d1_large_peak and peak_d1_g > 0 and peak_d2_g > 0:
        eps_d2_peak = eps_d1_large_peak * (peak_d2_g / peak_d1_g)
    eps_d2 = eps_d1_large * ratio_d2
    out["d2"] = WallEfficiency(
        "d2",
        eps_d2,
        None,
        eps_d2_peak,
        f"転送: 地上 d2/D1 壁窓比={ratio_d2:.3f}×D1εS_wall（PE 付き）",
        f_wall=None,
        epsilon_S_total_cm2=None,
    )

    if D2_TRANSFER_SITE == "linac":
        d1_ref = _pick_row(rows, "D1", "linac", filename_contains=D1_LINAC_SUBSTR)
        d2_ref = _pick_row(rows, "D2", "linac", filename_contains=D2_TRANSFER_SUBSTR)
        site_note = "linac 同日 D2/D1 壁窓比"
    else:
        d1_ref = d1_g
        d2_ref = _pick_row(rows, "D2", "地上")
        site_note = "地上 D2/D1 壁窓比"
    if not d1_ref or not d2_ref:
        raise RuntimeError(f"D2 wall 転送データがありません（site={D2_TRANSFER_SITE}）")
    ratio_d2_large = float(d2_ref["wall_net_cps"]) / float(d1_ref["wall_net_cps"])
    eps_d2_large = eps_d1_large * ratio_d2_large
    peak_d1_ref = float(d1_ref.get("peak_net_cps") or 0)
    peak_d2_ref = float(d2_ref.get("peak_net_cps") or 0)
    eps_D2_peak = None
    if eps_d1_large_peak and peak_d1_ref > 0 and peak_d2_ref > 0:
        eps_D2_peak = eps_d1_large_peak * (peak_d2_ref / peak_d1_ref)
    out["D2"] = WallEfficiency(
        "D2",
        eps_d2_large,
        None,
        eps_D2_peak,
        f"転送: {site_note}={ratio_d2_large:.3f}×D1εS_wall（PE 付き）",
        f_wall=None,
        epsilon_S_total_cm2=None,
    )

    return out


def load_wall_efficiencies_csv(path: Path | None = None) -> dict[str, WallEfficiency]:
    path = path or EFF_WALL_CSV
    if not path.exists():
        return {}
    out: dict[str, WallEfficiency] = {}
    for r in csv.DictReader(path.open(encoding="utf-8")):
        det = (r.get("検出器") or "").strip()
        v = (r.get("epsilon_S_wall_cm2") or "").strip()
        if not det or not v:
            continue
        std_s = (r.get("epsilon_S_wall_std_cm2") or "").strip()
        peak_s = (r.get("epsilon_S_peakROI_cm2") or "").strip()
        f_s = (r.get("f_wall") or "").strip()
        tot_s = (r.get("epsilon_S_total_cm2") or "").strip()
        out[det] = WallEfficiency(
            det,
            float(v),
            float(std_s) if std_s else None,
            float(peak_s) if peak_s else None,
            (r.get("備考") or "").strip(),
            f_wall=float(f_s) if f_s else None,
            epsilon_S_total_cm2=float(tot_s) if tot_s else None,
        )
    return out


def eps_wall_dict(eff: dict[str, WallEfficiency] | None = None) -> dict[str, float]:
    eff = eff or load_wall_efficiencies_csv()
    return {k: v.epsilon_S_wall_cm2 for k, v in eff.items()}


def eps_peak_dict(eff: dict[str, WallEfficiency] | None = None) -> dict[str, float]:
    """peak ROI 用 ε×S。無い検出器はスキップ。"""
    eff = eff or load_wall_efficiencies_csv()
    out: dict[str, float] = {}
    for k, v in eff.items():
        if v.epsilon_S_peakROI_cm2 and v.epsilon_S_peakROI_cm2 > 0:
            out[k] = float(v.epsilon_S_peakROI_cm2)
    return out


def write_manufacturer_comparison_csv(
    eff: dict[str, WallEfficiency],
    path: Path | None = None,
) -> Path:
    path = path or MFR_CMP_CSV
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "検出器",
        "メーカー感度_cps_nv",
        "S_iso_surf4_cm2",
        "ε_mfr",
        "S_proj_2rL_cm2",
        "ε_mfr_proj_参考",
        "f_wall",
        "epsilon_S_total_cm2",
        "epsilon_S_wall_cm2",
        "wall_over_mfr",
        "epsilon_S_peakROI_cm2",
        "peak_over_mfr",
        "備考",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for det in ("d1", "D1", "d2", "D2"):
            e = eff.get(det)
            if e is None:
                continue
            g = he3_geometric_areas(det)
            mfr = MFR_SENSITIVITY_CPS_NV[det]
            s_iso = g["S_he3_isotropic_cm2"]
            s_proj = g["S_he3_projected_cm2"]
            wall_frac = e.epsilon_S_wall_cm2 / mfr if mfr else float("nan")
            peak_frac = (
                e.epsilon_S_peakROI_cm2 / mfr
                if e.epsilon_S_peakROI_cm2 and mfr
                else float("nan")
            )
            pe_note = ""
            if det in ("d2", "D2"):
                pe_note = "PE 付きのためメーカー裸管感度との比は参考"
            tot = e.epsilon_S_total_cm2
            w.writerow(
                {
                    "検出器": det,
                    "メーカー感度_cps_nv": f"{mfr:.4g}",
                    "S_iso_surf4_cm2": f"{s_iso:.4g}",
                    "ε_mfr": f"{mfr / s_iso:.4g}",
                    "S_proj_2rL_cm2": f"{s_proj:.4g}",
                    "ε_mfr_proj_参考": f"{mfr / s_proj:.4g}",
                    "f_wall": f"{e.f_wall:.4g}" if e.f_wall is not None else "",
                    "epsilon_S_total_cm2": f"{tot:.4g}" if tot is not None else "",
                    "epsilon_S_wall_cm2": f"{e.epsilon_S_wall_cm2:.4g}",
                    "wall_over_mfr": f"{wall_frac:.4g}",
                    "epsilon_S_peakROI_cm2": (
                        f"{e.epsilon_S_peakROI_cm2:.4g}"
                        if e.epsilon_S_peakROI_cm2 is not None
                        else ""
                    ),
                    "peak_over_mfr": f"{peak_frac:.4g}" if peak_frac == peak_frac else "",
                    "備考": pe_note or e.note,
                }
            )
    return path


def write_wall_efficiencies_csv(
    eff: dict[str, WallEfficiency],
    path: Path | None = None,
) -> Path:
    path = path or EFF_WALL_CSV
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "検出器",
        "epsilon_S_wall_cm2",
        "epsilon_S_wall_std_cm2",
        "epsilon_S_peakROI_cm2",
        "wall_over_peak_cal",
        "manufacturer_cps_nv",
        "epsilon_S_total_cm2",
        "f_wall",
        "wall_over_mfr",
        "S_he3_isotropic_cm2",
        "ε_mfr",
        "S_he3_projected_cm2",
        "備考",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for det in ("d1", "D1", "d2", "D2"):
            e = eff.get(det)
            if e is None:
                continue
            wall_peak = (
                e.epsilon_S_wall_cm2 / e.epsilon_S_peakROI_cm2
                if e.epsilon_S_peakROI_cm2
                else float("nan")
            )
            mfr = MFR_SENSITIVITY_CPS_NV[det]
            g = he3_geometric_areas(det)
            s_iso = g["S_he3_isotropic_cm2"]
            w.writerow(
                {
                    "検出器": det,
                    "epsilon_S_wall_cm2": f"{e.epsilon_S_wall_cm2:.4g}",
                    "epsilon_S_wall_std_cm2": (
                        f"{e.epsilon_S_wall_std_cm2:.4g}"
                        if e.epsilon_S_wall_std_cm2 is not None
                        else ""
                    ),
                    "epsilon_S_peakROI_cm2": (
                        f"{e.epsilon_S_peakROI_cm2:.4g}"
                        if e.epsilon_S_peakROI_cm2 is not None
                        else ""
                    ),
                    "wall_over_peak_cal": (
                        f"{wall_peak:.4g}" if wall_peak == wall_peak else ""
                    ),
                    "manufacturer_cps_nv": f"{mfr:.4g}",
                    "epsilon_S_total_cm2": (
                        f"{e.epsilon_S_total_cm2:.4g}"
                        if e.epsilon_S_total_cm2 is not None
                        else ""
                    ),
                    "f_wall": f"{e.f_wall:.4g}" if e.f_wall is not None else "",
                    "wall_over_mfr": f"{e.epsilon_S_wall_cm2 / mfr:.4g}",
                    "S_he3_isotropic_cm2": f"{s_iso:.4g}",
                    "ε_mfr": f"{mfr / s_iso:.4g}",
                    "S_he3_projected_cm2": f"{g['S_he3_projected_cm2']:.4g}",
                    "備考": e.note,
                }
            )
    write_manufacturer_comparison_csv(eff)
    return path


def flux_phi(rate_wall_net: float, detector: str, eff: dict[str, WallEfficiency] | None = None) -> float:
    eff = eff or load_wall_efficiencies_csv()
    e = eff[detector].epsilon_S_wall_cm2
    return rate_wall_net / e
