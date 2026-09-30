#!/usr/bin/env python3
"""半無限コンクリート中の中性子深さ分布を、線源成分ごとに計算する PHITS 入力を作る。

ケース:
  mum : 宇宙線 muon- のみ（捕獲 + 高速ミューオン核反応 + シャワー光核反応）
  mup : 宇宙線 muon+ のみ（捕獲なし）
  had : 宇宙線 neutron + proton（大気由来ハドロン成分、深さ方向に importance）
  mumT, hadT : 上と同じ線源で、天井厚 300 cm（Linac3 相当）に幅・高さ 3 m のトンネルを置く

使い方:
  python3 make_inputs.py <case> <seed> [--maxcas N] [--maxbch N]
  → runs/<case>_s<seed>/main.inp と source.inp を作る
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent

LAYER_CM = 50.0
N_LAYERS = 18  # 0 .. -900 cm

PROJ = {
    "mum": ["muon-"],
    "mup": ["muon+"],
    "had": ["neutron", "proton"],
    "mumT": ["muon-"],
    "hadT": ["neutron", "proton"],
}

TUNNEL_CEIL_CM = 300.0
TUNNEL_IMP = 512.0

TITLE = {
    "mum": "Semi-infinite concrete, cosmic muon- only",
    "mup": "Semi-infinite concrete, cosmic muon+ only",
    "had": "Semi-infinite concrete, cosmic neutron + proton",
    "mumT": "Concrete with tunnel (ceiling 300 cm), cosmic muon- only",
    "hadT": "Concrete with tunnel (ceiling 300 cm), cosmic neutron + proton",
}


def build(case: str, seed: int, maxcas: int, maxbch: int) -> str:
    tunnel = case.endswith("T")
    hadronic = case.startswith("had")
    src = "\n".join(f" infl:{{source.inp}}\n     proj = {p}" for p in PROJ[case])

    surf = [f"  {21 + i:2d}   pz  {-LAYER_CM * (i + 1):8.1f}" for i in range(N_LAYERS)]
    cells = []
    for i in range(N_LAYERS):
        upper = 20 + i
        lower = 21 + i
        cells.append(f"  {201 + i}    2 -2.30  -10  -{upper}  {lower}")
    cells.append(f"  {201 + N_LAYERS}    2 -2.30  -10  -{20 + N_LAYERS}")
    if tunnel:
        cells = [c + "  60" for c in cells]
        cells.append("  300    1 -1.205e-3  -60")

    # 901: 地面より下の薄い真空殻（c3〜c4）。線源球の側面から地中へ直接入る非物理的な粒子を消す。
    # 線源は c1 上（902 内）から出るので、901 と c1 を重ねないこと。
    if hadronic:
        rows = [f"  {201 + i}   {2.0 ** (i + 1):.1f}" for i in range(N_LAYERS)]
        rows.append(f"  {201 + N_LAYERS}   {2.0 ** N_LAYERS:.1f}")
        if tunnel:
            rows.append(f"  300   {TUNNEL_IMP:.1f}")
        rows.append("  901   0.0")
        imp = "[ Importance ]\n part = neutron proton\n  reg   imp\n" + "\n".join(rows) + "\n"
    else:
        imp = "[ Importance ]\n part = muon+ muon-\n  reg   imp\n  901   0.0\n"

    tunnel_surf = ""
    tunnel_vol = ""
    tunnel_tally = ""
    if tunnel:
        top, bot = -TUNNEL_CEIL_CM, -TUNNEL_CEIL_CM - 300.0
        tunnel_surf = f"\n  60   rpp  -150.0 150.0  -1000.0 1000.0  {bot:.1f}  {top:.1f}"
        tunnel_vol = "\n   300    1.800e+08"
        tunnel_tally = """
[ T-Track ]
    title = Flux spectrum in tunnel air
     mesh =  reg
      reg =  300
   e-type =    3
       ne =   60
     emin =  1.0e-10
     emax =  1.0e+5
     unit =    1
     axis =  eng
     file = tunnel_spec.out
     part =  neutron  muon-  muon+  proton
   epsout =    0
"""

    return f"""[ Title ]
{TITLE[case]} (seed {seed})

[ Parameters ]
 icntl    =        0
 maxcas   = {maxcas:8d}
 maxbch   = {maxbch:8d}
 rseed    = {float(seed):8.1f}
 negs     =        1
 emin(12) =      5.0
 emin(13) =      5.0
 emin(14) =      5.0
 ipnint   =        1
 imuint   =        1
 maxbnk   =   200000

set: c1[1600.]
set: c2[2200.]
set: c3[1500.]
set: c4[1550.]

[ Source ]
  totfact = -pi*c1**2
{src}

[ Material ]
mat[1]
     N  -0.7553
     O  -0.2318
    Ar  -0.0129
mat[2]
     H  -0.010
     C  -0.001
     O  -0.529
    Na  -0.016
    Mg  -0.002
    Al  -0.034
    Si  -0.337
     K  -0.013
    Ca  -0.044
    Fe  -0.014

[ Mat Name Color ]
   mat     name       size  color
     1     Air         1.0  yellowgreen
     2     Concrete    1.0  lightgray

[ Surface ]
  10   so   c3
  12   so   c2
  13   so   c4
  20   pz   0.0
{chr(10).join(surf)}
  50   rpp  -800.0 800.0  -800.0 800.0   50.0  250.0{tunnel_surf}

[ Cell ]
  100    1 -1.205e-3  -10   20  50
  111    1 -1.205e-3  -50
{chr(10).join(cells)}
  900    0             10 -12   20
  901    0             10 -13  -20
  902    0             13 -12  -20
  999   -1             12

[ Volume ]
   reg          vol
   111    5.120e+08{tunnel_vol}

{imp}
[ T-Track ]
    title = Flux spectrum in open air above ground
     mesh =  reg
      reg =  111
   e-type =    3
       ne =   60
     emin =  1.0e-10
     emax =  1.0e+5
     unit =    1
     axis =  eng
     file = air_spec.out
     part =  neutron  muon-  muon+  proton
   epsout =    0

[ T-Track ]
    title = Flux spectra vs depth in concrete
     mesh =  xyz
   x-type =    2
       nx =    1
     xmin = -600.0
     xmax =  600.0
   y-type =    2
       ny =    1
     ymin = -600.0
     ymax =  600.0
   z-type =    2
       nz =   35
     zmin = -700.0
     zmax =    0.0
   e-type =    3
       ne =   60
     emin =  1.0e-10
     emax =  1.0e+5
     unit =    1
     axis =  eng
     file = depth_spec.out
     part =  neutron  muon-  muon+  proton
   epsout =    0
{tunnel_tally}
[ End ]
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("case", choices=sorted(PROJ))
    ap.add_argument("seed", type=int)
    ap.add_argument("--maxcas", type=int, default=2000)
    ap.add_argument("--maxbch", type=int, default=1)
    args = ap.parse_args()

    out = ROOT / "runs" / f"{args.case}_s{args.seed}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "main.inp").write_text(build(args.case, args.seed, args.maxcas, args.maxbch))
    shutil.copy(ROOT / "source.inp", out / "source.inp")
    print(out)


if __name__ == "__main__":
    main()
