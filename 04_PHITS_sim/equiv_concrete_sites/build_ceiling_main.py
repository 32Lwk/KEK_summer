#!/usr/bin/env python3
"""水平天井スラブ + 上から垂直降下中性子の main.inp を検出器別・各地点に生成する。"""

from __future__ import annotations

import argparse
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
        "maxcas": 8000,
        "maxbch": 10,
    },
    {
        "dir": "02_linac",
        "title_suffix": "linac 天井コンクリ150 cm",
        "tc": 150.0,
        "tl": 0.0,
        "tj": 0.0,
        "maxcas": 8000,
        "maxbch": 10,
    },
    {
        "dir": "03_BT",
        "title_suffix": "BT 天井コンクリ60+ローム220 cm",
        "tc": 60.0,
        "tl": 220.0,
        "tj": 0.0,
        "maxcas": 10000,
        "maxbch": 12,
    },
    {
        "dir": "04_KEKB",
        "title_suffix": "KEKB 天井コンクリ80+ローム400+常総270 cm",
        "tc": 80.0,
        "tl": 400.0,
        "tj": 270.0,
        "maxcas": 8000,
        "maxbch": 10,
    },
]

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
set: c1[400.0] c11[30.0] c2[250.0] c3[{tc:.1f}] c4[{tl:.1f}] c5[{tj:.1f}]
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
 30   rpp  -c1  c1  -c1  c1  -50.0  c7+100.0
 50   rpp  -c1  c1  -c1  c1  {room_zmin}  {room_top}

[ Cell ]
{detector_cells}{detector_void}{layer_cells} 99  -1               30

[ T-Deposit ]
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


def layer_cells(tc: float, tl: float, tj: float) -> str:
    lines = []
    if tc > 0:
        lines.append(" 20   2  -2.302      -30  21 -22")
    if tl > 0:
        lines.append(" 25   3  -1.35       -30  22 -23")
    if tj > 0:
        lines.append(" 26   4  -1.65       -30  23 -24")
    if tc + tl + tj > 0:
        if tj > 0:
            sky = "24"
        elif tl > 0:
            sky = "23"
        else:
            sky = "22"
        lines.append(f" 90   0               -30  21  {sky}")
        lines.append(" 98   3  -1.35       -50 -20")
    else:
        lines.append(" 90   0               -30  21")
        lines.append(" 98   3  -1.35       -50 -20")
    return "\n".join(lines) + "\n"


def build_site_inp(site: dict, spec: DetectorSpec) -> str:
    title = f"{site['title_suffix']} + {spec.label}"
    is_ground = site["tc"] + site["tl"] + site["tj"] == 0
    include_pmt = not is_ground
    room_top = "c2" if is_ground else "c2"
    room_zmin = "0.0"
    return HEADER.format(
        title=title,
        maxcas=site["maxcas"],
        maxbch=site["maxbch"],
        tc=site["tc"],
        tl=site["tl"],
        tj=site["tj"],
        room_top=room_top,
        room_zmin=room_zmin,
        detector_sets=detector_set_lines(spec),
        detector_surfaces=detector_surfaces(spec, include_pmt=include_pmt),
        detector_cells=detector_cells(spec, include_pmt=include_pmt) + "\n",
        detector_void=detector_void_cell(site["tc"], site["tl"], site["tj"], spec),
        layer_cells=layer_cells(site["tc"], site["tl"], site["tj"]),
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
