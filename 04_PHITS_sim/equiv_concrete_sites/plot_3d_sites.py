#!/usr/bin/env python3
"""各地点 PHITS 球殻ジオメトリと中性子スペクトルを 3D 可視化する。

各サイトフォルダに:
  figures/3d_geometry.html / .png  — 同心球殻（内腔・コンクリート・土）
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

SITES = [
    {
        "dir": "00_ground",
        "label": "地上",
        "layers": [("air", "空気（開空）", "#AED6F1", 0.25)],
    },
    {
        "dir": "01_PF",
        "label": "PF",
        "layers": [
            ("cavity", "内腔空気", "#D6EAF8", 0.15),
            ("concrete", "コンクリート 105 cm", "#7F8C8D", 0.35),
            ("outer", "外側大気", "#AED6F1", 0.08),
        ],
    },
    {
        "dir": "02_linac",
        "label": "linac",
        "layers": [
            ("cavity", "内腔空気", "#D6EAF8", 0.15),
            ("concrete", "コンクリート 150 cm", "#7F8C8D", 0.35),
            ("outer", "外側大気", "#AED6F1", 0.08),
        ],
    },
    {
        "dir": "03_BT",
        "label": "BT",
        "layers": [
            ("cavity", "内腔空気", "#D6EAF8", 0.12),
            ("concrete", "コンクリート 60 cm", "#7F8C8D", 0.35),
            ("loam", "ローム 220 cm", "#C0392B", 0.30),
            ("outer", "外側大気", "#AED6F1", 0.08),
        ],
    },
    {
        "dir": "04_KEKB",
        "label": "KEKB",
        "layers": [
            ("cavity", "内腔空気", "#D6EAF8", 0.10),
            ("concrete", "コンクリート 80 cm", "#7F8C8D", 0.30),
            ("loam", "ローム 400 cm", "#C0392B", 0.28),
            ("joso", "常総粘土 270 cm", "#6E2C00", 0.28),
            ("outer", "外側大気", "#AED6F1", 0.06),
        ],
    },
]


def parse_sets(main_inp: Path) -> dict[str, float]:
    text = main_inp.read_text(encoding="utf-8")
    return {m.group(1): float(m.group(2)) for m in re.finditer(r"set:c(\d+)\[([0-9.]+)\]", text)}


def radii_for_site(sets: dict[str, float], n_layers: int) -> list[float]:
    """各層の外半径 [cm] を内側から順に返す。"""
    if n_layers == 1:
        # 地上: 空気球のみ
        return [sets.get("1", 200.0)]
    c1 = sets["1"]  # source
    c2 = sets["2"]  # cavity
    c3 = sets.get("3", 0.0)
    c4 = sets.get("4", 0.0)
    c5 = sets.get("5", 0.0)
    if n_layers == 3:  # cavity, concrete, outer
        return [c2, c2 + c3, c1]
    if n_layers == 4:  # + loam
        return [c2, c2 + c3, c2 + c3 + c4, c1]
    if n_layers == 5:  # + joso
        return [c2, c2 + c3, c2 + c3 + c4, c2 + c3 + c4 + c5, c1]
    raise ValueError(f"unsupported n_layers={n_layers}")


def hex_to_rgb(h: str) -> str:
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgb({r},{g},{b})"


def sphere_mesh(r: float, n: int = 48) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n // 2)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones_like(u), np.cos(v))
    return x, y, z


# He-3 / SUS304（既存 he3_sus304.inp と同じ寸法）
R_HE3, R_SUS = 2.54, 2.74
L_HE3, L_SUS = 39.53, 39.93


def cylinder_mesh(
    radius: float, y0: float, y1: float, n_theta: int = 36, n_y: int = 12
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    th = np.linspace(0, 2 * np.pi, n_theta)
    yy = np.linspace(y0, y1, n_y)
    thg, yg = np.meshgrid(th, yy)
    x = radius * np.cos(thg)
    z = radius * np.sin(thg)
    return x, yg, z


def detector_plotly_traces() -> list[dict]:
    """中心の He-3 ガス筒 + SUS304 外壁。"""
    traces = []
    for r, y0, y1, color, name, op in [
        (R_HE3, -L_HE3 / 2, L_HE3 / 2, "#F4D03F", "He-3 ガス", 0.95),
        (R_SUS, -L_SUS / 2, L_SUS / 2, "#5D6D7E", "SUS304 壁", 0.55),
    ]:
        x, y, z = cylinder_mesh(r, y0, y1)
        traces.append(
            {
                "type": "surface",
                "x": x.tolist(),
                "y": y.tolist(),
                "z": z.tolist(),
                "name": f"{name} (R={r} cm, L={y1 - y0:.2f} cm)",
                "showscale": False,
                "opacity": op,
                "colorscale": [[0, hex_to_rgb(color)], [1, hex_to_rgb(color)]],
                "hoverinfo": "name",
            }
        )
    return traces


def draw_detector_mpl(ax) -> list:
    from matplotlib.patches import Patch

    for r, y0, y1, color, op in [
        (R_HE3, -L_HE3 / 2, L_HE3 / 2, "#F4D03F", 0.95),
        (R_SUS, -L_SUS / 2, L_SUS / 2, "#5D6D7E", 0.45),
    ]:
        x, y, z = cylinder_mesh(r, y0, y1, n_theta=28, n_y=10)
        ax.plot_surface(x, y, z, color=color, alpha=op, linewidth=0, shade=True)
    return [
        Patch(facecolor="#F4D03F", label=f"He-3 (R={R_HE3})"),
        Patch(facecolor="#5D6D7E", label=f"SUS304 (R={R_SUS})"),
    ]


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
    d = BASE / site["dir"]
    out = d / "figures"
    out.mkdir(parents=True, exist_ok=True)
    sets = parse_sets(d / "main.inp")
    radii = radii_for_site(sets, len(site["layers"]))
    label = site["label"]

    # ---- Plotly（外側球殻 → 内側検出器の順） ----
    traces: list[dict] = []
    for (key, name, color, opacity), r in reversed(list(zip(site["layers"], radii))):
        x, y, z = sphere_mesh(r, n=40)
        traces.append(
            {
                "type": "surface",
                "x": x.tolist(),
                "y": y.tolist(),
                "z": z.tolist(),
                "name": f"{name} (R={r:.0f} cm)",
                "showscale": False,
                "opacity": opacity,
                "colorscale": [[0, hex_to_rgb(color)], [1, hex_to_rgb(color)]],
                "hoverinfo": "name",
            }
        )
    traces.extend(detector_plotly_traces())
    rmax = max(radii) * 1.05
    layout = {
        "title": f"{label} — 遮蔽球殻 + He-3/SUS304",
        "scene": {
            "xaxis": {"title": "x [cm]", "range": [-rmax, rmax]},
            "yaxis": {"title": "y [cm]", "range": [-rmax, rmax]},
            "zaxis": {"title": "z [cm]", "range": [-rmax, rmax]},
            "aspectmode": "data",
            "camera": {"eye": {"x": 1.45, "y": 1.45, "z": 0.95}},
        },
        "legend": {"title": {"text": "層・検出器（クリックで切替）"}},
        "margin": {"l": 0, "r": 0, "t": 50, "b": 0},
        "template": "plotly_white",
    }
    note = (
        f"{label}: 中心に He-3 (R={R_HE3} cm) + SUS304 (R={R_SUS} cm)<br>"
        + " → ".join(f"{n}({r:.0f}cm)" for (_, n, _, _), r in zip(site["layers"], radii))
        + "<br>マウスで回転・ズーム"
    )
    write_plotly_html(traces, layout, out / "3d_geometry.html", f"{label} geometry", note)

    # ---- Matplotlib PNG（ズーム: 検出器が見える縮尺も別保存） ----
    from matplotlib.patches import Patch

    fig = plt.figure(figsize=(8.5, 7.5))
    ax = fig.add_subplot(111, projection="3d")
    for (key, name, color, opacity), r in reversed(list(zip(site["layers"], radii))):
        x, y, z = sphere_mesh(r, n=36)
        ax.plot_surface(x, y, z, color=color, alpha=min(opacity, 0.25), linewidth=0, shade=True)
        th = np.linspace(0, 2 * np.pi, 120)
        ax.plot(r * np.cos(th), r * np.sin(th), np.zeros_like(th), color=color, lw=1.0, alpha=0.7)
    det_handles = draw_detector_mpl(ax)
    ax.set_xlabel("x [cm]", fontproperties=_JP_FONT)
    ax.set_ylabel("y [cm]", fontproperties=_JP_FONT)
    ax.set_zlabel("z [cm]", fontproperties=_JP_FONT)
    ax.set_title(f"{label} — 遮蔽 + He-3/SUS304", fontproperties=_JP_FONT)
    handles = [
        Patch(facecolor=c, edgecolor=c, alpha=min(0.85, op + 0.3), label=f"{n} (R={r:.0f})")
        for (_, n, c, op), r in zip(site["layers"], radii)
    ] + det_handles
    ax.legend(handles=handles, loc="upper left", prop=_JP_FONT, fontsize=7)
    lim = max(radii) * 1.05
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    try:
        ax.set_box_aspect((1, 1, 1))
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
    d = BASE / site["dir"]
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
    out = BASE / "figures"
    out.mkdir(parents=True, exist_ok=True)
    mats = []
    labels = []
    loge_ref = None
    for site in SITES:
        rows = parse_spectrum(BASE / site["dir"] / "neutron_he3.out")
        if not rows:
            rows = parse_spectrum(BASE / site["dir"] / "neutron_cavity.out")
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
    for site in SITES:
        plot_geometry(site)
        plot_spectrum(site)
    plot_all_spectra_surface()
    # ルートにも各地点へのリンク一覧
    index = BASE / "figures" / "index.html"
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
        '<li><b>全地点</b>: <a href="3d_all_spectra.html">スペクトル比較</a></li>'
    )
    index.write_text(
        "<!DOCTYPE html><html lang='ja'><head><meta charset='utf-8'/>"
        "<title>PHITS 3D 一覧</title></head><body>"
        "<h1>等価コンクリート各地点 — 3D 可視化</h1><ul>"
        + "\n".join(links)
        + "</ul></body></html>",
        encoding="utf-8",
    )
    print(f"wrote {index}")


if __name__ == "__main__":
    main()
