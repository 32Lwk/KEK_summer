#!/usr/bin/env python3
"""He-3 比例計数管 + 信管（PMT）の推定ジオメトリ。

命名（測定ファイル名規則と同じ）:
  小文字 d … 小径検出器（SN 2162 系）
  大文字 D … 大径検出器（SN 1715 系）
  末尾 1 … PE 緩衝なし
  末尾 2 … PE あり（d2=薄肉筒、D2=実寸ポリエチレン容器）

座標: 筒軸 = z（床 z=0 から直立）。
信管: Hamamatsu R580 級（大径）を参考。小径は長さ比から比例推定。
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

# --- 小径 d（旧 he3_sus304 / SN 2162 級）---
SMALL_LENGTH_CM = 39.53
SMALL_R_OUT_CM = 2.74
SMALL_T_WALL_CM = 0.2
SMALL_L_PMT_CM = 8.5   # 信管占領長（推定・下記 README 参照）
SMALL_R_PMT_CM = 1.25  # 1 inch 級 PMT 想定（He 内半径 2.54 cm 未満）

# --- 大径 D（ユーザー指定 / SN 1715 級）---
LARGE_LENGTH_CM = 66.0
LARGE_R_OUT_CM = 5.0
LARGE_T_WALL_CM = 0.2
LARGE_L_PMT_CM = 10.0  # R580 全長 ~100 mm 級（推定）
LARGE_R_PMT_CM = 1.9   # R580 外径 38 mm → 半径 1.9 cm（以前 3.8 cm は mm 誤読）

# He-3 ガス内部圧 [atm]（実測値）
HE3_PRESSURE_ATM = 10
# PHITS ライブラリ基準密度 [g/cm³] @ 1 atm（pegs5 RHO=1.24e-3）
HE3_RHO_1ATM_G_CM3 = 0.00124
COMMON_RHO_HE3 = HE3_RHO_1ATM_G_CM3 * HE3_PRESSURE_ATM  # 0.0124 @ 10 atm

# d2: SUS 外側に厚み 5 cm の PE 筒
PE_WRAP_THICKNESS_CM = 5.0

# D2: 実測ポリエチレン緩衝容器（ユーザー指定）
D2_PE_OD_CM = 29.0
D2_PE_ID_CM = 15.0
D2_PE_HEIGHT_CM = 80.0
D2_PE_BORE_HEIGHT_CM = 74.0


@dataclass(frozen=True)
class DetectorSpec:
    key: str
    label: str
    size_class: str  # "small" | "large"
    length_cm: float
    r_out_cm: float
    t_wall_cm: float
    l_pmt_cm: float
    r_pmt_cm: float
    rho_he3: float
    pe_style: Literal["none", "wrap", "block"]
    pe_thickness_cm: float = 0.0
    pe_block_od_cm: float = 0.0
    pe_block_id_cm: float = 0.0
    pe_block_h_cm: float = 0.0
    pe_block_bore_h_cm: float = 0.0
    notes: str = ""

    @property
    def r_in_cm(self) -> float:
        return self.r_out_cm - self.t_wall_cm

    @property
    def active_length_cm(self) -> float:
        return self.length_cm - self.l_pmt_cm

    @property
    def has_pe(self) -> bool:
        return self.pe_style != "none"

    @property
    def r_pe_out_cm(self) -> float:
        if self.pe_style == "wrap":
            return self.r_out_cm + self.pe_thickness_cm
        if self.pe_style == "block":
            return self.pe_block_od_cm / 2.0
        return self.r_out_cm

    @property
    def r_pe_in_cm(self) -> float:
        if self.pe_style == "block":
            return self.pe_block_id_cm / 2.0
        return self.r_out_cm


def _small(**kwargs) -> dict:
    return {
        "size_class": "small",
        "length_cm": SMALL_LENGTH_CM,
        "r_out_cm": SMALL_R_OUT_CM,
        "t_wall_cm": SMALL_T_WALL_CM,
        "l_pmt_cm": SMALL_L_PMT_CM,
        "r_pmt_cm": SMALL_R_PMT_CM,
        "rho_he3": COMMON_RHO_HE3,
        **kwargs,
    }


def _large(**kwargs) -> dict:
    return {
        "size_class": "large",
        "length_cm": LARGE_LENGTH_CM,
        "r_out_cm": LARGE_R_OUT_CM,
        "t_wall_cm": LARGE_T_WALL_CM,
        "l_pmt_cm": LARGE_L_PMT_CM,
        "r_pmt_cm": LARGE_R_PMT_CM,
        "rho_he3": COMMON_RHO_HE3,
        **kwargs,
    }


DETECTORS: dict[str, DetectorSpec] = {
    "d1": DetectorSpec(
        key="d1",
        label="d1（小径・PE なし）",
        pe_style="none",
        notes="SN 2162 系。He-3 + SUS304 + 信管",
        **_small(),
    ),
    "d2": DetectorSpec(
        key="d2",
        label="d2（小径・PE 薄肉筒 5 cm）",
        pe_style="wrap",
        pe_thickness_cm=PE_WRAP_THICKNESS_CM,
        notes=f"SN 2162 系 + SUS 外 PE {PE_WRAP_THICKNESS_CM} cm",
        **_small(),
    ),
    "D1": DetectorSpec(
        key="D1",
        label="D1（大径・PE なし）",
        pe_style="none",
        notes="SN 1715 系。He-3 + SUS304 + 信管",
        **_large(),
    ),
    "D2": DetectorSpec(
        key="D2",
        label="D2（大径・PE 容器）",
        pe_style="block",
        pe_block_od_cm=D2_PE_OD_CM,
        pe_block_id_cm=D2_PE_ID_CM,
        pe_block_h_cm=D2_PE_HEIGHT_CM,
        pe_block_bore_h_cm=D2_PE_BORE_HEIGHT_CM,
        notes=(
            f"SN 1715 系 + PE 容器 OD{D2_PE_OD_CM} ID{D2_PE_ID_CM} "
            f"H{D2_PE_HEIGHT_CM} 内高{D2_PE_BORE_HEIGHT_CM} cm"
        ),
        **_large(),
    ),
}

DETECTOR_SUBDIR: dict[str, str] = {
    "d1": "small/d1",
    "d2": "small/d2",
    "D1": "large/D1",
    "D2": "large/D2",
}


def detector_result_tag(key: str) -> str:
    """CSV/図ファイル名用（macOS 大文字小文字非区別対策: small_d1 vs large_D1）。"""
    return DETECTOR_SUBDIR[key].replace("/", "_")


def detector_root(base: Path, key: str) -> Path:
    return base / DETECTOR_SUBDIR[key]


def detector_set_lines(spec: DetectorSpec) -> str:
    lines = [
        f"$ 検出器 {spec.label}: 高さ={spec.length_cm} cm OD={2 * spec.r_out_cm:.1f} cm（z 軸直立）",
        f"$ 信管 半径={spec.r_pmt_cm} cm 占領長={spec.l_pmt_cm} cm（He 内径 {2 * spec.r_in_cm:.1f} cm より小）",
        f"$ 有効 He-3 長 ~{spec.active_length_cm:.1f} cm",
        f"set: c31[{spec.length_cm}] c32[{spec.r_out_cm}] c33[{spec.t_wall_cm}] c34[c32-c33]",
        f"set: c35[{spec.l_pmt_cm}] c36[{spec.r_pmt_cm}]",
        "set: c37[0.0] c38[c31] c39[c38-c35]",
    ]
    if spec.pe_style == "wrap":
        lines.append(f"set: c41[{spec.pe_thickness_cm}] c42[c32+c41]")
    elif spec.pe_style == "block":
        lines.extend(
            [
                f"set: c41[{spec.pe_block_h_cm}] c42[{spec.pe_block_od_cm}/2] c43[{spec.pe_block_id_cm}/2]",
                f"set: c44[{spec.pe_block_bore_h_cm}]",
            ]
        )
    return "\n".join(lines)


def detector_surfaces(spec: DetectorSpec, *, include_pmt: bool = True) -> str:
    lines = [
        " 11   rcc  0  0  c37   0  0  c31  c34",
        " 12   rcc  0  0  c37   0  0  c31  c32",
    ]
    if include_pmt:
        lines.extend(
            [
                " 13   pz   c39",
                " 14   rcc  0  0  c39   0  0  c35  c36",
                " 15   pz   c38",
            ]
        )
    else:
        lines.append(" 15   pz   c38")
    if spec.pe_style == "wrap":
        lines.append(" 17   rcc  0  0  c37   0  0  c31  c42")
    elif spec.pe_style == "block":
        lines.extend(
            [
                " 17   rcc  0  0  c37   0  0  c41  c42",
                " 18   rcc  0  0  c37   0  0  c41  c43",
                " 16   pz   c44",
                " 19   pz   c41",
            ]
        )
    return "\n".join(lines)


def detector_cells(
    spec: DetectorSpec,
    *,
    include_pmt: bool = True,
    rho_scale: float = 1.0,
) -> str:
    rho = spec.rho_he3 * rho_scale
    if include_pmt:
        lines = [
            f"  1   5  -{rho:.5f}   -11  -13  20 -15",
            "  2   6  -8.0        11 -12  20 -13",
            "  6   6  -8.0        11 -12  13  14 -15",
            "  4   1  -0.001205     -14  13 -15",
        ]
    else:
        # 地上開空: 信管分割なし（cell 6 での lost 802 回避）
        lines = [
            f"  1   5  -{rho:.5f}   -11  20 -15",
            "  2   6  -8.0        11 -12  20 -15",
        ]
    if spec.pe_style == "wrap":
        lines.append("  5   7  -0.95        12 -17  20 -15")
    elif spec.pe_style == "block":
        lines.extend(
            [
                "  5   7  -0.95        17 -18  20 -19",
                "  7   7  -0.95       -18  20  16 -19",
                "  8   1  -0.001205     -18  12  20 -16",
            ]
        )
    return "\n".join(lines)


def detector_outer_surface(spec: DetectorSpec) -> str:
    if spec.has_pe:
        return "17"
    return "12"


def detector_void_cell(
    tc: float,
    tl: float,
    tj: float,
    spec: DetectorSpec,
) -> str:
    # 室内は空気 (m1)。真空だと遮蔽透過後の熱化・散乱が起きず Deposit が死ぬ。
    if tc + tl + tj == 0 and spec.pe_style == "block":
        return "  3   1  -0.001205     -50  20 -21\n"
    outer = detector_outer_surface(spec)
    if tc + tl + tj == 0:
        return f"  3   1  -0.001205     {outer}  -30  20 -21\n"
    return "  3   1  -0.001205     -50  20 -21\n"
