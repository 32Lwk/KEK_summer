#!/usr/bin/env python3
"""He-3 比例計数管 4 台（D1, D2, d1, d2）の中性子応答関数を求める PHITS 入力を作る。

各検出器を十分離して置き、それぞれを専用の球面等方線源（s-type=9, dir=-all）で囲む。
球の外は outer void なので、ある検出器の線源粒子が別の検出器に届くことはない。
有効ガス領域の飛跡長（[Volume] を 1 cm^3 にした T-Track）を出力し、
解析側で He-3(n,p) の 1/v 断面積を掛けて反応率（= 計数）に直す。

形状（過去の検出器モデルと同じ寸法）:
  D1 : SUS 管 外径 10.0 cm・肉厚 0.2 cm・長さ 66 cm、有効ガス長 56 cm（残りは不感部）
  d1 : SUS 管 外径 5.48 cm・肉厚 0.2 cm・長さ 39.53 cm、有効ガス長 31 cm
  D2 : D1 と同じ管を PE 容器（外径 29／内径 15／高さ 80 cm、上下のふた 6 cm）に入れる
  d2 : d1 と同じ管に厚さ 5 cm の PE 筒を密着させ、上下に厚さ 5 cm のふたを付ける
  He-3 : 10 atm（20 degC）

使い方:
  python3 make_resp.py <tag> <E_MeV> <seed> [--maxcas N]
  → runs/<tag>/main.inp
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent

RHO_HE3 = 1.254e-3
RHO_SUS = 8.0
RHO_PE = 0.95
RHO_AIR = 1.205e-3

DETS = {
    "D1": dict(x=0.0, r_src=35.0),
    "D2": dict(x=200.0, r_src=44.0),
    "d1": dict(x=400.0, r_src=22.0),
    "d2": dict(x=600.0, r_src=27.0),
}
GAS_CELL = {"D1": 101, "D2": 201, "d1": 301, "d2": 401}


def tube(base: int, x: float, z_bot: float, r_out: float, length: float, active: float):
    """管（SUS 殻＋有効ガス＋不感ガス）の surface と cell。外側の面番号も返す。"""
    wall = 0.2
    r_in = r_out - wall
    zg = z_bot + wall
    gas_len = length - 2 * wall
    surf = [
        f" {base + 1:4d}  rcc  {x:.3f} 0 {zg:.3f}  0 0 {active:.3f}  {r_in:.3f}",
        f" {base + 2:4d}  rcc  {x:.3f} 0 {zg + active:.3f}  0 0 {gas_len - active:.3f}  {r_in:.3f}",
        f" {base + 3:4d}  rcc  {x:.3f} 0 {z_bot:.3f}  0 0 {length:.3f}  {r_out:.3f}",
    ]
    cell = [
        f" {base + 1:4d}  5 -{RHO_HE3}  -{base + 1}",
        f" {base + 2:4d}  5 -{RHO_HE3}  -{base + 2}",
        f" {base + 3:4d}  6 -{RHO_SUS}  -{base + 3} {base + 1} {base + 2}",
    ]
    return surf, cell, base + 3


def build(energy: float, seed: int, maxcas: int) -> str:
    surf: list[str] = []
    cell: list[str] = []
    spheres: list[int] = []

    # D1: 裸の大径管
    x = DETS["D1"]["x"]
    s, c, outer = tube(100, x, -33.0, 5.0, 66.0, 56.0)
    surf += s + [f"  109  s  {x:.3f} 0 0  36.0"]
    cell += c + [f"  109  0  -109 {outer}"]
    spheres.append(109)

    # D2: 大径管 + PE 容器
    x = DETS["D2"]["x"]
    s, c, outer = tube(200, x, -34.0, 5.0, 66.0, 56.0)
    surf += s + [
        f"  204  rcc  {x:.3f} 0 -34.000  0 0 68.000  7.500",
        f"  205  rcc  {x:.3f} 0 -40.000  0 0 80.000  14.500",
        f"  209  s  {x:.3f} 0 0  45.0",
    ]
    cell += c + [
        f"  204  1 -{RHO_AIR}  -204 {outer}",
        f"  205  7 -{RHO_PE}  -205 204",
        "  209  0  -209 205",
    ]
    spheres.append(209)

    # d1: 裸の小径管
    x = DETS["d1"]["x"]
    s, c, outer = tube(300, x, -19.765, 2.74, 39.53, 31.0)
    surf += s + [f"  309  s  {x:.3f} 0 0  23.0"]
    cell += c + [f"  309  0  -309 {outer}"]
    spheres.append(309)

    # d2: 小径管 + PE 筒（密着）+ 上下のふた
    x = DETS["d2"]["x"]
    s, c, outer = tube(400, x, -19.765, 2.74, 39.53, 31.0)
    surf += s + [
        f"  405  rcc  {x:.3f} 0 -24.765  0 0 49.530  7.740",
        f"  409  s  {x:.3f} 0 0  28.0",
    ]
    cell += c + [
        f"  405  7 -{RHO_PE}  -405 {outer}",
        "  409  0  -409 405",
    ]
    spheres.append(409)

    cell.append("  999  -1  " + " ".join(str(s) for s in spheres))

    src = []
    for name, d in DETS.items():
        src.append(
            f""" <source> = 1.0
   s-type = 9
     proj = neutron
       x0 = {d['x']:.3f}
       y0 = 0.0
       z0 = 0.0
       r1 = {d['r_src']:.1f}
       r2 = {d['r_src']:.1f}
      dir = -all
       e0 = {energy:.6e}"""
        )

    gas = " ".join(str(GAS_CELL[k]) for k in DETS)
    vol = "\n".join(f"  {GAS_CELL[k]}   1.0" for k in DETS)

    return f"""[ Title ]
He-3 tube response, E = {energy:.4e} MeV (seed {seed})

[ Parameters ]
 icntl    =        0
 maxcas   = {maxcas:8d}
 maxbch   =        1
 rseed    = {float(seed):8.1f}
 emin(2)  =  1.0e-10
 dmax(2)  =     20.0
 emin(14) =   1000.0

[ Source ]
{chr(10).join(src)}

[ Material ]
mat[1]
     N  -0.7553
     O  -0.2318
    Ar  -0.0129
mat[5]
   3He   1.0
mat[6]
    Fe  70
    Cr  18
    Ni   9
    Mn   2
    Si   1
mat[7]
     H   2
     C   1
MT7  poly.20t

[ Mat Name Color ]
   mat     name       size  color
     1     Air         1.0  yellowgreen
     5     He3         1.0  pink
     6     SUS         1.0  gray
     7     PE          1.0  cyan

[ Surface ]
{chr(10).join(surf)}

[ Cell ]
{chr(10).join(cell)}

[ Volume ]
   reg   vol
{vol}

[ T-Track ]
    title = Neutron track length in active He-3 gas
     mesh =  reg
      reg =  {gas}
   e-type =    3
       ne =  130
     emin =  1.0e-10
     emax =  1.0e+3
     unit =    1
     axis =  eng
     file = gas_track.out
     part =  neutron
   epsout =    0

[ End ]
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("tag")
    ap.add_argument("energy", type=float)
    ap.add_argument("seed", type=int)
    ap.add_argument("--maxcas", type=int, default=20000)
    args = ap.parse_args()
    out = ROOT / "runs" / args.tag
    out.mkdir(parents=True, exist_ok=True)
    (out / "main.inp").write_text(build(args.energy, args.seed, args.maxcas))
    print(out)


if __name__ == "__main__":
    main()
