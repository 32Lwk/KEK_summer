#!/usr/bin/env python3
"""水平天井スラブ + 上から垂直降下中性子の main.inp を検出器別・各地点に生成する。

遮蔽地点では Deposit が統計ゼロになりやすいため、
  - 線源を検出器直上に絞る（c11 を小さく）
  - He-3 密度を一時的に上げる（相対比較時は倍率で補正）
  - PE なし検出器には熱化用 PE 筒を付ける（熱中性子が無いと Deposit が空）
  - 室内を空気にする
を入れる。
"""

from __future__ import annotations

import argparse
from dataclasses import replace
from pathlib import Path

from detector_specs import (
    DETECTORS,
    DetectorSpec,
    detector_cells,
    detector_root,
    detector_set_lines,
    detector_surfaces,
    detector_void_cell,
)

BASE = Path(__file__).resolve().parent

# 遮蔽地点の線源半幅 [cm]（小さいほど検出器付近のサンプリング密度が上がる）
SHIELD_C11_CM = 10.0
GROUND_C11_CM = 30.0
# 遮蔽地点の He-3 密度倍率（アナログ捕獲がほぼ 0 のため）。
# summarize_relative で相対比を出すときはこの倍率で割って地上と比較する。
SHIELD_HE3_RHO_SCALE = 100.0
# PE なし検出器を遮蔽下で使うとき、周囲に付ける熱化用 PE 厚 [cm]
# （rem カウンタ級に厚くしないと 105 cm コンクリ透過後の熱化が足りない）
SHIELD_ENV_PE_CM = 25.0

SITES = [
    {
        "dir": "00_ground",
        "title_suffix": "地上（開空）— 天井なし",
        "tc": 0.0,
        "tl": 0.0,
        "tj": 0.0,
        "maxcas": 20000,
        "maxbch": 20,
    },
    {
        "dir": "01_PF",
        "title_suffix": "PF 天井コンクリ105 cm",
        "tc": 105.0,
        "tl": 0.0,
        "tj": 0.0,
        "maxcas": 10000,
        "maxbch": 10,
    },
    {
        "dir": "02_linac",
        "title_suffix": "linac 天井コンクリ150 cm",
        "tc": 150.0,
        "tl": 0.0,
        "tj": 0.0,
        "maxcas": 10000,
        "maxbch": 10,
    },
    {
        "dir": "03_BT",
        "title_suffix": "BT 天井コンクリ60+ローム220 cm",
        "tc": 60.0,
        "tl": 220.0,
        "tj": 0.0,
        "maxcas": 8000,
        "maxbch": 10,
    },
    {
        "dir": "04_KEKB",
        "title_suffix": "KEKB 天井コンクリ80+ローム400+常総270 cm",
        "tc": 80.0,
        "tl": 400.0,
        "tj": 270.0,
        "maxcas": 6000,
        "maxbch": 10,
    },
]


def site_histories(site: dict, spec: DetectorSpec) -> tuple[int, int]:
    """Web PHITS は 1 ジョブ約 3 分制限。"""
    del spec
    return site["maxcas"], site["maxbch"]


HEADER = """[ Title ]
{title}

[ Parameters ]
 icntl    =   0
 maxcas   = {maxcas}
 maxbch   = {maxbch}
 e-mode   =   2
 irqmd    =   1
 negs     =   2
 igamma   =   1
 itall    =   1
 mdbatima = 3000
 maxbnk   = 100000
 iMeVperU =   1
 esmax    = 100000000.
 emin(12) = 1.0
 emin(13) = 1.0
 emin(15) = 1.0e-3
 emin(16) = 1.0e-3
 emin(17) = 1.0e-3
 emin(18) = 1.0e-3
 emin(19) = 1.0e-3

$ c1=部屋半幅 c11=線源面半幅（検出器付近） c2=室内高 c3=コンクリ…
$ c8=c2+c3, c9=c8+c4, c10=c9+c5, c7=線源高さ
set: c1[400.0] c11[{c11:.1f}] c2[250.0] c3[{tc:.1f}] c4[{tl:.1f}] c5[{tj:.1f}]
set: c8[c2+c3] c9[c8+c4] c10[c9+c5] c7[c10+50.0]
{detector_sets}

[ Source ]
  totfact = -(2*c11)**2
 infl:{{source_ceiling.inp}}
     proj = neutron

[ Material ]
m1
  N  0.7553
  O  0.2318
  Ar 0.0129

m2
  H     -0.023
  C     -0.0023
  O     -1.22
  Na    -0.0368
  Mg    -0.005
  Al    -0.078
  Si    -0.775
  K     -0.0299
  Ca    -0.1
  Fe    -0.032

m3
  H     -0.02
  C     -0.02
  O     -0.50
  Na    -0.01
  Mg    -0.02
  Al    -0.07
  Si    -0.27
  K     -0.02
  Ca    -0.03
  Fe    -0.04

m4
  H     -0.02
  C     -0.02
  O     -0.50
  Na    -0.01
  Mg    -0.02
  Al    -0.07
  Si    -0.27
  K     -0.02
  Ca    -0.03
  Fe    -0.04

m5
  3He  1.0

m6
  Fe 70
  Cr 18
  Ni  9
  Mn  2
  Si  1

m7
  H  2
  C  1

[ Surface ]
  1   so   500.0
{detector_surfaces}
 20   pz   0.0
 21   pz   c2
 22   pz   c8
 23   pz   c9
 24   pz   c10
{extra_surfaces} 30   rpp  -c1  c1  -c1  c1  -50.0  c7+100.0
 50   rpp  -c1  c1  -c1  c1  {room_zmin}  {room_top}

[ Cell ]
{detector_cells}{detector_void}{layer_cells} 99  -1               30

{vr_sections}[ T-Deposit ]
    title = He-3 有効ガス 付与エネルギー（信管側除く）
     mesh =  reg
      reg =  1
   output = deposit
   e-type =    2
       ne =   75
     emin =    0
     emax =  1.5
     file = de.out
     axis =  eng
     unit =    3
   epsout =    1
   dresol = 0.05

[ T-Track ]
    title = He-3 有効ガス 内中性子フラックス
     mesh =  reg
      reg =  1
   e-type =    3
       ne =   80
     emin =  1.0e-9
     emax =  1.0e4
     unit =    1
     axis =  eng
     file = neutron_he3.out
     part = neutron
   epsout =    1

[ End ]
"""


def build_shield_geometry(
    tc: float,
    tl: float,
    tj: float,
    *,
    spec: DetectorSpec,
    include_pmt: bool,
) -> tuple[str, str, str]:
    """遮蔽セルを生成。Returns (extra_surfaces, layer_cells, vr_sections)"""
    del spec, include_pmt
    if tc + tl + tj == 0:
        layer = (
            " 90   1  -0.001205     -30  21\n"
            " 98   3  -1.35       -30 -20\n"
        )
        return "", layer, ""

    cell_lines: list[str] = []
    if tc > 0:
        cell_lines.append(" 20   2  -2.302      -30  21 -22")
    if tl > 0:
        cell_lines.append(" 25   3  -1.35       -30  22 -23")
    if tj > 0:
        cell_lines.append(" 26   4  -1.65       -30  23 -24")

    sky = "24" if tj > 0 else ("23" if tl > 0 else "22")
    cell_lines.append(f" 90   1  -0.001205     -30  {sky}")
    cell_lines.append(" 98   3  -1.35       -30 -20")

    return "", "\n".join(cell_lines) + "\n", ""


def effective_spec(spec: DetectorSpec, *, is_ground: bool) -> DetectorSpec:
    """遮蔽下の PE なし検出器には熱化用 PE 筒を付ける（さもなくば Deposit=0）。"""
    if is_ground or spec.pe_style != "none":
        return spec
    return replace(spec, pe_style="wrap", pe_thickness_cm=SHIELD_ENV_PE_CM)


def build_site_inp(site: dict, spec: DetectorSpec) -> str:
    title = f"{site['title_suffix']} + {spec.label}"
    is_ground = site["tc"] + site["tl"] + site["tj"] == 0
    include_pmt = not is_ground
    maxcas, maxbch = site_histories(site, spec)
    spec_run = effective_spec(spec, is_ground=is_ground)
    extra_surfaces, layer_cells, vr_sections = build_shield_geometry(
        site["tc"],
        site["tl"],
        site["tj"],
        spec=spec_run,
        include_pmt=include_pmt,
    )
    c11 = SHIELD_C11_CM if not is_ground else GROUND_C11_CM
    rho_scale = 1.0 if is_ground else SHIELD_HE3_RHO_SCALE
    det_sets = detector_set_lines(spec_run)
    if rho_scale != 1.0:
        det_sets += f"\n$ He-3 密度 ×{rho_scale:g}（遮蔽地点の Deposit 統計用・相対比は ÷{rho_scale:g}）"
    if spec_run.pe_style == "wrap" and spec.pe_style == "none":
        det_sets += (
            f"\n$ 遮蔽地点の熱化用 PE 筒 +{SHIELD_ENV_PE_CM:g} cm"
            "（PE なしだと熱中性子到達ゼロで Deposit が空になる）"
        )
    return HEADER.format(
        title=title,
        maxcas=maxcas,
        maxbch=maxbch,
        tc=site["tc"],
        tl=site["tl"],
        tj=site["tj"],
        c11=c11,
        room_top="c2",
        room_zmin="0.0",
        detector_sets=det_sets,
        detector_surfaces=detector_surfaces(spec_run, include_pmt=include_pmt),
        detector_cells=detector_cells(
            spec_run, include_pmt=include_pmt, rho_scale=rho_scale
        )
        + "\n",
        detector_void=detector_void_cell(
            site["tc"], site["tl"], site["tj"], spec_run
        ),
        extra_surfaces=extra_surfaces,
        layer_cells=layer_cells,
        vr_sections=vr_sections,
    )


def write_detector(det_key: str, out_root: Path | None = None) -> None:
    spec = DETECTORS[det_key]
    root = out_root or detector_root(BASE, det_key)
    for site in SITES:
        out_dir = root / site["dir"]
        out_dir.mkdir(parents=True, exist_ok=True)
        text = build_site_inp(site, spec)
        out_path = out_dir / "main.inp"
        out_path.write_text(text, encoding="utf-8")
        print(f"wrote {out_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="天井スラブ PHITS main.inp 生成")
    parser.add_argument(
        "--detector",
        choices=list(DETECTORS),
        action="append",
        help="生成する検出器（省略時は d1 d2 D1 D2 すべて）",
    )
    args = parser.parse_args()
    keys = args.detector or list(DETECTORS)
    for key in keys:
        write_detector(key)


if __name__ == "__main__":
    main()
