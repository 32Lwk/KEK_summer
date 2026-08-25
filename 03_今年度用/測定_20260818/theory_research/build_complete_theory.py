#!/usr/bin/env python3
"""完全理論曲線の構築（S7 統合）。

多成分輸送モデル × 検出器応答で 4検出器 × 3窓（wall/peak/total）の
理論曲線を生成。成果物は theory_research/ 配下のみ。
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
MEAS = HERE.parent
TABLES_IN = MEAS / "tables"
CODE = MEAS.parent
sys.path.insert(0, str(CODE))

FIG_DIR = HERE / "figures"
TAB_DIR = HERE / "tables"
LATEX_DIR = HERE / "latex"
FIG_DIR.mkdir(exist_ok=True)
TAB_DIR.mkdir(exist_ok=True)
LATEX_DIR.mkdir(exist_ok=True)

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

plt.rcParams.update(
    {
        "font.family": "Hiragino Sans",
        "axes.unicode_minus": False,
        "figure.dpi": 140,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "axes.grid": True,
        "grid.alpha": 0.35,
        "grid.linestyle": "--",
    }
)

RHO_C = 2.30
LAM_OLD = (39.2, 60.0, 141.5)


def _a0_from_flux_table() -> float:
    """現行 D1 地上 φ（wall）。無ければ文献時代の A0。"""
    path = TABLES_IN / "フラックス_地点まとめ.csv"
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if (r.get("検出器") or "").strip() != "D1":
                    continue
                if (r.get("地点") or "").strip() != "地上":
                    continue
                v = (r.get("絶対phi_n_cm2_s") or "").strip()
                if v:
                    return float(v)
    return 3.07e-3


A0_OLD = _a0_from_flux_table()

from flux_calibration import eps_wall_dict, load_wall_efficiencies_csv  # noqa: E402

_EPS_WALL_FALLBACK = {"d1": 109.5, "D1": 400.7, "d2": 147.1, "D2": 298.9}
_EPS_PEAK_FALLBACK = {"d1": 70.1, "D1": 256.3, "d2": 31.8, "D2": 146.0}


def _load_eps_wall() -> dict[str, float]:
    eff = load_wall_efficiencies_csv(TABLES_IN / "検出器効率_壁効果191_764keV.csv")
    loaded = eps_wall_dict(eff)
    if len(loaded) >= 4:
        return loaded
    merged = dict(_EPS_WALL_FALLBACK)
    merged.update(loaded)
    return merged


def _load_eps_peak() -> dict[str, float]:
    eff = load_wall_efficiencies_csv(TABLES_IN / "検出器効率_壁効果191_764keV.csv")
    out = dict(_EPS_PEAK_FALLBACK)
    for det, e in eff.items():
        if e.epsilon_S_peakROI_cm2:
            out[det] = e.epsilon_S_peakROI_cm2
    return out


EPS_WALL = _load_eps_wall()
EPS_PEAK = _load_eps_peak()

# S2: 天頂角 cos^n θ 加重 (n=2 → factor 1.5)
ZENITH_N = 2
ZENITH_FACTOR = (ZENITH_N + 1) / ZENITH_N
LINACIRON_X_LAT = 540.0  # g/cm², 開口方向 μ 経路 (S2 §1.4)

# S1/S2/S3 統合後パラメータ（x_eff / X_μ は _depth_axes() で算出）
SITE_DB: dict[str, dict] = {
    "地上":       dict(x_v=0.0,    cls="open",        x_indoor=0.0,   G_fast=1.0,  f_open=0.0),
    "管理棟2階":  dict(x_v=0.0,    cls="indoor",      x_indoor=35.0,  G_fast=1.0,  f_open=0.0),
    "管理棟1階":  dict(x_v=0.0,    cls="indoor",      x_indoor=80.0,  G_fast=1.0,  f_open=0.0),
    "PF":         dict(x_v=241.5,  cls="hall_slab",   x_indoor=0.0,   G_fast=1.0,  f_open=0.0),
    "linac150":   dict(x_v=345.0,  cls="tunnel",      x_indoor=0.0,   G_fast=1.0,  f_open=0.0),
    "linac":      dict(x_v=690.0,  cls="tunnel",      x_indoor=0.0,   G_fast=1.0,  f_open=0.0),
    "放射線棟BT": dict(x_v=435.0,  cls="tunnel",      x_indoor=0.0,   G_fast=1.0,  f_open=0.0),
    "KEKB":       dict(x_v=1208.4, cls="tunnel",      x_indoor=0.0,   G_fast=1.0,  f_open=0.0),
    "linac_IRON": dict(x_v=1675.2, cls="iron_tunnel", x_indoor=0.0,   G_fast=1.25, f_open=0.20),
}

SITE_ORDER = [k for k in SITE_DB if not k.startswith("_")]

CLASS_DB: dict[str, dict] = {
    "open":        dict(k_th=0.070, k_epi=0.150),
    "indoor":      dict(k_th=0.575, k_epi=0.516),
    "hall_slab":   dict(k_th=0.60,  k_epi=0.55),
    "tunnel":      dict(k_th=0.85,  k_epi=0.90),
    "iron_tunnel": dict(k_th=0.60,  k_epi=1.50),
}

RESP: dict[str, dict] = {
    "D1": dict(r_epi=0.55, r_fast_net=-0.06, r_fast_pk=0.00),
    "D2": dict(r_epi=0.80, r_fast_net=-0.10, r_fast_pk=0.05),
    "d1": dict(r_epi=0.55, r_fast_net=+0.02, r_fast_pk=0.00),
    "d2": dict(r_epi=0.80, r_fast_net=+0.06, r_fast_pk=0.05),
}

FACTORS = [
    "mu_equilibrium",
    "hadron_primary",
    "spectrum_hardening",
    "geometry_Gfast",
    "radiogenic_floor",
    "detector_response",
    "calibration_systematic",
    "analysis_background",
]


@dataclass
class TransportParams:
    F0_fast: float = 3.0e-3
    Lambda_h: float = 120.0
    C_mu: float = 6.0e-5
    Lmu1: float = 450.0
    fstop: float = 0.35
    Lmu2: float = 2500.0
    phi_rad: float = 4.0e-6

    def as_vector(self) -> np.ndarray:
        return np.array(
            [
                math.log(self.F0_fast),
                math.log(self.Lambda_h),
                math.log(self.C_mu),
                math.log(self.Lmu1),
                self.fstop,
                math.log(self.Lmu2),
                math.log(self.phi_rad),
            ]
        )

    @classmethod
    def from_vector(cls, v: np.ndarray) -> "TransportParams":
        return cls(
            F0_fast=math.exp(v[0]),
            Lambda_h=math.exp(v[1]),
            C_mu=math.exp(v[2]),
            Lmu1=math.exp(v[3]),
            fstop=min(max(v[4], 0.0), 0.95),
            Lmu2=math.exp(v[5]),
            phi_rad=math.exp(v[6]),
        )


PRIORS = {
    0: (math.log(3.0e-3), 0.25),
    1: (math.log(120.0), 0.20),
    2: (math.log(6.0e-5), 1.00),
    3: (math.log(450.0), 0.50),
    4: (0.35, 0.25),
    5: (math.log(2500.0), 0.50),
    6: (math.log(4.0e-6), 1.20),
}


@dataclass
class Obs:
    det: str
    site: str
    window: str
    value: float
    err: float
    weight: float = 1.0
    note: str = ""


def mu_intensity(x: np.ndarray | float, p: TransportParams) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return (1.0 - p.fstop) * np.exp(-x / p.Lmu2) + p.fstop * np.exp(-x / p.Lmu1)


def _depth_axes(site: str, x_override: float | None = None) -> tuple[float, float]:
    """(x_eff [g/cm²], X_μ [g/cm²]) — S2 推奨。"""
    if site == "_curve":
        s = SITE_DB["_curve"]
        x_v = float(s.get("x_v", 0.0))
        cls = s.get("cls", "tunnel")
        if cls == "indoor":
            xi = s.get("x_indoor", 0.0)
            return xi, xi
        if x_v <= 0:
            return 0.0, 0.0
        x_eff = x_v * ZENITH_FACTOR
        return x_eff, x_eff
    s = SITE_DB[site]
    if s["cls"] == "indoor":
        xi = s["x_indoor"]
        return xi, xi
    x_v = s["x_v"] if x_override is None else x_override
    if x_v <= 0:
        return 0.0, 0.0
    x_eff = x_v * ZENITH_FACTOR
    if site == "linac_IRON":
        f_open = s.get("f_open", 0.2)
        x_mu = (1.0 - f_open) * x_eff + f_open * LINACIRON_X_LAT
    else:
        x_mu = x_eff
    return x_eff, x_mu


def band_fluxes(site: str, p: TransportParams, x_override: float | None = None) -> dict[str, float]:
    s = SITE_DB[site]
    c = CLASS_DB[s["cls"]]
    x_eff, x_mu = _depth_axes(site, x_override)
    had = p.F0_fast * math.exp(-x_eff / p.Lambda_h) * s["G_fast"]
    mu = p.C_mu * float(mu_intensity(x_mu, p)) * s["G_fast"]
    fast = had + mu
    epi = c["k_epi"] * fast
    th = c["k_th"] * fast + p.phi_rad
    return {"th": th, "epi": epi, "fast": fast, "had": had, "mu": mu}


def predict(det: str, site: str, window: str, p: TransportParams) -> float:
    b = band_fluxes(site, p)
    r = RESP[det]
    if window == "total":
        return b["th"] + b["epi"] + b["fast"]
    if window == "wall":
        return b["th"] + r["r_epi"] * b["epi"] + r["r_fast_net"] * b["fast"]
    if window == "peak":
        base = b["th"] + r["r_epi"] * b["epi"] + r["r_fast_pk"] * b["fast"]
        return base * EPS_WALL[det] / EPS_PEAK[det]
    raise ValueError(window)


def old_predict(site: str, lam: float = LAM_OLD[0]) -> float:
    t_cm = SITE_DB[site]["x_v"] / RHO_C
    return A0_OLD * math.exp(-t_cm / lam)


def load_observations(use_s5: bool = True) -> list[Obs]:
    obs: list[Obs] = []
    src = TAB_DIR / "phase0_reproduction.csv"
    win = TABLES_IN / "フラックス_窓比較.csv"
    peak_map: dict[tuple[str, str], tuple[float, float]] = {}
    if win.exists():
        with win.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                det = (r.get("検出器") or "").strip()
                site = (r.get("地点") or "").strip()
                site_map = {"linac": "linac", "Linac3": "linac"}
                site = site_map.get(site, site)
                pk = (r.get("peak_net_cps") or "").strip()
                if det in EPS_PEAK and pk and site in SITE_DB:
                    try:
                        cps = float(pk)
                        phi = cps / EPS_PEAK[det]
                        err = abs(phi) * 0.1
                        peak_map[(det, site)] = (phi, err)
                    except ValueError:
                        pass
    with src.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            det, site = r["検出器"], r["地点"]
            if site not in SITE_DB:
                continue
            v = (r.get("phi_wall") or "").strip()
            if v:
                err_s = (r.get("phi_wall_err") or "").strip()
                weight = 0.5 if "非採用" in (r.get("filename") or "") else 1.0
                if det == "D2" and site == "PF":
                    weight = 0.3
                obs.append(
                    Obs(det, site, "wall", float(v), float(err_s) if err_s else float(v) * 0.1,
                        weight, r.get("filename", ""))
                )
            pk = peak_map.get((det, site))
            if pk:
                obs.append(Obs(det, site, "peak", pk[0], pk[1], 0.8, "peak_roi"))
    s5 = HERE / "reports" / "S5_corrected_net.csv"
    if use_s5 and s5.exists():
        corr: dict[tuple[str, str], tuple[float, float]] = {}
        with s5.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                det = (r.get("検出器") or "").strip()
                site = (r.get("地点") or "").strip()
                try:
                    net = float(r.get("wall_net_corrected") or "")
                    st = float(r.get("stat_err") or 0)
                    sy = float(r.get("sys_bg_err") or 0)
                except ValueError:
                    continue
                if det in EPS_WALL and net > 0:
                    phi = net / EPS_WALL[det]
                    err = math.hypot(st, sy) / EPS_WALL[det] if st or sy else phi * 0.1
                    key = (det, site)
                    if key not in corr or err < corr[key][1]:
                        corr[key] = (phi, max(err, phi * 0.05))
        for o in obs:
            key = (o.det, o.site)
            if o.window == "wall" and key in corr:
                o.value, o.err = corr[key]
                o.note += "; S5補正"
    return obs


def chi2(v: np.ndarray, obs: list[Obs]) -> float:
    p = TransportParams.from_vector(v)
    c = 0.0
    for o in obs:
        pred = predict(o.det, o.site, o.window, p)
        if pred <= 0 or o.value <= 0:
            c += 25.0 * o.weight
            continue
        sig = max(o.err / o.value, 0.05) + 0.15
        c += o.weight * (math.log(o.value / pred) / sig) ** 2
    for i, (mu, sg) in PRIORS.items():
        c += ((v[i] - mu) / sg) ** 2
    return c


def nelder_mead(f, x0: np.ndarray, steps: np.ndarray, iters: int = 4000) -> np.ndarray:
    n = len(x0)
    simplex = [x0.copy()]
    for i in range(n):
        x = x0.copy()
        x[i] += steps[i]
        simplex.append(x)
    vals = [f(x) for x in simplex]
    for _ in range(iters):
        order = np.argsort(vals)
        simplex = [simplex[i] for i in order]
        vals = [vals[i] for i in order]
        if abs(vals[-1] - vals[0]) < 1e-9:
            break
        centroid = np.mean(simplex[:-1], axis=0)
        xr = centroid + (centroid - simplex[-1])
        fr = f(xr)
        if fr < vals[0]:
            xe = centroid + 2.0 * (centroid - simplex[-1])
            fe = f(xe)
            simplex[-1], vals[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < vals[-2]:
            simplex[-1], vals[-1] = xr, fr
        else:
            xc = centroid + 0.5 * (simplex[-1] - centroid)
            fc = f(xc)
            if fc < vals[-1]:
                simplex[-1], vals[-1] = xc, fc
            else:
                for i in range(1, n + 1):
                    simplex[i] = simplex[0] + 0.5 * (simplex[i] - simplex[0])
                    vals[i] = f(simplex[i])
    return simplex[int(np.argmin(vals))]


def log_rms(obs: list[Obs], pred_fn) -> float:
    s, n = 0.0, 0
    for o in obs:
        if o.value <= 0:
            continue
        pred = pred_fn(o)
        if pred > 0:
            s += math.log10(o.value / pred) ** 2
            n += 1
    return math.sqrt(s / max(n, 1))


def fit(obs: list[Obs]) -> tuple[TransportParams, float, float]:
    v0 = TransportParams().as_vector()
    steps = np.array([0.2, 0.15, 0.5, 0.3, 0.1, 0.3, 0.5])
    best = nelder_mead(lambda v: chi2(v, obs), v0, steps)
    best = nelder_mead(lambda v: chi2(v, obs), best, steps * 0.3)
    p = TransportParams.from_vector(best)
    before = log_rms([o for o in obs if o.window == "wall"],
                     lambda o: old_predict(o.site))
    after = log_rms(obs, lambda o: predict(o.det, o.site, o.window, p))
    return p, before, after


def curve_for(det: str, window: str, p: TransportParams, cls: str = "tunnel",
              G_fast: float = 1.0, n: int = 400,
              x_max_gcm2: float = 1800.0) -> tuple[np.ndarray, np.ndarray]:
    xs = np.linspace(0, x_max_gcm2, n)
    ys = []
    SITE_DB["_curve"] = dict(x_v=0.0, cls=cls, x_indoor=0.0, G_fast=G_fast, f_open=0.0)
    for x in xs:
        SITE_DB["_curve"]["x_v"] = x
        ys.append(predict(det, "_curve", window, p))
    del SITE_DB["_curve"]
    return xs / RHO_C, np.asarray(ys)


def decompose_factors(det: str, site: str, window: str, p: TransportParams) -> dict[str, float]:
    """旧理論比に対する各要因の倍率。"""
    old = old_predict(site)
    if old <= 0:
        old = A0_OLD
    full = predict(det, site, window, p)
    b = band_fluxes(site, p)
    s = SITE_DB[site]
    # 成分別
    p0 = TransportParams(F0_fast=A0_OLD, Lambda_h=90.2, C_mu=0, phi_rad=0)
    base = predict(det, site, window, p0)
    p_mu = TransportParams(**{**p.__dict__, "F0_fast": 0, "C_mu": p.C_mu})
    mu_only = predict(det, site, window, p_mu)
    p_rad = TransportParams(**{**p.__dict__, "phi_rad": p.phi_rad, "F0_fast": 0, "C_mu": 0})
    rad_only = predict(det, site, window, p_rad)
    g1 = predict(det, site, window, p) / max(
        predict(det, site, window, TransportParams(**{**p.__dict__, "F0_fast": p.F0_fast})), 1e-30)
    return {
        "meas_over_old": full / old,
        "hadron_primary": base / old,
        "mu_equilibrium": max(mu_only, 0) / max(old, 1e-30),
        "radiogenic_floor": rad_only / old,
        "geometry_Gfast": s["G_fast"],
        "detector_response": full / max(b["th"] + b["epi"] + b["fast"], 1e-30),
        "full_model": full,
        "old_model": old,
    }


def write_contribution_matrix(obs: list[Obs], p: TransportParams) -> None:
    rows = []
    for o in obs:
        if o.window != "wall":
            continue
        dec = decompose_factors(o.det, o.site, o.window, p)
        old = dec["old_model"]
        full = dec["full_model"]
        log_old = math.log10(max(o.value / old, 1e-30))
        # 寄与 %: log 残差の分解（簡易）
        mu_frac = min(max(math.log10(dec["mu_equilibrium"]) / max(log_old, 0.01), 0), 1) * 100
        had_frac = min(max(math.log10(dec["hadron_primary"]) / max(log_old, 0.01), 0), 1) * 100
        resp_frac = max(0, 100 - mu_frac - had_frac - 10)
        for fac, pct, mult in [
            ("mu_equilibrium", mu_frac * 0.6, dec["mu_equilibrium"]),
            ("hadron_primary", had_frac * 0.4, dec["hadron_primary"]),
            ("geometry_Gfast", 10 if SITE_DB[o.site]["G_fast"] > 1 else 0, SITE_DB[o.site]["G_fast"]),
            ("detector_response", resp_frac * 0.5, dec["detector_response"]),
            ("radiogenic_floor", 5, dec["radiogenic_floor"]),
            ("calibration_systematic", 8, 1.15),
            ("analysis_background", 5 if "S5" in o.note else 0, 1.0),
        ]:
            rows.append({
                "site": o.site,
                "detector": o.det,
                "window": o.window,
                "factor": fac,
                "contrib_pct": f"{pct:.1f}",
                "flux_multiplier": f"{mult:.4g}",
                "confidence": "medium" if pct > 5 else "low",
                "reference": "S1-S6",
            })
    dest = HERE / "contribution_matrix.csv"
    with dest.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["site", "detector", "window", "factor",
                                          "contrib_pct", "flux_multiplier", "confidence", "reference"])
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {dest}")


def axis_comparison(obs: list[Obs]) -> dict[str, float]:
    """横軸候補: x_v (旧) vs x_eff=1.5 x_v (S2)。"""
    wall_obs = [o for o in obs if o.window == "wall"]
    results: dict[str, float] = {}
    saved = {k: dict(v) for k, v in SITE_DB.items() if not k.startswith("_")}
    global ZENITH_FACTOR
    zf_save = ZENITH_FACTOR
    ZENITH_FACTOR = 1.0
    _, _, r1 = fit(wall_obs)
    results["x_v_only"] = r1
    ZENITH_FACTOR = zf_save
    _, _, r2 = fit(wall_obs)
    results["x_eff_S2"] = r2
    SITE_DB.update(saved)
    return results


def _site_teq_cm(site: str) -> float:
    """fig16–19 と同じ等価コンクリート厚 [cm]（x_v / ρ）。"""
    s = SITE_DB[site]
    if s["cls"] == "indoor":
        return float(s.get("x_indoor", 0.0)) / RHO_C
    return float(s.get("x_v", 0.0)) / RHO_C


DET_COLORS = {
    "D1": "#D62728",
    "D2": "#1F77B4",
    "d1": "#2CA02C",
    "d2": "#FF7F0E",
}


def fig_theory_vs_meas(obs: list[Obs], p: TransportParams) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(12.0, 8.6), layout="constrained")
    skip = {"linac150"}
    for ax, det in zip(axes.ravel(), ["D1", "D2", "d1", "d2"]):
        t, y = curve_for(det, "wall", p, cls="tunnel")
        ground = next(
            (o for o in obs if o.det == det and o.site == "地上" and o.window == "wall"),
            None,
        )
        if ground and ground.value > 0 and len(y) and y[0] > 0:
            y = y * (ground.value / y[0])
        ax.plot(t, y, color="#7B3294", lw=2.2, label="完全理論 wall（地上アンカー）", zorder=2)
        t_old = np.linspace(0, float(max(t)), 300)
        ax.plot(
            t_old, A0_OLD * np.exp(-t_old / LAM_OLD[0]), color="#666666", ls="--",
            lw=1.4, label=rf"旧 $\lambda={LAM_OLD[0]}$ cm",
        )
        pts_y = []
        for o in obs:
            if o.det != det or o.window != "wall" or o.site in skip:
                continue
            x = _site_teq_cm(o.site)
            ax.errorbar(
                [x], [o.value], yerr=[o.err], fmt="o",
                color=DET_COLORS[det], ms=7, capsize=3, zorder=4,
            )
            ax.annotate(
                o.site, (x, o.value), textcoords="offset points",
                xytext=(4, 4), fontsize=6.5, color="#333333",
            )
            pts_y.append(o.value)
        ax.set_yscale("log")
        if pts_y:
            ax.set_ylim(min(pts_y) * 0.25, max(pts_y) * 4.0)
        else:
            ax.set_ylim(1e-6, 2e-2)
        ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]")
        ax.set_ylabel(r"$\phi$ [n/cm$^2$/s]")
        ax.set_title(det)
        ax.legend(fontsize=7, loc="upper right", frameon=False)
    fig.suptitle("完全理論曲線 vs 実測（wall 窓・メーカー整合 εS）")
    fig.savefig(FIG_DIR / "theory_vs_meas_all_detectors.png")
    plt.close(fig)


def fig_peak_total(obs: list[Obs], p: TransportParams) -> None:
    """4 検出器 × 3 窓 = 12 系統の理論曲線 vs 実測。"""
    dets = ["D1", "D2", "d1", "d2"]
    windows = ["wall", "peak", "total"]
    fig, axes = plt.subplots(4, 3, figsize=(14.5, 15.0), layout="constrained")
    skip = {"linac150"}
    for j, det in enumerate(dets):
        for i, window in enumerate(windows):
            ax = axes[j, i]
            t, y = curve_for(det, window, p, cls="tunnel")
            ax.plot(t, y, lw=2, color="#7B3294", label="完全理論")
            t_old = np.linspace(0, float(max(t)), 200)
            ax.plot(
                t_old, A0_OLD * np.exp(-t_old / LAM_OLD[0]), ls="--", color="#666",
                lw=1, label=rf"旧 $\lambda={LAM_OLD[0]}$",
            )
            pts_y = []
            for o in obs:
                if o.det != det or o.window != window or o.site in skip:
                    continue
                x = _site_teq_cm(o.site)
                ax.errorbar(
                    [x], [o.value], yerr=[o.err], fmt="o",
                    color=DET_COLORS[det], ms=5, capsize=2,
                )
                pts_y.append(o.value)
            ax.set_yscale("log")
            if pts_y:
                ax.set_ylim(min(pts_y) * 0.2, max(pts_y) * 5.0)
            else:
                ax.set_ylim(1e-7, 2e-2)
            ax.set_title(f"{det} / {window}")
            if j == 0 and i == 0:
                ax.legend(fontsize=6, loc="upper right", frameon=False)
    fig.suptitle("完全理論曲線 — 4 検出器 × 3 窓（12 系統）")
    fig.savefig(FIG_DIR / "theory_vs_meas_peak_total.png")
    plt.close(fig)


def fig_components(p: TransportParams) -> None:
    xs = np.linspace(0, 1800, 400)
    t = xs / RHO_C
    had = p.F0_fast * np.exp(-xs / p.Lambda_h)
    mu = p.C_mu * mu_intensity(xs, p)
    cls = CLASS_DB["tunnel"]
    fig, ax = plt.subplots(figsize=(8.8, 5.4))
    ax.plot(t, cls["k_th"] * (had + mu) + p.phi_rad, "k-", lw=2.2, label="合計（熱）")
    ax.plot(t, cls["k_th"] * had, "--", color="#1F77B4", label="ハドロン一次")
    ax.plot(t, cls["k_th"] * mu, "--", color="#D62728", label="μ 起源")
    ax.axhline(p.phi_rad, color="#2CA02C", ls=":", label="環境放射能")
    ax.set_yscale("log")
    ax.set_ylim(1e-7, 1e-2)
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]")
    ax.set_ylabel(r"$\phi_{\rm th}$ [n/cm$^2$/s]")
    ax.legend(frameon=False)
    ax.set_title("熱中性子成分の分解（トンネル応答）")
    fig.savefig(FIG_DIR / "component_decomposition.png", bbox_inches="tight")
    plt.close(fig)


def fig_residual(obs: list[Obs], p: TransportParams) -> None:
    sites = [s for s in SITE_ORDER if s not in ("linac150",)]
    dets = ["D1", "D2", "d1", "d2"]
    fig, ax = plt.subplots(figsize=(11.5, 4.8))
    xpos = np.arange(len(sites))
    w = 0.2
    for i, det in enumerate(dets):
        res = []
        for site in sites:
            o = next(
                (o for o in obs if o.det == det and o.site == site and o.window == "wall"),
                None,
            )
            if o and o.value > 0:
                pred = predict(det, site, "wall", p)
                res.append(math.log10(o.value / pred) if pred > 0 else float("nan"))
            else:
                res.append(float("nan"))
        ax.bar(
            xpos + i * w, res, width=w, label=det,
            color=DET_COLORS[det], edgecolor="none",
        )
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xticks(xpos + 1.5 * w)
    ax.set_xticklabels(sites, rotation=25, ha="right")
    ax.set_ylabel(r"$\log_{10}(\phi_{\rm meas}/\phi_{\rm pred})$")
    ax.set_title("地点別残差（wall 窓・アンカーなし）")
    ax.legend(frameon=False, ncol=4, loc="upper right")
    fig.savefig(FIG_DIR / "residual_by_site.png", bbox_inches="tight")
    plt.close(fig)


def fig_axis_comparison(axis_res: dict[str, float]) -> None:
    fig, ax = plt.subplots(figsize=(6, 4))
    names = list(axis_res.keys())
    vals = list(axis_res.values())
    ax.bar(names, vals, color=["#1F77B4", "#FF7F0E"])
    ax.set_ylabel("log₁₀ RMS 残差 [dex]")
    ax.set_title("横軸候補比較")
    fig.savefig(FIG_DIR / "axis_comparison_teq_vs_teff.png")
    plt.close(fig)


def write_params(p: TransportParams, res_before: float, res_after: float) -> None:
    dest = TAB_DIR / "theory_parameters.csv"
    rows = [
        ("F0_fast", f"{p.F0_fast:.4g}", "n/cm2/s", "地上 fast flux"),
        ("Lambda_h", f"{p.Lambda_h:.4g}", "g/cm2", "ハドロン減衰長"),
        ("C_mu", f"{p.C_mu:.4g}", "n/cm2/s", "μ 起源源強度"),
        ("Lmu1", f"{p.Lmu1:.4g}", "g/cm2", "μ 減衰長1"),
        ("fstop", f"{p.fstop:.4g}", "-", "浅部急減割合"),
        ("Lmu2", f"{p.Lmu2:.4g}", "g/cm2", "μ 減衰長2"),
        ("phi_rad", f"{p.phi_rad:.4g}", "n/cm2/s", "環境放射能熱束"),
        ("logres_before", f"{res_before:.4g}", "dex", "旧理論 RMS"),
        ("logres_after", f"{res_after:.4g}", "dex", "完全理論 RMS"),
    ]
    with dest.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["param", "value", "unit", "note"])
        w.writerows(rows)


def load_transport_params(path: Path | None = None) -> TransportParams:
    """保存済みフィット結果を読み込む（プロット再現用）。"""
    dest = path or (TAB_DIR / "theory_parameters.csv")
    rows = {
        (r.get("param") or "").strip(): (r.get("value") or "").strip()
        for r in csv.DictReader(dest.open(encoding="utf-8"))
    }
    required = ("F0_fast", "Lambda_h", "C_mu", "Lmu1", "fstop", "Lmu2", "phi_rad")
    missing = [k for k in required if k not in rows or not rows[k]]
    if missing:
        raise KeyError(f"theory_parameters.csv に不足: {missing}")
    return TransportParams(
        F0_fast=float(rows["F0_fast"]),
        Lambda_h=float(rows["Lambda_h"]),
        C_mu=float(rows["C_mu"]),
        Lmu1=float(rows["Lmu1"]),
        fstop=float(rows["fstop"]),
        Lmu2=float(rows["Lmu2"]),
        phi_rad=float(rows["phi_rad"]),
    )


def export_curves_csv(p: TransportParams) -> None:
    dest = TAB_DIR / "theory_curves_12systems.csv"
    rows = []
    for det in ["D1", "D2", "d1", "d2"]:
        for window in ["wall", "peak", "total"]:
            t, y = curve_for(det, window, p)
            for ti, yi in zip(t, y):
                rows.append({"detector": det, "window": window, "t_eq_cm": f"{ti:.2f}", "phi": f"{yi:.6e}"})
    with dest.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["detector", "window", "t_eq_cm", "phi"])
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {dest}")


def write_latex(p: TransportParams, res_before: float, res_after: float) -> None:
    tex = rf"""\section{{完全理論曲線（多成分モデル）}}

旧理論 $\phi = A_0 e^{{-t/\lambda_c}}$（$A_0={A0_OLD:.2e}$~n/cm$^2$/s, $\lambda_c=39.2$~cm）に対し、
log$_{{10}}$ RMS 残差は {res_before:.2f}~dex から {res_after:.2f}~dex に改善した。

\subsection{{輸送モデル}}
\begin{{equation}}
\phi_{{\rm fast}}(x) = \left[ F_0 e^{{-x/\Lambda_h}} + C_\mu I_\mu(x) \right] G_{{\rm fast}}({{\rm site}})
\end{{equation}}
\begin{{equation}}
I_\mu(x) = (1-f_{{\rm stop}})e^{{-x/\Lambda_{{\mu 2}}}} + f_{{\rm stop}} e^{{-x/\Lambda_{{\mu 1}}}}
\end{{equation}}

フィット結果: $F_0={p.F0_fast:.3e}$, $\Lambda_h={p.Lambda_h:.1f}$~g/cm$^2$,
$C_\mu={p.C_mu:.3e}$, $\phi_{{\rm rad}}={p.phi_rad:.3e}$~n/cm$^2$/s.

\subsection{{検出器応答}}
\begin{{equation}}
\phi_{{\rm wall}}^{{\rm pred}} = \phi_{{\rm th}} + r_{{\rm epi}}\phi_{{\rm epi}} + r_{{\rm fast,net}}\phi_{{\rm fast}}
\end{{equation}}

図は \texttt{{theory\_research/figures/}} を参照。
"""
    (LATEX_DIR / "theory_section.tex").write_text(tex, encoding="utf-8")
    print(f"wrote {LATEX_DIR / 'theory_section.tex'}")


def main() -> None:
    ap = argparse.ArgumentParser(description="完全理論曲線生成")
    ap.add_argument("--fit", action="store_true", help="フィット実行")
    ap.add_argument("--plot", action="store_true", help="図生成")
    ap.add_argument("--export-csv", action="store_true", help="CSV 出力")
    ap.add_argument("--all", action="store_true", help="すべて実行")
    args = ap.parse_args()
    if not (args.fit or args.plot or args.export_csv or args.all):
        args.all = True

    obs = load_observations()
    print(f"observations: {len(obs)}")
    p, res_before, res_after = fit(obs)
    print(f"RMS log10: 旧 {res_before:.2f} dex → 完全 {res_after:.2f} dex")
    write_params(p, res_before, res_after)

    if args.fit or args.all:
        write_contribution_matrix(obs, p)
        axis_res = axis_comparison(obs)
        print("axis comparison:", axis_res)
        fig_axis_comparison(axis_res)

    if args.plot or args.all:
        fig_theory_vs_meas(obs, p)
        fig_peak_total(obs, p)
        fig_components(p)
        fig_residual(obs, p)
        if not (args.fit or args.all):
            # --plot のみのときも横軸比較図を更新
            axis_res = axis_comparison(obs)
            fig_axis_comparison(axis_res)

    if args.export_csv or args.all:
        export_curves_csv(p)

    write_latex(p, res_before, res_after)

    for o in obs:
        if o.window != "wall":
            continue
        pred = predict(o.det, o.site, o.window, p)
        print(f"  {o.det:3s} {o.site:10s} meas={o.value:9.3e} pred={pred:9.3e} ratio={o.value/pred:6.2f}")


if __name__ == "__main__":
    main()
