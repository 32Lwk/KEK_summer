#!/usr/bin/env python3
"""演習9班_v4.pptx スライド61・62（昨年度データ）のフラックス減衰図。

左 = 山（高度 > 0）、中央 = 地上 0、右 = 地下（高度 < 0）。
横軸は左右とも同じ線形スケール [m]。
空気と地下で λ を分ける。縦軸は 10^{-3} がおよそ半分になるカスタム対数。
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator

OUT = Path(__file__).resolve().parent / "figures"
BLUE, RED, ORANGE = "#1F77B4", "#D62728", "#FF7F0E"

LAM_THERMAL_AIR_M = 1470.0
AIR_MAX_M = 2000.0
H_MAX_M = AIR_MAX_M
H_VANISH_M = 1000.0  # 地下理論がおおよそここで 10^{-20} に達する

Y_MID = 4.0e-4  # 縦軸半分の境（MeV 地上 ≈9.8e-4 が上側に来るよう 10^{-3} より下）
Y_LO = 1.0e-20
# 指数ごとの目盛り・横線（10^{-2} … 10^{-20}）
Y_DECADE_LINES = [10.0 ** e for e in range(-2, -21, -1)]
Y_TICKS = Y_DECADE_LINES

SITES = [
    {"label": "屋外", "h_m": 20.0},
    {"label": "筑波山", "h_m": 802.0},
    {"label": "白根山", "h_m": 1992.0},
]
PHI_THERMAL = [1.70e-3, 3.12e-3, 7.10e-3]
PHI_MEV = [9.75e-4, 1.89e-3, 5.36e-3]


def _lam_mev_air_m() -> float:
    h_ref = SITES[0]["h_m"]
    dh = SITES[-1]["h_m"] - h_ref
    return dh / math.log(PHI_MEV[-1] / PHI_MEV[0])


def _lam_under_m(a0: float, h_vanish: float) -> float:
    """A₀ exp(−h_vanish/λ) = Y_LO となる地下側 λ [m]。"""
    return h_vanish / math.log(a0 / Y_LO)


LAM_MEV_AIR_M = _lam_mev_air_m()
# 熱と MeV で地下 λ をはっきり分ける（0 m 以降で重ならないように）
LAM_THERMAL_UNDER_M = _lam_under_m(PHI_THERMAL[0], H_VANISH_M)  # ≈ −1000 m で下限
LAM_MEV_UNDER_M = _lam_under_m(PHI_MEV[0], 700.0)  # MeV はより早く減衰

plt.rcParams.update(
    {
        "font.family": "Hiragino Sans",
        "axes.unicode_minus": False,
        "mathtext.fontset": "dejavusans",
        "figure.dpi": 140,
        "savefig.dpi": 200,
        "axes.grid": True,
        "grid.alpha": 0.35,
        "grid.linestyle": "--",
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "legend.fontsize": 8.5,
    }
)


def _phi(a0: float, h: np.ndarray, lam_air: float, lam_under: float) -> np.ndarray:
    """空気側 λ_air・地下側 λ_under。h=0 で連続。"""
    h = np.asarray(h, dtype=float)
    out = np.empty_like(h)
    pos = h >= 0.0
    out[pos] = a0 * np.exp(h[pos] / lam_air)
    out[~pos] = a0 * np.exp(np.clip(h[~pos] / lam_under, -700.0, 0.0))
    return out


def _make_y_transform(y_hi: float):
    """区分対数。境 Y_MID が軸の半分。10^{-3} は上側に入り MeV 地上と重ならない。"""
    log_mid = math.log10(Y_MID)
    log_lo = math.log10(Y_LO)
    log_hi = math.log10(y_hi)

    def forward(y):
        y = np.asarray(y, dtype=float)
        y = np.clip(y, Y_LO, y_hi)
        logy = np.log10(y)
        upper = y >= Y_MID
        out = np.empty_like(y)
        out[upper] = 0.5 + 0.5 * (logy[upper] - log_mid) / (log_hi - log_mid)
        out[~upper] = 0.5 * (logy[~upper] - log_lo) / (log_mid - log_lo)
        return out

    def inverse(n):
        n = np.asarray(n, dtype=float)
        upper = n >= 0.5
        out = np.empty_like(n)
        out[upper] = 10 ** (log_mid + (n[upper] - 0.5) / 0.5 * (log_hi - log_mid))
        out[~upper] = 10 ** (log_lo + n[~upper] / 0.5 * (log_mid - log_lo))
        return out

    return forward, inverse


def _format_log_tick(value: float, _pos: int) -> str:
    if value <= 0:
        return ""
    exp = int(round(math.log10(value)))
    return rf"$10^{{{exp}}}$"


def _plot_combined(*, logy: bool = False) -> None:
    h_ref = SITES[0]["h_m"]
    a0_th, a0_mev = PHI_THERMAL[0], PHI_MEV[0]

    h_pts = np.array([s["h_m"] - h_ref for s in SITES], dtype=float)
    x_pts = -h_pts
    y_th = np.array(PHI_THERMAL, dtype=float)
    y_mev = np.array(PHI_MEV, dtype=float)

    # 山→地上と地上→地下を分けて描き、0 m で熱/MeV が同一点に潰れるのを防ぐ
    h_air = np.linspace(H_MAX_M, 0.0, 800)
    h_und = np.linspace(0.0, -H_MAX_M, 2000)

    def _lines(a0: float, lam_air: float, lam_under: float):
        phi_air = a0 * np.exp(h_air / lam_air)
        phi_und = a0 * np.exp(np.clip(h_und / lam_under, -700.0, 0.0))
        # 下限到達で打ち切り
        hit = np.where(phi_und <= Y_LO)[0]
        if hit.size:
            i = int(hit[0]) + 1
            h_u, p_u = h_und[:i], np.maximum(phi_und[:i], Y_LO)
        else:
            h_u, p_u = h_und, np.maximum(phi_und, Y_LO)
        return (-h_air, phi_air), (-h_u, p_u)

    (x_th_air, y_th_air), (x_th_und, y_th_und) = _lines(
        a0_th, LAM_THERMAL_AIR_M, LAM_THERMAL_UNDER_M
    )
    (x_mev_air, y_mev_air), (x_mev_und, y_mev_und) = _lines(
        a0_mev, LAM_MEV_AIR_M, LAM_MEV_UNDER_M
    )

    y_hi = max(max(PHI_THERMAL), max(PHI_MEV)) * 2.2
    forward, inverse = _make_y_transform(y_hi)

    fig, ax = plt.subplots(figsize=(10.4, 6.2))
    fig.subplots_adjust(left=0.14, right=0.98, top=0.88, bottom=0.15)

    ax.plot(
        x_th_air,
        y_th_air,
        color=BLUE,
        lw=2.4,
        ls="-",
        solid_capstyle="round",
        label=(
            rf"熱 理論  $\Phi=A_0\,e^{{h/\lambda}}$"
            rf"（空気 $\lambda={LAM_THERMAL_AIR_M:.0f}$ m、"
            rf"地下 $\lambda=40$ cm）"
        ),
        zorder=2,
    )
    ax.plot(x_th_und, y_th_und, color=BLUE, lw=2.4, ls="-", solid_capstyle="round", zorder=2)
    ax.plot(
        x_mev_air,
        y_mev_air,
        color=ORANGE,
        lw=2.4,
        ls="--",
        solid_capstyle="round",
        label=(
            rf"MeV 理論  $\Phi=A_0\,e^{{h/\lambda}}$"
            rf"（空気 $\lambda={LAM_MEV_AIR_M:.0f}$ m、"
            rf"地下 $\lambda=40$ cm）"
        ),
        zorder=2,
    )
    ax.plot(x_mev_und, y_mev_und, color=ORANGE, lw=2.4, ls="--", solid_capstyle="round", zorder=2)

    # 0 m で熱・MeV を同一点に合わせる接続マーカーは置かない
    ax.axvline(0.0, color="#CCCCCC", lw=1.0, zorder=1)

    ax.plot(x_pts, y_th, "o", color=RED, ms=9, zorder=4, label="熱中性子（測定）")
    ax.plot(x_pts, y_mev, "^", color=ORANGE, ms=9, zorder=4, label="MeV（測定）")

    for s, x, yth in zip(SITES, x_pts, y_th):
        if s["label"] == "白根山":
            ax.annotate(
                s["label"],
                (x, yth),
                textcoords="offset points",
                xytext=(14, 8),
                fontsize=9,
                color=RED,
                ha="left",
                va="bottom",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.92),
            )
        elif s["label"] == "筑波山":
            ax.annotate(
                s["label"],
                (x, yth),
                textcoords="offset points",
                xytext=(8, 8),
                fontsize=8.5,
                color=RED,
            )
        else:
            ax.annotate(
                s["label"],
                (x, yth),
                textcoords="offset points",
                xytext=(-10, 10),
                fontsize=8.5,
                color=RED,
                ha="right",
            )

    h_ticks = [2000, 1500, 1000, 500, 0, -500, -1000, -1500, -2000]
    ax.set_xticks([-h for h in h_ticks])
    ax.set_xticklabels([str(h) for h in h_ticks])
    ax.set_xlim(-H_MAX_M * 1.04, H_MAX_M * 1.04)
    ax.set_xlabel("高度 [m]（左: 山 ←　地上 = 0　→ 右: 地下）")

    ax.set_yscale("function", functions=(forward, inverse))
    ax.set_ylim(Y_LO, y_hi)
    ax.yaxis.set_major_locator(FixedLocator(Y_TICKS))
    ax.yaxis.set_major_formatter(FuncFormatter(_format_log_tick))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.grid(True, axis="x", linestyle="--", alpha=0.35)
    ax.grid(False, axis="y")

    # スケール確定後に、指数ごとの横線を描く
    for y in Y_DECADE_LINES:
        ax.axhline(y, color="#B0B0B0", lw=0.9, ls="-", zorder=0)

    if logy:
        ax.set_ylabel("フラックス Φ [cm$^{-2}$ s$^{-1}$]（片対数）")
    else:
        ax.set_ylabel("フラックス Φ [cm$^{-2}$ s$^{-1}$]")

    ax.set_title("昨年度9班：熱中性子・MeV フラックス（スライド61・62）")
    ax.legend(frameon=False, loc="upper right", borderaxespad=0.5)

    suffix = "_片対数" if logy else ""
    out = OUT / f"01_昨年_熱MeV_絶対_空気地下{suffix}.png"
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight", pad_inches=0.10)
    plt.close(fig)
    print(
        f"saved {out}  "
        f"(λ_air th/MeV={LAM_THERMAL_AIR_M:.0f}/{LAM_MEV_AIR_M:.0f} m, "
        f"λ_under th/MeV={LAM_THERMAL_UNDER_M:.0f}/{LAM_MEV_UNDER_M:.0f} m)"
    )


def _plot_air_only() -> None:
    """地上（空気）側のみ。

    横軸は標高 0→2000（左→右）。縦軸は対数なので
    Φ = A₀ exp(h/λ) は直線になる（片対数の理論直線）。
    A₀ は屋外測定値、h は屋外基準の相対高度。
    """
    h_ref = SITES[0]["h_m"]
    a0_th, a0_mev = PHI_THERMAL[0], PHI_MEV[0]

    # 横軸は絶対標高 [m]（表の標高そのもの）
    h_abs = np.array([s["h_m"] for s in SITES], dtype=float)
    h_rel = h_abs - h_ref  # 理論は屋外基準の相対高度
    y_th = np.array(PHI_THERMAL, dtype=float)
    y_mev = np.array(PHI_MEV, dtype=float)

    # 直線描画用：端点2点だけで十分（片対数で真の直線）
    h_line_abs = np.array([h_abs[0], H_MAX_M], dtype=float)
    h_line_rel = h_line_abs - h_ref
    y_th_line = a0_th * np.exp(h_line_rel / LAM_THERMAL_AIR_M)
    y_mev_line = a0_mev * np.exp(h_line_rel / LAM_MEV_AIR_M)

    y_hi = max(max(PHI_THERMAL), max(PHI_MEV), float(y_th_line[-1]), float(y_mev_line[-1])) * 1.35
    y_lo = min(min(PHI_THERMAL), min(PHI_MEV)) * 0.55
    y_ticks = [10.0 ** e for e in range(-4, -1) if y_lo <= 10.0 ** e <= y_hi]

    fig, ax = plt.subplots(figsize=(9.2, 5.8))
    fig.subplots_adjust(left=0.14, right=0.98, top=0.88, bottom=0.15)

    ax.plot(
        h_line_abs,
        y_th_line,
        color=BLUE,
        lw=2.4,
        ls="-",
        solid_capstyle="round",
        label=(
            rf"熱 理論直線  $\Phi=A_0\,e^{{h/\lambda}}$"
            rf"（$\lambda={LAM_THERMAL_AIR_M:.0f}$ m）"
        ),
        zorder=2,
    )
    ax.plot(
        h_line_abs,
        y_mev_line,
        color=ORANGE,
        lw=2.4,
        ls="--",
        solid_capstyle="round",
        label=(
            rf"MeV 理論直線  $\Phi=A_0\,e^{{h/\lambda}}$"
            rf"（$\lambda={LAM_MEV_AIR_M:.0f}$ m）"
        ),
        zorder=2,
    )

    ax.plot(h_abs, y_th, "o", color=RED, ms=9, zorder=4, label="熱中性子（測定）")
    ax.plot(h_abs, y_mev, "^", color=ORANGE, ms=9, zorder=4, label="MeV（測定）")

    for s, x, yth in zip(SITES, h_abs, y_th):
        if s["label"] == "白根山":
            ax.annotate(
                s["label"],
                (x, yth),
                textcoords="offset points",
                xytext=(-8, 10),
                fontsize=9,
                color=RED,
                ha="right",
                va="bottom",
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.92),
            )
        elif s["label"] == "筑波山":
            ax.annotate(
                s["label"],
                (x, yth),
                textcoords="offset points",
                xytext=(8, 8),
                fontsize=8.5,
                color=RED,
            )
        else:
            ax.annotate(
                s["label"],
                (x, yth),
                textcoords="offset points",
                xytext=(8, 10),
                fontsize=8.5,
                color=RED,
                ha="left",
            )

    ax.set_xticks([0, 500, 1000, 1500, 2000])
    ax.set_xlim(-80.0, H_MAX_M * 1.04)
    ax.set_xlabel("標高 [m]")

    ax.set_yscale("log")
    ax.set_ylim(y_lo, y_hi)
    ax.yaxis.set_major_locator(FixedLocator(y_ticks))
    ax.yaxis.set_major_formatter(FuncFormatter(_format_log_tick))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.grid(True, axis="both", linestyle="--", alpha=0.35)

    ax.set_ylabel("フラックス Φ [cm$^{-2}$ s$^{-1}$]（片対数）")
    ax.set_title("昨年度9班：熱中性子・MeV フラックス（地上・理論直線）")
    ax.legend(frameon=False, loc="upper left", borderaxespad=0.5)

    out = OUT / "01_昨年_熱MeV_絶対_地上のみ.png"
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight", pad_inches=0.10)
    plt.close(fig)
    print(
        f"saved {out}  "
        f"(λ_air th/MeV={LAM_THERMAL_AIR_M:.0f}/{LAM_MEV_AIR_M:.0f} m, "
        f"A0 th/MeV={a0_th:.2e}/{a0_mev:.2e})"
    )


def main() -> None:
    _plot_combined(logy=False)
    _plot_combined(logy=True)
    _plot_air_only()


if __name__ == "__main__":
    main()
