#!/usr/bin/env python3
"""前年9班と同じ定義で、2地点のフラックスから平均自由行程を計算する。

昨年の主結果（熱中性子・管理棟1階→白根山）:
  空気を一様密度とし、標高差 Δh = 2000 m
  λ = Δh / ln(φ₂/φ₁) ≈ 1470 m

使い方:
  python3 calc_mean_free_path.py
  python3 calc_mean_free_path.py --h1 0 --h2 2000 --phi1 1.83e-3 --phi2 7.10e-3
"""

from __future__ import annotations

import argparse
import math


def atm_depth_g_cm2(h_m: float) -> float:
    """標準大気近似の大気深度 X [g/cm²]（比較用。昨年の主計算では使わない）。"""
    pressure_hpa = 1013.25 * (1 - 2.25577e-5 * h_m) ** 5.25588
    return pressure_hpa * 1.019716


def mean_free_path(h1: float, h2: float, phi1: float, phi2: float) -> dict:
    if h2 == h1:
        raise ValueError("標高が同じです")
    if phi1 <= 0 or phi2 <= 0:
        raise ValueError("フラックスは正である必要があります")
    if (h2 - h1) * math.log(phi2 / phi1) <= 0:
        raise ValueError("高度増加とフラックス増加の向きが一致しません")

    rho_air = 1.00e-3  # g/cm³
    ratio = phi2 / phi1
    dh = h2 - h1
    lambda_m = dh / math.log(ratio)  # 一様密度ならこれが空気中の平均自由行程
    dX_uniform = rho_air * dh * 100.0  # g/cm²
    lam_x = dX_uniform / math.log(ratio)
    x1_isa = atm_depth_g_cm2(h1)
    x2_isa = atm_depth_g_cm2(h2)
    lam_isa = (x1_isa - x2_isa) / math.log(ratio)
    lambda_isa_m = lam_isa / rho_air / 100.0
    return {
        "ratio": ratio,
        "lambda_m": lambda_m,
        "Lambda_g_cm2": lam_x,
        "dX_uniform": dX_uniform,
        "lambda_isa_m": lambda_isa_m,
        "Lambda_isa": lam_isa,
        "X1_isa": x1_isa,
        "X2_isa": x2_isa,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="宇宙線中性子の平均自由行程を計算")
    parser.add_argument("--h1", type=float, default=0.0, help="低地点の標高差 [m]（昨年は 0）")
    parser.add_argument("--h2", type=float, default=2000.0, help="高地点の標高差 [m]（昨年は 2000）")
    parser.add_argument("--phi1", type=float, default=1.83e-3, help="低地点のフラックス")
    parser.add_argument("--phi2", type=float, default=7.10e-3, help="高地点のフラックス")
    parser.add_argument(
        "--label",
        type=str,
        default="熱中性子・管理棟1階→白根山（前年と同じ定義）",
    )
    args = parser.parse_args()

    result = mean_free_path(args.h1, args.h2, args.phi1, args.phi2)
    print(f"=== {args.label} ===")
    print(f"h1={args.h1:.1f} m, h2={args.h2:.1f} m, Δh={args.h2 - args.h1:.1f} m")
    print(f"φ1={args.phi1:.3e}, φ2={args.phi2:.3e}, 比={result['ratio']:.3f}")
    print(f"λ = {result['lambda_m']:.0f} m  （Λ = {result['Lambda_g_cm2']:.1f} g/cm²）")
    print(f"ΔX（一様密度）={result['dX_uniform']:.1f} g/cm²")
    print(
        "参考（標準大気 X(h) を使うと）"
        f" λ = {result['lambda_isa_m']:.0f} m、Λ = {result['Lambda_isa']:.1f} g/cm²"
        " ← 昨年の 1470 m とは定義が違う"
    )


if __name__ == "__main__":
    main()
