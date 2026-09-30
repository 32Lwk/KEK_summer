#!/usr/bin/env python3
"""runs/ の PHITS 結果を積算し、線源成分ごとの中性子深さ分布を実測と比べる。

成分の切り分け（μ+ は原子核に捕獲されないことを使う）:
  R        = S(mu-) / S(mu+)          地表の mu-/mu+ フラックス比（線源の重み和）
  高速ミューオン起源 = mup × (1 + R)      核破砕・ミューオン核反応・シャワー光核反応（両符号）
  負ミューオン捕獲   = mum − R × mup
  大気ハドロン起源   = had（宇宙線 n + p）

出力:
  最終レポート_20260925/figures/fig11_phits_components.png
  最終レポート_20260925/figures/fig12_phits_fraction_muflux.png
  results/phits_components_at_sites.csv

実行: python3 analyze.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
REPORT = HERE.parents[1] / "03_今年度用" / "最終レポート_20260925"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPORT))

import make_figures as mf  # noqa: E402
from phits_io import accumulate, group, one_over_v_weight  # noqa: E402
from theory_modufy_curves import components_for  # noqa: E402

RUNS = HERE / "runs"
OUT_FIG = REPORT / "figures"
OUT_TAB = HERE / "results"

ZMIN, DZ = -700.0, 20.0
REBIN = 2
RHO = 2.3
I0_CM2, D0_MWE, GAMMA = 1.0e-2, 11.5, 2.2

N, MUM, MUP, P = 0, 1, 2, 3

COLORS = {
    "had": "#F58518",
    "cap": "#C71585",
    "fast": "#4C78A8",
    "total": "#7B3294",
}
LABELS = {
    "had": "大気由来ハドロン（宇宙線 n, p）",
    "cap": r"負ミューオン捕獲（$\mu^-$ − $\mu^+$）",
    "fast": r"高速ミューオン（核破砕・光核, $\mu^\pm$）",
    "total": "PHITS 合計",
}


def source_total(run: Path) -> float:
    """PARMA から決まった線源の全フラックス [/cm2/s]（revised totfact / pi c1^2）。"""
    m = re.search(r"^\$\s*totfact\s*=\s*(\S+)\s*# revised", (run / "phits.out").read_text(), re.M)
    return abs(float(m.group(1))) / (np.pi * 1600.0**2)


def finished(run: Path) -> bool:
    log = run / "run.log"
    return log.exists() and "finished normally" in log.read_text() and (run / "depth_spec.out").exists()


def load(case: str, region_file: str = "air_spec.out"):
    runs = sorted(r for r in RUNS.glob(f"{case}_s*") if finished(r))
    if not runs:
        raise SystemExit(f"no finished runs for {case}")
    depth = accumulate([r / "depth_spec.out" for r in runs])
    region = accumulate([r / region_file for r in runs])
    src = float(np.mean([source_total(r) for r in runs]))
    return depth, region, src, len(runs)


def tunnel_values(data, lo, hi, weighted):
    """トンネル内（天井 300 cm）の合計。mu+ 分は同じ深さの半無限体系での mu+/mu- 比で足す。"""
    (_, t_had, _, _), (_, t_mum, _, _) = data
    h, hs = (a[0, N] for a in reduce(t_had, lo, hi, weighted))
    m, ms = (a[0, N] for a in reduce(t_mum, lo, hi, weighted))
    return {"had": (h, hs), "mum": (m, ms)}


def rebin(v: np.ndarray, s: np.ndarray, k: int):
    n = (v.shape[0] // k) * k
    off = v.shape[0] - n
    vv = v[off:].reshape(-1, k, *v.shape[1:]).mean(axis=1)
    ss = np.sqrt((s[off:].reshape(-1, k, *s.shape[1:]) ** 2).sum(axis=1)) / k
    return vv, ss


def reduce(tally, lo, hi, weighted=False):
    e_lo, e_hi, val, rel = tally
    w = one_over_v_weight(e_lo, e_hi) if weighted else None
    return group(e_lo, e_hi, val, rel, lo, hi, w)


def components(data, lo, hi, weighted):
    """深さ分布（teq, 成分 dict）と地上（空気中）の成分 dict を返す。"""
    (d_had, a_had, _, _), (d_mum, a_mum, s_mum, _), (d_mup, a_mup, s_mup, _) = data
    r = s_mum / s_mup
    out = {}
    for key, tallies in (("depth", (d_had, d_mum, d_mup)), ("air", (a_had, a_mum, a_mup))):
        (h, hs), (m, ms), (p, ps) = (reduce(t, lo, hi, weighted) for t in tallies)
        h, hs, m, ms, p, ps = h[:, N], hs[:, N], m[:, N], ms[:, N], p[:, N], ps[:, N]
        comp = {
            "had": (h, hs),
            "cap": (m - r * p, np.hypot(ms, r * ps)),
            "fast": (p * (1 + r), ps * (1 + r)),
            "total": (h + m + p, np.sqrt(hs**2 + ms**2 + ps**2)),
        }
        if key == "depth":
            comp = {k: rebin(v, s, REBIN) for k, (v, s) in comp.items()}
        out[key] = comp
    nz = d_had[2].shape[0]
    zc = ZMIN + DZ * (np.arange(nz) + 0.5)
    zc = rebin(zc, np.zeros_like(zc), REBIN)[0]
    return -zc, out["depth"], out["air"], r


def muon_flux(data):
    (_, _, _, _), (d_mum, _, _, _), (d_mup, _, _, _) = data
    v = []
    s = []
    for t, idx in ((d_mum, MUM), (d_mup, MUP)):
        val, err = reduce(t, 1e-10, 1e9)
        v.append(val[:, idx])
        s.append(err[:, idx])
    tot = v[0] + v[1]
    sig = np.hypot(s[0], s[1])
    nz = tot.shape[0]
    zc = ZMIN + DZ * (np.arange(nz) + 0.5)
    return -zc, tot, sig


def draw_panel(ax, teq, comp, air, title, dets, y_lo, y_hi, report_model=None, tunnel=None):
    for key in ("had", "fast", "cap", "total"):
        v, s = comp[key]
        ok = v > 0
        lw = 2.4 if key == "total" else 1.6
        ls = "-" if key in ("total", "cap") else ("--" if key == "fast" else ":")
        ax.plot(teq[ok], v[ok], color=COLORS[key], lw=lw, ls=ls, label=LABELS[key], zorder=3)
        ax.fill_between(teq[ok], np.clip(v - s, 1e-12, None)[ok], (v + s)[ok],
                        color=COLORS[key], alpha=0.15, lw=0, zorder=2)
    ax.errorbar([0.0], [air["total"][0][0]], yerr=[air["total"][1][0]], fmt="*", ms=11,
                color=COLORS["total"], mec="white", zorder=5, label="PHITS 地上（空気中 0.5–2.5 m）")
    if tunnel is not None:
        ax.errorbar([300.0], [tunnel[0]], yerr=[tunnel[1]], fmt="D", ms=8, color=COLORS["total"],
                    mec="white", zorder=5, label="PHITS トンネル内（天井 300 cm, 幅・高さ 3 m）")
    if report_model is not None:
        x_c, y_c = report_model
        ax.plot(x_c, y_c, color="#999999", lw=1.4, ls="-.", label=r"レポートのモデル $f_1+f_2+f_3$", zorder=2)
    by_det = mf._points(mf.pm.load_flux_summary(), dets)
    mf._errorbars(ax, by_det, with_sys=True)
    mf._axes(ax, title, r"中性子フラックス $\phi$ [cm$^{-2}$ s$^{-1}$]", y_lo, y_hi, 600.0)
    mf._annotate(ax, by_det)
    ax.legend(frameon=True, framealpha=0.92, fontsize=8.5, loc="lower left")
    return by_det


SITE_HALF_WIDTH_CM = 40.0


def site_value(x, teq, comp):
    """teq±40 cm のビン平均（成分ごとに同じビンを使うので合計と内訳が整合する）。"""
    m = np.abs(teq - x) <= SITE_HALF_WIDTH_CM
    return {k: float(v[m].mean()) for k, (v, _) in comp.items()}


def main() -> None:
    mf.pm.FLUX_SUMMARY_CSV = mf.FLUX_CSV
    data = [load(c) for c in ("had", "mum", "mup")]
    for c, d in zip(("had", "mum", "mup"), data):
        print(f"{c}: {d[3]} runs, source total = {d[2]:.4e} /cm2/s")

    th = components(data, 1e-10, 1e9, weighted=True)
    fa = components(data, 0.1, 20.0, weighted=False)
    print(f"mu-/mu+ = {th[3]:.3f}")

    tdata = [load("hadT", "tunnel_spec.out"), load("mumT", "tunnel_spec.out")]
    print(f"tunnel: hadT {tdata[0][3]} runs, mumT {tdata[1][3]} runs")
    tunnel = {}
    tunnel_rows = []
    for kind, lo, hi, wtd in (("熱", 1e-10, 1e9, True), ("MeV", 0.1, 20.0, False)):
        tv = tunnel_values(tdata, lo, hi, wtd)
        slab = {}
        for case_idx, key in ((0, "had"), (1, "mum"), (2, "mup")):
            v, s = reduce(data[case_idx][0], lo, hi, wtd)
            teq = -(ZMIN + DZ * (np.arange(v.shape[0]) + 0.5))
            for name, m in (("天井300", np.abs(teq - 300.0) <= SITE_HALF_WIDTH_CM),
                            ("300-600平均", (teq >= 300.0) & (teq <= 600.0))):
                slab[(key, name)] = float(v[m, N].mean())
        mup_over_mum = slab[("mup", "300-600平均")] / slab[("mum", "300-600平均")]
        tot = tv["had"][0] + tv["mum"][0] * (1 + mup_over_mum)
        tot_s = np.hypot(tv["had"][1], tv["mum"][1] * (1 + mup_over_mum))
        tunnel[kind] = (tot, tot_s)
        for key in ("had", "mum"):
            tunnel_rows.append({
                "種類": kind, "線源": key,
                "トンネル内": f"{tv[key][0]:.3e}", "トンネル内_誤差": f"{tv[key][1]:.1e}",
                "コンクリート中_天井300": f"{slab[(key, '天井300')]:.3e}",
                "コンクリート中_300-600平均": f"{slab[(key, '300-600平均')]:.3e}",
                "トンネル/コンクリート中300-600": f"{tv[key][0] / slab[(key, '300-600平均')]:.2f}",
            })
        print(f"tunnel total {kind}: {tot:.3e} ± {tot_s:.1e}")

    OUT_FIG.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(15.0, 6.0))
    x_c = np.linspace(0.0, 600.0, 400)
    f1, f2, f3 = components_for("mev", x_c)
    pts_th = draw_panel(axes[0], th[0], th[1], th[2], r"熱中性子（裸管 D1, d1 ／ PHITS は $1/v$ 重み）",
                        ("D1", "d1"), 1e-7, 1e-2, tunnel=tunnel["熱"])
    pts_fa = draw_panel(axes[1], fa[0], fa[1], fa[2], "MeV 中性子（PE 付き D2, d2 ／ PHITS は 0.1–20 MeV）",
                        ("D2", "d2"), 1e-7, 1e-2, report_model=(x_c, f1 + f2 + f3), tunnel=tunnel["MeV"])
    fig.tight_layout()
    p11 = OUT_FIG / "fig11_phits_components.png"
    fig.savefig(p11, bbox_inches="tight")
    plt.close(fig)
    print(p11)

    fig, axes = plt.subplots(1, 2, figsize=(14.0, 5.2))
    ax = axes[0]
    for (teq, comp, _, _), lab, col in ((th, "熱中性子（1/v 重み）", "#E45756"), (fa, "MeV 中性子（0.1–20 MeV）", "#4C78A8")):
        tot = comp["total"][0]
        mu = comp["cap"][0] + comp["fast"][0]
        cap = comp["cap"][0]
        ok = tot > 0
        ax.plot(teq[ok], (mu / tot)[ok], color=col, lw=2.2, label=f"{lab}：ミューオン起源の割合")
        ax.plot(teq[ok], (cap / tot)[ok], color=col, lw=1.4, ls="--", label=f"{lab}：うち負ミューオン捕獲")
    ax.set_ylim(0, 1.05)
    ax.set_xlim(0, 600)
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]")
    ax.set_ylabel("PHITS 合計に占める割合")
    ax.set_title("中性子のうちミューオン起源の割合（PHITS）", fontsize=12)
    ax.legend(fontsize=8.5, loc="lower right")

    ax = axes[1]
    teq_mu, mu, mus = muon_flux(data)
    ax.errorbar(teq_mu, mu, yerr=mus, fmt="o", ms=3, color="#333333", label=r"PHITS $\mu^+ + \mu^-$（コンクリート中）")
    d = RHO * teq_mu / 100.0
    ax.plot(teq_mu, I0_CM2 * (1 + d / D0_MWE) ** (-GAMMA), color="#C71585", lw=1.8,
            label=r"レポートの $I_\mu(d)=I_0(1+d/d_0)^{-\gamma}$")
    ax.set_yscale("log")
    ax.set_xlim(0, 700)
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]")
    ax.set_ylabel(r"ミューオンフラックス [cm$^{-2}$ s$^{-1}$]")
    ax.set_title("地下のミューオンフラックス", fontsize=12)
    ax.legend(fontsize=9)
    fig.tight_layout()
    p12 = OUT_FIG / "fig12_phits_fraction_muflux.png"
    fig.savefig(p12, bbox_inches="tight")
    plt.close(fig)
    print(p12)

    OUT_TAB.mkdir(parents=True, exist_ok=True)
    rows = []
    for kind, res, pts in (("熱", th, pts_th), ("MeV", fa, pts_fa)):
        teq, comp, air, _ = res
        for det, plist in pts.items():
            for pt in plist:
                x = pt["x"]
                if x < 1.0:
                    vals = {k: air[k][0][0] for k in comp}
                else:
                    vals = site_value(x, teq, comp)
                tot = vals["total"]
                rows.append({
                    "種類": kind, "検出器": det, "地点": pt.get("label") or pt.get("site"),
                    "teq_cm": f"{x:.0f}", "実測": f"{pt['y']:.3e}",
                    "PHITS_大気ハドロン": f"{vals['had']:.3e}", "PHITS_負μ捕獲": f"{vals['cap']:.3e}",
                    "PHITS_高速μ": f"{vals['fast']:.3e}", "PHITS_合計": f"{tot:.3e}",
                    "実測/PHITS": f"{pt['y'] / tot:.2f}",
                    "μ起源の割合": f"{(vals['cap'] + vals['fast']) / tot:.2f}",
                    "うち捕獲の割合": f"{vals['cap'] / tot:.2f}",
                })
    out_csv = OUT_TAB / "phits_components_at_sites.csv"
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(out_csv)
    out_t = OUT_TAB / "phits_tunnel_vs_slab.csv"
    with out_t.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(tunnel_rows[0]))
        w.writeheader()
        w.writerows(tunnel_rows)
    print(out_t)


if __name__ == "__main__":
    main()
