#!/usr/bin/env python3
"""公式キャンパス案内図の上に測定地点を重ねた HTML を生成する。

地図 PNG は 05_施設図/Campus_Map_J_2026_05.pdf から抽出する。
座標は tables/測定地点マスタ.csv の map_x_pct / map_y_pct で管理する。
"""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "測定_20260818"
TABLES = OUT / "tables"
FIGURES = OUT / "figures"
MASTER = TABLES / "測定地点マスタ.csv"
HTML_OUT = OUT / "測定地点マップ.html"
PDF = ROOT.parent / "05_施設図" / "Campus_Map_J_2026_05.pdf"
MAP_PNG = FIGURES / "campus_official_2026_05.png"


def extract_campus_png() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    if not PDF.exists():
        sys.exit(f"公式地図 PDF が見つかりません: {PDF}")
    subprocess.run(
        [
            "gs",
            "-dNOPAUSE",
            "-dBATCH",
            "-sDEVICE=png16m",
            "-r300",
            "-dFirstPage=1",
            "-dLastPage=1",
            f"-sOutputFile={MAP_PNG}",
            str(PDF),
        ],
        check=True,
    )


def load_sites() -> list[dict]:
    with MASTER.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def render_html(sites: list[dict]) -> str:
    on_campus = [s for s in sites if s.get("地図_x_pct") and s.get("地図_y_pct")]
    rows = []
    for s in sites:
        roi = s.get("ROI_net_cps") or ""
        if roi:
            try:
                roi = f"{float(roi):.3f}"
            except ValueError:
                pass
        rows.append(
            f"""        <tr data-site="{s['site_id']}">
          <td>{s['表示名']}</td>
          <td>{s.get('公式棟No') or '—'}</td>
          <td>{s.get('公式番地') or '—'}</td>
          <td>{s['標高_m']}</td>
          <td>{s['GLからの高さ_m'] or '0'}</td>
          <td>{s['覆土深さ_m'] or '0'}</td>
          <td>{s['屋内_屋外']}</td>
          <td>{roi or '—'}</td>
        </tr>"""
        )

    pin_js = []
    for s in on_campus:
        alt = s.get("昨年参照") == "昨年"
        pin_js.append(
            f"""      {{
        id: {s['site_id']!r},
        name: {s['表示名']!r},
        code: {s.get('公式棟No') or ''!r},
        x: {float(s['地図_x_pct'])},
        y: {float(s['地図_y_pct'])},
        alt: {str(alt).lower()}
      }}"""
        )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>測定地点マップ — KEK 2026-08</title>
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #f4f4f4;
      --card: #fff;
      --line: #ccc;
      --muted: #555;
      --accent: #1f4e79;
      --pin: #c0392b;
      --pin-ring: #fff;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{ --bg: #1a1a1a; --card: #242424; --line: #444; --muted: #aaa; }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: system-ui, sans-serif;
      max-width: 52rem;
      margin: 1rem auto 2rem;
      padding: 0 0.75rem;
      line-height: 1.5;
      background: var(--bg);
    }}
    h1 {{ font-size: 1.2rem; margin-bottom: 0.2rem; }}
    h2 {{ font-size: 0.95rem; margin: 1.25rem 0 0.4rem; color: var(--accent); }}
    .lead {{ color: var(--muted); font-size: 0.88rem; margin-bottom: 0.75rem; }}
    .source {{
      font-size: 0.8rem;
      color: var(--muted);
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 0.5rem 0.65rem;
      background: var(--card);
      margin-bottom: 0.75rem;
    }}
    .axis-box {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.45rem;
      font-size: 0.78rem;
      margin-bottom: 0.75rem;
    }}
    @media (max-width: 640px) {{ .axis-box {{ grid-template-columns: 1fr; }} }}
    .axis-box div {{
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 0.45rem;
      background: var(--card);
    }}
    .axis-box strong {{ display: block; color: var(--accent); font-size: 0.75rem; }}
    .map-wrap {{
      position: relative;
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
      background: #fff;
    }}
    .map-wrap img {{
      display: block;
      width: 100%;
      height: auto;
    }}
    .overlay {{
      position: absolute;
      inset: 0;
      pointer-events: none;
    }}
    .pin {{
      position: absolute;
      transform: translate(-50%, -100%);
      pointer-events: auto;
      cursor: pointer;
      text-align: center;
    }}
    .pin-dot {{
      width: 14px;
      height: 14px;
      margin: 0 auto;
      border-radius: 50%;
      background: var(--pin);
      border: 2px solid var(--pin-ring);
      box-shadow: 0 0 0 1px var(--pin);
    }}
    .pin.active .pin-dot {{
      width: 18px;
      height: 18px;
      background: #e67e22;
      box-shadow: 0 0 0 2px #e67e22;
    }}
    .pin-label {{
      font-size: 0.62rem;
      font-weight: 700;
      color: #111;
      background: rgba(255,255,255,0.92);
      border: 1px solid #999;
      border-radius: 3px;
      padding: 0 0.25rem;
      margin-bottom: 2px;
      white-space: nowrap;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.78rem;
      background: var(--card);
    }}
    th, td {{
      border: 1px solid var(--line);
      padding: 0.3rem 0.4rem;
      text-align: left;
    }}
    th {{ background: var(--accent); color: #fff; }}
    tr[data-site] {{ cursor: pointer; }}
    tr.highlight {{ background: rgba(192, 57, 43, 0.12); }}
    .panel {{
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
      margin-top: 0.5rem;
    }}
    code {{ font-size: 0.85em; }}
  </style>
</head>
<body>
  <h1>測定地点マップ（公式案内図ベース）</h1>
  <p class="lead">
    背景は KEK 公式案内図（Ver.2026.05）。赤ピンは 2026-08-18〜19 の MCA 測定地点。
    座標は <code>tables/測定地点マスタ.csv</code> で編集し、
    <code>python3 _build_site_map.py</code> で再生成する。
  </p>

  <div class="source">
    出典: <code>05_施設図/Campus_Map_J_2026_05.pdf</code>
    （大学共同利用機関法人 高エネルギー加速器研究機構案内図）<br>
    画像: <code>figures/campus_official_2026_05.png</code>
  </div>

  <div class="axis-box">
    <div><strong>① 標高 h</strong>海面から [m]。KEK ≈ 30 m</div>
    <div><strong>② GL+ z</strong>地面から上 [m]。2階 ≈ +4 m</div>
    <div><strong>③ 覆土 d</strong>地面より下 [m]。8/18 測定はすべて 0</div>
  </div>

  <h2>公式案内図 + 測定点</h2>
  <div class="map-wrap" id="map">
    <img src="figures/campus_official_2026_05.png" alt="KEK公式案内図 Ver.2026.05">
    <div class="overlay" id="pins"></div>
  </div>
  <p class="lead" style="margin-top:0.4rem">ピンまたは表の行をクリックで対応付け。座標の微調整は CSV の <code>地図_x_pct</code>, <code>地図_y_pct</code>（画像左上=0,0、右下=100,100）。</p>

  <h2>地点一覧</h2>
  <div class="panel">
    <table>
      <thead>
        <tr>
          <th>地点</th><th>棟No</th><th>番地</th>
          <th>h [m]</th><th>z [m]</th><th>d [m]</th><th>内外</th><th>ROI net CPS</th>
        </tr>
      </thead>
      <tbody>
{chr(10).join(rows)}
      </tbody>
    </table>
  </div>

  <script>
    const SITES = [
{",".join(pin_js)}
    ];

    const pinRoot = document.getElementById("pins");

    function highlight(id) {{
      document.querySelectorAll("tr[data-site]").forEach(r => {{
        r.classList.toggle("highlight", r.dataset.site === id);
      }});
      document.querySelectorAll(".pin").forEach(p => {{
        p.classList.toggle("active", p.dataset.site === id);
      }});
    }}

    SITES.forEach(s => {{
      const el = document.createElement("div");
      el.className = "pin";
      el.dataset.site = s.id;
      el.style.left = s.x + "%";
      el.style.top = s.y + "%";
      el.innerHTML = `<div class="pin-label">${{s.code ? s.code + " " : ""}}${{s.name}}</div><div class="pin-dot"></div>`;
      el.title = s.name;
      el.addEventListener("click", () => highlight(s.id));
      pinRoot.appendChild(el);
    }});

    document.querySelectorAll("tr[data-site]").forEach(r => {{
      r.addEventListener("click", () => highlight(r.dataset.site));
    }});
  </script>
</body>
</html>
"""


def main() -> None:
    extract_campus_png()
    sites = load_sites()
    HTML_OUT.write_text(render_html(sites), encoding="utf-8")
    print(f"Wrote {HTML_OUT}")
    print(f"Map image: {MAP_PNG}")


if __name__ == "__main__":
    main()
