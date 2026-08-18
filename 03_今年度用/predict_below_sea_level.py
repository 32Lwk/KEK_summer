#!/usr/bin/env python3
"""昨年度の λ・Λ を使い、海面下（負標高／地下）のフラックスを予測する。"""

from __future__ import annotations

import argparse
import math


def predict_atmosphere(h_m: float, phi_sea: float, lam_km: float) -> float:
    return phi_sea * math.exp(h_m / (lam_km * 1000.0))


def predict_overburden(phi_surface: float, depth_m: float, density: float, Lam: float) -> float:
    x = density * depth_m * 100.0  # g/cm^2
    return phi_surface * math.exp(-x / Lam)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["atm", "underground"], default="underground")
    p.add_argument("--h", type=float, default=-100.0, help="標高 [m]（atmモード）")
    p.add_argument("--depth", type=float, default=2.0, help="覆土深さ [m]（underground）")
    p.add_argument("--density", type=float, default=1.8, help="覆土密度 [g/cm3]")
    p.add_argument("--phi0", type=float, default=1.83e-3, help="地上基準フラックス（管理棟1階 熱中性子）")
    p.add_argument("--lam-km", type=float, default=1.47)
    p.add_argument("--Lam", type=float, default=147.5)
    args = p.parse_args()

    if args.mode == "atm":
        # 地上30mの測定を海面へ換算してから負標高へ
        phi_sea = args.phi0 * math.exp(-(30.0) / (args.lam_km * 1000.0))
        phi = predict_atmosphere(args.h, phi_sea, args.lam_km)
        print(f"[大気] h={args.h:.1f} m")
        print(f"φ ≈ {phi:.3e}  （海面比 {phi/phi_sea:.3f}）")
    else:
        phi = predict_overburden(args.phi0, args.depth, args.density, args.Lam)
        x = args.density * args.depth * 100.0
        print(f"[地下] depth={args.depth:.2f} m, ρ={args.density:.2f} g/cm3, X={x:.1f} g/cm2")
        print(f"宇宙線成分の粗い予測 φ ≈ {phi:.3e}  （地上比 {phi/args.phi0:.3e}）")
        print("※深い場所では放射起源フロアが支配するため下限値にはならない")


if __name__ == "__main__":
    main()
