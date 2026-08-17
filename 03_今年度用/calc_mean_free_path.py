#!/usr/bin/env python3
"""前年9班と同じ定義で、2地点のフラックスから平均自由行程を計算する。

使い方:
  python3 calc_mean_free_path.py
  python3 calc_mean_free_path.py --h1 30 --h2 2160 --phi1 1.02e-3 --phi2 5.37e-3
"""

from __future__ import annotations

import argparse
import math


def atm_depth_g_cm2(h_m: float) -> float:
    """標準大気近似の大気深度 X [g/cm²]。"""
    pressure_hpa = 1013.25 * (1 - 2.25577e-5 * h_m) ** 5.25588
    return pressure_hpa * 1.019716


def mean_free_path(h1: float, h2: float, phi1: float, phi2: float) -> dict:
    if h2 == h1:
        raise ValueError("標高が同じです")
    if phi1 <= 0 or phi2 <= 0:
        raise ValueError("フラックスは正である必要があります")
    if (h2 - h1) * math.log(phi2 / phi1) <= 0:
        raise ValueError("高度増加とフラックス増加の向きが一致しません")

    ratio = phi2 / phi1
    lam_m = (h2 - h1) / math.log(ratio)
    x1 = atm_depth_g_cm2(h1)
    x2 = atm_depth_g_cm2(h2)
    lam_x = (x1 - x2) / math.log(ratio)
    return {
        "ratio": ratio,
        "lambda_km": lam_m / 1000,
        "alpha_per_km": 1000 / lam_m,
        "X1": x1,
        "X2": x2,
        "Lambda_g_cm2": lam_x,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="宇宙線中性子の平均自由行程を計算")
    parser.add_argument("--h1", type=float, default=30.0, help="低地点の標高 [m]")
    parser.add_argument("--h2", type=float, default=2160.0, help="高地点の標高 [m]")
    parser.add_argument("--phi1", type=float, default=1.02e-3, help="低地点のフラックス")
    parser.add_argument("--phi2", type=float, default=5.37e-3, help="高地点のフラックス")
    parser.add_argument("--label", type=str, default="MeV・管理棟2階→白根山（前年デフォルト）")
    args = parser.parse_args()

    result = mean_free_path(args.h1, args.h2, args.phi1, args.phi2)
    print(f"=== {args.label} ===")
    print(f"h1={args.h1:.1f} m, h2={args.h2:.1f} m, Δh={args.h2 - args.h1:.1f} m")
    print(f"φ1={args.phi1:.3e}, φ2={args.phi2:.3e}, 比={result['ratio']:.3f}")
    print(f"λ = {result['lambda_km']:.3f} km  (α = {result['alpha_per_km']:.3f} /km)")
    print(f"X1={result['X1']:.1f}, X2={result['X2']:.1f}, ΔX={result['X1'] - result['X2']:.1f} g/cm²")
    print(f"Λ = {result['Lambda_g_cm2']:.1f} g/cm²")


if __name__ == "__main__":
    main()
