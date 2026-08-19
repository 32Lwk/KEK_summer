#!/usr/bin/env python3
"""PHITS 4dtrack から He-3 検出器の 3D 軌跡プロットを作る。"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

ROOT = Path(__file__).resolve().parent
FOURDT = ROOT / "4dt.out"
if not FOURDT.exists():
    FOURDT = ROOT / "archive_webzip" / "4dt.out"
if not FOURDT.exists():
    FOURDT = Path("/tmp/phits_he3_sus304/4dt.out")
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

COLORS = {
    "neutron": "#4c78a8",
    "proton": "#e45756",
    "triton": "#54a24b",
    "photon": "#f58518",
    "electron": "#b279a2",
    "positron": "#72b7b2",
}
R_IN, R_OUT = 2.54, 2.74
Y0, Y1 = -39.53 / 2, 39.53 / 2
Y0o, Y1o = -39.93 / 2, 39.93 / 2
Z_SRC = -2.74 - 15.0


def parse_4dt(path: Path):
    histories: list[dict] = []
    hist = None
    track = None
    with path.open() as f:
        for line in f:
            if line.startswith("h:"):
                if hist is not None:
                    histories.append(hist)
                hid = int(line.split()[1])
                hist = {"id": hid, "tracks": []}
                track = None
            elif line.startswith("t:") and hist is not None:
                parts = line.split()
                track = {"kf": int(parts[1]), "name": parts[2], "pts": []}
                hist["tracks"].append(track)
            elif track is not None and line.strip() and not line.startswith("#"):
                cols = line.split()
                if len(cols) < 8:
                    continue
                x, y, z, t, e, w = (float(cols[i]) for i in range(6))
                cell = int(cols[6])
                track["pts"].append((x, y, z, t, e, cell))
    if hist is not None:
        histories.append(hist)
    return histories


def clip_track(pts, rmax=22.0):
    """遠方へ逃げる光子などを検出器近傍で切る（はみ出し点は捨てる）。"""
    out = []
    for p in pts:
        r = np.sqrt(p[0] ** 2 + p[1] ** 2 + p[2] ** 2)
        if r > rmax or abs(p[2]) > 22 or abs(p[1]) > 25:
            break
        out.append(p)
    return out


def cylinder_wire(R, y0, y1, n_theta=48, n_y=2):
    th = np.linspace(0, 2 * np.pi, n_theta)
    ys = np.linspace(y0, y1, n_y)
    rings = []
    for y in ys:
        rings.append((R * np.cos(th), np.full_like(th, y), R * np.sin(th)))
    gens = []
    for t in np.linspace(0, 2 * np.pi, 12, endpoint=False):
        gens.append(
            (np.array([R * np.cos(t), R * np.cos(t)]), np.array([y0, y1]), np.array([R * np.sin(t), R * np.sin(t)]))
        )
    return rings, gens


def traces_for_plotly(histories):
    grouped: dict[str, dict[str, list]] = {}
    for h in histories:
        for tr in h["tracks"]:
            name = tr["name"]
            pts = clip_track(tr["pts"])
            if len(pts) < 2:
                continue
            g = grouped.setdefault(name, {"x": [], "y": [], "z": []})
            xs, ys, zs = zip(*[(p[0], p[1], p[2]) for p in pts])
            g["x"].extend(list(xs) + [None])
            g["y"].extend(list(ys) + [None])
            g["z"].extend(list(zs) + [None])
    traces = []
    widths = {"neutron": 2, "proton": 5, "triton": 5, "photon": 1.5}
    for name, g in grouped.items():
        traces.append(
            {
                "type": "scatter3d",
                "mode": "lines",
                "name": name,
                "x": g["x"],
                "y": g["y"],
                "z": g["z"],
                "line": {
                    "color": COLORS.get(name, "#888"),
                    "width": widths.get(name, 3),
                },
                "hoverinfo": "name",
                "opacity": 0.35 if name == "neutron" else 0.9,
            }
        )
    rings_in, gens_in = cylinder_wire(R_IN, Y0, Y1)
    rings_out, gens_out = cylinder_wire(R_OUT, Y0o, Y1o)
    for i, (x, y, z) in enumerate(rings_in + gens_in):
        traces.append(
            {
                "type": "scatter3d",
                "mode": "lines",
                "name": "He-3 gas",
                "x": x.tolist(),
                "y": y.tolist(),
                "z": z.tolist(),
                "line": {"color": "rgba(80,80,80,0.7)", "width": 3},
                "showlegend": i == 0,
                "hoverinfo": "skip",
                "legendgroup": "gas",
            }
        )
    for i, (x, y, z) in enumerate(rings_out + gens_out):
        traces.append(
            {
                "type": "scatter3d",
                "mode": "lines",
                "name": "SUS304 wall",
                "x": x.tolist(),
                "y": y.tolist(),
                "z": z.tolist(),
                "line": {"color": "rgba(120,120,120,0.45)", "width": 2, "dash": "dot"},
                "showlegend": i == 0,
                "hoverinfo": "skip",
                "legendgroup": "wall",
            }
        )
    xs = [-2.54, 2.54, 2.54, -2.54, -2.54]
    ys = [Y0, Y0, Y1, Y1, Y0]
    zs = [Z_SRC] * 5
    traces.append(
        {
            "type": "scatter3d",
            "mode": "lines",
            "name": "source plane",
            "x": xs,
            "y": ys,
            "z": zs,
            "line": {"color": "#9e9ac8", "width": 4},
            "hoverinfo": "name",
        }
    )
    return traces


def write_html(traces, path: Path):
    layout = {
        "title": "He-3 / SUS304 — PHITS 4dtrack (first 100 histories)",
        "scene": {
            "xaxis": {"title": "x [cm]", "range": [-8, 8]},
            "yaxis": {"title": "y [cm] (tube axis)", "range": [-22, 22]},
            "zaxis": {"title": "z [cm] (beam)", "range": [-20, 6]},
            "aspectmode": "manual",
            "aspectratio": {"x": 0.55, "y": 1.6, "z": 0.95},
            "camera": {
                "eye": {"x": 1.6, "y": 1.2, "z": 0.9},
                "up": {"x": 0, "y": 1, "z": 0},
            },
        },
        "legend": {"title": {"text": "click to toggle"}},
        "margin": {"l": 0, "r": 0, "t": 50, "b": 0},
        "template": "plotly_white",
    }
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8"/>
<title>He-3 detector 3D tracks</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  html, body, #plot {{ margin:0; height:100%; width:100%; font-family: sans-serif; }}
  .note {{ position:absolute; left:12px; bottom:12px; z-index:2; background:rgba(255,255,255,.85);
           padding:8px 12px; font-size:13px; border-radius:6px; }}
</style>
</head>
<body>
<div id="plot"></div>
<div class="note">青: 中性子　赤: 陽子　緑: トリトン　橙: 光子<br>
凡例クリックで表示切替。マウスで回転・ズーム。</div>
<script>
const data = {json.dumps(traces)};
const layout = {json.dumps(layout)};
Plotly.newPlot("plot", data, layout, {{responsive: true}});
</script>
</body>
</html>
"""
    path.write_text(html, encoding="utf-8")


def plot_matplotlib(histories, path: Path):
    fig = plt.figure(figsize=(11, 8))
    ax = fig.add_subplot(111, projection="3d")
    plotted = set()
    for h in histories:
        for tr in h["tracks"]:
            pts = clip_track(tr["pts"])
            if len(pts) < 2:
                continue
            xs, ys, zs = zip(*[(p[0], p[1], p[2]) for p in pts])
            name = tr["name"]
            label = name if name not in plotted else None
            plotted.add(name)
            lw = 0.6 if name == "neutron" else (2.0 if name in ("proton", "triton") else 0.8)
            alpha = 0.25 if name == "neutron" else 0.85
            ax.plot(xs, ys, zs, color=COLORS.get(name, "gray"), lw=lw, alpha=alpha, label=label)

    th = np.linspace(0, 2 * np.pi, 80)
    for y in (Y0, Y1):
        ax.plot(R_IN * np.cos(th), np.full_like(th, y), R_IN * np.sin(th), color="k", lw=1.0, alpha=0.7)
        ax.plot(R_OUT * np.cos(th), np.full_like(th, y), R_OUT * np.sin(th), color="k", lw=0.6, ls=":", alpha=0.5)
    for t in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        ax.plot(
            [R_IN * np.cos(t), R_IN * np.cos(t)],
            [Y0, Y1],
            [R_IN * np.sin(t), R_IN * np.sin(t)],
            color="k",
            lw=0.7,
            alpha=0.5,
        )
    ax.plot(
        [-2.54, 2.54, 2.54, -2.54, -2.54],
        [Y0, Y0, Y1, Y1, Y0],
        [Z_SRC] * 5,
        color="#9e9ac8",
        lw=1.4,
        label="source",
    )
    ax.set_xlabel("x [cm]")
    ax.set_ylabel("y [cm] (tube axis)")
    ax.set_zlabel("z [cm] (beam)")
    ax.set_title("He-3 / SUS304 — PHITS 4dtrack (first 100 histories)")
    ax.legend(loc="upper left", fontsize=9)
    ax.view_init(elev=18, azim=-55)
    ax.set_xlim(-8, 8)
    ax.set_ylim(-22, 22)
    ax.set_zlim(-20, 6)
    ax.set_box_aspect((16, 44, 26))
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def plot_capture_zoom(histories, path: Path):
    """捕獲点付近だけ拡大（陽子・トリトンの飛程が見える）。"""
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection="3d")
    plotted = set()
    for h in histories:
        cap = None
        for tr in h["tracks"]:
            if tr["name"] in ("proton", "triton") and tr["pts"]:
                cap = np.array(tr["pts"][0][:3])
                break
        if cap is None:
            continue
        for tr in h["tracks"]:
            if tr["name"] not in ("proton", "triton"):
                continue
            pts = np.array([(p[0], p[1], p[2]) for p in tr["pts"]])
            label = tr["name"] if tr["name"] not in plotted else None
            plotted.add(tr["name"])
            ax.plot(pts[:, 0], pts[:, 1], pts[:, 2], color=COLORS[tr["name"]], lw=1.6, label=label)
            ax.scatter(*pts[0], color=COLORS[tr["name"]], s=8, depthshade=False)
    th = np.linspace(0, 2 * np.pi, 80)
    ax.plot(R_IN * np.cos(th), np.zeros_like(th), R_IN * np.sin(th), color="k", lw=1.0, alpha=0.5, label="inner wall (y=0)")
    ax.set_xlabel("x [cm]")
    ax.set_ylabel("y [cm]")
    ax.set_zlabel("z [cm]")
    ax.set_title("Capture zoom: proton (red) and triton (green)")
    ax.legend(fontsize=9)
    ax.view_init(elev=22, azim=-40)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def main():
    histories = parse_4dt(FOURDT)
    print(f"histories: {len(histories)} from {FOURDT}")
    traces = traces_for_plotly(histories)
    html_path = OUT / "3d_tracks.html"
    write_html(traces, html_path)
    png1 = OUT / "3d_tracks.png"
    png2 = OUT / "3d_capture_zoom.png"
    plot_matplotlib(histories, png1)
    plot_capture_zoom(histories, png2)
    print(f"wrote {html_path}")
    print(f"wrote {png1}")
    print(f"wrote {png2}")


if __name__ == "__main__":
    main()
