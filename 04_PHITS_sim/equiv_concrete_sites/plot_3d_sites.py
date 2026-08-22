#!/usr/bin/env python3
"""各地点 PHITS 天井スラブジオメトリと中性子スペクトルを 3D 可視化する。

各サイトフォルダに:
  figures/3d_geometry.html / .png  — 水平天井スラブ + He-3/SUS304
  figures/3d_spectrum.html / .png  — エネルギー×フラックスの 3D 棒
を書き出す。
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

BASE = Path(__file__).resolve().parent

from detector_specs import DETECTORS, DetectorSpec, detector_root  # noqa: E402

_DET_ROOT = detector_root(BASE, "D1")
_SPEC: DetectorSpec = DETECTORS["D1"]

_FONT_CANDIDATES = [
    Path("/Library/Fonts/Arial Unicode.ttf"),
    Path("/System/Library/Fonts/Supplemental/AppleGothic.ttf"),
    Path("/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"),
]
_JP_FONT = None
for _p in _FONT_CANDIDATES:
    if _p.is_file():
        font_manager.fontManager.addfont(str(_p))
        _JP_FONT = font_manager.FontProperties(fname=str(_p))
        break
if _JP_FONT is None:
    _JP_FONT = font_manager.FontProperties(family="Hiragino Sans")

plt.rcParams.update(
    {
        "font.family": _JP_FONT.get_name(),
        "axes.unicode_minus": False,
    }
)

LXY_DEFAULT = 400.0
HROOM_DEFAULT = 250.0
ZSRC_MARGIN = 50.0

SITES = [
    {
        "dir": "00_ground",
        "label": "地上",
        "tc": 0.0,
        "tl": 0.0,
        "tj": 0.0,
    },
    {"dir": "01_PF", "label": "PF", "tc": 105.0, "tl": 0.0, "tj": 0.0},
    {"dir": "02_linac", "label": "linac", "tc": 150.0, "tl": 0.0, "tj": 0.0},
    {"dir": "03_BT", "label": "BT", "tc": 60.0, "tl": 220.0, "tj": 0.0},
    {"dir": "04_KEKB", "label": "KEKB", "tc": 80.0, "tl": 400.0, "tj": 270.0},
]

SLAB_STYLE = {
    "air": ("室内空気", "#D6EAF8", 0.18),
    "concrete": ("コンクリート", "#7F8C8D", 0.45),
    "loam": ("ローム", "#C0392B", 0.40),
    "joso": ("常総粘土", "#6E2C00", 0.40),
    "source": ("線源面（垂直降下）", "#F39C12", 0.25),
}


def parse_params(main_inp: Path) -> dict[str, float]:
    text = main_inp.read_text(encoding="utf-8")
    params: dict[str, float] = {}
    for m in re.finditer(r"set:\s*c(\d+)\[([0-9.]+)\]", text):
        params[f"c{m.group(1)}"] = float(m.group(2))
    return params


def slabs_for_site(site: dict, lxy: float, hroom: float) -> list[tuple[str, str, str, float, float, float]]:
    """(key, name, color, opacity, z0, z1) を床から上へ返す。"""
    tc, tl, tj = site["tc"], site["tl"], site["tj"]
    slabs: list[tuple[str, str, str, float, float, float]] = []
    z = 0.0
    name, color, op = SLAB_STYLE["air"]
    slabs.append(("air", f"{name} 0–{hroom:.0f} cm", color, op, z, hroom))
    z = hroom
    if tc > 0:
        name, color, op = SLAB_STYLE["concrete"]
        slabs.append(("concrete", f"{name} {tc:.0f} cm", color, op, z, z + tc))
        z += tc
    if tl > 0:
        name, color, op = SLAB_STYLE["loam"]
        slabs.append(("loam", f"{name} {tl:.0f} cm", color, op, z, z + tl))
        z += tl
    if tj > 0:
        name, color, op = SLAB_STYLE["joso"]
        slabs.append(("joso", f"{name} {tj:.0f} cm", color, op, z, z + tj))
        z += tj
    name, color, op = SLAB_STYLE["source"]
    zsrc = z + ZSRC_MARGIN
    slabs.append(("source", f"{name} z={zsrc:.0f} cm", color, op, zsrc, zsrc))
    return slabs


def hex_to_rgb(h: str) -> str:
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgb({r},{g},{b})"


def slab_top_mesh(
    lxy: float, z: float, n: int = 24
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    xs = np.linspace(-lxy, lxy, n)
    ys = np.linspace(-lxy, lxy, n)
    xg, yg = np.meshgrid(xs, ys)
    zg = np.full_like(xg, z)
    return xg, yg, zg


def slab_side_mesh(
    lxy: float, z0: float, z1: float, n_z: int = 8
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    ys = np.linspace(-lxy, lxy, 2)
    zs = np.linspace(z0, z1, n_z)
    yg, zg = np.meshgrid(ys, zs)
    xg = np.full_like(yg, lxy)
    return xg, yg, zg


# He-3 / SUS304 / 信管 / PE（detector_specs から取得、筒軸=z）
def _det_dims() -> tuple[float, float, float, float, float, float]:
    s = _SPEC
    z0, z1 = 0.0, s.length_cm
    z_pmt = z1 - s.l_pmt_cm
    return s.r_in_cm, s.r_out_cm, s.r_pe_out_cm, z0, z1, z_pmt


def cylinder_mesh(
    radius: float, z0: float, z1: float, n_theta: int = 36, n_z: int = 12
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    th = np.linspace(0, 2 * np.pi, n_theta)
    zz = np.linspace(z0, z1, n_z)
    thg, zg = np.meshgrid(th, zz)
    x = radius * np.cos(thg)
    y = radius * np.sin(thg)
    return x, y, zg


def detector_plotly_traces() -> list[dict]:
    """He-3 有効ガス + SUS304 + 信管 + PE（任意）。"""
    r_in, r_out, r_pe, z0, z1, z_pmt = _det_dims()
    traces = []
    parts = [
        (r_in, z0, z_pmt, "#F4D03F", "He-3 有効ガス", 0.95),
        (r_out, z0, z1, "#5D6D7E", "SUS304 壁", 0.55),
        (_SPEC.r_pmt_cm, z_pmt, z1, "#AEB6BF", "信管（推定）", 0.7),
    ]
    if _SPEC.pe_style == "wrap":
        parts.append((r_pe, z0, z1, "#AED6F1", "PE 薄肉筒", 0.35))
    elif _SPEC.pe_style == "block":
        pe_z1 = _SPEC.pe_block_h_cm
        parts.append((r_pe, z0, pe_z1, "#AED6F1", "PE 容器（外筒）", 0.35))
        parts.append(
            (_SPEC.r_pe_in_cm, z0, _SPEC.pe_block_bore_h_cm, "#D5F5E3", "PE 内空", 0.15)
        )
    for r, za, zb, color, name, op in parts:
        x, y, z = cylinder_mesh(r, za, zb)
        traces.append(
            {
                "type": "surface",
                "x": x.tolist(),
                "y": y.tolist(),
                "z": z.tolist(),
                "name": f"{name} (R={r:.1f} cm)",
                "showscale": False,
                "opacity": op,
                "colorscale": [[0, hex_to_rgb(color)], [1, hex_to_rgb(color)]],
                "hoverinfo": "name",
            }
        )
    return traces


def draw_detector_mpl(ax) -> list:
    from matplotlib.patches import Patch

    r_in, r_out, r_pe, z0, z1, z_pmt = _det_dims()
    patches = []
    for r, za, zb, color, op, lab in [
        (r_in, z0, z_pmt, "#F4D03F", 0.95, f"He-3 R={r_in:.1f}"),
        (r_out, z0, z1, "#5D6D7E", 0.45, f"SUS R={r_out:.1f}"),
        (_SPEC.r_pmt_cm, z_pmt, z1, "#AEB6BF", 0.5, f"信管 R={_SPEC.r_pmt_cm:.1f}"),
    ]:
        x, y, z = cylinder_mesh(r, za, zb, n_theta=28, n_z=10)
        ax.plot_surface(x, y, z, color=color, alpha=op, linewidth=0, shade=True)
        patches.append(Patch(facecolor=color, label=lab))
    if _SPEC.pe_style == "wrap":
        x, y, z = cylinder_mesh(r_pe, z0, z1, n_theta=28, n_z=10)
        ax.plot_surface(x, y, z, color="#AED6F1", alpha=0.3, linewidth=0, shade=True)
        patches.append(Patch(facecolor="#AED6F1", label="PE 薄肉筒"))
    elif _SPEC.pe_style == "block":
        pe_z1 = _SPEC.pe_block_h_cm
        x, y, z = cylinder_mesh(r_pe, z0, pe_z1, n_theta=28, n_z=10)
        ax.plot_surface(x, y, z, color="#AED6F1", alpha=0.3, linewidth=0, shade=True)
        patches.append(Patch(facecolor="#AED6F1", label="PE 容器"))
    return patches


def parse_spectrum(path: Path) -> list[tuple[float, float, float, float]]:
    rows = []
    with path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.split()
            if len(parts) < 4:
                continue
            try:
                lo, hi, y, err = map(float, parts[:4])
            except ValueError:
                continue
            rows.append((lo, hi, y, err))
    return rows


def write_plotly_html(traces: list[dict], layout: dict, path: Path, title: str, note: str) -> None:
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8"/>
<title>{title}</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  html, body, #plot {{ margin:0; height:100%; width:100%; font-family: sans-serif; }}
  .note {{ position:absolute; left:12px; bottom:12px; z-index:2; background:rgba(255,255,255,.9);
           padding:8px 12px; font-size:13px; border-radius:6px; max-width:420px; }}
</style>
</head>
<body>
<div id="plot"></div>
<div class="note">{note}</div>
<script>
const data = {json.dumps(traces, ensure_ascii=False)};
const layout = {json.dumps(layout, ensure_ascii=False)};
Plotly.newPlot("plot", data, layout, {{responsive: true}});
</script>
</body>
</html>
"""
    path.write_text(html, encoding="utf-8")


def plot_geometry(site: dict) -> None:
    d = _DET_ROOT / site["dir"]
    out = d / "figures"
    out.mkdir(parents=True, exist_ok=True)
    params = parse_params(d / "main.inp")
    lxy = params.get("c1", LXY_DEFAULT)
    hroom = params.get("c2", HROOM_DEFAULT)
    slabs = slabs_for_site(site, lxy, hroom)
    label = site["label"]
    zmax = max(s[5] for s in slabs) + 80.0

    # ---- Plotly ----
    traces: list[dict] = []
    for key, name, color, opacity, z0, z1 in reversed(slabs):
        if key == "source":
            x, y, z = slab_top_mesh(lxy * 0.85, z0, n=20)
        else:
            x, y, z = slab_top_mesh(lxy, z1, n=24)
            traces.append(
                {
                    "type": "surface",
                    "x": x.tolist(),
                    "y": y.tolist(),
                    "z": z.tolist(),
                    "name": f"{name} (上面 z={z1:.0f})",
                    "showscale": False,
                    "opacity": opacity,
                    "colorscale": [[0, hex_to_rgb(color)], [1, hex_to_rgb(color)]],
                    "hoverinfo": "name",
                }
            )
            if z1 - z0 > 1.0:
                for sign in (-1.0, 1.0):
                    xs, ys, zs = slab_side_mesh(lxy * sign, z0, z1, n_z=6)
                    traces.append(
                        {
                            "type": "surface",
                            "x": xs.tolist(),
                            "y": ys.tolist(),
                            "z": zs.tolist(),
                            "name": name,
                            "showscale": False,
                            "opacity": opacity * 0.55,
                            "colorscale": [[0, hex_to_rgb(color)], [1, hex_to_rgb(color)]],
                            "hoverinfo": "skip",
                            "showlegend": False,
                        }
                    )
            continue
        traces.append(
            {
                "type": "surface",
                "x": x.tolist(),
                "y": y.tolist(),
                "z": z.tolist(),
                "name": name,
                "showscale": False,
                "opacity": opacity,
                "colorscale": [[0, hex_to_rgb(color)], [1, hex_to_rgb(color)]],
                "hoverinfo": "name",
            }
        )
    traces.extend(detector_plotly_traces())
    layout = {
        "title": f"{label} — 水平天井スラブ + {_SPEC.label}",
        "scene": {
            "xaxis": {"title": "x [cm]", "range": [-lxy, lxy]},
            "yaxis": {"title": "y [cm]", "range": [-lxy, lxy]},
            "zaxis": {"title": "z [cm]（上向き）", "range": [-20, zmax]},
            "aspectmode": "data",
            "camera": {"eye": {"x": 1.6, "y": 1.35, "z": 0.55}},
        },
        "legend": {"title": {"text": "層・検出器（クリックで切替）"}},
        "margin": {"l": 0, "r": 0, "t": 50, "b": 0},
        "template": "plotly_white",
    }
    r_in, r_out, _, z0, z1, z_pmt = _det_dims()
    note = (
        f"{label}: z=0 床、{_SPEC.label}<br>"
        f"高さ={z1-z0:.0f} cm, He-3 R={r_in:.1f}, SUS R={r_out:.1f}, 有効長~{z_pmt-z0:.0f} cm<br>"
        + " / ".join(s[1] for s in slabs[:-1])
        + "<br>上から垂直降下中性子（dir=-1）"
    )
    write_plotly_html(traces, layout, out / "3d_geometry.html", f"{label} geometry", note)

    # ---- Matplotlib PNG ----
    from matplotlib.patches import Patch

    fig = plt.figure(figsize=(9.0, 7.5))
    ax = fig.add_subplot(111, projection="3d")
    for key, name, color, opacity, z0, z1 in slabs:
        if key == "source":
            x, y, z = slab_top_mesh(lxy * 0.85, z0, n=16)
            ax.plot_surface(x, y, z, color=color, alpha=opacity, linewidth=0, shade=False)
            continue
        x, y, z = slab_top_mesh(lxy, z1, n=18)
        ax.plot_surface(x, y, z, color=color, alpha=min(opacity, 0.35), linewidth=0, shade=True)
        if z1 - z0 > 1.0:
            for sign in (-1.0, 1.0):
                xs, ys, zs = slab_side_mesh(lxy * sign, z0, z1, n_z=5)
                ax.plot_surface(xs, ys, zs, color=color, alpha=min(opacity, 0.20), linewidth=0)
    det_handles = draw_detector_mpl(ax)
    ax.set_xlabel("x [cm]", fontproperties=_JP_FONT)
    ax.set_ylabel("y [cm]", fontproperties=_JP_FONT)
    ax.set_zlabel("z [cm]", fontproperties=_JP_FONT)
    ax.set_title(f"{label} — 天井スラブ + He-3/SUS304", fontproperties=_JP_FONT)
    handles = [
        Patch(facecolor=s[2], edgecolor=s[2], alpha=0.75, label=s[1]) for s in slabs
    ] + det_handles
    ax.legend(handles=handles, loc="upper left", prop=_JP_FONT, fontsize=7)
    ax.set_xlim(-lxy, lxy)
    ax.set_ylim(-lxy, lxy)
    ax.set_zlim(-20, zmax)
    try:
        ax.set_box_aspect((1, 1, max(zmax / (2 * lxy), 0.4)))
    except Exception:
        pass
    fig.tight_layout()
    fig.savefig(out / "3d_geometry.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    # 検出器ズーム
    fig = plt.figure(figsize=(7.5, 6.5))
    ax = fig.add_subplot(111, projection="3d")
    draw_detector_mpl(ax)
    ax.set_xlabel("x [cm]", fontproperties=_JP_FONT)
    ax.set_ylabel("y [cm] (管軸)", fontproperties=_JP_FONT)
    ax.set_zlabel("z [cm]", fontproperties=_JP_FONT)
    ax.set_title(f"{label} — He-3/SUS304 検出器ズーム", fontproperties=_JP_FONT)
    ax.set_xlim(-8, 8)
    ax.set_ylim(-22, 22)
    ax.set_zlim(-8, 8)
    fig.tight_layout()
    fig.savefig(out / "3d_detector_zoom.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out / '3d_geometry.html'} / .png / 3d_detector_zoom.png")


def plot_spectrum(site: dict) -> None:
    d = _DET_ROOT / site["dir"]
    out = d / "figures"
    out.mkdir(parents=True, exist_ok=True)
    label = site["label"]
    # 検出器内フラックス優先（なければ旧 cavity）
    spe_path = d / "neutron_he3.out"
    if not spe_path.is_file():
        spe_path = d / "neutron_cavity.out"
    rows = parse_spectrum(spe_path) if spe_path.is_file() else []
    if not rows:
        print(f"skip spectrum {label}: empty")
        return

    e_lo = np.array([r[0] for r in rows])
    e_hi = np.array([r[1] for r in rows])
    flux = np.array([r[2] for r in rows])
    e_mid = np.sqrt(np.maximum(e_lo * e_hi, 1e-30))
    loge = np.log10(e_mid)
    dx = 0.85 * np.mean(np.diff(loge)) if len(loge) > 1 else 0.2
    z = np.maximum(flux, 0.0)

    traces: list[dict] = []
    xs, ys, zs = [], [], []
    for lx, f in zip(loge, z):
        xs += [lx, lx, None]
        ys += [0.0, 0.0, None]
        zs += [0.0, f, None]
    traces.append(
        {
            "type": "scatter3d",
            "mode": "lines",
            "x": xs,
            "y": ys,
            "z": zs,
            "line": {"color": "#2471A3", "width": 4},
            "name": "フラックス",
            "hoverinfo": "skip",
        }
    )
    traces.append(
        {
            "type": "scatter3d",
            "mode": "markers",
            "x": loge.tolist(),
            "y": [0.0] * len(loge),
            "z": z.tolist(),
            "marker": {
                "size": 3,
                "color": z.tolist(),
                "colorscale": "Viridis",
                "colorbar": {"title": "flux"},
            },
            "text": [f"E={e:.3g} MeV<br>φ={f:.3g}" for e, f in zip(e_mid, z)],
            "hoverinfo": "text",
            "name": "bin",
        }
    )
    zmax = float(z.max()) if z.max() > 0 else 1.0
    layout = {
        "title": f"{label} — He-3 内中性子スペクトル (3D)",
        "scene": {
            "xaxis": {"title": "log10(E / MeV)"},
            "yaxis": {"title": "", "showticklabels": False, "range": [-0.5, 0.5]},
            "zaxis": {"title": "φ [1/cm²/source]", "range": [0, zmax * 1.1]},
            "camera": {"eye": {"x": 1.6, "y": 1.8, "z": 0.7}},
        },
        "margin": {"l": 0, "r": 0, "t": 50, "b": 0},
        "template": "plotly_white",
        "showlegend": False,
    }
    note = (
        f"{label}: He-3 内 T-Track（積分 φ = {z.sum():.4g}）<br>"
        "縦軸=フラックス、横軸=log10(エネルギー)"
    )
    write_plotly_html(traces, layout, out / "3d_spectrum.html", f"{label} spectrum", note)

    fig = plt.figure(figsize=(9.5, 6.5))
    ax = fig.add_subplot(111, projection="3d")
    ypos = np.zeros_like(loge)
    ax.bar3d(
        loge - dx / 2,
        ypos - 0.15,
        np.zeros_like(z),
        dx,
        0.3,
        z,
        color="#2471A3",
        shade=True,
        alpha=0.85,
    )
    ax.set_xlabel("log10(E / MeV)", fontproperties=_JP_FONT)
    ax.set_ylabel("", fontproperties=_JP_FONT)
    ax.set_zlabel("φ [1/cm²/source]", fontproperties=_JP_FONT)
    ax.set_title(
        f"{label} — He-3 内中性子 (積分={z.sum():.4g})",
        fontproperties=_JP_FONT,
    )
    ax.set_yticks([])
    fig.tight_layout()
    fig.savefig(out / "3d_spectrum.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out / '3d_spectrum.html'} / .png")

    # Deposit 波高も同様に
    de_rows = parse_spectrum(d / "de.out") if (d / "de.out").is_file() else []
    if de_rows and sum(r[2] for r in de_rows) > 0:
        e_lo = np.array([r[0] for r in de_rows])
        e_hi = np.array([r[1] for r in de_rows])
        dep = np.array([r[2] for r in de_rows])
        e_mid = 0.5 * (e_lo + e_hi)
        fig = plt.figure(figsize=(9.0, 5.5))
        ax = fig.add_subplot(111, projection="3d")
        dx = 0.85 * np.mean(np.diff(e_mid)) if len(e_mid) > 1 else 0.02
        ax.bar3d(
            e_mid - dx / 2,
            np.zeros_like(e_mid) - 0.15,
            np.zeros_like(dep),
            dx,
            0.3,
            dep,
            color="#C0392B",
            shade=True,
            alpha=0.85,
        )
        ax.set_xlabel("付与エネルギー [MeV]", fontproperties=_JP_FONT)
        ax.set_zlabel("counts [/source]", fontproperties=_JP_FONT)
        ax.set_title(f"{label} — He-3 T-Deposit (積分={dep.sum():.4g})", fontproperties=_JP_FONT)
        ax.set_yticks([])
        fig.tight_layout()
        fig.savefig(out / "3d_deposit.png", dpi=180, bbox_inches="tight")
        plt.close(fig)
        print(f"wrote {out / '3d_deposit.png'}")

def plot_all_spectra_surface() -> None:
    """全地点スペクトルを 1 枚の 3D 曲面で比較。"""
    out = _DET_ROOT / "figures"
    out.mkdir(parents=True, exist_ok=True)
    mats = []
    labels = []
    loge_ref = None
    for site in SITES:
        rows = parse_spectrum(_DET_ROOT / site["dir"] / "neutron_he3.out")
        if not rows:
            rows = parse_spectrum(_DET_ROOT / site["dir"] / "neutron_cavity.out")
        if not rows:
            continue
        e_mid = np.array([np.sqrt(max(r[0] * r[1], 1e-30)) for r in rows])
        flux = np.array([r[2] for r in rows])
        loge = np.log10(e_mid)
        if loge_ref is None:
            loge_ref = loge
        mats.append(flux)
        labels.append(site["label"])
    if not mats:
        print("skip all-spectra: no data")
        return
    Z = np.vstack(mats)  # (n_site, n_E)
    X, Y = np.meshgrid(loge_ref, np.arange(len(labels)))

    # Plotly
    traces = [
        {
            "type": "surface",
            "x": X.tolist(),
            "y": Y.tolist(),
            "z": Z.tolist(),
            "colorscale": "Viridis",
            "colorbar": {"title": "φ"},
            "name": "スペクトル",
        }
    ]
    layout = {
        "title": "全地点 中性子スペクトル比較 (3D)",
        "scene": {
            "xaxis": {"title": "log10(E / MeV)"},
            "yaxis": {
                "title": "地点",
                "tickvals": list(range(len(labels))),
                "ticktext": labels,
            },
            "zaxis": {"title": "φ [1/cm²/source]", "type": "log"},
            "camera": {"eye": {"x": 1.5, "y": -1.7, "z": 0.9}},
        },
        "margin": {"l": 0, "r": 0, "t": 50, "b": 0},
        "template": "plotly_white",
    }
    write_plotly_html(
        traces,
        layout,
        out / "3d_all_spectra.html",
        "all spectra",
        "地点 × エネルギー × フラックス。マウスで回転。",
    )

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")
    # log z のためにゼロを置換
    Zp = np.where(Z > 0, Z, np.nan)
    ax.plot_surface(X, Y, np.log10(Zp), cmap="viridis", linewidth=0, antialiased=True)
    ax.set_xlabel("log10(E / MeV)", fontproperties=_JP_FONT)
    ax.set_ylabel("地点", fontproperties=_JP_FONT)
    ax.set_zlabel("log10(φ)", fontproperties=_JP_FONT)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontproperties=_JP_FONT)
    ax.set_title("全地点 中性子スペクトル比較 (3D)", fontproperties=_JP_FONT)
    fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.92)
    fig.savefig(out / "3d_all_spectra.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {out / '3d_all_spectra.html'} / .png")


def main() -> None:
    import argparse

    global _DET_ROOT, _SPEC

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--detector",
        choices=list(DETECTORS),
        default="D1",
        help="可視化する検出器サブフォルダ",
    )
    args = parser.parse_args()
    _DET_ROOT = detector_root(BASE, args.detector)
    _SPEC = DETECTORS[args.detector]

    for site in SITES:
        plot_geometry(site)
        plot_spectrum(site)
    plot_all_spectra_surface()
    index = detector_root(BASE, args.detector) / "figures" / "index.html"
    index.parent.mkdir(parents=True, exist_ok=True)
    links = []
    for site in SITES:
        d = site["dir"]
        lab = site["label"]
        links.append(
            f"<li><b>{lab}</b> ({d}): "
            f'<a href="../{d}/figures/3d_geometry.html">ジオメトリ</a> / '
            f'<a href="../{d}/figures/3d_spectrum.html">スペクトル</a></li>'
        )
    links.append(
        f'<li><b>全地点</b>: <a href="3d_all_spectra.html">スペクトル比較</a></li>'
    )
    index.write_text(
        "<!DOCTYPE html><html lang='ja'><head><meta charset='utf-8'/>"
        f"<title>PHITS 3D — {args.detector}</title></head><body>"
        f"<h1>等価コンクリート各地点 — 3D ({_SPEC.label})</h1><ul>"
        + "\n".join(links)
        + "</ul></body></html>",
        encoding="utf-8",
    )
    print(f"wrote {index}")


if __name__ == "__main__":
    main()
