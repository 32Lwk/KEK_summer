#!/usr/bin/env python3
"""測定地点ごとの遮蔽（土とコンクリートの積層）と部屋（空洞）を持つ体系の PHITS 入力を作る。

体系: 地表（z=0）から下へ遮蔽層を積み、その直下に幅 3 m・長さ 20 m・高さ 3 m の部屋を置く。
部屋のまわり（壁・床）はコンクリートで、床の下も半無限に続く。
部屋の空気を上部 2 m と床から 1 m に分けて中性子スペクトルを出す（room_spec.out の 2 ページ）。

線源は muon_capture_study と同じ宇宙線（PARMA）で、成分ごとに分けて計算する。
  had : 宇宙線 neutron + proton（層ごとに importance を掛けて深部の統計を確保）
  mum : 宇宙線 muon-
  mup : 宇宙線 muon+

使い方:
  python3 make_site.py <site> <case> <seed> [--maxcas N]
  → runs/<site>/<case>_s<seed>/main.inp, source.inp
"""

from __future__ import annotations

import argparse
import math
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "muon_capture_study" / "source.inp"

SUB_CM = 50.0
ROOM_H, ROOM_HALF_X, ROOM_HALF_Y = 300.0, 150.0, 1000.0
BELOW_CM = 600.0
IMP_CAP = 4096.0
LAMBDA_IMP = 160.0

# 質量分率。土は乾燥鉱物と水の混合（含水量は水の質量分率）。
DRY_LOAM = {"H": 0.02, "O": 0.475, "Na": 0.01, "Mg": 0.02, "Al": 0.13, "Si": 0.21,
            "K": 0.01, "Ca": 0.03, "Ti": 0.01, "Fe": 0.085}
DRY_SEDIMENT = {"H": 0.01, "O": 0.49, "Na": 0.015, "Mg": 0.015, "Al": 0.08, "Si": 0.30,
                "K": 0.02, "Ca": 0.02, "Ti": 0.01, "Fe": 0.04}
CONCRETE = {"H": 0.010, "C": 0.001, "O": 0.529, "Na": 0.016, "Mg": 0.002, "Al": 0.034,
            "Si": 0.337, "K": 0.013, "Ca": 0.044, "Fe": 0.014}
REPORT_SOIL = {"H": 0.02, "O": 0.50, "Na": 0.01, "Mg": 0.02, "Al": 0.07, "Si": 0.27,
               "K": 0.02, "Ca": 0.03, "Fe": 0.04, "C": 0.02}


def wet(dry: dict[str, float], water: float) -> dict[str, float]:
    out = {k: v * (1.0 - water) for k, v in dry.items()}
    out["H"] = out.get("H", 0.0) + water * 0.1119
    out["O"] = out.get("O", 0.0) + water * 0.8881
    return out


MATERIALS = {
    "concrete": (2, 2.30, CONCRETE),
    "loam": (3, 1.35, wet(DRY_LOAM, 0.50)),
    "joso": (4, 1.65, wet(DRY_SEDIMENT, 0.27)),
    "shimosa": (5, 1.85, wet(DRY_SEDIMENT, 0.19)),
    "loam_dry": (6, 1.35, REPORT_SOIL),
    "joso_dry": (7, 1.65, REPORT_SOIL),
    "shimosa_dry": (8, 1.85, REPORT_SOIL),
}

# 上から順に (材料, 厚さ cm)。レポートの表の垂直積層と同じ。
SITES = {
    "TH": [("concrete", 57.0)],
    "PF": [("concrete", 105.0)],
    "PS": [("concrete", 480.0)],
    "BT": [("loam", 220.0), ("concrete", 60.0)],
    "KEKB": [("loam", 350.0), ("joso", 200.0), ("shimosa", 120.0), ("concrete", 80.0)],
    "KEKBdry": [("loam_dry", 350.0), ("joso_dry", 200.0), ("shimosa_dry", 120.0), ("concrete", 80.0)],
}

PROJ = {"had": ["neutron", "proton"], "mum": ["muon-"], "mup": ["muon+"]}


def sublayers(site: str):
    """(材料名, 上端 z, 下端 z) の列。遮蔽層は 50 cm ごとに分け、部屋より下はコンクリート。"""
    out = []
    z = 0.0
    for mat, t in SITES[site]:
        n = max(1, math.ceil(t / SUB_CM - 1e-9))
        dz = t / n
        for _ in range(n):
            out.append((mat, z, z - dz))
            z -= dz
    depth = -z
    n = int(BELOW_CM / SUB_CM)
    for _ in range(n):
        out.append(("concrete", z, z - SUB_CM))
        z -= SUB_CM
    return out, depth


def build(site: str, case: str, seed: int, maxcas: int) -> str:
    layers, depth = sublayers(site)
    used = sorted({MATERIALS[m][0]: m for m, _, _ in layers}.items())

    planes = sorted({round(zt, 3) for _, zt, _ in layers} | {round(zb, 3) for _, _, zb in layers}, reverse=True)
    pid = {z: 20 + i for i, z in enumerate(planes)}
    assert 20 + len(planes) <= 50, "surface ids would collide with 50/60/61"
    surf = [f"  {pid[z]:3d}   pz  {z:10.3f}" for z in planes]
    z_ceil, z_mid, z_floor = -depth, -depth - (ROOM_H - 100.0), -depth - ROOM_H
    surf += [
        f"  60   rpp  {-ROOM_HALF_X} {ROOM_HALF_X}  {-ROOM_HALF_Y} {ROOM_HALF_Y}  {z_mid:.3f} {z_ceil:.3f}",
        f"  61   rpp  {-ROOM_HALF_X} {ROOM_HALF_X}  {-ROOM_HALF_Y} {ROOM_HALF_Y}  {z_floor:.3f} {z_mid:.3f}",
    ]

    cells, imps = [], []
    imp = 1.0
    for i, (mat, zt, zb) in enumerate(layers):
        num, rho, _ = MATERIALS[mat]
        c = 201 + i
        room = "  60 61" if zb < z_ceil - 1e-6 else ""
        cells.append(f"  {c}    {num} -{rho:.3f}  -10  -{pid[round(zt, 3)]}  {pid[round(zb, 3)]}{room}")
        imp = min(IMP_CAP, imp * math.exp(rho * (zt - zb) / LAMBDA_IMP))
        imps.append((c, imp))
    last = 201 + len(layers)
    cells.append(f"  {last}    2 -2.300  -10  -{pid[round(layers[-1][2], 3)]}")
    imps.append((last, imps[-1][1]))
    ceil_imp = next(v for (c, v), (_, zt, zb) in zip(imps, layers) if zb < z_ceil - 1e-6)
    cells += [
        f"  300    1 -1.205e-3  -60",
        f"  301    1 -1.205e-3  -61",
    ]
    imps += [(300, ceil_imp), (301, ceil_imp)]

    src = "\n".join(f" infl:{{source.inp}}\n     proj = {p}" for p in PROJ[case])
    if case == "had":
        rows = "\n".join(f"  {c}   {v:.3f}" for c, v in imps)
        imp_sec = f"[ Importance ]\n part = neutron proton\n  reg   imp\n{rows}\n  901   0.0\n"
    else:
        imp_sec = "[ Importance ]\n part = muon+ muon-\n  reg   imp\n  901   0.0\n"

    mats = ["mat[1]\n     N  -0.7553\n     O  -0.2318\n    Ar  -0.0129"]
    for num, name in used:
        comp = MATERIALS[name][2]
        mats.append(f"mat[{num}]\n" + "\n".join(f"    {el:>2s}  -{fr:.4f}" for el, fr in comp.items()))

    layer_txt = " / ".join(f"{m} {t:.0f} cm" for m, t in SITES[site])
    return f"""[ Title ]
Site model {site}: {layer_txt}, room 3x3 m, case {case} (seed {seed})

[ Parameters ]
 icntl    =        0
 maxcas   = {maxcas:8d}
 maxbch   =        1
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
{chr(10).join(mats)}

[ Surface ]
  10   so   c3
  12   so   c2
  13   so   c4
  50   rpp  -800.0 800.0  -800.0 800.0   50.0  250.0
{chr(10).join(surf)}

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
   111    5.120e+08
   300    {2 * ROOM_HALF_X * 2 * ROOM_HALF_Y * (ROOM_H - 100.0):.4e}
   301    {2 * ROOM_HALF_X * 2 * ROOM_HALF_Y * 100.0:.4e}

{imp_sec}
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
    title = Flux spectrum in room air (upper 2 m, lower 1 m)
     mesh =  reg
      reg =  300 301
   e-type =    3
       ne =   60
     emin =  1.0e-10
     emax =  1.0e+5
     unit =    1
     axis =  eng
     file = room_spec.out
     part =  neutron  muon-  muon+  proton
   epsout =    0

[ End ]
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("site", choices=sorted(SITES))
    ap.add_argument("case", choices=sorted(PROJ))
    ap.add_argument("seed", type=int)
    ap.add_argument("--maxcas", type=int, default=800)
    args = ap.parse_args()
    out = ROOT / "runs" / args.site / f"{args.case}_s{args.seed}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "main.inp").write_text(build(args.site, args.case, args.seed, args.maxcas))
    shutil.copy(SOURCE, out / "source.inp")
    print(out)


if __name__ == "__main__":
    main()
