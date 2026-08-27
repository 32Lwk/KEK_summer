#!/usr/bin/env python3
"""検出器ごとのフラックスまとめ表を作る。

主窓: 191–764 keV（³He 壁効果連続帯）· 側帯/平坦部背景 → NET
副窓: peak ROI（参考列 peak_ROI_net_CPS）

絶対 φ [n/cm²/s]:
  φ = R_wall_NET / εS_wall

εS_wall は `calc_window_comparison.py` → `flux_calibration.py` が
`tables/検出器効率_壁効果191_764keV.csv` に書き込む値を唯一のソースとする。
先に calc_window_comparison.py を実行すること。
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from flux_calibration import (  # noqa: E402
    eps_peak_dict,
    eps_wall_dict,
    load_wall_efficiencies_csv,
)
from mca_common import is_pf_d2_mca  # noqa: E402

TABLES = ROOT / "測定_20260818" / "tables"
RECORD = TABLES / "測定記録.csv"
OUT_LONG = TABLES / "フラックス_地点まとめ.csv"
OUT_WIDE = TABLES / "フラックス_検出器別相対.csv"

# wall: φ = NET_191–764 / εS_wall
# peak: φ = peak ROI NET / εS_peak（本解析採用: peak764_cut200）
FLUX_WINDOW = "peak"

SITES_ORDER = [
    "地上",
    "管理棟2階",
    "管理棟1階",
    "testhole",
    "PF",
    "linac",
    "PS",
    "放射線棟BT",
    "KEKB",
]

# 本解析のフラックスまとめから除外（測定記録には残る）
ANALYSIS_EXCLUDE_SITES = frozenset({"linac_IRON", "linacIRON"})

CALIB_TAG = {
    "d1": "メーカー123×パイル窓比",
    "D1": "メーカー450×d1窓比",
    "d2": "d2/D1転送@地上",
    "D2": "D2/D1転送@linac",
}


def detector_key(filename: str, serial: str) -> str:
    stem = Path(filename).stem
    if re.search(r"(^|_)D2($|_)", stem) or stem.startswith("D2"):
        return "D2"
    if re.search(r"(^|_)d2($|_)", stem) or stem.startswith("d2") or "smalld2" in stem.lower():
        return "d2"
    if re.search(r"(^|_)D1($|_)", stem) or stem.startswith("D1"):
        return "D1"
    if re.search(r"(^|_)d1($|_)", stem) or stem.startswith("d1"):
        return "d1"
    return "?"


def site_label(place: str, filename: str) -> str:
    s = f"{place} {filename}"
    low = s.lower()
    if "熱中性子" in s:
        return "熱中性子管理棟"
    if "地上" in s or "ground" in low:
        return "地上"
    if "管理棟2" in s or "kanri2f" in low:
        return "管理棟2階"
    if "管理棟1" in s or "kanri1f" in low:
        return "管理棟1階"
    if "iron" in low or "IRON" in s:
        return "linac_IRON"
    if "error" in low:
        return "その他"
    if "testhole" in low:
        return "testhole"
    if re.search(r"(^|[_\s])ps($|[_\s])", low) or "_PS" in s:
        return "PS"
    if "linac" in low:
        return "linac"
    if re.search(r"(^|[_\s])pf($|[_\s])", low) or "PF_" in s or "_PF" in s:
        return "PF"
    if "BT" in s or "放射線" in s:
        return "放射線棟BT"
    if "KEKB" in s or "kekb" in low:
        return "KEKB"
    if "ep1" in low or "k2k" in low:
        return "K2KBL"
    return "その他"


def prefer_score(filename: str, live_s: float, *, wall_valid: bool = True, bg_mode: str = "") -> float:
    stem = Path(filename).stem
    score = live_s
    if stem.startswith("2026"):
        score += 1e7
    if stem.lower().startswith("smalld2"):
        score -= 1e6
    if stem.startswith("D2_20260822"):
        score -= 5e5
    if not wall_valid:
        score -= 5e6
    if bg_mode == "none_gross":
        score -= 1e6
    if "error" in stem.lower():
        score -= 1e7
    return score


def main() -> None:
    use_peak = FLUX_WINDOW.strip().lower() == "peak"
    wall_eff = load_wall_efficiencies_csv()
    eps_wall = eps_wall_dict(wall_eff)
    eps_peak = eps_peak_dict(wall_eff)
    missing = [d for d in ("d1", "D1", "d2", "D2") if d not in eps_wall]
    if missing:
        print(
            f"ERROR: εS_wall 未較正: {missing}\n"
            "  先に python calc_window_comparison.py を実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)
    if use_peak:
        missing_p = [d for d in ("d1", "D1", "d2", "D2") if d not in eps_peak]
        if missing_p:
            print(
                f"ERROR: εS_peak 未較正: {missing_p}\n"
                "  先に python calc_window_comparison.py を実行してください。",
                file=sys.stderr,
            )
            sys.exit(1)

    rows = list(csv.DictReader(RECORD.open(encoding="utf-8")))

    parsed: list[dict] = []
    for r in rows:
        fn = r.get("filename") or ""
        if is_pf_d2_mca(fn):
            continue
        serial = str(r.get("シリアル") or "")
        det = detector_key(fn, serial)
        if det == "?":
            continue
        place = r.get("場所") or ""
        site = site_label(place, fn)
        if site.startswith("熱中性子") or site == "その他" or site in ANALYSIS_EXCLUDE_SITES:
            continue
        try:
            wall = float(r["wall_net_cps"])
            wall_err = float(r.get("wall_net_cps_err") or 0)
            peak = float(r["roi_net_cps"])
            peak_err = float(r.get("roi_net_cps_err") or 0)
        except (KeyError, ValueError):
            continue
        live = float(r.get("live_s") or r.get("測定時間_s") or 0)
        wall_valid = str(r.get("wall_net_valid", "1")) not in ("0", "False", "false")
        peak_valid = str(r.get("roi_net_valid", "1")) not in ("0", "False", "false")
        if use_peak:
            score = prefer_score(
                fn,
                live,
                wall_valid=peak_valid and peak > 0,
                bg_mode="",
            )
        else:
            score = prefer_score(
                fn,
                live,
                wall_valid=wall_valid and wall > 0,
                bg_mode=(r.get("wall_bg_mode") or "").strip(),
            )
        parsed.append(
            {
                "検出器": det,
                "シリアル": serial,
                "地点": site,
                "filename": fn,
                "wall_net_cps": wall,
                "wall_net_cps_err": wall_err,
                "wall_valid": wall_valid,
                "wall_bg_mode": (r.get("wall_bg_mode") or "").strip(),
                "peak_net_cps": peak,
                "peak_net_cps_err": peak_err,
                "peak_valid": peak_valid,
                "live_s": live,
                "score": score,
            }
        )

    best: dict[tuple[str, str], dict] = {}
    for p in parsed:
        key = (p["検出器"], p["地点"])
        if key not in best or p["score"] > best[key]["score"]:
            best[key] = p

    eps_use = eps_peak if use_peak else eps_wall
    net_key = "peak_net_cps" if use_peak else "wall_net_cps"
    err_key = "peak_net_cps_err" if use_peak else "wall_net_cps_err"
    valid_key = "peak_valid" if use_peak else "wall_valid"
    eps_label = "εS_peak" if use_peak else "εS_wall"
    window_label = "peak ROI NET" if use_peak else "191–764 keV NET"

    ref_cps: dict[str, float] = {}
    ref_site: dict[str, str] = {}
    for det in ("d1", "D1", "d2", "D2"):
        for site in ("地上", "管理棟2階", "linac"):
            hit = best.get((det, site))
            if hit and hit[valid_key] and hit[net_key] > 0:
                ref_cps[det] = hit[net_key]
                ref_site[det] = site
                break

    phi0_d1_ground: float | None = None
    d1_ground = best.get(("D1", "地上"))
    if d1_ground and d1_ground[valid_key] and d1_ground[net_key] > 0:
        phi0_d1_ground = d1_ground[net_key] / eps_use["D1"]

    def sort_key(item: tuple[str, str]) -> tuple:
        det, site = item
        si = SITES_ORDER.index(site) if site in SITES_ORDER else 99
        return (det, si)

    summary: list[dict] = []
    for det, site in sorted(best.keys(), key=sort_key):
        p = best[(det, site)]
        wall = p["wall_net_cps"]
        wall_err = p["wall_net_cps_err"]
        peak = p["peak_net_cps"]
        peak_err = p["peak_net_cps_err"]
        net = p[net_key]
        net_err = p[err_key]
        valid = bool(p[valid_key] and net > 0)
        notes: list[str] = []

        e = eps_use[det]
        if valid:
            phi_abs = f"{net / e:.6g}"
            phi_err = f"{net_err / e:.6g}"
            notes.append(f"絶対φ={window_label}/({eps_label}={e:.4g},{CALIB_TAG[det]})")
        else:
            phi_abs = phi_err = ""
            notes.append(f"{window_label} 無効または≤0")

        if det in ref_cps and valid:
            rel = f"{net / ref_cps[det]:.4g}"
            rel_err = f"{net_err / ref_cps[det]:.4g}"
            notes.append(f"相対基準={ref_site[det]}")
        else:
            rel = rel_err = ""
            if det in ref_cps:
                notes.append(f"相対基準={ref_site[det]}（当該地点 NET 不可）")

        if phi0_d1_ground and valid:
            phi_val = net / e
            rel_d1 = f"{phi_val / phi0_d1_ground:.4g}"
            rel_d1_err = f"{net_err / e / phi0_d1_ground:.4g}"
        else:
            rel_d1 = rel_d1_err = ""

        if not p["wall_valid"] or wall <= 0:
            notes.append("参考: wall NET 無効")

        summary.append(
            {
                "検出器": det,
                "地点": site,
                "filename": p["filename"],
                "シリアル": p["シリアル"],
                "NET_CPS_191_764keV": f"{wall:.6g}" if p["wall_valid"] and wall > 0 else "",
                "NET_CPS_191_764keV_err": f"{wall_err:.6g}" if p["wall_valid"] and wall > 0 else "",
                "peak_ROI_net_CPS": f"{peak:.6g}",
                "peak_ROI_net_CPS_err": f"{peak_err:.6g}",
                "相対_基準地点": ref_site.get(det, ""),
                "相対フラックス": rel,
                "相対フラックス_err": rel_err,
                "相対_D1地上": rel_d1,
                "相対_D1地上_err": rel_d1_err,
                "絶対phi_n_cm2_s": phi_abs,
                "絶対phi_err": phi_err,
                "備考": "; ".join(notes),
            }
        )

    by_det_site: dict[str, dict[str, dict]] = {}
    for row in summary:
        by_det_site.setdefault(row["検出器"], {})[row["地点"]] = row

    ref_note = "; ".join(f"{d}基準={ref_site[d]}" for d in ("d1", "D1", "d2", "D2") if d in ref_site)
    if use_peak:
        ref_note += "; " + "; ".join(
            f"{d} εS_peak={eps_peak[d]:.4g} cm²" for d in ("d1", "D1", "d2", "D2")
        )
        ref_note += "; FLUX_WINDOW=peak"
    else:
        ref_note += "; " + "; ".join(
            f"{d} εS_wall={eps_wall[d]:.4g} cm²" for d in ("d1", "D1", "d2", "D2")
        )
    if phi0_d1_ground:
        ref_note += f"; D1地上φ={phi0_d1_ground:.4g} n/cm²/s"

    wide_rows: list[dict] = []
    for site in SITES_ORDER:
        wr: dict[str, str] = {"地点": site}
        any_hit = False
        for det in ("d1", "D1", "d2", "D2"):
            cell = by_det_site.get(det, {}).get(site)
            if cell:
                any_hit = True
                wr[f"{det}_NET"] = (
                    cell["peak_ROI_net_CPS"] if use_peak else cell["NET_CPS_191_764keV"]
                )
                wr[f"{det}_相対"] = cell["相対フラックス"]
                wr[f"{det}_相対D1地上"] = cell["相対_D1地上"]
                wr[f"{det}_絶対phi"] = cell["絶対phi_n_cm2_s"]
            else:
                wr[f"{det}_NET"] = ""
                wr[f"{det}_相対"] = ""
                wr[f"{det}_相対D1地上"] = ""
                wr[f"{det}_絶対phi"] = ""
        if any_hit:
            wr["注"] = ref_note
            wide_rows.append(wr)

    with OUT_LONG.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        w.writeheader()
        w.writerows(summary)

    with OUT_WIDE.open("w", newline="", encoding="utf-8") as f:
        fields = ["地点"]
        for det in ("d1", "D1", "d2", "D2"):
            fields += [f"{det}_NET", f"{det}_相対", f"{det}_相対D1地上", f"{det}_絶対phi"]
        fields.append("注")
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(wide_rows)

    print("=" * 72)
    if use_peak:
        print("フラックス地点まとめ（764 keV peak ROI · NET）")
        for d in ("d1", "D1", "d2", "D2"):
            print(f"  {d} ε×S_peak = {eps_peak[d]:.4g} cm²  ({CALIB_TAG[d]})")
        net_col = "peak_ROI_net_CPS"
        net_hdr = "NET_peak"
    else:
        print("フラックス地点まとめ（主窓 191–764 keV · NET）")
        for d in ("d1", "D1", "d2", "D2"):
            print(f"  {d} ε×S_wall = {eps_wall[d]:.4g} cm²  ({CALIB_TAG[d]})")
        net_col = "NET_CPS_191_764keV"
        net_hdr = "NET191-764"
    print(f"  相対基準（検出器別）: {ref_site}")
    if phi0_d1_ground:
        print(f"  図18 正規化: D1 地上 φ = {phi0_d1_ground:.4g} n/cm²/s")
    print("=" * 72)
    print(f"{'検出器':4s} {'地点':12s} {net_hdr:>12s} {'相対':>8s} {'D1地上':>8s} {'φ[n/cm2/s]':>14s}")
    for row in summary:
        print(
            f"{row['検出器']:4s} {row['地点']:12s} "
            f"{(row[net_col] or '—'):>12s} "
            f"{(row['相対フラックス'] or '—'):>8s} "
            f"{(row['相対_D1地上'] or '—'):>8s} "
            f"{(row['絶対phi_n_cm2_s'] or '—'):>14s}"
        )
    print(f"\n出力: {OUT_LONG}")
    print(f"出力: {OUT_WIDE}")


if __name__ == "__main__":
    main()
