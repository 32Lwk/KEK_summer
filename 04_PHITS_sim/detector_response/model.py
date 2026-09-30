#!/usr/bin/env python3
"""PHITS に基づく深さ依存モデルを実測の計数率に当てはめる。

各地点・各検出器の予測計数率（peak ROI）を
    R_pred = k_type × (H + r × M)
と書く。H は大気由来ハドロン、M はミューオン起源（負ミューオン捕獲＋高速ミューオン）による
予測計数率で、PHITS の中性子スペクトルと検出器の応答関数から求める（fold.py）。
  k_type : 検出器の種類（裸管 / PE 付き管）ごとの規格化（絶対較正と周囲の環境の違いを吸収）
  r      : ミューオン起源の成分の倍率（PHITS そのままなら 1）

地点の値は地点モデル（部屋を持つ積層体系、Linac3 はトンネル）から求める（site_predictions）。
地上は地面の模型が粗いので当てはめから除く。

出力: results/model_fit.csv, results/model_points.csv,
      最終レポート_20260925/figures/fig13_phits_model.png
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
REPORT = HERE.parents[1] / "03_今年度用" / "最終レポート_20260925"
sys.path.insert(0, str(REPORT))

import fold as fd  # noqa: E402
from resp_io import DET_ORDER  # noqa: E402

SYS_REL = 0.10
TYPE = {"D1": "bare", "d1": "bare", "D2": "pe", "d2": "pe"}
ES_PEAK = {"D1": 256.3, "d1": 70.05, "D2": 178.5, "d2": 33.06}
ROOM_SITES = {"テストホール": "TH", "PF": "PF", "放射線棟BT": "BT", "PS": "PS", "KEKB": "KEKB"}


def site_predictions(e_tab, r_tab, soil: str = "wet", linac3_teq: float = 300.0):
    """(det, site) -> {'H': (v, s), 'M': (v, s), 'src': 'room'|'tunnel'|'slab'}（peak ROI の計数率）。

    部屋の地点モデルがある地点はそれを使う。Linac3 は天井 300 cm のトンネル計算を使い、
    linac3_teq が 300 cm と異なるときはコンクリート中の深さ分布の比で成分ごとに換算する。
    K2K は半無限コンクリート中の値に、PS の部屋/コンクリート中の比を成分ごとに掛ける。"""
    depth, _ = fd.components(fd.MCS / "runs", "depth_spec.out", e_tab, r_tab)
    nz = depth["total"][0].shape[0]
    teq_c = -(-700.0 + 20.0 * (np.arange(nz) + 0.5))
    rooms = {}
    for site, name in ROOM_SITES.items():
        key = "KEKBdry" if (name == "KEKB" and soil == "dry") else name
        try:
            rooms[site] = fd.room_components(key, e_tab, r_tab)
        except SystemExit:
            pass
    tunnel = fd.tunnel_components(e_tab, r_tab)
    if linac3_teq != 300.0:
        a = fd.slab_site_values(depth, teq_c, linac3_teq)
        b = fd.slab_site_values(depth, teq_c, 300.0)
        tunnel = {k: (v * a[k][0] / b[k][0], s * a[k][0] / b[k][0]) for k, (v, s) in tunnel.items()}
    rooms["Linac3"] = tunnel
    if "PS" in rooms:
        a = fd.slab_site_values(depth, teq_c, fd.SITE_TEQ["K2K"])
        b = fd.slab_site_values(depth, teq_c, fd.SITE_TEQ["PS"])
        rooms["K2K"] = {k: (v * a[k][0] / b[k][0], s * a[k][0] / b[k][0]) for k, (v, s) in rooms["PS"].items()}
    out = {}
    for (det, site) in fd.MEASURED:
        if site == "地上":
            continue
        j = DET_ORDER.index(det)
        if site in rooms:
            c = {k: (v[j], s[j]) for k, (v, s) in rooms[site].items()}
            src = "tunnel" if site == "Linac3" else "room"
        else:
            sv = fd.slab_site_values(depth, teq_c, fd.SITE_TEQ[site])
            c = {k: (v[j], s[j]) for k, (v, s) in sv.items()}
            src = "slab"
        h, hs = c["had"]
        m = c["cap"][0] + c["fast"][0]
        ms = np.hypot(c["cap"][1], c["fast"][1])
        out[(det, site)] = {"H": (fd.F_PEAK * h, fd.F_PEAK * hs), "M": (fd.F_PEAK * m, fd.F_PEAK * ms), "src": src}
    return out, depth, teq_c


def fit(points, free_r: bool = True):
    keys = list(points)
    meas = np.array([fd.MEASURED[k][0] for k in keys])
    meas_e = np.array([fd.MEASURED[k][1] for k in keys])
    H = np.array([points[k]["H"][0] for k in keys])
    Hs = np.array([points[k]["H"][1] for k in keys])
    M = np.array([points[k]["M"][0] for k in keys])
    Ms = np.array([points[k]["M"][1] for k in keys])
    is_pe = np.array([TYPE[k[0]] == "pe" for k in keys])

    def model(p):
        kb, kp, r = (p if free_r else (*p, 1.0))
        return np.where(is_pe, kp, kb) * (H + r * M)

    def sigma(p):
        r = p[2] if free_r else 1.0
        pred_rel = np.hypot(Hs, r * Ms) / (H + r * M)
        return np.sqrt((meas_e / meas) ** 2 + pred_rel**2 + SYS_REL**2)

    def resid(p):
        return np.log(meas / model(p)) / sigma(p)

    p0 = [1.0, 1.0, 1.0] if free_r else [1.0, 1.0]
    res = least_squares(resid, p0, bounds=(1e-3, 1e3))
    J = res.jac
    cov = np.linalg.inv(J.T @ J)
    chi2 = float(np.sum(res.fun**2))
    ndf = len(keys) - len(p0)
    return {"p": res.x, "err": np.sqrt(np.diag(cov)), "chi2": chi2, "ndf": ndf,
            "keys": keys, "ratio": meas / model(res.x), "model": model(res.x)}


def fit_offset(points):
    """R = k_type × (H + M) + B_size。B は管の大きさ（大径 D1/D2，小径 d1/d2）ごとの一定の計数率。"""
    keys = list(points)
    meas = np.array([fd.MEASURED[k][0] for k in keys])
    meas_e = np.array([fd.MEASURED[k][1] for k in keys])
    T = np.array([points[k]["H"][0] + points[k]["M"][0] for k in keys])
    Ts = np.array([np.hypot(points[k]["H"][1], points[k]["M"][1]) for k in keys])
    is_pe = np.array([TYPE[k[0]] == "pe" for k in keys])
    is_large = np.array([k[0].isupper() for k in keys])

    def model(p):
        kb, kp, bl, bs = p
        return np.where(is_pe, kp, kb) * T + np.where(is_large, bl, bs)

    def resid(p):
        m = model(p)
        kb, kp = p[0], p[1]
        pred_s = np.where(is_pe, kp, kb) * Ts
        s = np.sqrt((meas_e / meas) ** 2 + (pred_s / m) ** 2 + SYS_REL**2)
        return np.log(meas / m) / s

    res = least_squares(resid, [0.8, 1.0, 0.03, 0.005], bounds=([1e-3, 1e-3, 0.0, 0.0], [1e3, 1e3, 1.0, 1.0]))
    cov = np.linalg.inv(res.jac.T @ res.jac)
    return {"p": res.x, "err": np.sqrt(np.diag(cov)), "chi2": float(np.sum(res.fun**2)),
            "ndf": len(keys) - 4, "keys": keys, "ratio": meas / model(res.x), "model": model(res.x)}


def main() -> None:
    e_tab, r_tab, _ = fd.response_table()
    results = []
    variants = [("標準（土は含水、Linac3=300 cm）", "wet", 300.0),
                ("土を乾燥組成", "dry", 300.0),
                ("Linac3=250 cm", "wet", 250.0)]
    main_points = None
    for label, soil, l3 in variants:
        pts, depth, teq_c = site_predictions(e_tab, r_tab, soil, l3)
        f1 = fit(pts, free_r=False)
        f3 = fit(pts, free_r=True)
        fb = fit_offset(pts)
        results.append((label, f1, f3, fb))
        if main_points is None:
            main_points = (pts, depth, teq_c, f1, f3, fb)
        print(f"[{label}]")
        print(f"  r=1 固定 : k_bare={f1['p'][0]:.2f}±{f1['err'][0]:.2f} k_PE={f1['p'][1]:.2f}±{f1['err'][1]:.2f} "
              f"chi2/ndf={f1['chi2']:.1f}/{f1['ndf']}")
        print(f"  r 自由   : k_bare={f3['p'][0]:.2f}±{f3['err'][0]:.2f} k_PE={f3['p'][1]:.2f}±{f3['err'][1]:.2f} "
              f"r={f3['p'][2]:.2f}±{f3['err'][2]:.2f} chi2/ndf={f3['chi2']:.1f}/{f3['ndf']}")
        print(f"  一定成分 : k_bare={fb['p'][0]:.2f}±{fb['err'][0]:.2f} k_PE={fb['p'][1]:.2f}±{fb['err'][1]:.2f} "
              f"B_large={fb['p'][2]:.4f}±{fb['err'][2]:.4f} B_small={fb['p'][3]:.4f}±{fb['err'][3]:.4f} "
              f"chi2/ndf={fb['chi2']:.1f}/{fb['ndf']}")

    fd.OUT.mkdir(parents=True, exist_ok=True)
    with (fd.OUT / "model_fit.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["条件", "モデル", "k_bare", "k_bare_err", "k_PE", "k_PE_err", "r", "r_err",
                    "B_large", "B_large_err", "B_small", "B_small_err", "chi2", "ndf"])
        for label, f1, f3, fb in results:
            w.writerow([label, "r=1", f"{f1['p'][0]:.3f}", f"{f1['err'][0]:.3f}", f"{f1['p'][1]:.3f}",
                        f"{f1['err'][1]:.3f}", "1", "0", "0", "0", "0", "0", f"{f1['chi2']:.2f}", f1["ndf"]])
            w.writerow([label, "r自由", f"{f3['p'][0]:.3f}", f"{f3['err'][0]:.3f}", f"{f3['p'][1]:.3f}",
                        f"{f3['err'][1]:.3f}", f"{f3['p'][2]:.3f}", f"{f3['err'][2]:.3f}", "0", "0", "0", "0",
                        f"{f3['chi2']:.2f}", f3["ndf"]])
            w.writerow([label, "一定成分", f"{fb['p'][0]:.3f}", f"{fb['err'][0]:.3f}", f"{fb['p'][1]:.3f}",
                        f"{fb['err'][1]:.3f}", "1", "0", f"{fb['p'][2]:.4f}", f"{fb['err'][2]:.4f}",
                        f"{fb['p'][3]:.4f}", f"{fb['err'][3]:.4f}", f"{fb['chi2']:.2f}", fb["ndf"]])

    pts, depth, teq_c, f1, f3, fb = main_points
    with (fd.OUT / "model_points.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["検出器", "地点", "teq_cm", "地点の値", "実測_RNET", "予測_H", "予測_M", "予測_合計",
                    "実測/予測(PHITSそのまま)", "実測/モデル(r=1)", "実測/モデル(r自由)", "実測/モデル(一定成分)",
                    "M/(H+M)"])
        for i, k in enumerate(f3["keys"]):
            H, M = pts[k]["H"][0], pts[k]["M"][0]
            w.writerow([k[0], k[1], f"{fd.SITE_TEQ[k[1]]:.0f}", pts[k]["src"], f"{fd.MEASURED[k][0]:.4f}",
                        f"{H:.4e}", f"{M:.4e}", f"{H + M:.4e}", f"{fd.MEASURED[k][0] / (H + M):.2f}",
                        f"{f1['ratio'][i]:.2f}", f"{f3['ratio'][i]:.2f}", f"{fb['ratio'][i]:.2f}",
                        f"{M / (H + M):.2f}"])
    print(fd.OUT / "model_fit.csv")
    write_tex_rows(pts, f1, f3, fb)
    draw(pts, f1, f3, fb)
    draw_response(e_tab, r_tab)


def write_tex_rows(pts, f1, f3, fb) -> None:
    """レポートの表に貼る行（検出器・地点・体系・実測・予測・比・μ起源の割合・各モデルの比）。"""
    geo = {"room": "部屋", "tunnel": "トンネル", "slab": "コンクリート中"}
    name = {"放射線棟BT": "放射線棟 BT"}
    lines = []
    for i, k in enumerate(f3["keys"]):
        H, Hs = pts[k]["H"]
        M, Ms = pts[k]["M"]
        T = H + M
        rel = np.hypot(Hs, Ms) / T
        meas = fd.MEASURED[k][0]
        lines.append(
            f"    {k[0]} & {name.get(k[1], k[1])} & {fd.SITE_TEQ[k[1]]:.0f} & {geo[pts[k]['src']]} & "
            f"{meas:.4f} & {T:.4f} & {rel * 100:.0f} & {meas / T:.2f} & {M / T:.2f} & "
            f"{f3['ratio'][i]:.2f} & {fb['ratio'][i]:.2f} \\\\")
    out = fd.OUT / "model_table_rows.tex"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)


def draw_response(e_tab, r_tab) -> None:
    import make_figures as mf  # noqa: F401
    _, _, s_tab = fd.response_table()
    fig, ax = plt.subplots(figsize=(8.0, 5.2))
    style = {"D1": ("#1f77b4", "-", "o"), "d1": ("#ff7f0e", "-", "o"),
             "D2": ("#1f77b4", "--", "s"), "d2": ("#ff7f0e", "--", "s")}
    label = {"D1": "D1（裸管，大）", "d1": "d1（裸管，小）", "D2": "D2（PE 付き，大）", "d2": "d2（PE 付き，小）"}
    e_ev = e_tab * 1e6
    for j, det in enumerate(DET_ORDER):
        c, ls, mk = style[det]
        ax.errorbar(e_ev, r_tab[:, j], yerr=s_tab[:, j], color=c, ls=ls, marker=mk, ms=4.5, lw=1.5,
                    capsize=0, label=label[det])
    for det, val in (("D1", 450.0), ("d1", 123.0)):
        ax.plot([0.0253], [val], marker="*", ms=13, color=style[det][0], mec="black", ls="none",
                label=f"メーカー感度（{det}）")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(3e-3, 2e9)
    ax.set_ylim(5e-3, 2e3)
    ax.set_xlabel("中性子のエネルギー [eV]")
    ax.set_ylabel(r"応答（等方入射，$^3$He(n,p) 反応率 / フルエンス）[cm$^2$]")
    ax.grid(alpha=0.3, which="both")
    ax.legend(fontsize=9, loc="lower left", framealpha=0.92)
    fig.tight_layout()
    out = REPORT / "figures" / "fig13_response.png"
    fig.savefig(out, bbox_inches="tight", dpi=150)
    plt.close(fig)
    print(out)


def draw(pts, f1, f3, fb) -> None:
    import make_figures as mf  # noqa: F401  (フォントと体裁を揃える)
    fig, axes = plt.subplots(1, 2, figsize=(15.0, 6.2), gridspec_kw={"width_ratios": [1.0, 1.25]})
    color = {"D1": "#1f77b4", "d1": "#ff7f0e", "D2": "#1f77b4", "d2": "#ff7f0e"}
    marker = {"D1": "o", "d1": "o", "D2": "s", "d2": "s"}
    fill = {"D1": True, "d1": True, "D2": False, "d2": False}
    short = {"テストホール": "TH", "放射線棟BT": "BT"}

    ax = axes[0]
    seen = set()
    for k in f3["keys"]:
        det, site = k
        x, xs = pts[k]["H"][0] + pts[k]["M"][0], np.hypot(pts[k]["H"][1], pts[k]["M"][1])
        y, ys = fd.MEASURED[k]
        ax.errorbar([x], [y], xerr=[xs], yerr=[ys], fmt=marker[det], ms=7.5, color=color[det],
                    mfc=color[det] if fill[det] else "white", mec=color[det], mew=1.6, capsize=0,
                    label=det if det not in seen else None, zorder=4)
        seen.add(det)
        xy = {("D2", "PF"): (6, -11), ("d2", "放射線棟BT"): (6, -10), ("D1", "テストホール"): (-18, 6)}
        ax.annotate(short.get(site, site), (x, y), textcoords="offset points", xytext=xy.get(k, (5, 4)),
                    fontsize=8)
    lim = np.array([1e-3, 1.0])
    ax.plot(lim, lim, color="black", lw=1.2, label="実測 = PHITS")
    for fct, ls in ((2.0, "--"), (5.0, ":")):
        ax.plot(lim, fct * lim, color="#666666", lw=1.0, ls=ls, label=f"実測 = {fct:.0f} × PHITS")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1.5e-3, 0.5)
    ax.set_ylim(5e-3, 0.5)
    ax.set_xlabel(r"PHITS の予測計数率（peak ROI）[s$^{-1}$]")
    ax.set_ylabel(r"実測の正味計数率 $R_{\rm NET}$ [s$^{-1}$]")
    ax.set_title("自由パラメータなしの比較", fontsize=12)
    ax.grid(alpha=0.3, which="both")
    ax.legend(fontsize=8.5, loc="upper left", framealpha=0.92)

    ax = axes[1]
    raw = np.array([fd.MEASURED[k][0] / (pts[k]["H"][0] + pts[k]["M"][0]) for k in f3["keys"]])
    kb1, kp1 = f1["p"]
    kb3, kp3, r3 = f3["p"]
    series = [
        (raw, "#999999", "PHITS そのまま", -9.0),
        (f1["ratio"], "#F58518", fr"$k_{{\rm type}}(H+M)$（$\chi^2$/ndf={f1['chi2']:.0f}/{f1['ndf']}）", -3.0),
        (f3["ratio"], "#7B3294", fr"$k_{{\rm type}}(H+rM)$，$r$={r3:.1f}（{f3['chi2']:.0f}/{f3['ndf']}）", 3.0),
        (fb["ratio"], "#2CA02C", fr"$k_{{\rm type}}(H+M)+B$（{fb['chi2']:.0f}/{fb['ndf']}）", 9.0),
    ]
    for vals, c, lab, dx in series:
        for i, k in enumerate(f3["keys"]):
            det = k[0]
            ax.plot(fd.SITE_TEQ[k[1]] + dx, vals[i], marker=marker[det], ms=7, ls="none", color=c,
                    mfc=c if fill[det] else "white", mec=c, mew=1.5, label=lab if i == 0 else None)
    ax.axhline(1.0, color="black", lw=1.0)
    ax.set_yscale("log")
    ax.set_xlim(0, 580)
    ax.set_ylim(0.2, 15)
    ax.set_xlabel(r"等価コンクリート厚 $t_{\rm eq}$ [cm]")
    ax.set_ylabel("実測 / 予測")
    ax.set_title("実測 / 予測（○：裸管，□：PE 付き管）", fontsize=12)
    ax.grid(alpha=0.3, which="both")
    ax.legend(fontsize=8.5, loc="upper left", framealpha=0.92)
    fig.tight_layout()
    out = REPORT / "figures" / "fig13_phits_model.png"
    fig.savefig(out, bbox_inches="tight", dpi=150)
    plt.close(fig)
    print(out)


if __name__ == "__main__":
    main()
