#!/usr/bin/env python3
"""土・コンクリート厚 → 等価コンクリート厚の共通換算。

高エネルギー宇宙線中性子の減衰長は質量厚さで扱い、教材の元素混合則で
Λ [g/cm²] を求め、幾何平均自由行程 λ = Λ/ρ [cm] に直す。

  σ ≈ 45 · A^{0.7}  [mb]       （教材）
  Λ_i = 37 · A^{0.3}  [g/cm²]  （上式から導出）
  1/Λ = Σ w_i / Λ_i            （質量分率の混合則）

等価コンクリート厚:
  t_eq = (X_c/Λ_c + τ_soil) · Λ_c / ρ_c

CLI:
  python3 equiv_shielding.py --concrete 150 --soil 0
  python3 equiv_shielding.py --concrete 80 --soil 670 --profile tsukuba
  python3 equiv_shielding.py --report
  python3 equiv_shielding.py --depth-table --profile asahi
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parent
TABLES = ROOT / "測定_20260818" / "tables"

# ---------------------------------------------------------------------------
# 元素
# ---------------------------------------------------------------------------

ELEMENTS: dict[str, float] = {
    "H": 1.008,
    "C": 12.011,
    "O": 15.999,
    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.085,
    "K": 39.098,
    "Ca": 40.078,
    "Ti": 47.867,
    "Fe": 55.845,
    "Pb": 207.2,
}


def elemental_lambda_gcm2(symbol: str) -> float:
    """単一元素の減衰長 Λ [g/cm²]（教材: 37·A^0.3）。"""
    return 37.0 * (ELEMENTS[symbol] ** 0.3)


def elemental_sigma_mb(symbol: str) -> float:
    """単一元素の実効断面積 σ [mb]（教材: 45·A^0.7）。"""
    return 45.0 * (ELEMENTS[symbol] ** 0.7)


def mix_lambda_gcm2(weights: dict[str, float]) -> float:
    """質量分率混合則 1/Λ = Σ w_i/Λ_i。"""
    total = sum(max(w, 0.0) for w in weights.values())
    if total <= 0:
        raise ValueError("質量分率の合計が 0")
    inv = 0.0
    for sym, w in weights.items():
        if w <= 0:
            continue
        inv += (w / total) / elemental_lambda_gcm2(sym)
    return 1.0 / inv


# ---------------------------------------------------------------------------
# 組成・物質
# ---------------------------------------------------------------------------

COMPOSITION_CONCRETE_SLIDE = {"O": 0.53, "Si": 0.34, "Ca": 0.04, "Al": 0.03, "H": 0.01}
COMPOSITION_SOIL_SLIDE = {"O": 0.50, "Si": 0.27, "Al": 0.07, "Fe": 0.04, "H": 0.02}
COMPOSITION_CONCRETE_NIST = {
    "H": 0.0221,
    "C": 0.0025,
    "O": 0.5749,
    "Na": 0.0152,
    "Mg": 0.0013,
    "Al": 0.0200,
    "Si": 0.3046,
    "K": 0.0100,
    "Ca": 0.0429,
    "Fe": 0.0064,
}
COMPOSITION_KANTO_LOAM = {
    # 火山灰質粘性土（関東ローム）の代表値。
    # 筑波台地・KEK 向け。Si やや低め、Al/Fe やや高め（風化火山灰質）。
    # 出典の位置づけ: 地質層序は宇野沢ほか1988・坂田ほか2018/2024、
    # 元素比は教材土(O50/Si27/Al7/Fe4)と沖積論文52(8)の傾向を踏まえた推定。
    "O": 0.52,
    "Si": 0.22,
    "Al": 0.12,
    "Fe": 0.07,
    "H": 0.014,
    "Ca": 0.008,
    "Mg": 0.010,
    "Na": 0.006,
    "K": 0.007,
    "Ti": 0.006,
}

# 常総粘土（凝灰質粘土）— ロームより Al/Fe↑ Si↓（粘土鉱物多め）
COMPOSITION_JOSO_CLAY = {
    "O": 0.50,
    "Si": 0.18,
    "Al": 0.14,
    "Fe": 0.08,
    "H": 0.015,
    "Ca": 0.006,
    "Mg": 0.012,
    "Na": 0.005,
    "K": 0.008,
    "Ti": 0.006,
}

# 下総層群（砂〜シルト質細砂）— Si やや高め
COMPOSITION_SHIMOSA_SAND = {
    "O": 0.48,
    "Si": 0.32,
    "Al": 0.06,
    "Fe": 0.05,
    "H": 0.012,
    "Ca": 0.008,
    "Mg": 0.008,
    "Na": 0.004,
    "K": 0.005,
    "Ti": 0.004,
}

# 埋土（完新世・造成地浅部）— 旭 B1 の 0.35–5.55 m 相当
COMPOSITION_FILL_SOIL = {
    "O": 0.50,
    "Si": 0.25,
    "Al": 0.09,
    "Fe": 0.05,
    "H": 0.018,
    "Ca": 0.008,
    "Mg": 0.008,
    "Na": 0.005,
    "K": 0.006,
    "Ti": 0.004,
}


@dataclass(frozen=True)
class Material:
    name: str
    rho_g_cm3: float
    composition: dict[str, float]
    note: str = ""

    @property
    def lambda_gcm2(self) -> float:
        return mix_lambda_gcm2(self.composition)

    @property
    def lambda_cm(self) -> float:
        return self.lambda_gcm2 / self.rho_g_cm3

    @property
    def lambda_m(self) -> float:
        return self.lambda_cm / 100.0


CONCRETE_SLIDE = Material("コンクリート（教材組成）", 2.30, COMPOSITION_CONCRETE_SLIDE, "ρ=2.3")
CONCRETE_KEK = Material("コンクリート（KEK ρ=2.35）", 2.35, COMPOSITION_CONCRETE_SLIDE, "ρ=2.35")
CONCRETE_NIST = Material("コンクリート（NIST Ordinary）", 2.30, COMPOSITION_CONCRETE_NIST, "NIST NBS 04")
SOIL_SLIDE = Material("土（教材組成）", 1.90, COMPOSITION_SOIL_SLIDE, "教材代表土")
LOAM = Material(
    "関東ローム",
    1.35,
    COMPOSITION_KANTO_LOAM,
    "筑波台地表層・火山灰質粘性土（代表組成）",
)
JOSO = Material(
    "常総粘土",
    1.65,
    COMPOSITION_JOSO_CLAY,
    "凝灰質粘土（Al/Fe↑ Si↓）",
)
SHIMOSA = Material(
    "下総層群（砂）",
    1.85,
    COMPOSITION_SHIMOSA_SAND,
    "更新世砂〜シルト質細砂",
)
FILL = Material(
    "埋土",
    1.55,
    COMPOSITION_FILL_SOIL,
    "完新世埋土（旭 B1 浅部）",
)
PAVEMENT = Material("舗装", 2.20, COMPOSITION_CONCRETE_SLIDE, "AS+砕石")
# 申請・施設表の代表値（純鉄 7.86 より小さく安全側の 7.2）
IRON = Material("鉄", 7.20, {"Fe": 1.0}, "ρ=7.2（ATF/PF/PS・SKEKB 系の代表）")


@dataclass
class SoilLayer:
    name: str
    thickness_m: float
    material: Material


@dataclass
class SoilProfile:
    name: str
    layers: list[SoilLayer] = field(default_factory=list)
    note: str = ""

    def mass_thickness_gcm2(self, depth_m: float) -> float:
        if depth_m <= 0:
            return 0.0
        x = 0.0
        rem = depth_m
        for layer in self.layers:
            take = min(rem, layer.thickness_m)
            if take <= 0:
                break
            x += layer.material.rho_g_cm3 * take * 100.0
            rem -= take
        if rem > 0 and self.layers:
            x += self.layers[-1].material.rho_g_cm3 * rem * 100.0
        return x

    def optical_depth(self, depth_m: float) -> float:
        if depth_m <= 0:
            return 0.0
        tau = 0.0
        rem = depth_m
        for layer in self.layers:
            take = min(rem, layer.thickness_m)
            if take <= 0:
                break
            x = layer.material.rho_g_cm3 * take * 100.0
            tau += x / layer.material.lambda_gcm2
            rem -= take
        if rem > 0 and self.layers:
            last = self.layers[-1]
            x = last.material.rho_g_cm3 * rem * 100.0
            tau += x / last.material.lambda_gcm2
        return tau


PROFILE_TEXTBOOK = SoilProfile(
    name="textbook",
    note="教材: ローム≤4 m (ρ=1.35)、以深は常総 (ρ=1.65)",
    layers=[
        SoilLayer("関東ローム", 4.0, LOAM),
        SoilLayer("常総粘土", 1e9, JOSO),
    ],
)

PROFILE_TSUKUBA = SoilProfile(
    name="tsukuba",
    note=(
        "筑波台地・自然地盤（KEK 向け推奨）: ローム 3.5 m → 常総 2.0 m → 下総。"
        "層厚・ρ は区域代表。構内ボーリングがあれば差し替え。"
    ),
    layers=[
        SoilLayer("関東ローム", 3.5, LOAM),
        SoilLayer("常総粘土", 2.0, JOSO),
        SoilLayer("下総層群", 1e9, SHIMOSA),
    ],
)

PROFILE_ASAHI = SoilProfile(
    name="asahi",
    note=(
        "国総研・つくば市旭 B1（2021, KuniJiban）: 舗装 0.35 m + 埋土 5.20 m + "
        "凝灰質粘土 2.15 m → 下総。造成地モデル（自然ロームではない）。"
    ),
    layers=[
        SoilLayer("舗装・砕石", 0.35, PAVEMENT),
        SoilLayer("埋土", 5.20, FILL),
        SoilLayer("凝灰質粘土（常総相当）", 2.15, JOSO),
        SoilLayer("下総層群", 1e9, SHIMOSA),
    ],
)

PROFILES: dict[str, SoilProfile] = {
    "textbook": PROFILE_TEXTBOOK,
    "tsukuba": PROFILE_TSUKUBA,
    "asahi": PROFILE_ASAHI,
}

DEFAULT_CONCRETE = CONCRETE_SLIDE
DEFAULT_PROFILE = "tsukuba"


@dataclass(frozen=True)
class EquivResult:
    concrete_cm: float
    soil_cm: float
    profile: str
    x_concrete_gcm2: float
    x_soil_gcm2: float
    x_total_gcm2: float
    tau: float
    t_eq_cm: float
    t_eq_density_only_cm: float
    lambda_concrete_gcm2: float
    lambda_concrete_cm: float
    rho_concrete: float
    attenuation: float
    iron_cm: float = 0.0
    x_iron_gcm2: float = 0.0

    @property
    def t_eq_m(self) -> float:
        return self.t_eq_cm / 100.0


def compute_concrete_mfp(
    *,
    composition: dict[str, float] | None = None,
    rho_g_cm3: float = 2.30,
) -> dict:
    """コンクリート MFP の詳細計算。"""
    comp = dict(composition or COMPOSITION_CONCRETE_SLIDE)
    total = sum(comp.values())
    lam_g = mix_lambda_gcm2(comp)
    parts = []
    for sym, w in sorted(comp.items(), key=lambda kv: -kv[1]):
        wi = w / total
        li = elemental_lambda_gcm2(sym)
        parts.append(
            {
                "element": sym,
                "weight_pct": wi * 100.0,
                "A": ELEMENTS[sym],
                "sigma_mb": elemental_sigma_mb(sym),
                "lambda_i_gcm2": li,
                "w_over_lambda": wi / li,
            }
        )
    return {
        "method": "Λ_i=37·A^0.3 [g/cm²], 1/Λ=Σ w_i/Λ_i（教材混合則）",
        "composition": ", ".join(f"{p['element']}:{p['weight_pct']:.1f}%" for p in parts),
        "parts": parts,
        "lambda_gcm2": lam_g,
        "rho_g_cm3": rho_g_cm3,
        "lambda_cm": lam_g / rho_g_cm3,
        "lambda_m": lam_g / rho_g_cm3 / 100.0,
    }


def compare_concrete_mfp_methods() -> list[dict]:
    rows = []
    for mat in (CONCRETE_SLIDE, CONCRETE_KEK, CONCRETE_NIST):
        rows.append(
            {
                "name": mat.name,
                "rho": mat.rho_g_cm3,
                "lambda_gcm2": mat.lambda_gcm2,
                "lambda_cm": mat.lambda_cm,
                "note": mat.note,
            }
        )
    rows.append(
        {
            "name": "旧解析（誤り・参考）",
            "rho": 2.30,
            "lambda_gcm2": 77.0 * 2.30,
            "lambda_cm": 77.0,
            "note": "λ=77 cm は単位取り違え/経験フィット。非推奨",
        }
    )
    return rows


def equiv_concrete(
    concrete_cm: float = 0.0,
    soil_cm: float = 0.0,
    *,
    iron_cm: float = 0.0,
    profile: str | SoilProfile = DEFAULT_PROFILE,
    concrete: Material | None = None,
    iron: Material | None = None,
) -> EquivResult:
    """コンクリート・土・鉄厚 [cm] から等価コンクリート厚を計算。"""
    mat_c = concrete or DEFAULT_CONCRETE
    mat_fe = iron or IRON
    if isinstance(profile, str):
        if profile not in PROFILES:
            raise KeyError(f"未知の profile: {profile}. 候補={list(PROFILES)}")
        prof = PROFILES[profile]
        prof_name = profile
    else:
        prof = profile
        prof_name = profile.name

    soil_m = max(soil_cm, 0.0) / 100.0
    x_c = max(concrete_cm, 0.0) * mat_c.rho_g_cm3
    x_s = prof.mass_thickness_gcm2(soil_m)
    x_fe = max(iron_cm, 0.0) * mat_fe.rho_g_cm3
    tau = (
        x_c / mat_c.lambda_gcm2
        + prof.optical_depth(soil_m)
        + (x_fe / mat_fe.lambda_gcm2 if x_fe > 0 else 0.0)
    )
    t_eq = tau * mat_c.lambda_gcm2 / mat_c.rho_g_cm3
    t_eq_dens = (x_c + x_s + x_fe) / mat_c.rho_g_cm3

    return EquivResult(
        concrete_cm=float(concrete_cm),
        soil_cm=float(soil_cm),
        profile=prof_name,
        x_concrete_gcm2=x_c,
        x_soil_gcm2=x_s,
        x_total_gcm2=x_c + x_s + x_fe,
        tau=tau,
        t_eq_cm=t_eq,
        t_eq_density_only_cm=t_eq_dens,
        lambda_concrete_gcm2=mat_c.lambda_gcm2,
        lambda_concrete_cm=mat_c.lambda_cm,
        rho_concrete=mat_c.rho_g_cm3,
        attenuation=math.exp(-tau),
        iron_cm=float(iron_cm),
        x_iron_gcm2=x_fe,
    )


def equiv_concrete_batch(
    rows: Iterable[tuple[str, float, float]],
    *,
    profile: str = DEFAULT_PROFILE,
) -> list[dict]:
    out = []
    for label, tc, ts in rows:
        r = equiv_concrete(tc, ts, profile=profile)
        out.append(
            {
                "地点": label,
                "コンクリート_cm": tc,
                "土_cm": ts,
                "profile": r.profile,
                "X_コンクリート": round(r.x_concrete_gcm2, 2),
                "X_土": round(r.x_soil_gcm2, 2),
                "質量厚さ_X": round(r.x_total_gcm2, 2),
                "光学厚さ_tau": round(r.tau, 6),
                "等価コンクリート_cm": round(r.t_eq_cm, 1),
                "等価コンクリート_m": round(r.t_eq_m, 4),
                "密度のみ等価_cm": round(r.t_eq_density_only_cm, 1),
                "理論残存": f"{r.attenuation:.6e}",
                "lambda_concrete_cm": round(r.lambda_concrete_cm, 2),
            }
        )
    return out


def depth_table(
    depths_m: Sequence[float],
    *,
    profile: str = DEFAULT_PROFILE,
    concrete_cm: float = 0.0,
) -> list[dict]:
    rows = []
    for d in depths_m:
        r = equiv_concrete(concrete_cm, d * 100.0, profile=profile)
        rows.append(
            {
                "深さ_m": d,
                "X_土": round(r.x_soil_gcm2, 1),
                "等価コンクリート_cm": round(r.t_eq_cm, 1),
                "等価コンクリート_m": round(r.t_eq_m, 3),
                "理論残存": f"{r.attenuation:.4e}",
            }
        )
    return rows


def write_reference_tables(out_dir: Path | None = None) -> list[Path]:
    out_dir = out_dir or TABLES
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    p1 = out_dir / "コンクリート_平均自由行程_詳細.csv"
    with p1.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "rho", "lambda_gcm2", "lambda_cm", "note"])
        w.writeheader()
        for row in compare_concrete_mfp_methods():
            w.writerow(
                {
                    "name": row["name"],
                    "rho": f"{row['rho']:.2f}",
                    "lambda_gcm2": f"{row['lambda_gcm2']:.2f}",
                    "lambda_cm": f"{row['lambda_cm']:.2f}",
                    "note": row["note"],
                }
            )
    written.append(p1)

    detail = compute_concrete_mfp()
    p1b = out_dir / "コンクリート_元素寄与.csv"
    with p1b.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["element", "weight_pct", "A", "sigma_mb", "lambda_i_gcm2", "w_over_lambda"],
        )
        w.writeheader()
        for p in detail["parts"]:
            w.writerow(
                {
                    "element": p["element"],
                    "weight_pct": f"{p['weight_pct']:.2f}",
                    "A": f"{p['A']:.3f}",
                    "sigma_mb": f"{p['sigma_mb']:.1f}",
                    "lambda_i_gcm2": f"{p['lambda_i_gcm2']:.1f}",
                    "w_over_lambda": f"{p['w_over_lambda']:.6f}",
                }
            )
    written.append(p1b)

    p2 = out_dir / "元素別_減衰長.csv"
    with p2.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["元素", "A", "sigma_mb", "lambda_gcm2"])
        w.writeheader()
        for sym, a in ELEMENTS.items():
            w.writerow(
                {
                    "元素": sym,
                    "A": f"{a:.3f}",
                    "sigma_mb": f"{elemental_sigma_mb(sym):.1f}",
                    "lambda_gcm2": f"{elemental_lambda_gcm2(sym):.1f}",
                }
            )
    written.append(p2)

    p2b = out_dir / "土壌_組成と減衰長.csv"
    soil_mats = [LOAM, JOSO, SHIMOSA, FILL, SOIL_SLIDE, PAVEMENT]
    with p2b.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["name", "rho", "lambda_gcm2", "lambda_cm", "composition", "note"],
        )
        w.writeheader()
        for m in soil_mats:
            total = sum(m.composition.values())
            comp = ", ".join(
                f"{k}:{v/total*100:.1f}%"
                for k, v in sorted(m.composition.items(), key=lambda kv: -kv[1])
            )
            w.writerow(
                {
                    "name": m.name,
                    "rho": f"{m.rho_g_cm3:.2f}",
                    "lambda_gcm2": f"{m.lambda_gcm2:.2f}",
                    "lambda_cm": f"{m.lambda_cm:.2f}",
                    "composition": comp,
                    "note": m.note,
                }
            )
    written.append(p2b)

    p2c = out_dir / "土壌_文献とプロファイル.csv"
    lit_rows = [
        {
            "topic": "関東ローム組成",
            "source": "教材土 + 筑波台地層序",
            "url": "https://www.jstage.jst.go.jp/article/bullgsj/52/8/52_347/_pdf/-char/ja",
            "note": "52(8)は沖積中心。ロームは火山灰質の代表値として別途推定",
        },
        {
            "topic": "常総粘土組成",
            "source": "凝灰質粘土（Al/Fe↑ Si↓）",
            "url": "",
            "note": "ロームと分離。密度1.65は地質予測・旭B1",
        },
        {
            "topic": "層序・密度",
            "source": "KuniJiban つくば市旭 B1",
            "url": "https://www.kunijiban.pwri.go.jp/viewer/",
            "note": "組成ではなく層厚・ρ の根拠。asahi プロファイル",
        },
        {
            "topic": "筑波台地層序",
            "source": "宇野沢ほか1988、坂田ほか2018/2024",
            "url": "",
            "note": "tsukuba: ローム3.5m→常総2.0m→下総",
        },
    ]
    with p2c.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["topic", "source", "url", "note"])
        w.writeheader()
        w.writerows(lit_rows)
    written.append(p2c)

    depths = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 10]
    for pname in ("tsukuba", "asahi", "textbook"):
        p = out_dir / f"深さ_等価コンクリート_{pname}.csv"
        rows = depth_table(depths, profile=pname)
        with p.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        written.append(p)

    sites = [
        ("地上", 0.0, 0.0),
        ("PF", 105.0, 0.0),
        ("linac", 150.0, 0.0),
        ("BT", 60.0, 220.0),
        ("KEKB", 80.0, 670.0),
    ]
    p4 = out_dir / "等価コンクリート_自動換算.csv"
    rows = equiv_concrete_batch(sites, profile=DEFAULT_PROFILE)
    with p4.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    written.append(p4)

    p5 = out_dir / "遮蔽換算_推奨パラメータ.csv"
    with p5.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["key", "value", "unit", "note"])
        w.writerow(["lambda_concrete_gcm2", f"{detail['lambda_gcm2']:.2f}", "g/cm2", detail["method"]])
        w.writerow(["lambda_concrete_cm", f"{detail['lambda_cm']:.2f}", "cm", "Λ/ρ, ρ=2.3"])
        w.writerow(["lambda_concrete_m", f"{detail['lambda_m']:.4f}", "m", "旧0.77 m は誤り"])
        w.writerow(["rho_concrete", "2.30", "g/cm3", "教材・申請の設計密度"])
        w.writerow(["lambda_soil_gcm2", f"{SOIL_SLIDE.lambda_gcm2:.2f}", "g/cm2", "教材土組成"])
        w.writerow(["lambda_loam_gcm2", f"{LOAM.lambda_gcm2:.2f}", "g/cm2", LOAM.note])
        w.writerow(["lambda_joso_gcm2", f"{JOSO.lambda_gcm2:.2f}", "g/cm2", JOSO.note])
        w.writerow(["lambda_shimosa_gcm2", f"{SHIMOSA.lambda_gcm2:.2f}", "g/cm2", SHIMOSA.note])
        w.writerow(["default_soil_profile", DEFAULT_PROFILE, "-", PROFILE_TSUKUBA.note])
        w.writerow(["composition_concrete", detail["composition"], "-", "教材スライド3"])
    written.append(p5)

    return written


# ---------------------------------------------------------------------------
# 他スクリプトが import する定数（詳細計算の推奨値）
# ---------------------------------------------------------------------------

_MFP = compute_concrete_mfp(rho_g_cm3=2.30)
LAMBDA_CONCRETE_GCM2 = float(_MFP["lambda_gcm2"])
LAMBDA_SOIL_GCM2 = float(SOIL_SLIDE.lambda_gcm2)
RHO_CONCRETE = 2.30
LAMBDA_CONCRETE_CM = LAMBDA_CONCRETE_GCM2 / RHO_CONCRETE
LAMBDA_CONCRETE_M = LAMBDA_CONCRETE_CM / 100.0
RHO_LOAM = LOAM.rho_g_cm3
RHO_JOSO = JOSO.rho_g_cm3
RHO_SHIMOSA = SHIMOSA.rho_g_cm3
RHO_IRON = IRON.rho_g_cm3
LAMBDA_IRON_GCM2 = float(IRON.lambda_gcm2)
LAMBDA_IRON_CM = LAMBDA_IRON_GCM2 / RHO_IRON
LOAM_MAX_CM = PROFILE_TSUKUBA.layers[0].thickness_m * 100.0


def theory_attenuation(t_eq_cm, a0: float = 1.0):
    """A = A0 · exp(-t_eq / λ_c)。単位はともに [cm]。"""
    import numpy as np

    x = np.asarray(t_eq_cm, dtype=float)
    return a0 * np.exp(-x / LAMBDA_CONCRETE_CM)


def soil_mass_thickness_gcm2(soil_cm: float, profile: str = DEFAULT_PROFILE) -> float:
    return PROFILES[profile].mass_thickness_gcm2(max(soil_cm, 0.0) / 100.0)


def main() -> None:
    parser = argparse.ArgumentParser(description="土・コンクリート → 等価コンクリート換算")
    parser.add_argument("--concrete", type=float, default=None, help="コンクリート厚 [cm]")
    parser.add_argument("--soil", type=float, default=0.0, help="土厚 [cm]")
    parser.add_argument("--profile", choices=list(PROFILES), default=DEFAULT_PROFILE)
    parser.add_argument("--report", action="store_true", help="MFP詳細と参照CSVを出力")
    parser.add_argument("--depth-table", action="store_true", help="深さ表を表示")
    args = parser.parse_args()

    if args.report:
        print("=== コンクリート平均自由行程（詳細） ===")
        for row in compare_concrete_mfp_methods():
            print(
                f"  {row['name']}: ρ={row['rho']:.2f}  "
                f"Λ={row['lambda_gcm2']:.1f} g/cm²  λ={row['lambda_cm']:.1f} cm  ({row['note']})"
            )
        detail = compute_concrete_mfp()
        print(
            f"\n推奨: λ = {detail['lambda_cm']:.2f} cm  "
            f"（Λ={detail['lambda_gcm2']:.1f}, ρ={detail['rho_g_cm3']}）"
        )
        print(f"手法: {detail['method']}")
        print(f"組成: {detail['composition']}")
        print("\n元素寄与:")
        for p in detail["parts"]:
            print(
                f"  {p['element']:2s}  {p['weight_pct']:5.1f}%  "
                f"A={p['A']:6.1f}  σ={p['sigma_mb']:6.1f} mb  "
                f"Λ_i={p['lambda_i_gcm2']:6.1f}  w/Λ={p['w_over_lambda']:.5f}"
            )
        print("\n=== 土壌 Λ（層別組成） ===")
        for m in (LOAM, JOSO, SHIMOSA, FILL, SOIL_SLIDE):
            print(
                f"  {m.name}: ρ={m.rho_g_cm3}  Λ={m.lambda_gcm2:.2f} g/cm²  "
                f"λ={m.lambda_cm:.1f} cm"
            )
        paths = write_reference_tables()
        print("\nCSV:")
        for p in paths:
            print(f"  {p}")
        return

    if args.depth_table:
        print(f"profile={args.profile}")
        for row in depth_table([0, 1, 2, 3, 4, 5, 6, 7, 8, 10], profile=args.profile):
            print(
                f"  z={row['深さ_m']:4.1f} m  X={row['X_土']:7.1f}  "
                f"t_eq={row['等価コンクリート_cm']:7.1f} cm  残存={row['理論残存']}"
            )
        return

    if args.concrete is None:
        parser.error("--concrete を指定するか --report / --depth-table を使ってください")

    r = equiv_concrete(args.concrete, args.soil, profile=args.profile)
    print(f"コンクリート {r.concrete_cm:.1f} cm + 土 {r.soil_cm:.1f} cm  （profile={r.profile}）")
    print(f"  X_c = {r.x_concrete_gcm2:.2f} g/cm²")
    print(f"  X_s = {r.x_soil_gcm2:.2f} g/cm²")
    print(f"  τ   = {r.tau:.4f}")
    print(f"  t_eq = {r.t_eq_cm:.1f} cm = {r.t_eq_m:.3f} m")
    print(f"  （密度のみ換算 {r.t_eq_density_only_cm:.1f} cm）")
    print(
        f"  λ_c = {r.lambda_concrete_cm:.2f} cm  "
        f"（Λ={r.lambda_concrete_gcm2:.1f} g/cm², ρ={r.rho_concrete}）"
    )
    print(f"  理論残存 e^{{-τ}} = {r.attenuation:.6e}")


if __name__ == "__main__":
    main()
