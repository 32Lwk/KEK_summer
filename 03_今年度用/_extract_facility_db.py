#!/usr/bin/env python3
"""05_施設図 PDF と Campus_Map から施設 3D データベースを生成する。

出力 (tables/):
  - 施設3D_建物マスタ.csv   … 全棟（グリッド中心・デフォルト外形）
  - 施設3D_遮蔽層.csv       … PDF 由来の遮蔽層（出典明記）
  - 施設3D_評価点.csv       … 線量評価点
  - 施設3D_地質層.json      … 地下地質モデル
  - 施設3D_施設詳細/*.json  … PDF 施設ごとの詳細 3D 定義
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

from campus_geo import grid_to_pct, pct_to_scene

ROOT = Path(__file__).resolve().parent
FACILITY_PDF = ROOT.parent / "05_施設図"
TABLES = ROOT / "測定_20260818" / "tables"
DETAIL_DIR = TABLES / "施設3D_施設詳細"

# --- デフォルト外形 (grid 配置棟) -------------------------------------------
DEFAULT_SIZE = {
    "default": (18, 14, 8),
    "power": (14, 12, 7),       # MR・D*, SM 電源棟
    "mechanical": (16, 14, 8),  # *M 機械棟
    "experiment": (28, 22, 10),
    "storage": (12, 10, 6),
    "large": (40, 30, 12),
    "linac": (22, 135, 14),
    "ring_tunnel": (0, 0, 0),   # torus で別描画
}


def _size_for(code: str, name: str) -> tuple[float, float, float]:
    if code == "H02":
        return DEFAULT_SIZE["linac"]
    if re.search(r"MR・D\d|電源棟", name):
        return DEFAULT_SIZE["power"]
    if re.search(r"SM\d|機械棟|コンプレッサー", name):
        return DEFAULT_SIZE["mechanical"]
    if re.search(r"実験|研究本館|4号館|ホール", name):
        return DEFAULT_SIZE["experiment"]
    if re.search(r"保管|倉庫|ボンベ|更衣", name):
        return DEFAULT_SIZE["storage"]
    if re.search(r"光源棟|入射器|管理棟|体育館|食堂", name):
        return DEFAULT_SIZE["large"]
    return DEFAULT_SIZE["default"]


def _parse_grid(grid: str) -> tuple[float, float]:
    """'a-5', 'a-5・6・7', 'b-2・c-2' → (x_pct, y_pct) 平均。"""
    parts = re.split(r"[・·]", grid)
    xs, ys = [], []
    for p in parts:
        m = re.match(r"([a-d])-(\d+)", p.strip())
        if m:
            xp, yp = grid_to_pct(m.group(1), int(m.group(2)))
            xs.append(xp)
            ys.append(yp)
    if not xs:
        return 50.0, 50.0
    return sum(xs) / len(xs), sum(ys) / len(ys)


def parse_campus_buildings() -> list[dict]:
    from pypdf import PdfReader

    pdf = FACILITY_PDF / "Campus_Map_J_2026_05.pdf"
    reader = PdfReader(str(pdf))
    text = reader.pages[1].extract_text() or ""
    text = text.replace("･", "・").replace("Ｇ", "G").replace("Ｃ", "C")
    text = re.sub(r"\s+", " ", text)

    entries: list[dict] = []
    seen: set[str] = set()
    for m in re.finditer(
        r"([A-N]\d{2})\s+([a-d](?:-\d+(?:[・·][a-z\d-]+)?)?)\s+(.+?)(?=\s+[A-N]\d{2}\s+[a-d]-|\s*$)",
        text,
    ):
        code, grid, name = m.group(1), m.group(2), m.group(3).strip()
        name = re.sub(r"\s+[A-N]\s*$", "", name).strip()
        if code in seen:
            continue
        seen.add(code)
        zone = code[0]
        x_pct, y_pct = _parse_grid(grid)
        w, d, h = _size_for(code, name)
        entries.append({
            "id": code,
            "name": name,
            "棟No": code,
            "zone": zone,
            "番地": grid,
            "x_pct": round(x_pct, 2),
            "y_pct": round(y_pct, 2),
            "width_m": w,
            "depth_m": d,
            "height_m": h,
            "elev_bottom_m": -2 if code == "H02" else 0,
            "source": "Campus_Map_J_2026_05.pdf (Ver.2026.05) 番地グリッド中心",
            "footprint_confidence": "grid_default",
            "wall_status": "unknown",
        })
    return sorted(entries, key=lambda r: r["id"])


# --- PDF 由来の遮蔽・評価点（手動整理＋PDF 表引用） -------------------------
# BT.pdf 表 2.1, 2.2 (p.34-35)
BT_SHIELDING = [
    ("BT", "LER_ring", "S1", "E1", "コンクリート", 50, "cm", "BT.pdf 表2.1 p.34", "LER側 S1→E1"),
    ("BT", "LER_ring", "S1", "E1", "土", 640, "cm", "BT.pdf 表2.1 p.34", "LER側 S1→E1"),
    ("BT", "LER_ring", "S2", "E2", "コンクリート", 50, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "LER_ring", "S2", "E2", "土", 480, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "LER_ring", "S3", "E3", "コンクリート", 40, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "LER_ring", "S3", "E3", "土", 213, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "HER_ring", "S1", "E1", "コンクリート", 50, "cm", "BT.pdf 表2.1 p.34", "HER側"),
    ("BT", "HER_ring", "S1", "E1", "土", 640, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "HER_ring", "S3", "E3", "コンクリート", 40, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "HER_ring", "S7", "E7", "コンクリート", 43, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "HER_ring", "S8", "E8", "コンクリート", 100, "cm", "BT.pdf 表2.1 p.34", "距離22.5m+土15m"),
    ("BT", "HER_ring", "S10", "E10", "コンクリート", 50, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "HER_ring", "S11", "E11", "鉄", 3, "cm", "BT.pdf 表2.1 p.34", ""),
    ("BT", "HER_ring", "S12", "E12", "コンクリート", 200, "cm", "BT.pdf 表2.1 p.34", "距離35m"),
    ("BT", "PF-AR", "S15", "E15A", "コンクリート", 80, "cm", "BT.pdf 表2.1 p.34", "図1.18"),
    ("BT", "LER_ring", "S4", "E4", "コンクリート", 100, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "LER_ring", "S4", "E4", "土", 50, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "LER_ring", "S5", "E5", "コンクリート", 60, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "LER_ring", "S5", "E5", "土", 90, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "LER_ring", "S6", "E6", "コンクリート", 60, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "LER_ring", "S6", "E6", "土", 220, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "HER_ring", "S13", "E13", "コンクリート", 65, "cm", "BT.pdf 表2.2 p.35", "図1.15"),
    ("BT", "HER_ring", "S13", "E13", "土", 705, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "HER_ring", "S13", "E13", "鉄", 24, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "LER_ring", "S14", "E14", "コンクリート", 65, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "LER_ring", "S14", "E14", "土", 705, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "LER_ring", "S14", "E14", "鉄", 19, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "PF-AR", "S15", "E15B", "コンクリート", 60, "cm", "BT.pdf 表2.2 p.35", "図1.16"),
    ("BT", "PF-AR", "S15", "E15B", "土", 96, "cm", "BT.pdf 表2.2 p.35", ""),
    ("BT", "PF-AR", "S15", "E15C", "コンクリート", 170, "cm", "BT.pdf 表2.2 p.35", "図1.17"),
    ("BT", "PF-AR", "S15", "E15D", "コンクリート", 140, "cm", "BT.pdf 表2.2 p.35", "図1.19"),
]

# PS.pdf 表 2-1-1, 2-1-2 (FEL)
PS_SHIELDING = [
    ("PS", "FEL", "S1", "E4", "コンクリート", 70, "cm", "PS.pdf 表2-1-1 p.35", "第1 25度偏向電磁石"),
    ("PS", "FEL", "S1", "E4", "鉛", 20, "cm", "PS.pdf 表2-1-1 p.35", ""),
    ("PS", "FEL", "S2", "E5", "コンクリート", 70, "cm", "PS.pdf 表2-1-1 p.35", ""),
    ("PS", "FEL", "S2", "E5", "鉛", 20, "cm", "PS.pdf 表2-1-1 p.35", ""),
    ("PS", "FEL", "S3", "E6", "コンクリート", 70, "cm", "PS.pdf 表2-1-1 p.35", "最大 0.99 µSv/h"),
    ("PS", "FEL", "S3", "E6", "鉛", 20, "cm", "PS.pdf 表2-1-1 p.35", ""),
    ("PS", "FEL", "S1", "E9", "コンクリート", 50, "cm", "PS.pdf 表2-1-1 p.35", ""),
    ("PS", "FEL", "S1", "E1", "コンクリート", 65, "cm", "PS.pdf 表2-1-2 p.36", ""),
    ("PS", "FEL", "S1", "E1", "鉛", 30, "cm", "PS.pdf 表2-1-2 p.36", ""),
    ("PS", "FEL", "S1", "E13", "コンクリート", 65, "cm", "PS.pdf 表2-1-2 p.36", ""),
    ("PS", "FEL", "S1", "E13", "鉄", 15, "cm", "PS.pdf 表2-1-2 p.36", ""),
    ("PS", "FEL", "S1", "E13", "鉛", 5, "cm", "PS.pdf 表2-1-2 p.36", ""),
]

# PF.pdf ストレージリング遮蔽
PF_SHIELDING = [
    ("PF", "storage_ring", "injection", "E_side", "コンクリート", 70, "cm", "PF.pdf 表2-1 p.41", "入射点側面"),
    ("PF", "storage_ring", "injection", "G_front", "コンクリート", 200, "cm", "PF.pdf 表2-1 p.41", "入射点前方"),
    ("PF", "storage_ring", "slit", "M_lab", "コンクリート", 33, "cm", "PF.pdf 表2-1 p.41", "有効厚"),
    ("PF", "storage_ring", "slit", "M_lab", "鉄", 8.8, "cm", "PF.pdf 表2-1 p.41", "有効厚"),
    ("PF", "storage_ring", "dump", "A5", "コンクリート", 190, "cm", "PF.pdf 表2-2 p.42", "有効厚"),
    ("PF", "storage_ring", "dump", "A5", "鉄", 54, "cm", "PF.pdf 表2-2 p.42", "有効厚"),
    ("PF", "storage_ring", "beamline", "H", "鉛", 20, "cm", "PF.pdf p.36", "ビームライン周囲"),
    ("PF", "RI", "storage", "A-B", "コンクリート", 16, "cm", "PF.pdf p.46-47", "線源保管室隣室"),
    ("PF", "RI", "storage", "C-D", "コンクリート", 36, "cm", "PF.pdf p.47", "16+20cm 合算"),
]

# DR.pdf 表 3.4 (p.49)
DR_SHIELDING = [
    ("DR", "ring", "tunnel", "E1", "コンクリート", 85, "cm", "DR.pdf 表3.4 p.49", "DR棟 EV→SR"),
    ("DR", "ring", "tunnel", "E1", "鉄", 10, "cm", "DR.pdf 表3.4 p.49", ""),
    ("DR", "ring", "tunnel", "E1", "土", 500, "cm", "DR.pdf 表3.4 p.49", ""),
    ("DR", "ring", "SR_hall", "E4", "コンクリート", 40, "cm", "DR.pdf 表3.5 p.50", "40×40 cm"),
    ("DR", "ring", "LTR", "A-B", "コンクリート", 100, "cm", "DR.pdf p.39", "LTR/RTL 上部"),
    ("DR", "ring", "LTR", "A-B", "土", 210, "cm", "DR.pdf p.39", "床面下"),
]

# ATF.pdf 図1.8
ATF_SHIELDING = [
    ("ATF", "linac", "target", "section", "コンクリート", 300, "cm", "ATF.pdf 図1.8 p.12", "3m 加速管区間"),
    ("ATF", "linac", "target", "section", "鉛", 5, "cm", "ATF.pdf 図1.8 p.12", "加速管"),
    ("ATF", "linac", "target", "section", "鉛", 20, "cm", "ATF.pdf 図1.8 p.12", ""),
    ("ATF", "linac", "target", "section", "鉛", 10, "cm", "ATF.pdf 図1.8 p.12", ""),
    ("ATF", "linac", "target", "section", "鉄", 50, "cm", "ATF.pdf 図1.8 p.12", "厚さ50"),
]

# Linac.pdf — ビームトンネル（鉄筋コンクリート、深さは配置図より推定）
LINAC_SHIELDING = [
    ("Linac", "H02", "tunnel", "beam", "コンクリート", 100, "cm", "Linac.pdf 図1.9 等", "ビームトンネル側壁（推定・要図面確認）"),
    ("Linac", "H02", "building", "1F", "コンクリート", 20, "cm", "Linac.pdf + 解析レポート", "入射器棟外壁（推定・要現地確認）"),
]

# SKEKB — KEKB リングトンネル（BT/SKEKB 共通）
SKEKB_SHIELDING = [
    ("SKEKB", "KEKB_ring", "LER", "S1-E1", "コンクリート", 50, "cm", "SKEKB.pdf / BT.pdf 表2.1", "LER 側壁"),
    ("SKEKB", "KEKB_ring", "HER", "S8-E8", "コンクリート", 100, "cm", "SKEKB.pdf / BT.pdf 表2.1", ""),
    ("SKEKB", "KEKB_ring", "HER", "S12-E12", "コンクリート", 200, "cm", "SKEKB.pdf / BT.pdf 表2.1", ""),
]

# 先端計測実験棟 — 国立大学法人等施設実態調査
SENTAN_SHIELDING = [
    ("先端計測", "N15", "B1", "wall", "コンクリート", 30, "cm", "先端計測実験棟.pdf", "地下1階平面図（様式3）外壁推定"),
    ("先端計測", "N15", "B2", "wall", "コンクリート", 30, "cm", "先端計測実験棟.pdf", "地下2階"),
]

ALL_SHIELDING = BT_SHIELDING + PS_SHIELDING + PF_SHIELDING + DR_SHIELDING + ATF_SHIELDING + LINAC_SHIELDING + SKEKB_SHIELDING + SENTAN_SHIELDING

MATERIAL_COLOR = {
    "コンクリート": "#95a5a6",
    "土": "#8B6914",
    "鉄": "#566573",
    "鉛": "#2c3e50",
    "ポリエチレン": "#ecf0f1",
}


def geology_layers() -> dict:
    return {
        "source": "KEK地下測定_地質予測.xlsx / 地質_KEK シート",
        "layers": [
            {"id": "loam", "name": "関東ローム", "top_m": 0, "bottom_m": -3, "density_g_cm3": 1.35, "color": "#c4a574", "lambda_m": 1.09},
            {"id": "joso", "name": "常総粘土", "top_m": -3, "bottom_m": -5, "density_g_cm3": 1.65, "color": "#8b7355", "lambda_m": 0.89},
            {"id": "shimousa", "name": "下総層群", "top_m": -5, "bottom_m": -10, "density_g_cm3": 1.85, "color": "#6b5344", "lambda_m": 0.80},
        ],
        "reference": "宇野沢ほか1988、坂田ほか2018/2024、筑波台地標準層序",
    }


def _tunnel_cross_section(facility_id: str, name: str, pdf: str, inner_w: float, inner_h: float, layers: list) -> dict:
    """材質別同心矩形断面（トンネル用）。"""
    return {
        "id": facility_id,
        "name": name,
        "source_pdf": pdf,
        "type": "tunnel_cross_section",
        "inner_width_m": inner_w,
        "inner_height_m": inner_h,
        "layers": layers,
    }


def build_facility_details() -> dict[str, dict]:
    """PDF 施設ごとの詳細 3D 定義。"""
    details: dict[str, dict] = {}

    details["BT"] = {
        "id": "BT",
        "name": "Beam Transport (KEKB BT)",
        "source_pdf": "05_施設図/BT.pdf",
        "map_anchor": {"x_pct": 46.5, "y_pct": 42.5, "棟No": "", "notes": "KEKB リング周辺 BT 区域"},
        "tunnel": {
            "type": "torus",
            "majorR_m": 88,
            "minorR_m": 5,
            "yCenter_m": -8,
            "innerR_m": 3.5,
        },
        "evaluation_points": [
            {"id": "E1", "label": "E1 (LER S1)", "ring": "LER"},
            {"id": "E6", "label": "E6 (LER S6)", "ring": "LER"},
            {"id": "E13", "label": "E13 (HER S13)", "ring": "HER"},
            {"id": "E15A", "label": "E15A (PF-AR)", "ring": "PF-AR"},
        ],
        "cross_sections": [
            _tunnel_cross_section("BT_LER_S1", "LER S1→E1 断面", "BT.pdf 図1.8", 5.0, 4.0, [
                {"material": "コンクリート", "thickness_cm": 50, "source": "BT.pdf 表2.1"},
                {"material": "土", "thickness_cm": 640, "source": "BT.pdf 表2.1"},
            ]),
            _tunnel_cross_section("BT_HER_S11", "HER S11→E11 断面", "BT.pdf 図1.14", 4.5, 3.8, [
                {"material": "鉄", "thickness_cm": 3, "source": "BT.pdf 表2.1"},
            ]),
        ],
        "tables_ref": ["表2.1 p.34", "表2.2 p.35", "図1.8-1.19"],
    }

    details["Linac"] = {
        "id": "Linac",
        "name": "電子陽電子 Linear Accelerator",
        "source_pdf": "05_施設図/Linac.pdf",
        "map_anchor": {"x_pct": 20.5, "y_pct": 74.0, "棟No": "H02"},
        "building": {"width_m": 22, "depth_m": 135, "height_m": 14, "yBottom_m": -2},
        "tunnel": {"type": "box", "width_m": 10, "depth_m": 95, "height_m": 8, "yBottom_m": -4},
        "evaluation_points": [{"id": "D1", "label": "Linac D1", "notes": "施設図上の評価点（MCA D1 とは別）"}],
        "cross_sections": [
            _tunnel_cross_section("Linac_tunnel", "ビームトンネル断面", "Linac.pdf", 3.0, 2.5, [
                {"material": "コンクリート", "thickness_cm": 100, "source": "Linac.pdf 図1.9（推定）"},
            ]),
        ],
    }

    details["PF"] = {
        "id": "PF",
        "name": "放射光科学研究施設 (PF)",
        "source_pdf": "05_施設図/PF.pdf",
        "map_anchor": {"x_pct": 24.0, "y_pct": 50.0, "棟No": "H04"},
        "building": {"width_m": 58, "depth_m": 40, "height_m": 16, "yBottom_m": 0},
        "ring": {"type": "torus", "majorR_m": 50, "minorR_m": 4, "yCenter_m": -5},
        "evaluation_points": [
            {"id": "E_side", "label": "入射点側面"},
            {"id": "M_lab", "label": "光源棟実験室"},
        ],
        "cross_sections": [
            _tunnel_cross_section("PF_injection", "入射点側面", "PF.pdf 図1-10", 6.0, 5.0, [
                {"material": "コンクリート", "thickness_cm": 70, "source": "PF.pdf 表2-1"},
            ]),
            _tunnel_cross_section("PF_dump", "ダンプ A5", "PF.pdf 図2-1", 8.0, 6.0, [
                {"material": "コンクリート", "thickness_cm": 190, "source": "PF.pdf 表2-2 有効厚"},
                {"material": "鉄", "thickness_cm": 54, "source": "PF.pdf 表2-2 有効厚"},
            ]),
        ],
    }

    details["PS"] = {
        "id": "PS",
        "name": "陽子シンクロトロン施設 (PS)",
        "source_pdf": "05_施設図/PS.pdf",
        "map_anchor": {"x_pct": 50.0, "y_pct": 45.0, "棟No": "K01-K32 区域"},
        "evaluation_points": [
            {"id": "E4", "label": "FEL E4", "dose_uSv_h": 0.77},
            {"id": "E6", "label": "FEL E6", "dose_uSv_h": 0.99},
            {"id": "L", "label": "評価点 L"},
        ],
        "cross_sections": [
            _tunnel_cross_section("PS_FEL", "FEL 加速器室", "PS.pdf 図1-12", 5.0, 4.0, [
                {"material": "コンクリート", "thickness_cm": 70, "source": "PS.pdf 表2-1-1"},
                {"material": "鉛", "thickness_cm": 20, "source": "PS.pdf 表2-1-1"},
            ]),
        ],
        "notes": "ビームライントンネルは鉄筋コンクリート製 (PS.pdf p.35)",
    }

    details["DR"] = {
        "id": "DR",
        "name": "Positron Damping Ring (DR)",
        "source_pdf": "05_施設図/DR.pdf",
        "map_anchor": {"x_pct": 35.0, "y_pct": 48.0, "棟No": "H12-H15"},
        "evaluation_points": [{"id": "E1", "label": "DR E1"}, {"id": "E4", "label": "SR E4"}],
        "cross_sections": [
            _tunnel_cross_section("DR_tunnel", "DR→SR 断面", "DR.pdf 表3.4", 4.0, 3.5, [
                {"material": "コンクリート", "thickness_cm": 85, "source": "DR.pdf 表3.4"},
                {"material": "鉄", "thickness_cm": 10, "source": "DR.pdf 表3.4"},
                {"material": "土", "thickness_cm": 500, "source": "DR.pdf 表3.4"},
            ]),
        ],
    }

    details["ATF"] = {
        "id": "ATF",
        "name": "Advanced Test Facility (ATF)",
        "source_pdf": "05_施設図/ATF.pdf",
        "map_anchor": {"x_pct": 40.0, "y_pct": 38.0, "棟No": "KEKB 区域"},
        "cross_sections": [
            _tunnel_cross_section("ATF_linac", "ATF 加速管区間", "ATF.pdf 図1.8", 5.5, 3.5, [
                {"material": "コンクリート", "thickness_cm": 300, "source": "ATF.pdf 図1.8 (3m)"},
                {"material": "鉛", "thickness_cm": 20, "source": "ATF.pdf 図1.8"},
                {"material": "鉄", "thickness_cm": 50, "source": "ATF.pdf 図1.8"},
            ]),
        ],
    }

    details["SKEKB"] = {
        "id": "SKEKB",
        "name": "Super KEKB",
        "source_pdf": "05_施設図/SKEKB.pdf",
        "map_anchor": {"x_pct": 47.0, "y_pct": 40.0, "棟No": ""},
        "tunnel": {"type": "torus", "majorR_m": 88, "minorR_m": 5, "yCenter_m": -8},
        "evaluation_points": [
            {"id": "D1", "label": "評価点 D1"},
            {"id": "D2", "label": "評価点 D2"},
        ],
        "cross_sections": [
            _tunnel_cross_section("SKEKB_LER", "LER 側壁", "SKEKB.pdf / BT.pdf", 4.0, 3.5, [
                {"material": "コンクリート", "thickness_cm": 50, "source": "BT.pdf 表2.1"},
            ]),
            _tunnel_cross_section("SKEKB_HER", "HER S12", "SKEKB.pdf / BT.pdf", 4.0, 3.5, [
                {"material": "コンクリート", "thickness_cm": 200, "source": "BT.pdf 表2.1"},
            ]),
        ],
    }

    details["先端計測"] = {
        "id": "先端計測",
        "name": "先端計測実験棟",
        "source_pdf": "05_施設図/先端計測実験棟.pdf",
        "map_anchor": {"x_pct": 55.0, "y_pct": 52.0, "棟No": "I15/N15"},
        "building": {"width_m": 30, "depth_m": 20, "height_m": 12, "yBottom_m": -7},
        "cross_sections": [
            _tunnel_cross_section("sentan_B1", "地下1階 RI測定室", "先端計測実験棟.pdf", 8.38, 7.25, [
                {"material": "コンクリート", "thickness_cm": 30, "source": "先端計測実験棟.pdf 地下1階平面図"},
            ]),
        ],
    }

    return details


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    DETAIL_DIR.mkdir(parents=True, exist_ok=True)

    buildings = parse_campus_buildings()
    write_csv(
        TABLES / "施設3D_建物マスタ.csv",
        ["id", "name", "棟No", "zone", "番地", "x_pct", "y_pct",
         "width_m", "depth_m", "height_m", "elev_bottom_m",
         "source", "footprint_confidence", "wall_status"],
        buildings,
    )

    shield_rows = []
    for i, row in enumerate(ALL_SHIELDING):
        fac, part, src, ev, mat, thick, unit, source, notes = row
        shield_rows.append({
            "layer_id": f"SH{i+1:03d}",
            "facility": fac,
            "part": part,
            "source_point": src,
            "eval_point": ev,
            "material": mat,
            "thickness": thick,
            "unit": unit,
            "source_ref": source,
            "notes": notes,
            "color": MATERIAL_COLOR.get(mat, "#888888"),
        })
    write_csv(
        TABLES / "施設3D_遮蔽層.csv",
        ["layer_id", "facility", "part", "source_point", "eval_point",
         "material", "thickness", "unit", "source_ref", "notes", "color"],
        shield_rows,
    )

    eval_rows = []
    for s in shield_rows:
        if s["eval_point"] and s["eval_point"] not in {e["eval_point"] for e in eval_rows if e["facility"] == s["facility"]}:
            eval_rows.append({
                "facility": s["facility"],
                "eval_point": s["eval_point"],
                "source_ref": s["source_ref"],
            })
    write_csv(
        TABLES / "施設3D_評価点.csv",
        ["facility", "eval_point", "source_ref"],
        eval_rows,
    )

    geo = geology_layers()
    (TABLES / "施設3D_地質層.json").write_text(
        json.dumps(geo, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    details = build_facility_details()
    for fid, data in details.items():
        out = DETAIL_DIR / f"{fid}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "buildings": len(buildings),
        "shield_layers": len(shield_rows),
        "eval_points": len(eval_rows),
        "facility_details": list(details.keys()),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
