#!/usr/bin/env python3
"""fig16/17/18 相当の三方式比較プロット（theory_research/figures 専用）。

- 完全理論は各検出器の地上実測値でアンカー（t=0 で旧理論・実測と一致）
- 片対数＋誤差棒を主とし、軸レンジはデータ域に合わせる
- 既存 _plot_mca.py / 測定_20260818/figures/ は変更しない
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, FuncFormatter, LogLocator, MaxNLocator, MultipleLocator

HERE = Path(__file__).resolve().parent
MEAS = HERE.parent
CODE = MEAS.parent
FIG_DIR = HERE / "figures"
sys.path.insert(0, str(CODE))
sys.path.insert(0, str(HERE))

import _plot_mca as pm  # noqa: E402
import equiv_shielding as esh  # noqa: E402
from build_complete_theory import (  # noqa: E402
    EPS_WALL,
    RHO_C,
    TransportParams,
    curve_for,
    fit,
    load_observations,
    load_transport_params,
    predict,
)

plt.rcParams.update({
    "font.family": "Hiragino Sans",
    "axes.unicode_minus": False,
    "figure.dpi": 120,
    "savefig.dpi": 180,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
})

FIG_DIR.mkdir(exist_ok=True)
COMPLETE_COLOR = "#7B3294"
COMPLETE_LW = 2.4
COMPLETE_LABEL = "完全理論（多成分）"
# 混合形: e^{-x/λ} の2成分展開
# (1/10) e^{-x/λ} + (9/10)(1 - e^{-x/λ}) = 9/10 - (4/5) e^{-x/λ}
MIX_LAM = 39.2
MIX_COLOR = "#C51B7D"
MIX_COMP_DECAY = "#E7298A"   # 減衰成分 (1/10)e
MIX_COMP_EQ = "#FDAE61"      # 平衡成分 (9/10)(1-e)
MIX_LW = 2.2
MIX_LW_COMP = 1.2
MIX_LS = "-"
MIX_LABEL = r"混合形 $\frac{9}{10}-\frac{4}{5}e^{-x/\lambda}$"
MIX_COMP_LABELS = (
    r"減衰 $\frac{1}{10}e^{-x/\lambda}$",
    r"平衡 $\frac{9}{10}(1-e^{-x/\lambda})$",
)
OLD_LAM = (39.2, 60.0, 141.5)
FACILITY_SITES = pm.FACILITY_SITES

# 文献参考点: 神岡（神岡）地下 laboratory（覆土深 1000 m, PTEP 系文献値）
KAMIOKA_REF = {
    "label": "神岡",
    "depth_m": 1000.0,
    "phi_n_cm2_s": 7.8e-6,
}
KAMIOKA_STYLE = {
    "marker": "*",
    "color": "#C99700",
    "ms": 13,
}

# ミュオン起源中性子生成率（Malgin 型; d [m], x [m.w.e.], y [n/(m²·s)]）
MUON_RHO = 2.3
MUON_Y0 = 2.0
MUON_X_SCALE = 11.5
MUON_POWER = -2.2
MUON_ATM_SCALE = 0.15  # m, 15 cm ごとに半減

# 生成する図（片対数中心・必要最小限）
FIG16_DETECTORS = ("D1", "d2")
FIG17_DETECTORS = ("D1", "d2")


def _save(fig, name: str) -> None:
    pm.save(fig, name, folder=FIG_DIR, bbox_inches="tight")
    print(f"  {name}.png")


def _anchor_curve(y: np.ndarray, anchor_y: float) -> np.ndarray:
    """曲線先端 (t=0) を anchor_y に合わせる。"""
    if len(y) > 0 and y[0] > 0 and anchor_y > 0:
        return y * (anchor_y / y[0])
    return y


def _scale_flux_area(flux: dict, area_scale: float) -> dict:
    """S を area_scale 倍 → φ = R/(εS) は 1/area_scale。"""
    if area_scale == 1.0:
        return flux
    out = copy.deepcopy(flux)
    inv = 1.0 / area_scale
    for rows in out.values():
        for row in rows:
            for key in ("絶対phi_n_cm2_s", "絶対phi_err"):
                v = (row.get(key) or "").strip()
                if v:
                    row[key] = f"{float(v) * inv:.6g}"
    return out


def _meas_phi(det: str, site: str, flux: dict) -> float | None:
    for row in flux.get(det, []):
        if (row.get("地点") or "").strip() == site:
            v = (row.get("絶対phi_n_cm2_s") or "").strip()
            if v:
                return float(v)
    return None


def _ground_anchor(det: str, p: TransportParams, flux: dict, *, cps: bool = False) -> float:
    """地上実測値（アンカー用）。"""
    if cps:
        return float(pm.load_detector_cps(det).get("地上") or 0.0)
    return _meas_phi(det, "地上", flux) or 0.0


def _complete_flux(
    det: str, p: TransportParams, flux: dict, *, norm: float | None = None
) -> tuple[np.ndarray, np.ndarray]:
    t, y = curve_for(det, "wall", p)
    anchor = _ground_anchor(det, p, flux)
    if anchor > 0:
        y = _anchor_curve(y, anchor)
    if norm and norm > 0:
        y = y / norm
    return t, y


def _complete_flux_extended(
    det: str,
    p: TransportParams,
    flux: dict,
    *,
    x_max_teq_cm: float,
    norm: float | None = None,
    n: int = 700,
) -> tuple[np.ndarray, np.ndarray]:
    """完全理論曲線を深部（神岡等）まで延長。"""
    t, y = curve_for(
        det,
        "wall",
        p,
        n=n,
        x_max_gcm2=x_max_teq_cm * RHO_C,
    )
    anchor = _ground_anchor(det, p, flux)
    if anchor > 0:
        y = _anchor_curve(y, anchor)
    if norm and norm > 0:
        y = y / norm
    return t, y


def _complete_cps(
    det: str, p: TransportParams, *, relative: bool = False
) -> tuple[np.ndarray, np.ndarray]:
    t, y = curve_for(det, "wall", p)
    y = y * EPS_WALL[det]
    anchor = _ground_anchor(det, p, {}, cps=True)
    if anchor > 0:
        y = _anchor_curve(y, anchor)
    if relative and anchor > 0:
        y = y / anchor
    return t, y


def _plot_old_theory(
    ax, x_c: np.ndarray, a0: float, *, relative: bool, compact: bool = False
) -> None:
    styles = (
        (OLD_LAM[0], "#555555", "-", 2.0),
        (OLD_LAM[1], "#888888", "--", 1.6),
        (OLD_LAM[2], "#AAAAAA", ":", 1.8),
    )
    if compact:
        styles = (styles[0],)
    for lam, color, ls, lw in styles:
        y = a0 * np.exp(-x_c / lam) if not relative else np.exp(-x_c / lam)
        ax.plot(x_c, y, color=color, ls=ls, lw=lw,
                label=rf"旧理論  $\lambda={lam:.1f}$ cm")


def _mix_theory_components(
    x_c: np.ndarray, *, lam: float = MIX_LAM
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """減衰・平衡・合計の3系列。"""
    e = np.exp(-x_c / lam)
    decay = e * (1.0 / 10.0)
    equil = (1.0 - e) * (9.0 / 10.0)
    return decay, equil, decay + equil


def _mix_theory_curve(x_c: np.ndarray, *, lam: float = MIX_LAM) -> np.ndarray:
    """(1/10) e^{-x/λ} + (9/10)(1 - e^{-x/λ})."""
    _, _, total = _mix_theory_components(x_c, lam=lam)
    return total


def _plot_mix_theory(ax, x_c: np.ndarray, *, scale: float = 1.0, components: bool = False) -> None:
    decay, equil, total = _mix_theory_components(x_c)
    decay *= scale
    equil *= scale
    total *= scale
    if components:
        ax.plot(
            x_c, decay, color=MIX_COMP_DECAY, ls=":", lw=MIX_LW_COMP,
            label=MIX_COMP_LABELS[0] + rf" ($\lambda={MIX_LAM:.1f}$ cm)", zorder=2.3,
        )
        ax.plot(
            x_c, equil, color=MIX_COMP_EQ, ls=":", lw=MIX_LW_COMP,
            label=MIX_COMP_LABELS[1], zorder=2.3,
        )
    ax.plot(
        x_c, total, color=MIX_COLOR, ls=MIX_LS, lw=MIX_LW,
        label=MIX_LABEL + rf" ($\lambda={MIX_LAM:.1f}$ cm)", zorder=2.5,
    )


def _muon_induced_curves(x_c: np.ndarray) -> dict[str, np.ndarray]:
    """等価コンクリート厚 [cm] → 地上正規化相対フラックス。"""
    d = x_c / 100.0  # m
    x_mwe = d * MUON_RHO
    y_total = MUON_Y0 * (1.0 + x_mwe / MUON_X_SCALE) ** MUON_POWER
    y_atmosphere = MUON_Y0 * np.exp(-d / MUON_ATM_SCALE)
    norm = MUON_Y0
    return {
        "total": y_total / norm,
        "evap": 0.90 * y_total / norm,
        "thermal": 0.45 * y_total / norm,
        "high": 0.10 * y_total / norm,
        "atmosphere": y_atmosphere / norm,
    }


def _plot_muon_induced_theory(
    ax, x_c: np.ndarray, *, scale: float = 1.0, components: bool = False
) -> None:
    """ミュオン起源中性子生成率モデル（S1 Malgin 型）を重ね描き。"""
    curves = _muon_induced_curves(x_c)
    ax.plot(
        x_c, curves["total"] * scale, color="black", lw=2.2, zorder=2.2,
        label=rf"μ起源 総生成 $y_{{\rm total}}={MUON_Y0}(1+x/{MUON_X_SCALE})^{{{MUON_POWER}}}$",
    )
    if components:
        ax.plot(
            x_c, curves["evap"] * scale, color="tab:blue", ls="--", lw=1.5, zorder=2.1,
            label="μ起源 蒸発成分 (1–10 MeV) [90%]",
        )
        ax.plot(
            x_c, curves["thermal"] * scale, color="tab:purple", ls="-.", lw=1.5, zorder=2.1,
            label="μ起源 熱化成分 (<0.5 eV) [~45%]",
        )
        ax.plot(
            x_c, curves["high"] * scale, color="tab:red", ls=":", lw=1.5, zorder=2.1,
            label="μ起源 超高速成分 (>10 MeV) [10%]",
        )
        ax.plot(
            x_c, curves["atmosphere"] * scale, color="tab:gray", ls="--", lw=1.2,
            alpha=0.55, zorder=2.0,
            label="大気中性子カットオフ（参考, 15 cm 半減）",
        )


def _log_ylim(ax, ys: list[np.ndarray], pts_y: list[float], *, floor: float = 1e-5,
              ceil: float | None = None) -> None:
    vals = [v for arr in ys for v in np.asarray(arr).flat if v > 0]
    vals.extend(v for v in pts_y if v > 0)
    if not vals:
        return
    y_min = max(min(vals) * 0.35, floor)
    y_max = min(max(vals) * 2.5, ceil) if ceil else max(vals) * 2.5
    ax.set_yscale("log")
    ax.set_ylim(y_min, y_max)
    ax.yaxis.set_major_locator(LogLocator(base=10, numticks=8))
    ax.yaxis.set_minor_locator(LogLocator(base=10, subs=(0.2, 0.5, 2, 5)))


def _annotate_sites_short(ax, points: list[dict]) -> None:
    """地点名のみ（数値なし）で注釈。"""
    offsets = {
        "地上": (8, 10, "left", "bottom"),
        "testhole": (8, -12, "left", "top"),
        "PF": (8, 12, "left", "bottom"),
        "linac": (8, -16, "left", "top"),
        "Linac3": (8, -16, "left", "top"),
        "BT": (-8, 12, "right", "bottom"),
        "PS": (10, 14, "left", "bottom"),
        "KEKB": (-10, -16, "right", "top"),
        "linacIRON": (-8, 12, "right", "bottom"),
        "神岡": (10, -14, "left", "top"),
    }
    for pt in points:
        lab = pt.get("label") or pt.get("site", "")
        dx, dy, ha, va = offsets.get(lab, (6, 6, "left", "bottom"))
        ax.annotate(
            lab, (pt["x"], pt["y"]),
            xytext=(dx, dy), textcoords="offset points",
            fontsize=7.5, ha=ha, va=va, color="#333333", zorder=6,
        )


def _annotate_sites_once(ax, points: list[dict]) -> None:
    """同一地点は1回だけ注釈。"""
    best: dict[str, dict] = {}
    for pt in points:
        lab = pt.get("label") or pt.get("site", "")
        if lab not in best or pt["y"] > best[lab]["y"]:
            best[lab] = pt
    _annotate_sites_short(ax, list(best.values()))


def _broken_axis_slash(ax_left, ax_right, *, size: float = 0.012) -> None:
    """二分割横軸の切断マーク。"""
    kw = dict(color="0.35", clip_on=False, linewidth=0.9)
    ax_left.plot(
        (1 - size, 1 + size), (-size, +size), transform=ax_left.transAxes, **kw
    )
    ax_left.plot(
        (1 - size, 1 + size), (1 - size, 1 + size), transform=ax_left.transAxes, **kw
    )
    ax_right.plot(
        (-size, +size), (-size, +size), transform=ax_right.transAxes, **kw
    )
    ax_right.plot(
        (-size, +size), (1 - size, 1 + size), transform=ax_right.transAxes, **kw
    )


def _setup_linear_x(
    ax,
    x_lo: float,
    x_hi: float,
    *,
    step: float,
) -> None:
    """等間隔の linear 横軸（目盛り重なりを避ける）。"""
    ax.set_xlim(x_lo, x_hi)
    start = 0.0 if x_lo <= 0 else np.ceil(x_lo / step) * step
    ticks = list(np.arange(start, x_hi + 0.01 * step, step))
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_major_formatter(
        FuncFormatter(lambda x, _: f"{int(round(x))}")
    )
    ax.xaxis.set_minor_locator(FixedLocator([]))
    ax.tick_params(axis="x", which="major", direction="out", labelsize=9)


# 連続版横軸: 0–KEKB を画面幅のこの割合以上にする（残りは神岡側を圧縮）
FIG19_KEK_AXIS_FRAC = 0.60


def _symlog_linthresh() -> float:
    """KEKB までを symlog の線形域に含める（0–KEKB が等間隔になる）。"""
    return pm._kek_axis_x_max()


def _symlog_linscale(x_max: float, *, linthresh: float, kek_frac: float = FIG19_KEK_AXIS_FRAC) -> float:
    """0–linthresh が横軸の kek_frac 以上になるよう linscale を決める。

    matplotlib symlog: 線形域の表示幅 ∝ linscale、対数域 ∝ log10(xmax/linthresh)。
    """
    lin = max(float(linthresh), 1.0)
    xmax = max(float(x_max), lin * 1.01)
    log_decades = float(np.log10(xmax / lin))
    f = min(max(float(kek_frac), 0.51), 0.85)
    return log_decades * f / (1.0 - f)


def _symlog_teq_ticks(x_max: float, *, linthresh: float | None = None) -> list[float]:
    """symlog 横軸用 major tick（KEK 域は 100 cm 等間隔、深部は疎）。"""
    lin = _symlog_linthresh() if linthresh is None else float(linthresh)
    ticks: list[float] = []
    t = 0.0
    while t <= lin + 1e-9:
        ticks.append(t)
        t += 100.0
    # 深部は省略気味（神岡付近だけ）
    for t in (10000, 30000, 50000, 80000, 100000):
        if t > lin * 1.5 and t <= x_max * 1.001:
            ticks.append(float(t))
    if x_max > lin and all(abs(x_max - t) > 2000 for t in ticks):
        ticks.append(float(x_max))
    return sorted(set(ticks))


def _format_teq_cm(x: float, _pos) -> str:
    """等価コンクリート厚 [cm] の目盛りラベル。"""
    x = float(x)
    if abs(x) < 0.5:
        return "0"
    if x >= 10000.0:
        return rf"${int(round(x / 1000))}\times10^3$"
    return f"{int(round(x))}"


def _setup_symlog_x(ax, x_max: float, *, linthresh: float | None = None) -> None:
    """fig19 連続版: symlog 横軸と明示目盛り。

    0–KEKB は線形（100 cm 等間隔）かつ横幅の過半。神岡側は対数圧縮。
    """
    lin = _symlog_linthresh() if linthresh is None else float(linthresh)
    linscale = _symlog_linscale(x_max, linthresh=lin)
    ax.set_xscale("symlog", linthresh=lin, linscale=linscale)
    ax.set_xlim(0, x_max)
    ticks = _symlog_teq_ticks(x_max, linthresh=lin)
    ax.xaxis.set_major_locator(FixedLocator(ticks))
    ax.xaxis.set_major_formatter(FuncFormatter(_format_teq_cm))
    ax.xaxis.set_minor_locator(FixedLocator([]))
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]（$X/\rho_c$）")
    ax.tick_params(axis="x", which="major", direction="out", labelsize=8.5)
    for lab in ax.get_xticklabels():
        lab.set_rotation(0)
        lab.set_ha("center")


def _fig19_draw_theory(
    ax,
    x_c: np.ndarray,
    *,
    p: TransportParams,
    flux: dict,
    phi0: float,
    absolute: bool,
    theory_scale: float,
    x_max: float,
) -> tuple[np.ndarray, np.ndarray]:
    _plot_old_theory(ax, x_c, theory_scale, relative=not absolute, compact=True)
    if absolute:
        t_c, y_c = _complete_flux_extended("D1", p, flux, x_max_teq_cm=x_max)
    else:
        t_c, y_c = _complete_flux_extended(
            "D1", p, flux, x_max_teq_cm=x_max, norm=phi0
        )
    ax.plot(t_c, y_c, color=COMPLETE_COLOR, lw=COMPLETE_LW, label=COMPLETE_LABEL, zorder=2)
    _plot_mix_theory(ax, x_c, scale=theory_scale, components=False)
    _plot_muon_induced_theory(ax, x_c, scale=theory_scale, components=False)
    return t_c, y_c


def _fig19_draw_data(
    ax,
    *,
    plotted: list[str],
    flux: dict,
    absolute: bool,
    include_detectors: bool = True,
    include_kamioka: bool = False,
    kamioka: dict | None = None,
) -> None:
    if include_detectors:
        for det in plotted:
            if absolute:
                pts = pm._build_flux_points(det, absolute=True, flux=flux)
            else:
                pts = pm._build_flux_points_ground_norm(det, flux=flux)
            pts = [pt for pt in pts if pt.get("label") in FACILITY_SITES or pt["site"] == "地上"]
            st = pm.DETECTOR_STYLE[det]
            ax.errorbar(
                [pt["x"] for pt in pts], [pt["y"] for pt in pts],
                xerr=[pt["x_err"] for pt in pts], yerr=[pt["y_err"] for pt in pts],
                fmt=st["marker"], color=st["color"], ms=st["ms"] - 1,
                linestyle="none", capsize=2.5, elinewidth=0.8, zorder=4,
                label=st["label"],
            )
    if include_kamioka:
        pt = kamioka or _kamioka_ref_point(flux, absolute=absolute)
        _plot_kamioka_ref(ax, pt)


FIG19_X_KEK = pm._kek_axis_x_max()  # 左パネル上限 [cm]（KEKB まで統一）
FIG19_X_DEEP_LO = 8000.0  # 右パネル下限 [cm]（中断部）


def _fig19_prepare(
    p: TransportParams,
    *,
    absolute: bool,
    flux_data: dict | None = None,
    detectors: tuple[str, ...] | None = None,
):
    """fig19 共通: データ点・x 範囲を準備。不足時は None。"""
    flux = flux_data if flux_data is not None else pm.load_flux_summary()
    try:
        phi0 = pm._flux_phi0_ground(flux)
    except KeyError:
        print(f"skip fig19 {'absolute' if absolute else 'relative'}")
        return None

    det_order = detectors or ("D1", "D2", "d1", "d2")
    plotted: list[str] = []
    all_pts: list[dict] = []
    for det in det_order:
        if absolute:
            pts = pm._build_flux_points(det, absolute=True, flux=flux)
        else:
            pts = pm._build_flux_points_ground_norm(det, flux=flux)
        pts = [pt for pt in pts if pt.get("label") in FACILITY_SITES or pt["site"] == "地上"]
        if len(pts) >= 1:
            plotted.append(det)
            all_pts.extend(pts)

    if len(plotted) < 1 or not all_pts:
        print("skip fig19: 検出器不足")
        return None

    kamioka = _kamioka_ref_point(flux, absolute=absolute)
    kek_pts = list(all_pts)
    all_pts.append(kamioka)
    kek_x_max = pm._kek_axis_x_max()
    x_max = max(kamioka["x"], kek_x_max) * 1.02
    return flux, phi0, plotted, kek_pts, kamioka, all_pts, x_max


def _fig19_apply_yscale(ax, *, absolute: bool, x_c, y_c, all_pts, theory_scale, kamioka) -> None:
    if absolute:
        _log_ylim(
            ax,
            _fig18_theory_ys(x_c, y_c, scale=theory_scale),
            [pt["y"] for pt in all_pts],
            floor=max(2e-7, kamioka["y"] * 0.25),
            ceil=max(pt["y"] for pt in all_pts) * 6.0,
        )
    else:
        ax.set_yscale("log")
        y_lo = min(3e-3, kamioka["y"] * 0.35)
        ax.set_ylim(y_lo, pm.EQUIV_Y_PAD_LOGY)
        ax.yaxis.set_major_locator(LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))


def _setup_ax(
    ax,
    x_max: float,
    *,
    logy: bool,
    symlog_x: bool = False,
    x_left: float = -15.0,
) -> None:
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]（$X/\rho_c$）")
    if symlog_x:
        _setup_symlog_x(ax, x_max)
    else:
        # KEKB までの線形軸は 100 cm 等間隔（全図統一）
        ax.set_xlim(x_left if not logy else 0, x_max)
        step = 100.0 if x_max >= 400 else 50.0
        ax.xaxis.set_major_locator(MultipleLocator(step))
        ax.xaxis.set_minor_locator(MultipleLocator(step / 5.0))
    ax.tick_params(which="both", direction="out")
    if logy:
        ax.axvline(0, color="#DDDDDD", lw=0.6, zorder=0)


def _legend(ax, *, logy: bool = True, outside: bool = False) -> None:
    """凡例は常にグラフ内左下（outside は互換のため残し、無視）。"""
    del logy, outside
    ax.legend(
        frameon=False, fontsize=7.5, ncol=1,
        loc="lower left",
        borderaxespad=0.6, handlelength=1.8, labelspacing=0.45,
    )


# ---------------------------------------------------------------------------
# 図16: CPS（d2 中心 + D1）
# ---------------------------------------------------------------------------

def fig16_cps(p: TransportParams, *, absolute: bool, detector: str = "d2") -> None:
    from mca_common import detector_fs_suffix

    cps = pm.load_detector_cps(detector)
    cps_err = pm.load_detector_cps_err(detector)
    if not cps or "地上" not in cps:
        print(f"skip fig16 {detector}")
        return

    cps0 = float(cps["地上"])
    a0 = cps0 if absolute else 1.0
    sites = pm._site_shielding(cps)
    points = []
    for site in sites:
        if site["label"] not in FACILITY_SITES and site["label"] != "地上":
            continue
        x_eq = pm._equiv_concrete_cm_from_x(site["X"])
        sys = pm._teq_systematic_err_cm(
            site["concrete_cm"], site["soil_cm"], site.get("iron_cm", 0.0)
        )
        y_rel = site["cps"] / cps0
        y = site["cps"] if absolute else y_rel
        e_cps = float(cps_err.get(site["label"], 0.0))
        y_err = e_cps if absolute else pm._rel_cps_err(
            site["cps"], e_cps, cps0, float(cps_err.get("地上", 0.0))
        )
        points.append({
            "label": site["label"], "x": x_eq, "y": y,
            "x_err": float(sys["dteq_cm"]), "y_err": y_err,
        })

    x_max = pm._kek_axis_x_max()
    x_c = np.linspace(0, x_max, 400)

    fig, ax = plt.subplots(figsize=(9.0, 6.2))
    fig.subplots_adjust(left=0.13, right=0.97, top=0.94, bottom=0.12)

    _plot_old_theory(ax, x_c, a0, relative=not absolute)
    t_c, y_c = _complete_cps(detector, p, relative=not absolute)
    ax.plot(t_c, y_c, color=COMPLETE_COLOR, lw=COMPLETE_LW, label=COMPLETE_LABEL, zorder=2)

    st = pm.DETECTOR_STYLE.get(detector, {"color": pm.RED, "marker": "o", "ms": 8})
    ax.errorbar(
        [pt["x"] for pt in points], [pt["y"] for pt in points],
        xerr=[pt["x_err"] for pt in points], yerr=[pt["y_err"] for pt in points],
        fmt=st["marker"], color=st["color"], ms=st["ms"] - 1,
        linestyle="none", capsize=2.5, elinewidth=0.9, zorder=4,
        label=f"実測 {detector}",
    )

    _log_ylim(ax, [y_c], [pt["y"] for pt in points], floor=1e-4 if absolute else 1e-3)
    _setup_ax(ax, x_max, logy=True)
    ax.set_ylabel("実測 CPS [1/s]" if absolute else "相対 CPS（地上 = 1）")
    _annotate_sites_short(ax, points)
    _legend(ax, logy=True)

    base = "16_全地点_等価コンクリート_実測CPS_誤差棒" if absolute else "16_全地点_等価コンクリート_誤差棒"
    _save(fig, f"{base}{detector_fs_suffix(detector)}_片対数")


# ---------------------------------------------------------------------------
# 図17: 絶対 φ
# ---------------------------------------------------------------------------

def fig17_flux(p: TransportParams, *, detector: str = "d2") -> None:
    flux = pm.load_flux_summary()
    points = pm._build_flux_points(detector, absolute=True, flux=flux)
    points = [pt for pt in points if pt.get("label") in FACILITY_SITES or pt["site"] == "地上"]
    if not points:
        print(f"skip fig17 {detector}")
        return

    phi0 = pm._flux_phi0_ground(flux)
    x_max = pm._kek_axis_x_max()
    x_c = np.linspace(0, x_max, 400)

    fig, ax = plt.subplots(figsize=(9.0, 6.2))
    fig.subplots_adjust(left=0.13, right=0.97, top=0.94, bottom=0.12)

    _plot_old_theory(ax, x_c, phi0, relative=False)
    t_c, y_c = _complete_flux(detector, p, flux)
    ax.plot(t_c, y_c, color=COMPLETE_COLOR, lw=COMPLETE_LW, label=COMPLETE_LABEL, zorder=2)

    st = pm.DETECTOR_STYLE.get(detector, {"color": pm.RED, "marker": "o", "ms": 9})
    ax.errorbar(
        [pt["x"] for pt in points], [pt["y"] for pt in points],
        xerr=[pt["x_err"] for pt in points], yerr=[pt["y_err"] for pt in points],
        fmt=st["marker"], color=st["color"], ms=st["ms"] - 1,
        linestyle="none", capsize=3, elinewidth=0.9, zorder=4,
        label=f"実測 {st['label']}",
    )

    _log_ylim(ax, [y_c], [pt["y"] for pt in points], floor=1e-5)
    _setup_ax(ax, x_max, logy=True)
    ax.set_ylabel(r"中性子フラックス $\phi$ [n/cm$^2$/s]")
    _annotate_sites_short(ax, points)
    _legend(ax, logy=True)

    _save(fig, f"17_全地点_フラックス_絶対_{detector}_誤差棒_片対数")


# ---------------------------------------------------------------------------
# 図18: 相対/絶対 φ（4 検出器、完全理論は D1 のみ）
# ---------------------------------------------------------------------------

def _kamioka_teq_cm(depth_m: float) -> float:
    """覆土深 [m] → 等価コンクリート厚 [cm]（密度換算、KEK 地点と同軸）。"""
    return esh.equiv_concrete(0.0, depth_m * 100.0).t_eq_density_only_cm


def _kamioka_ref_point(flux: dict, *, absolute: bool) -> dict:
    x_eq = _kamioka_teq_cm(KAMIOKA_REF["depth_m"])
    phi = KAMIOKA_REF["phi_n_cm2_s"]
    if absolute:
        y = phi
    else:
        y = phi / pm._flux_phi0_ground(flux)
    return {
        "site": KAMIOKA_REF["label"],
        "label": KAMIOKA_REF["label"],
        "x": x_eq,
        "y": y,
        "y_err": 0.0,
        "x_err": 0.0,
        "literature": True,
    }


def _plot_kamioka_ref(ax, pt: dict) -> None:
    st = KAMIOKA_STYLE
    depth_m = int(KAMIOKA_REF["depth_m"])
    ax.plot(
        pt["x"],
        pt["y"],
        linestyle="none",
        marker=st["marker"],
        color=st["color"],
        ms=st["ms"],
        markeredgecolor="#5C4A00",
        markeredgewidth=0.6,
        zorder=5,
        label=rf"神岡（文献, {depth_m} m）",
    )


def _fig18_theory_ys(x_c: np.ndarray, y_c: np.ndarray, *, scale: float) -> list[np.ndarray]:
    """Y 軸レンジ用: 主曲線のみ（補助成分で軸が潰れないようにする）。"""
    _, _, mix_total = _mix_theory_components(x_c)
    muon = _muon_induced_curves(x_c)
    return [
        y_c,
        mix_total * scale,
        muon["total"] * scale,
    ]


# 図18 分割: 熱中性子（裸管）/ MeV（PE）
FIG18_THERMAL_DETS = ("D1", "d1")
FIG18_MEV_DETS = ("D2", "d2")
FIG18_DET_LABELS = {
    "D1": "D1（熱・大径・SN1715）",
    "d1": "d1（熱・小径・SN2162）",
    "D2": "D2（MeV・大径・SN1715）",
    "d2": "d2（MeV・小径・SN2162）",
}


def _fig18_anchor_phi0(flux: dict, detectors: tuple[str, ...]) -> float:
    """理論曲線スケール用 φ0。グループ先頭検出器の地上、なければ D1 地上。"""
    for det in detectors:
        phi = _meas_phi(det, "地上", flux)
        if phi and phi > 0:
            return phi
    return pm._flux_phi0_ground(flux)


def fig18_compare(
    p: TransportParams,
    *,
    absolute: bool,
    detectors: tuple[str, ...] = ("D1", "D2", "d1", "d2"),
    name_suffix: str = "",
    title: str | None = None,
    det_labels: dict[str, str] | None = None,
) -> None:
    """図18: 絶対/相対 φ の検出器比較。detectors で系列を絞れる。"""
    flux = pm.load_flux_summary()
    try:
        phi0 = _fig18_anchor_phi0(flux, detectors) if absolute else pm._flux_phi0_ground(flux)
    except KeyError:
        print(f"skip fig18 {'absolute' if absolute else 'relative'}{name_suffix}")
        return

    plotted: list[str] = []
    all_pts: list[dict] = []
    for det in detectors:
        if absolute:
            pts = pm._build_flux_points(det, absolute=True, flux=flux)
        else:
            pts = pm._build_flux_points_ground_norm(det, flux=flux)
        pts = [pt for pt in pts if pt.get("label") in FACILITY_SITES or pt["site"] == "地上"]
        if pts:
            plotted.append(det)
            all_pts.extend(pts)

    if len(all_pts) < 2:
        print(f"skip fig18{name_suffix}: 測定点不足")
        return

    x_max = pm._kek_axis_x_max()
    x_c = np.linspace(0, x_max, 400)
    theory_scale = phi0 if absolute else 1.0
    theory_det = next((d for d in detectors if _meas_phi(d, "地上", flux)), "D1")

    fig, ax = plt.subplots(figsize=(10.6, 6.4))
    fig.subplots_adjust(left=0.11, right=0.97, top=0.90 if title else 0.94, bottom=0.12)

    _plot_old_theory(ax, x_c, theory_scale, relative=not absolute, compact=True)
    if absolute:
        t_c, y_c = _complete_flux(theory_det, p, flux)
    else:
        t_c, y_c = _complete_flux(theory_det, p, flux, norm=phi0)
    ax.plot(t_c, y_c, color=COMPLETE_COLOR, lw=COMPLETE_LW, label=COMPLETE_LABEL, zorder=2)
    _plot_mix_theory(ax, x_c, scale=theory_scale, components=False)
    _plot_muon_induced_theory(ax, x_c, scale=theory_scale, components=False)

    labels = det_labels or {}
    for det in plotted:
        if absolute:
            pts = pm._build_flux_points(det, absolute=True, flux=flux)
        else:
            pts = pm._build_flux_points_ground_norm(det, flux=flux)
        pts = [pt for pt in pts if pt.get("label") in FACILITY_SITES or pt["site"] == "地上"]
        st = pm.DETECTOR_STYLE[det]
        ax.errorbar(
            [pt["x"] for pt in pts], [pt["y"] for pt in pts],
            xerr=[pt["x_err"] for pt in pts], yerr=[pt["y_err"] for pt in pts],
            fmt=st["marker"], color=st["color"], ms=st["ms"] - 1,
            linestyle="none", capsize=2.5, elinewidth=0.8, zorder=4,
            label=labels.get(det, st["label"]),
        )

    if absolute:
        _log_ylim(
            ax,
            _fig18_theory_ys(x_c, y_c, scale=theory_scale),
            [pt["y"] for pt in all_pts],
            floor=max(1e-5, min(pt["y"] for pt in all_pts) * 0.25),
            ceil=max(pt["y"] for pt in all_pts) * 8.0,
        )
    else:
        ax.set_yscale("log")
        y_lo = max(1e-2, min(pt["y"] for pt in all_pts) * 0.35)
        ax.set_ylim(y_lo, pm.EQUIV_Y_PAD_LOGY)
        ax.yaxis.set_major_locator(LogLocator(base=10.0))
        ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))
    _setup_ax(ax, x_max, logy=True)
    if absolute:
        ax.set_ylabel(r"中性子フラックス $\phi$ [n/cm$^2$/s]")
    else:
        ax.set_ylabel("相対フラックス（D1 地上 = 1）")
    if title:
        ax.set_title(title, fontsize=12, pad=8)
    _annotate_sites_once(ax, all_pts)
    _legend(ax, logy=True)

    kind = "絶対" if absolute else "相対"
    _save(fig, f"18_全地点_フラックス_{kind}_検出器比較_誤差棒_片対数{name_suffix}")


def fig18_thermal_mev_split(p: TransportParams, *, absolute: bool = True) -> None:
    """図18を熱中性子（D1,d1）と MeV（D2,d2）に分割。"""
    fig18_compare(
        p,
        absolute=absolute,
        detectors=FIG18_THERMAL_DETS,
        name_suffix="_熱中性子_D1d1",
        title="熱中性子（D1, d1）",
        det_labels=FIG18_DET_LABELS,
    )
    fig18_compare(
        p,
        absolute=absolute,
        detectors=FIG18_MEV_DETS,
        name_suffix="_MeV_D2d2",
        title="MeV 中性子（D2, d2）",
        det_labels=FIG18_DET_LABELS,
    )

def fig19_deep_compare(p: TransportParams, *, absolute: bool) -> None:
    """図19: fig18 + 神岡文献点。横軸は KEK / 深部の二分割。"""
    prep = _fig19_prepare(p, absolute=absolute)
    if prep is None:
        return
    flux, phi0, plotted, kek_pts, kamioka, all_pts, x_max = prep
    x_c = np.linspace(0, x_max, 900)
    theory_scale = phi0 if absolute else 1.0

    # 左(KEKB)を過半・右(神岡)は省略気味に圧縮
    kek_w = FIG19_KEK_AXIS_FRAC / (1.0 - FIG19_KEK_AXIS_FRAC)
    fig, (ax_ke, ax_dp) = plt.subplots(
        1, 2, sharey=True, figsize=(13.2, 6.5),
        gridspec_kw=dict(width_ratios=[kek_w, 1.0], wspace=0.06),
    )
    fig.subplots_adjust(left=0.08, right=0.97, top=0.94, bottom=0.14)

    for ax in (ax_ke, ax_dp):
        t_c, y_c = _fig19_draw_theory(
            ax, x_c, p=p, flux=flux, phi0=phi0, absolute=absolute,
            theory_scale=theory_scale, x_max=x_max,
        )

    _fig19_draw_data(ax_ke, plotted=plotted, flux=flux, absolute=absolute)
    _fig19_draw_data(
        ax_dp, plotted=plotted, flux=flux, absolute=absolute,
        include_detectors=False, include_kamioka=True, kamioka=kamioka,
    )

    _fig19_apply_yscale(
        ax_ke, absolute=absolute, x_c=x_c, y_c=y_c,
        all_pts=all_pts, theory_scale=theory_scale, kamioka=kamioka,
    )

    ax_ke.spines["right"].set_visible(False)
    ax_dp.spines["left"].set_visible(False)
    ax_dp.tick_params(axis="y", labelleft=False)
    _broken_axis_slash(ax_ke, ax_dp)

    _setup_linear_x(ax_ke, 0, FIG19_X_KEK, step=100)
    deep_hi = float(np.ceil(x_max / 10000.0) * 10000.0)
    _setup_linear_x(ax_dp, FIG19_X_DEEP_LO, deep_hi, step=10000)
    fig.supxlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]（$X/\rho_c$）", y=0.02)

    ax_ke.axvline(0, color="#DDDDDD", lw=0.6, zorder=0)
    ax_ke.tick_params(axis="y", which="both", direction="out")
    if absolute:
        ax_ke.set_ylabel(r"中性子フラックス $\phi$ [n/cm$^2$/s]")
    else:
        ax_ke.set_ylabel("相対フラックス（D1 地上 = 1）")

    kek_ann = [pt for pt in kek_pts if pt["x"] <= FIG19_X_KEK]
    _annotate_sites_once(ax_ke, kek_ann)
    _annotate_sites_short(ax_dp, [kamioka])
    handles, labels = ax_ke.get_legend_handles_labels()
    for hh, ll in zip(*ax_dp.get_legend_handles_labels()):
        if "神岡" in ll and ll not in labels:
            handles.append(hh)
            labels.append(ll)
    ax_ke.legend(
        handles, labels, frameon=False, fontsize=7.5, ncol=1,
        loc="lower left", borderaxespad=0.6, handlelength=1.8, labelspacing=0.45,
    )

    kind = "絶対" if absolute else "相対"
    _save(fig, f"19_全地点_フラックス_{kind}_検出器比較_神岡_誤差棒_片対数")


def fig19_deep_compare_continuous(
    p: TransportParams,
    *,
    absolute: bool,
    s_area_scale: float = 1.0,
    detectors: tuple[str, ...] | None = None,
    name_suffix: str = "",
) -> None:
    """図19 連続版: 神岡点あり、横軸 symlog（0–KEKB 線形 + 深部対数）。

    s_area_scale: フラックス計算の検出器面積倍率（2 → φ は 1/2、理論曲線は不変）。
    detectors: 重ねる検出器（例: ("D1","d1") 裸管同型、("D2","d2") PE同型）。
    name_suffix: 保存名末尾（例: "_同型裸管_D1d1"）。
    """
    flux_theory = pm.load_flux_summary()
    flux_data = _scale_flux_area(flux_theory, s_area_scale)
    prep = _fig19_prepare(
        p, absolute=absolute, flux_data=flux_data, detectors=detectors,
    )
    if prep is None:
        return
    _, phi0, plotted, _kek_pts, kamioka, all_pts, x_max = prep
    x_c = np.linspace(0, x_max, 900)
    try:
        phi0_theory = pm._flux_phi0_ground(flux_theory)
    except KeyError:
        phi0_theory = phi0
    theory_scale = phi0_theory if absolute else 1.0

    fig, ax = plt.subplots(figsize=(11.4, 6.5))
    fig.subplots_adjust(left=0.11, right=0.97, top=0.94, bottom=0.16)

    t_c, y_c = _fig19_draw_theory(
        ax, x_c, p=p, flux=flux_theory, phi0=phi0_theory, absolute=absolute,
        theory_scale=theory_scale, x_max=x_max,
    )
    _fig19_draw_data(
        ax, plotted=plotted, flux=flux_data, absolute=absolute,
        include_kamioka=True, kamioka=kamioka,
    )
    _fig19_apply_yscale(
        ax, absolute=absolute, x_c=x_c, y_c=y_c,
        all_pts=all_pts, theory_scale=theory_scale, kamioka=kamioka,
    )
    _setup_symlog_x(ax, x_max)
    ax.tick_params(axis="y", which="both", direction="out")
    ax.axvline(0, color="#DDDDDD", lw=0.6, zorder=0)
    if absolute:
        ax.set_ylabel(r"中性子フラックス $\phi$ [n/cm$^2$/s]")
    else:
        ax.set_ylabel("相対フラックス（D1 地上 = 1）")
    _annotate_sites_once(ax, all_pts)
    _legend(ax, logy=True)

    kind = "絶対" if absolute else "相対"
    _save(
        fig,
        f"19_全地点_フラックス_{kind}_検出器比較_神岡_連続_誤差棒_片対数{name_suffix}",
    )


def fig19_same_type_continuous(p: TransportParams, *, absolute: bool = True) -> None:
    """同型同士（裸管 D1–d1 / PE D2–d2）の図19連続版。"""
    fig19_deep_compare_continuous(
        p,
        absolute=absolute,
        detectors=("D1", "d1"),
        name_suffix="_同型裸管_D1d1",
    )
    fig19_deep_compare_continuous(
        p,
        absolute=absolute,
        detectors=("D2", "d2"),
        name_suffix="_同型PE_D2d2",
    )


def fig18_relative(p: TransportParams) -> None:
    fig18_compare(p, absolute=False)


def _cleanup_obsolete() -> None:
    """重複・低品質版を削除。"""
    keep = {
        "16_全地点_等価コンクリート_誤差棒_片対数.png",
        "16_全地点_等価コンクリート_実測CPS_誤差棒_片対数.png",
        "16_全地点_等価コンクリート_誤差棒_small_d2_片対数.png",
        "16_全地点_等価コンクリート_実測CPS_誤差棒_small_d2_片対数.png",
        "17_全地点_フラックス_絶対_D1_誤差棒_片対数.png",
        "17_全地点_フラックス_絶対_d2_誤差棒_片対数.png",
        "18_全地点_フラックス_相対_検出器比較_誤差棒_片対数.png",
        "18_全地点_フラックス_絶対_検出器比較_誤差棒_片対数.png",
        "18_全地点_フラックス_絶対_検出器比較_誤差棒_片対数_熱中性子_D1d1.png",
        "18_全地点_フラックス_絶対_検出器比較_誤差棒_片対数_MeV_D2d2.png",
        "19_全地点_フラックス_相対_検出器比較_神岡_誤差棒_片対数.png",
        "19_全地点_フラックス_絶対_検出器比較_神岡_誤差棒_片対数.png",
        "19_全地点_フラックス_相対_検出器比較_神岡_連続_誤差棒_片対数.png",
        "19_全地点_フラックス_絶対_検出器比較_神岡_連続_誤差棒_片対数.png",
        "19_全地点_フラックス_絶対_検出器比較_神岡_連続_誤差棒_片対数_同型裸管_D1d1.png",
        "19_全地点_フラックス_絶対_検出器比較_神岡_連続_誤差棒_片対数_同型PE_D2d2.png",
    }
    removed = 0
    for f in list(FIG_DIR.glob("*.png")):
        name = f.name
        if name.startswith(("16_", "17_", "18_", "19_", "comparison_")) and name not in keep:
            f.unlink(missing_ok=True)
            removed += 1
            print(f"  removed {name}")
    return removed


def main() -> None:
    obs = load_observations()
    p = load_transport_params()
    print(f"完全理論: theory_parameters.csv を使用 "
          f"(F0={p.F0_fast:.4g}, Λh={p.Lambda_h:.1f}, Cμ={p.C_mu:.4g}, φ_rad={p.phi_rad:.4g})")

    print("cleanup obsolete figures...")
    _cleanup_obsolete()

    print("generating comparison figures...")
    for det in FIG16_DETECTORS:
        fig16_cps(p, absolute=False, detector=det)
        fig16_cps(p, absolute=True, detector=det)
    for det in FIG17_DETECTORS:
        fig17_flux(p, detector=det)
    fig18_relative(p)
    fig18_compare(p, absolute=True)
    fig18_thermal_mev_split(p, absolute=True)
    fig19_deep_compare(p, absolute=False)
    fig19_deep_compare(p, absolute=True)
    fig19_deep_compare_continuous(p, absolute=False)
    fig19_deep_compare_continuous(p, absolute=True)

    kept = sorted(FIG_DIR.glob("1[6789]_*.png"))
    print(f"done: {len(kept)} fig16-18 comparison plots")
    for f in kept:
        print(f"  {f.name}")


if __name__ == "__main__":
    main()
