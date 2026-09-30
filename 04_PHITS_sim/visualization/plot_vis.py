#!/usr/bin/env python3
"""make_vis.py の計算結果から、レポート用の断面図を作る。

fig14_phits_sites.png     : PF と PS の地点体系の xz 断面での中性子フラックス（大気由来ハドロン／負ミューオン）
fig15_phits_detectors.png : 管の軸を通る断面での中性子フラックス（入射フルエンスとの比）

実行: python3 plot_vis.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parent
SIM = ROOT.parent
sys.path.insert(0, str(SIM / "site_models"))
sys.path.insert(0, str(SIM / "detector_response"))

import make_resp  # noqa: E402
import make_site  # noqa: E402
from make_vis import det_map_file  # noqa: E402

OUT = SIM.parent / "03_今年度用" / "最終レポート_20260925" / "figures"

plt.rcParams.update({"font.family": "Hiragino Sans", "axes.unicode_minus": False,
                     "figure.dpi": 120, "savefig.dpi": 200})


def read_map(path: Path) -> list[dict]:
    """2D-type=4 の出力を、ページ（粒子・エネルギー区分）ごとの 2 次元配列にする。"""
    pages, cur = [], None
    for line in path.read_text().splitlines():
        s = line.strip()
        if s.startswith("#   no. ="):
            cur = {"part": s.split("part. =")[1].strip(), "rows": []}
            pages.append(cur)
        elif s.startswith("#   e = ("):
            lo, hi = s.split("(")[1].split(")")[0].split(" - ")
            cur["e"] = (float(lo), float(hi))
        elif cur is not None and s and not s.startswith("#") and not s.startswith("newpage"):
            v = s.split()
            if len(v) == 4:
                cur["rows"].append([float(t) for t in v])
    out = []
    for p in pages:
        a = np.array(p["rows"])
        xs, zs = np.unique(a[:, 0]), np.unique(a[:, 1])
        f = np.zeros((zs.size, xs.size))
        f[np.searchsorted(zs, a[:, 1]), np.searchsorted(xs, a[:, 0])] = a[:, 2]
        out.append({"part": p["part"], "e": p["e"], "x": xs, "z": zs, "f": f})
    return out


def mean_map(runs: list[Path], name: str) -> list[dict]:
    maps = [read_map(r / name) for r in runs]
    base = maps[0]
    for i, pg in enumerate(base):
        pg["f"] = np.mean([m[i]["f"] for m in maps], axis=0)
    return base


def total(pages: list[dict], part: str) -> dict:
    sel = [p for p in pages if p["part"] == part]
    return {"x": sel[0]["x"], "z": sel[0]["z"], "f": np.sum([p["f"] for p in sel], axis=0)}


def edges(c: np.ndarray) -> np.ndarray:
    d = np.diff(c)
    return np.concatenate([[c[0] - d[0] / 2], c[:-1] + d / 2, [c[-1] + d[-1] / 2]])


def runs(prefix: str) -> list[Path]:
    rs = sorted(p for p in (ROOT / "runs").glob(prefix + "_s*") if "total cpu time" in (p / "phits.out").read_text())
    if not rs:
        raise SystemExit(f"no finished runs for {prefix}")
    return rs


LAYER_NAME = {"concrete": "コンクリート", "loam": "関東ローム", "joso": "常総層", "shimosa": "下総層群"}


def rebin2(m: dict) -> dict:
    """20 cm メッシュを 2×2 で平均して 40 cm にする（端の余りは捨てる）。"""
    nz, nx = (m["f"].shape[0] // 2) * 2, (m["f"].shape[1] // 2) * 2
    f = m["f"][-nz:, :nx].reshape(nz // 2, 2, nx // 2, 2).mean(axis=(1, 3))
    return {"x": m["x"][:nx].reshape(-1, 2).mean(1), "z": m["z"][-nz:].reshape(-1, 2).mean(1), "f": f}


def draw_site(ax, site: str, m: dict, norm, title: str):
    x_lo, x_hi = m["x"][0], m["x"][-1]
    pc = ax.pcolormesh(edges(m["x"]) / 100, edges(m["z"]) / 100, np.clip(m["f"], norm.vmin, None),
                       norm=norm, cmap="inferno", shading="flat", rasterized=True)
    z = 0.0
    ax.axhline(0, color="w", lw=0.8)
    for mat, t in make_site.SITES[site]:
        z -= t
        ax.axhline(z / 100, color="w", lw=0.5, ls=":")
    depth = -z
    ax.add_patch(Rectangle((-make_site.ROOM_HALF_X / 100, -(depth + make_site.ROOM_H) / 100),
                           2 * make_site.ROOM_HALF_X / 100, make_site.ROOM_H / 100,
                           fill=False, ec="cyan", lw=1.2))
    kw = dict(color="w", fontsize=8, va="center", ha="left")
    ax.text(x_lo / 100 + 0.3, 1.0, "空気", **kw)
    ax.text(x_lo / 100 + 0.3, -min(depth, 300.0) / 200, f"コンクリート（天井 {depth:.0f} cm）", **kw)
    ax.text(0, -(depth + make_site.ROOM_H + 40.0) / 100, "部屋", color="cyan", fontsize=8, ha="center", va="top")
    ax.set_xlim(x_lo / 100, x_hi / 100)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=10)
    return pc


def fig_sites() -> Path:
    rows = [("PF", "PF（$t_{\\rm eq}$=105 cm）"), ("PS", "PS（$t_{\\rm eq}$=480 cm）")]
    cols = [("had", "大気由来ハドロン（中性子・陽子）"), ("mum", "負ミューオン")]
    maps = {}
    for s, _ in rows:
        maps[(s, "had")] = rebin2(total(mean_map(runs(f"{s}_had"), "map_xz.out"), "neutron"))
        maps[(s, "mum")] = total(mean_map(runs(f"{s}_mum"), "map_xz.out"), "neutron")
    norm = LogNorm(1e-6, 1e-2)
    lows = {s: max(maps[(s, "had")]["z"][0], maps[(s, "mum")]["z"][0]) / 100 - 0.2 for s, _ in rows}
    fig, axes = plt.subplots(2, 2, figsize=(10.0, 8.9),
                             gridspec_kw={"height_ratios": [2.2 - lows["PF"], 2.2 - lows["PS"]]})
    for r, (s, st) in enumerate(rows):
        for c, (case, ct) in enumerate(cols):
            ax = axes[r][c]
            pc = draw_site(ax, s, maps[(s, case)], norm, f"{st}：{ct}")
            ax.set_ylim(lows[s], 2.0)
            if c == 0:
                ax.set_ylabel("z [m]（地表 = 0）")
            else:
                ax.set_yticklabels([])
        axes[r][0].set_xlabel("x [m]")
        axes[r][1].set_xlabel("x [m]")
    cb = fig.colorbar(pc, ax=axes, fraction=0.03, pad=0.02)
    cb.set_label("中性子フラックス（全エネルギー）[cm$^{-2}$ s$^{-1}$]")
    out = OUT / "fig14_phits_sites.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def det_outline(ax, name: str):
    """管の軸を通る断面の輪郭（make_resp.py の寸法）。座標は管の中心を原点とする。"""
    kw = dict(fill=False, lw=0.9)
    if name in ("D1", "D2"):
        z_bot, r_out, length, active = (-33.0 if name == "D1" else -34.0), 5.0, 66.0, 56.0
    else:
        z_bot, r_out, length, active = -19.765, 2.74, 39.53, 31.0
    ax.add_patch(Rectangle((-r_out, z_bot), 2 * r_out, length, ec="w", **kw))
    ax.add_patch(Rectangle((-(r_out - 0.2), z_bot + 0.2), 2 * (r_out - 0.2), active, ec="w", ls="--", **kw))
    if name == "D2":
        ax.add_patch(Rectangle((-7.5, -34.0), 15.0, 68.0, ec="cyan", ls=":", **kw))
        ax.add_patch(Rectangle((-14.5, -40.0), 29.0, 80.0, ec="cyan", **kw))
    if name == "d2":
        ax.add_patch(Rectangle((-7.74, -24.765), 15.48, 49.53, ec="cyan", **kw))


def fig_detectors() -> Path:
    fast = [mean_map(runs("det_E1.000e+00"), det_map_file(n)) for n in ("D2", "d2")]
    therm = [mean_map(runs("det_E2.530e-08"), det_map_file(n)) for n in ("D1", "d1")]
    n_src = len(make_resp.DETS)

    def rel(pages, name, ie=None):
        x0 = make_resp.DETS[name]["x"]
        scale = np.pi * make_resp.DETS[name]["r_src"] ** 2 * n_src
        sel = pages if ie is None else [pages[ie]]
        f = np.sum([p["f"] for p in sel], axis=0) * scale
        x = pages[0]["x"] - x0
        xx, zz = np.meshgrid(x, pages[0]["z"])
        inside = np.hypot(xx, zz) < make_resp.DETS[name]["r_src"] - 0.5
        f = np.where(inside, np.maximum(f, 1e-6), np.nan)
        return {"x": x, "z": pages[0]["z"], "f": f}

    rows = [
        ([(rel(fast[0], "D2", 0), "D2", "D2（PE 容器）"), (rel(fast[1], "d2", 0), "d2", "d2（PE 密着）")],
         LogNorm(3e-3, 3.0), "1 MeV の中性子を等方入射したときの\n熱中性子（< 0.5 eV）のフラックス / 入射フルエンス"),
        ([(rel(therm[0], "D1"), "D1", "D1（裸管）"), (rel(therm[1], "d1"), "d1", "d1（裸管）")],
         LogNorm(0.05, 2.0), "熱中性子（0.0253 eV）を等方入射したときの\nフラックス / 入射フルエンス"),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 9.6), gridspec_kw={"width_ratios": [1.0, 0.62]})
    for r, (panels, norm, label) in enumerate(rows):
        for ax, (m, name, title) in zip(axes[r], panels):
            pc = ax.pcolormesh(edges(m["x"]), edges(m["z"]), np.clip(m["f"], norm.vmin, None),
                               norm=norm, cmap="viridis", shading="flat", rasterized=True)
            det_outline(ax, name)
            ax.set_aspect("equal")
            ax.set_title(title, fontsize=10)
            ax.set_xlabel("x [cm]")
        axes[r][0].set_ylabel("z [cm]")
        cb = fig.colorbar(pc, ax=list(axes[r]), fraction=0.035, pad=0.02)
        cb.set_label(label, fontsize=8.5)
    out = OUT / "fig15_phits_detectors.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


if __name__ == "__main__":
    which = sys.argv[1:] or ["sites", "det"]
    if "det" in which:
        print(fig_detectors())
    if "sites" in which:
        print(fig_sites())
