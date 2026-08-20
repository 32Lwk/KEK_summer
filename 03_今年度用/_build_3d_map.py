#!/usr/bin/env python3
"""公式案内図・施設PDFに基づく KEK 施設 3D マップ（2段構成）を生成する。

出力:
  - 測定_20260818/施設3Dマップ.html
  - 測定_20260818/tables/施設3D_シーン.json

事前に python3 _extract_facility_db.py を実行してマスタを更新すること。
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

from campus_geo import MAP_HEIGHT_M, MAP_WIDTH_M, pct_to_scene

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "測定_20260818"
TABLES = OUT / "tables"
FIGURES = OUT / "figures"
MASTER_CSV = TABLES / "施設3D_建物マスタ.csv"
SHIELD_CSV = TABLES / "施設3D_遮蔽層.csv"
GEO_JSON = TABLES / "施設3D_地質層.json"
DETAIL_DIR = TABLES / "施設3D_施設詳細"
SITES_CSV = TABLES / "測定地点マスタ.csv"
JSON_OUT = TABLES / "施設3D_シーン.json"
HTML_OUT = OUT / "施設3Dマップ.html"
MAP_PNG = FIGURES / "campus_official_2026_05.png"
PDF = ROOT.parent / "05_施設図" / "Campus_Map_J_2026_05.pdf"

# 棟No / 名称 → 詳細施設 PDF ID
DETAIL_LINK: dict[str, str] = {
    "H02": "Linac", "H01": "Linac", "H04": "PF", "H05": "PF", "H06": "PF",
    "H12": "DR", "H13": "DR", "H14": "DR", "H15": "DR",
    "I15": "先端計測",
}

FACILITY_ANCHORS: dict[str, tuple[float, float]] = {
    "BT": (46.5, 42.5),
    "SKEKB": (47.0, 40.0),
    "Linac": (20.5, 74.0),
    "PF": (24.0, 50.0),
    "PS": (50.0, 45.0),
    "DR": (35.0, 48.0),
    "ATF": (40.0, 38.0),
    "先端計測": (55.0, 52.0),
}


def ensure_campus_png() -> None:
    if MAP_PNG.exists():
        return
    FIGURES.mkdir(parents=True, exist_ok=True)
    if not PDF.exists():
        sys.exit(f"PDF not found: {PDF}")
    subprocess.run(
        [
            "gs", "-dNOPAUSE", "-dBATCH", "-sDEVICE=png16m", "-r300",
            "-dFirstPage=1", "-dLastPage=1",
            f"-sOutputFile={MAP_PNG}", str(PDF),
        ],
        check=True,
    )


def _f(row: dict, key: str, default: float = 0.0) -> float:
    v = row.get(key, "")
    if v is None or v == "":
        return default
    return float(v)


def load_buildings() -> list[dict]:
    rows: list[dict] = []
    with MASTER_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            x, z = pct_to_scene(_f(row, "x_pct"), _f(row, "y_pct"))
            code = row["id"]
            detail = DETAIL_LINK.get(code, "")
            if not detail and "PF" in row.get("name", ""):
                detail = "PF"
            item: dict = {
                "id": code,
                "name": row["name"],
                "code": code,
                "type": "box",
                "x": round(x, 2),
                "z": round(z, 2),
                "zone": row.get("zone", ""),
                "color": _zone_color(row.get("zone", "")),
                "source": row.get("source", ""),
                "notes": row.get("番地", ""),
                "width": _f(row, "width_m", 18),
                "depth": _f(row, "depth_m", 14),
                "height": _f(row, "height_m", 8),
                "yBottom": _f(row, "elev_bottom_m"),
                "rotDeg": 0.0,
                "wallStatus": row.get("wall_status", "unknown"),
                "detailFacility": detail,
            }
            rows.append(item)
    return rows


def _zone_color(zone: str) -> str:
    colors = {
        "A": "#e74c3c", "B": "#e67e22", "C": "#3498db", "D": "#2ecc71",
        "E": "#2980b9", "F": "#27ae60", "G": "#f1c40f", "H": "#7f8c8d",
        "I": "#1abc9c", "J": "#e91e63", "K": "#9b59b6", "L": "#5dade2",
        "M": "#d35400", "N": "#16a085",
    }
    return colors.get(zone, "#888888")


def load_underground() -> list[dict]:
    return [
        {
            "id": "KEKB_ring", "name": "KEKBリング", "type": "torus",
            "x": pct_to_scene(47.0, 40.0)[0], "z": pct_to_scene(47.0, 40.0)[1],
            "zone": "E", "color": "#2980b9",
            "source": "BT.pdf 図1.2 + SKEKB.pdf",
            "notes": "major R=88m minor=5m 床面y=-8m",
            "majorR": 88.0, "minorR": 5.0, "yCenter": -8.0,
            "detailFacility": "SKEKB",
        },
        {
            "id": "PFAR_ring", "name": "PF-ARリング", "type": "torus",
            "x": pct_to_scene(35.0, 38.0)[0], "z": pct_to_scene(35.0, 38.0)[1],
            "zone": "G", "color": "#9b59b6",
            "source": "Campus_Map + PF.pdf",
            "notes": "major R=50m 床面y=-5m",
            "majorR": 50.0, "minorR": 4.0, "yCenter": -5.0,
            "detailFacility": "PF",
        },
        {
            "id": "linac_beam", "name": "Linacビームトンネル", "type": "box",
            "x": pct_to_scene(21.0, 68.0)[0], "z": pct_to_scene(21.0, 68.0)[1],
            "zone": "H", "color": "#566573",
            "source": "Linac.pdf",
            "notes": "入射器地下部 深さ≈4m",
            "width": 10.0, "depth": 95.0, "height": 8.0, "yBottom": -4.0, "rotDeg": 0.0,
            "detailFacility": "Linac",
        },
        {
            "id": "BT_zone", "name": "BT区域（KEKB周辺）", "type": "marker",
            "x": pct_to_scene(46.5, 42.5)[0], "z": pct_to_scene(46.5, 42.5)[1],
            "zone": "E", "color": "#1f4e79",
            "source": "BT.pdf",
            "detailFacility": "BT",
        },
    ]


def load_shielding() -> list[dict]:
    if not SHIELD_CSV.exists():
        return []
    with SHIELD_CSV.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_geology() -> dict:
    if GEO_JSON.exists():
        return json.loads(GEO_JSON.read_text(encoding="utf-8"))
    return {"layers": []}


def load_facility_details() -> dict:
    details = {}
    if not DETAIL_DIR.exists():
        return details
    for p in DETAIL_DIR.glob("*.json"):
        details[p.stem] = json.loads(p.read_text(encoding="utf-8"))
    return details


def load_measurements() -> list[dict]:
    rows: list[dict] = []
    with SITES_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            xp, yp = row.get("地図_x_pct"), row.get("地図_y_pct")
            if not xp or not yp:
                continue
            x, z = pct_to_scene(float(xp), float(yp))
            gl = _f(row, "GLからの高さ_m")
            burial = _f(row, "覆土深さ_m")
            y = gl if burial <= 0 else -burial
            roi = row.get("ROI_net_cps") or ""
            rows.append({
                "id": row["site_id"],
                "name": row["表示名"],
                "code": row.get("公式棟No") or "",
                "x": round(x, 2), "y": round(y, 2), "z": round(z, 2),
                "h_m": _f(row, "標高_m", 30),
                "gl_m": gl, "burial_m": burial,
                "indoor": row.get("屋内_屋外") == "屋内",
                "roi": float(roi) if roi else None,
                "year": "2025" if row.get("昨年参照") == "昨年" else "2026",
            })
    return rows


def build_scene() -> dict:
    return {
        "meta": {
            "title": "KEK 施設 3D マップ",
            "sources": [
                "05_施設図/Campus_Map_J_2026_05.pdf (Ver.2026.05)",
                "05_施設図/BT.pdf, Linac.pdf, PF.pdf, PS.pdf, DR.pdf, ATF.pdf, SKEKB.pdf, 先端計測実験棟.pdf",
                "tables/施設3D_建物マスタ.csv, 施設3D_遮蔽層.csv",
                "KEK地下測定_地質予測.xlsx（地質層）",
            ],
            "mapWidthM": MAP_WIDTH_M,
            "mapHeightM": MAP_HEIGHT_M,
            "axes": "X=東, Y=上（GL+）, Z=南",
            "north": "-Z",
            "seaLevelAtCampusM": 30,
            "groundTexture": "figures/campus_official_2026_05.png",
        },
        "buildings": load_buildings(),
        "underground": load_underground(),
        "shielding": load_shielding(),
        "geology": load_geology(),
        "facilityDetails": load_facility_details(),
        "facilityAnchors": {
            k: {"x_pct": v[0], "y_pct": v[1]} for k, v in FACILITY_ANCHORS.items()
        },
        "measurements": load_measurements(),
    }


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KEK 施設 3D マップ</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { width: 100%; height: 100%; overflow: hidden; font-family: system-ui, sans-serif; }
    #canvas-wrap { width: 100%; height: 100%; }
    #hud {
      position: fixed; top: 10px; left: 10px; max-width: 340px;
      background: rgba(255,255,255,0.93); border: 1px solid #bbb;
      border-radius: 8px; padding: 10px 12px; font-size: 12px; line-height: 1.45; z-index: 10;
    }
    #hud h1 { font-size: 14px; margin-bottom: 4px; color: #1f4e79; }
    #hud .muted { color: #555; font-size: 11px; }
    #panel {
      position: fixed; bottom: 10px; left: 10px; right: 10px; max-width: 640px;
      background: rgba(255,255,255,0.95); border: 1px solid #bbb;
      border-radius: 8px; padding: 8px 12px; font-size: 12px; z-index: 10;
      max-height: 35vh; overflow-y: auto;
    }
    #panel strong { color: #1f4e79; }
    #panel .shield-row { font-size: 11px; padding: 2px 0; border-bottom: 1px solid #eee; }
    .controls {
      position: fixed; top: 10px; right: 10px; z-index: 10;
      display: flex; flex-direction: column; gap: 6px; max-height: 90vh; overflow-y: auto;
    }
    .controls label, .controls button {
      background: rgba(255,255,255,0.93); border: 1px solid #bbb;
      border-radius: 6px; padding: 6px 10px; font-size: 12px; cursor: pointer;
    }
    .controls button { text-align: left; font-weight: 600; color: #1f4e79; }
    .controls button:hover { background: #eef5fb; }
    .label-3d {
      color: #111; font-size: 10px; font-weight: 600;
      background: rgba(255,255,255,0.85); padding: 1px 4px;
      border-radius: 3px; border: 1px solid #999;
      pointer-events: none; white-space: nowrap;
    }
    #detail-banner {
      position: fixed; top: 10px; left: 50%; transform: translateX(-50%);
      background: #1f4e79; color: #fff; padding: 6px 16px; border-radius: 20px;
      font-size: 13px; font-weight: 600; z-index: 11; display: none;
    }
    @media (prefers-color-scheme: dark) {
      #hud, #panel, .controls label, .controls button { background: rgba(30,30,30,0.93); color: #eee; border-color: #555; }
      #hud h1, #panel strong { color: #7ec8ff; }
      .label-3d { background: rgba(20,20,20,0.9); color: #eee; border-color: #666; }
    }
  </style>
</head>
<body>
  <div id="hud">
    <h1>KEK 施設 3D マップ</h1>
    <div class="muted">Campus_Map Ver.2026.05 + 施設PDF遮蔽データ</div>
    <div class="muted">左ドラッグ: 回転 / 右: 平行 / ホイール: ズーム</div>
    <div class="muted">建物クリック → 詳細3D（遮蔽層・評価点）</div>
    <div class="muted" id="view-mode">モード: キャンパス概観</div>
  </div>
  <div id="detail-banner"></div>
  <div class="controls">
    <button type="button" id="btn-campus">↩ キャンパス概観に戻る</button>
    <label><input type="checkbox" id="tog-buildings" checked> 地上建物 (__N_BUILDINGS__)</label>
    <label><input type="checkbox" id="tog-underground" checked> 地下トンネル・リング</label>
    <label><input type="checkbox" id="tog-geology" checked> 地質層（地下）</label>
    <label><input type="checkbox" id="tog-measure" checked> 測定点 (2026)</label>
    <label><input type="checkbox" id="tog-labels"> ラベル（主要のみ）</label>
    <hr style="border:none;border-top:1px solid #ccc;margin:2px 0">
    <div style="font-size:11px;color:#555;padding:2px 4px">詳細施設 (PDF)</div>
    __FACILITY_BUTTONS__
  </div>
  <div id="panel"><strong>選択:</strong> <span id="sel-info">—</span><div id="shield-list"></div></div>
  <div id="canvas-wrap"></div>

  <script type="importmap">
  { "imports": {
      "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
      "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
  }}
  </script>
  <script type="module">
    import * as THREE from 'three';
    import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
    import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

    const SCENE = __SCENE_JSON__;
    const MAP_W = SCENE.meta.mapWidthM;
    const MAP_H = SCENE.meta.mapHeightM;

    const wrap = document.getElementById('canvas-wrap');
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(wrap.clientWidth, wrap.clientHeight);
    renderer.shadowMap.enabled = true;
    wrap.appendChild(renderer.domElement);

    const labelRenderer = new CSS2DRenderer();
    labelRenderer.setSize(wrap.clientWidth, wrap.clientHeight);
    labelRenderer.domElement.style.cssText = 'position:absolute;top:0;pointer-events:none';
    wrap.appendChild(labelRenderer.domElement);

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xc8dce8);
    scene.fog = new THREE.Fog(0xc8dce8, 400, 1200);

    const camera = new THREE.PerspectiveCamera(50, wrap.clientWidth / wrap.clientHeight, 0.5, 3000);
    const campusCam = { pos: [-120, 200, 240], target: [20, -5, 0] };
    camera.position.set(...campusCam.pos);

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.target.set(...campusCam.target);
    controls.maxPolarAngle = Math.PI / 2.02;
    controls.update();

    scene.add(new THREE.AmbientLight(0xffffff, 0.55));
    const sun = new THREE.DirectionalLight(0xffffff, 0.85);
    sun.position.set(-200, 300, 100);
    sun.castShadow = true;
    scene.add(sun);

    const groups = {
      campus: new THREE.Group(),
      buildings: new THREE.Group(),
      underground: new THREE.Group(),
      geology: new THREE.Group(),
      measurements: new THREE.Group(),
      labels: new THREE.Group(),
      detail: new THREE.Group(),
      helpers: new THREE.Group(),
    };
    groups.campus.add(groups.buildings, groups.underground, groups.geology, groups.measurements, groups.labels, groups.helpers);
    scene.add(groups.campus, groups.detail);

    const pickables = [];
    let detailMode = false;

    function addLabel(parent, text, x, y, z) {
      const div = document.createElement('div');
      div.className = 'label-3d';
      div.textContent = text;
      const obj = new CSS2DObject(div);
      obj.position.set(x, y, z);
      parent.add(obj);
      return obj;
    }

    // --- 地面 ---
    new THREE.TextureLoader().load(SCENE.meta.groundTexture, (tex) => {
      tex.colorSpace = THREE.SRGBColorSpace;
      const ground = new THREE.Mesh(
        new THREE.PlaneGeometry(MAP_W, MAP_H),
        new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95 })
      );
      ground.rotation.x = -Math.PI / 2;
      ground.receiveShadow = true;
      groups.buildings.add(ground);
    });

    const glGrid = new THREE.GridHelper(Math.max(MAP_W, MAP_H), 24, 0x888888, 0xcccccc);
    glGrid.position.y = 0.05;
    groups.helpers.add(glGrid);
    groups.helpers.add(new THREE.ArrowHelper(
      new THREE.Vector3(0,0,-1), new THREE.Vector3(-MAP_W/2+20,1,-MAP_H/2+20), 25, 0xcc0000
    ));

    // --- 地質層 ---
    (SCENE.geology.layers || []).forEach(layer => {
      const h = layer.top_m - layer.bottom_m;
      const mesh = new THREE.Mesh(
        new THREE.BoxGeometry(MAP_W * 0.95, h, MAP_H * 0.95),
        new THREE.MeshStandardMaterial({
          color: layer.color || '#8B6914',
          transparent: true, opacity: 0.22, roughness: 0.9,
        })
      );
      mesh.position.y = (layer.top_m + layer.bottom_m) / 2;
      mesh.userData = { kind: 'geology', ...layer };
      groups.geology.add(mesh);
    });

    // --- 建物 ---
    const MAJOR_CODES = new Set(['L01','M01','H02','H04','K01','E27','N02','I15']);
    SCENE.buildings.forEach(b => {
      const yBottom = b.yBottom ?? 0;
      const geo = new THREE.BoxGeometry(b.width, b.height, b.depth);
      const unknown = b.wallStatus === 'unknown';
      const mat = new THREE.MeshStandardMaterial({
        color: b.color, transparent: true,
        opacity: unknown ? 0.45 : 0.78, roughness: 0.7,
      });
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(b.x, yBottom + b.height / 2, b.z);
      mesh.rotation.y = THREE.MathUtils.degToRad(b.rotDeg || 0);
      mesh.castShadow = true;
      mesh.userData = { kind: 'building', ...b };
      if (unknown) {
        const edges = new THREE.LineSegments(
          new THREE.EdgesGeometry(geo),
          new THREE.LineBasicMaterial({ color: 0xe67e22, transparent: true, opacity: 0.5 })
        );
        mesh.add(edges);
      }
      groups.buildings.add(mesh);
      pickables.push(mesh);
      if (MAJOR_CODES.has(b.code)) {
        addLabel(groups.labels, `${b.code}`, b.x, yBottom + b.height + 1.5, b.z);
      }
    });

    // --- 地下 ---
    SCENE.underground.forEach(u => {
      if (u.type === 'torus') {
        const mesh = new THREE.Mesh(
          new THREE.TorusGeometry(u.majorR, u.minorR, 12, 64),
          new THREE.MeshStandardMaterial({ color: u.color, transparent: true, opacity: 0.5 })
        );
        mesh.rotation.x = Math.PI / 2;
        mesh.position.set(u.x, u.yCenter, u.z);
        mesh.userData = { kind: 'tunnel', ...u };
        groups.underground.add(mesh);
        pickables.push(mesh);
      } else if (u.type === 'box') {
        const mesh = new THREE.Mesh(
          new THREE.BoxGeometry(u.width, u.height, u.depth),
          new THREE.MeshStandardMaterial({ color: u.color, transparent: true, opacity: 0.55 })
        );
        mesh.position.set(u.x, u.yBottom + u.height/2, u.z);
        mesh.userData = { kind: 'tunnel', ...u };
        groups.underground.add(mesh);
        pickables.push(mesh);
      } else if (u.type === 'marker') {
        const sph = new THREE.Mesh(
          new THREE.SphereGeometry(6, 12, 12),
          new THREE.MeshStandardMaterial({ color: u.color, emissive: u.color, emissiveIntensity: 0.3 })
        );
        sph.position.set(u.x, 3, u.z);
        sph.userData = { kind: 'facility_marker', ...u };
        groups.underground.add(sph);
        pickables.push(sph);
        addLabel(groups.labels, 'BT', u.x, 10, u.z);
      }
    });

    // --- 測定点 ---
    SCENE.measurements.filter(m => m.year === '2026').forEach(m => {
      const col = m.indoor ? 0xc0392b : 0x27ae60;
      const sphere = new THREE.Mesh(
        new THREE.SphereGeometry(2.5, 16, 16),
        new THREE.MeshStandardMaterial({ color: col, emissive: col, emissiveIntensity: 0.3 })
      );
      sphere.position.set(m.x, m.y + 2.5, m.z);
      sphere.userData = { kind: 'measurement', ...m };
      groups.measurements.add(sphere);
      pickables.push(sphere);
      addLabel(groups.labels, m.name, m.x, m.y + 7, m.z);
    });

    // --- 詳細ビュー: 材質別遮蔽層 ---
    function clearDetail() {
      while (groups.detail.children.length) groups.detail.remove(groups.detail.children[0]);
    }

    function showFacilityDetail(facId) {
      const fac = SCENE.facilityDetails[facId];
      if (!fac) return;
      clearDetail();
      detailMode = true;
      groups.campus.visible = false;
      groups.detail.visible = true;
      document.getElementById('detail-banner').style.display = 'block';
      document.getElementById('detail-banner').textContent = `${fac.name} — 詳細3D（${fac.source_pdf}）`;
      document.getElementById('view-mode').textContent = `モード: 施設詳細 (${facId})`;

      const cx = 0, cy = 0, cz = 0;
      // 断面: 同心箱型レイヤー
      (fac.cross_sections || []).forEach((sec, si) => {
        const ox = si * 25 - ((fac.cross_sections.length-1) * 12.5);
        let w = sec.inner_width_m, h = sec.inner_height_m, d = 8;
        const base = new THREE.Mesh(
          new THREE.BoxGeometry(w, h, d),
          new THREE.MeshStandardMaterial({ color: 0x3498db, transparent: true, opacity: 0.35 })
        );
        base.position.set(ox, h/2, cz);
        groups.detail.add(base);
        addLabel(groups.detail, sec.id, ox, h + 2, cz);

        let layerOffset = 0;
        (sec.layers || []).forEach(layer => {
          const t = (layer.thickness_cm || 0) / 100;
          w += t * 2; h += t * 2; d += t * 2;
          layerOffset += t;
          const col = { 'コンクリート': 0x95a5a6, '土': 0x8B6914, '鉄': 0x566573, '鉛': 0x2c3e50 }[layer.material] || 0x888888;
          const shell = new THREE.Mesh(
            new THREE.BoxGeometry(w, h, d),
            new THREE.MeshStandardMaterial({ color: col, transparent: true, opacity: 0.65, roughness: 0.6 })
          );
          shell.position.set(ox, h/2, cz);
          shell.userData = { kind: 'shield_layer', material: layer.material, thickness_cm: layer.thickness_cm, source: layer.source };
          groups.detail.add(shell);
          pickables.push(shell);
        });
      });

      // 評価点マーカー
      (fac.evaluation_points || []).forEach((ep, i) => {
        const m = new THREE.Mesh(
          new THREE.SphereGeometry(0.8, 12, 12),
          new THREE.MeshStandardMaterial({ color: 0xff4444, emissive: 0xff0000, emissiveIntensity: 0.4 })
        );
        m.position.set(-15 + i * 5, 1, 6);
        m.userData = { kind: 'eval_point', ...ep, facility: facId };
        groups.detail.add(m);
        pickables.push(m);
        addLabel(groups.detail, ep.label || ep.id, m.position.x, 3, m.position.z);
      });

      camera.position.set(40, 25, 50);
      controls.target.set(0, 5, 0);
      controls.update();
      updateShieldPanel(facId);
    }

    function returnToCampus() {
      detailMode = false;
      clearDetail();
      groups.campus.visible = true;
      groups.detail.visible = false;
      document.getElementById('detail-banner').style.display = 'none';
      document.getElementById('view-mode').textContent = 'モード: キャンパス概観';
      camera.position.set(...campusCam.pos);
      controls.target.set(...campusCam.target);
      controls.update();
      document.getElementById('sel-info').textContent = '—';
      document.getElementById('shield-list').innerHTML = '';
    }

    groups.detail.visible = false;

    document.getElementById('btn-campus').onclick = returnToCampus;
    document.querySelectorAll('[data-facility]').forEach(btn => {
      btn.onclick = () => showFacilityDetail(btn.dataset.facility);
    });

    document.getElementById('tog-buildings').onchange = e => { groups.buildings.visible = e.target.checked; };
    document.getElementById('tog-underground').onchange = e => { groups.underground.visible = e.target.checked; };
    document.getElementById('tog-geology').onchange = e => { groups.geology.visible = e.target.checked; };
    document.getElementById('tog-measure').onchange = e => { groups.measurements.visible = e.target.checked; };
    document.getElementById('tog-labels').onchange = e => { groups.labels.visible = e.target.checked; };

    const selInfo = document.getElementById('sel-info');
    const shieldList = document.getElementById('shield-list');

    function updateShieldPanel(facId) {
      const rows = SCENE.shielding.filter(s => s.facility === facId);
      shieldList.innerHTML = rows.length
        ? '<div style="margin-top:6px"><strong>遮蔽層一覧（出典付き）:</strong></div>' +
          rows.map(r => `<div class="shield-row">${r.eval_point}: ${r.material} ${r.thickness}${r.unit} — <em>${r.source_ref}</em> ${r.notes||''}</div>`).join('')
        : '';
    }

    renderer.domElement.addEventListener('click', (ev) => {
      const rect = renderer.domElement.getBoundingClientRect();
      const pointer = new THREE.Vector2(
        ((ev.clientX - rect.left) / rect.width) * 2 - 1,
        -((ev.clientY - rect.top) / rect.height) * 2 + 1
      );
      const raycaster = new THREE.Raycaster();
      raycaster.setFromCamera(pointer, camera);
      const hits = raycaster.intersectObjects(pickables);
      if (!hits.length) return;
      const u = hits[0].object.userData;
      if (u.kind === 'measurement') {
        selInfo.textContent = `${u.name} | GL+${u.gl_m}m 覆土${u.burial_m}m | ROI=${u.roi?.toFixed(3)??'—'}`;
      } else if (u.kind === 'shield_layer') {
        selInfo.textContent = `${u.material} ${u.thickness_cm}cm — 出典: ${u.source}`;
      } else if (u.kind === 'eval_point') {
        selInfo.textContent = `評価点 ${u.label||u.id} (${u.facility})`;
      } else if (u.detailFacility && SCENE.facilityDetails[u.detailFacility]) {
        showFacilityDetail(u.detailFacility);
      } else if (u.kind === 'building') {
        selInfo.textContent = `${u.code} ${u.name} | ${u.source} | 壁: ${u.wallStatus==='unknown'?'出典なし・要確認':'—'}`;
        if (u.detailFacility) showFacilityDetail(u.detailFacility);
      } else if (u.kind === 'tunnel' || u.kind === 'facility_marker') {
        selInfo.textContent = `${u.name} | ${u.source}`;
        if (u.detailFacility) showFacilityDetail(u.detailFacility);
      }
    });

    function onResize() {
      const w = wrap.clientWidth, h = wrap.clientHeight;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
      labelRenderer.setSize(w, h);
    }
    window.addEventListener('resize', onResize);

    (function animate() {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
      labelRenderer.render(scene, camera);
    })();
  </script>
</body>
</html>
"""


def render_html(scene: dict) -> str:
    n = len(scene["buildings"])
    fac_ids = sorted(scene.get("facilityDetails", {}).keys())
    buttons = "\n".join(
        f'    <button type="button" data-facility="{fid}">{fid}</button>'
        for fid in fac_ids
    )
    html = HTML_TEMPLATE.replace("__N_BUILDINGS__", str(n))
    html = html.replace("__FACILITY_BUTTONS__", buttons)
    html = html.replace("__SCENE_JSON__", json.dumps(scene, ensure_ascii=False))
    return html


def main() -> None:
    if not MASTER_CSV.exists():
        print("Run _extract_facility_db.py first", file=sys.stderr)
        sys.exit(1)
    ensure_campus_png()
    scene = build_scene()
    JSON_OUT.write_text(json.dumps(scene, ensure_ascii=False, indent=2), encoding="utf-8")
    HTML_OUT.write_text(render_html(scene), encoding="utf-8")
    print(f"Wrote {HTML_OUT}")
    print(f"Wrote {JSON_OUT}")
    print(f"  buildings={len(scene['buildings'])}, shield_layers={len(scene['shielding'])}, "
          f"facilities={len(scene['facilityDetails'])}")


if __name__ == "__main__":
    main()
