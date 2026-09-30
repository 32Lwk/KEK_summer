#!/usr/bin/env python3
"""レポートに載せるシミュレーションの様子（中性子フラックスの断面図）を作る PHITS 入力。

体系と線源は本計算と同じ入力をそのまま使い、断面のメッシュタリーだけを足す。
  site : site_models/make_site.py の地点体系（地層＋部屋）。xz 断面（部屋の長さ方向 y の中央 ±100 cm）
  det  : detector_response/make_resp.py の 4 台の管。管の軸を通る xz 断面（y の ±0.5 cm）

使い方:
  python3 make_vis.py site <site> <had|mum> <seed> [--maxcas N]
  python3 make_vis.py det <E_MeV> <seed> [--maxcas N]
  → runs/<tag>/main.inp（site は source.inp も）
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SIM = ROOT.parent
sys.path.insert(0, str(SIM / "site_models"))
sys.path.insert(0, str(SIM / "detector_response"))

import make_resp  # noqa: E402
import make_site  # noqa: E402

PHITS_DIR = "/Users/yuto/PHITS335/phits"

# 熱（< 0.5 eV）、熱外（0.5 eV–0.1 MeV）、高速（0.1–20 MeV）、それ以上
E_EDGES = [1.0e-10, 5.0e-7, 0.1, 20.0, 1.0e5]


def mesh_tally(title: str, file: str, part: str, x: tuple, y: tuple, z: tuple) -> str:
    edges = "\n".join(f"        {e:.3e}" for e in E_EDGES)
    return f"""
[ T-Track ]
    title = {title}
     mesh =  xyz
   x-type =    2
       nx = {x[2]:4d}
     xmin = {x[0]:.1f}
     xmax = {x[1]:.1f}
   y-type =    2
       ny =    1
     ymin = {y[0]:.1f}
     ymax = {y[1]:.1f}
   z-type =    2
       nz = {z[2]:4d}
     zmin = {z[0]:.1f}
     zmax = {z[1]:.1f}
   e-type =    1
       ne = {len(E_EDGES) - 1}
{edges}
     unit =    1
     axis =   xz
  2D-type =    4
     file = {file}
     part = {part}
   epsout =    0
"""


def with_tallies(inp: str, tallies: str) -> str:
    inp = inp.replace("[ Parameters ]\n", f"[ Parameters ]\n file(1)  = {PHITS_DIR}\n", 1)
    return inp.replace("[ End ]", tallies.strip("\n") + "\n\n[ End ]")


def site_input(site: str, case: str, seed: int, maxcas: int) -> str:
    """had は 20 cm メッシュ・y ±3 m。mum は中性子の生成が少ないので、部屋の長さ全体（y ±10 m）で平均し 40 cm メッシュにする。"""
    _, depth = make_site.sublayers(site)
    z_lo = -depth - make_site.ROOM_H - 300.0
    if case == "had":
        dx, half_y, parts = 20.0, 300.0, "neutron"
    else:
        dx, half_y, parts = 40.0, make_site.ROOM_HALF_Y, "neutron muon-"
    nz = int(round((200.0 - z_lo) / dx))
    tally = mesh_tally("Neutron flux map, xz section", "map_xz.out", parts,
                       (-700.0, 700.0, int(1400 / dx)), (-half_y, half_y), (z_lo, 200.0, nz))
    return with_tallies(make_site.build(site, case, seed, maxcas), tally)


def det_map_file(name: str) -> str:
    """macOS のファイル名は大文字小文字を区別しないので、D1 と d1 を別名にする。"""
    return f"map_{name}_{'large' if name[0] == 'D' else 'small'}.out"


def det_input(energy: float, seed: int, maxcas: int) -> str:
    tallies = ""
    for name, half_x, half_z in (("D1", 40.0, 40.0), ("D2", 50.0, 50.0), ("d1", 25.0, 25.0), ("d2", 30.0, 30.0)):
        x0 = make_resp.DETS[name]["x"]
        n = int(round(2 * half_x / 0.5))
        tallies += mesh_tally(f"Neutron flux map around {name}", det_map_file(name), "neutron",
                              (x0 - half_x, x0 + half_x, n), (-0.5, 0.5), (-half_z, half_z, n))
    return with_tallies(make_resp.build(energy, seed, maxcas), tallies)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="kind", required=True)
    s = sub.add_parser("site")
    s.add_argument("site", choices=sorted(make_site.SITES))
    s.add_argument("case", choices=["had", "mum"])
    s.add_argument("seed", type=int)
    s.add_argument("--maxcas", type=int, default=2000)
    d = sub.add_parser("det")
    d.add_argument("energy", type=float)
    d.add_argument("seed", type=int)
    d.add_argument("--maxcas", type=int, default=20000)
    args = ap.parse_args()

    if args.kind == "site":
        out = ROOT / "runs" / f"{args.site}_{args.case}_s{args.seed}"
        out.mkdir(parents=True, exist_ok=True)
        (out / "main.inp").write_text(site_input(args.site, args.case, args.seed, args.maxcas))
        shutil.copy(make_site.SOURCE, out / "source.inp")
    else:
        out = ROOT / "runs" / f"det_E{args.energy:.3e}_s{args.seed}"
        out.mkdir(parents=True, exist_ok=True)
        (out / "main.inp").write_text(det_input(args.energy, args.seed, args.maxcas))
    print(out)


if __name__ == "__main__":
    main()
