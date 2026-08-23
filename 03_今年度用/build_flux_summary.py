#!/usr/bin/env python3
"""検出器ごとのフラックスまとめ表を作る。

主窓: 191–764 keV（³He 壁効果連続帯）· 右側帯背景 → NET（ROI あり）
副窓: peak ROI（固定 ch、参考列 peak_ROI_net_CPS）

絶対 φ [n/cm²/s]:
  - d1 … 黒鉛パイル（wall ε×S）
  - D1 … 管理棟2階 D1/d1 転送（wall）
  - d2 / D2 … 地上 d2/D1・D2/D1 転送（wall；D2 地上は wall NET≤0 のため linac で ε×S 決定）
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TABLES = ROOT / "測定_20260818" / "tables"
RECORD = TABLES / "測定記録.csv"
EFF_WALL = TABLES / "検出器効率_壁効果191_764keV.csv"
OUT_LONG = TABLES / "フラックス_地点まとめ.csv"
OUT_WIDE = TABLES / "フラックス_検出器別相対.csv"

EPS_S_WALL_DEFAULTS = {
    "d1": 74.2,
    "D1": 134.6,
}

SITES_ORDER = [
    "地上",
    "管理棟2階",
    "管理棟1階",
    "PF",
    "linac",
    "linac_IRON",
    "放射線棟BT",
    "KEKB",
]


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
    if "linac" in low:
        return "linac"
    if re.search(r"(^|[_\s])pf($|[_\s])", low) or "PF_" in s or "_PF" in s:
        return "PF"
    if "BT" in s or "放射線" in s:
        return "放射線棟BT"
    if "KEKB" in s or "kekb" in low:
        return "KEKB"
    return "その他"


def prefer_score(filename: str, live_s: float) -> float:
    stem = Path(filename).stem
    score = live_s
    if stem.startswith("2026"):
        score += 1e7
    if stem.lower().startswith("smalld2"):
        score -= 1e6
    if stem.startswith("D2_20260822"):
        score -= 5e5
    return score


def load_eps_wall(best: dict[tuple[str, str], dict]) -> dict[str, float]:
    """191–764 keV 窓の ε×S [cm²]。"""
    out = dict(EPS_S_WALL_DEFAULTS)
    if EFF_WALL.exists():
        for r in csv.DictReader(EFF_WALL.open(encoding="utf-8")):
            det = (r.get("検出器") or "").strip()
            v = (r.get("epsilon_S_wall_cm2") or "").strip()
            if det in out and v:
                out[det] = float(v)

    def wall_cps(det: str, site: str) -> float | None:
        p = best.get((det, site))
        if not p or not p.get("wall_valid") or p["wall_net_cps"] <= 0:
            return None
        return p["wall_net_cps"]

    d1_g = wall_cps("D1", "地上")
    d2_g = wall_cps("d2", "地上")
    if d1_g and d2_g and "D1" in out:
        out["d2"] = out["D1"] * d2_g / d1_g

    d1_l = wall_cps("D1", "linac")
    d2_l = wall_cps("D2", "linac")
    if d1_l and d2_l and "D1" in out:
        out["D2"] = out["D1"] * d2_l / d1_l

    return out


def main() -> None:
    rows = list(csv.DictReader(RECORD.open(encoding="utf-8")))

    parsed: list[dict] = []
    for r in rows:
        fn = r.get("filename") or ""
        serial = str(r.get("シリアル") or "")
        det = detector_key(fn, serial)
        if det == "?":
            continue
        place = r.get("場所") or ""
        site = site_label(place, fn)
        if site.startswith("熱中性子") or site == "その他":
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
        parsed.append(
            {
                "検出器": det,
                "シリアル": serial,
                "地点": site,
                "filename": fn,
                "wall_net_cps": wall,
                "wall_net_cps_err": wall_err,
                "wall_valid": wall_valid,
                "peak_net_cps": peak,
                "peak_net_cps_err": peak_err,
                "peak_valid": peak_valid,
                "live_s": live,
                "score": prefer_score(fn, live),
            }
        )

    best: dict[tuple[str, str], dict] = {}
    for p in parsed:
        key = (p["検出器"], p["地点"])
        if key not in best or p["score"] > best[key]["score"]:
            best[key] = p

    eps_wall = load_eps_wall(best)

    ref_cps: dict[str, float] = {}
    ref_site: dict[str, str] = {}
    for det in ("d1", "D1", "d2", "D2"):
        for site in ("地上", "管理棟2階", "linac"):
            hit = best.get((det, site))
            if hit and hit["wall_valid"] and hit["wall_net_cps"] > 0:
                ref_cps[det] = hit["wall_net_cps"]
                ref_site[det] = site
                break

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
        notes: list[str] = []

        if det in eps_wall:
            e = eps_wall[det]
            if p["wall_valid"] and wall > 0:
                phi_abs = f"{wall / e:.6g}"
                phi_err = f"{wall_err / e:.6g}"
                tag = (
                    "パイル"
                    if det == "d1"
                    else (
                        "D1/d1転送"
                        if det == "D1"
                        else ("d2/D1転送" if det == "d2" else "D2/D1転送(linac)")
                    )
                )
                notes.append(f"絶対φ=NET/(εS_191-764={e:.4g} cm²,{tag})")
            else:
                phi_abs = phi_err = ""
                notes.append("wall NET 無効または≤0")
        else:
            phi_abs = phi_err = ""
            notes.append("絶対φなし（εS未較正）")

        if det in ref_cps and p["wall_valid"] and wall > 0:
            rel = f"{wall / ref_cps[det]:.4g}"
            rel_err = f"{wall_err / ref_cps[det]:.4g}"
            notes.append(f"相対基準={ref_site[det]}")
        else:
            rel = rel_err = ""
            if det in ref_cps:
                notes.append(f"相対基準={ref_site[det]}（当該地点 wall 不可）")

        if not p["wall_valid"] or wall <= 0:
            notes.append("主窓191–764keV NET 無効（参考: peak ROI）")

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
                "絶対phi_n_cm2_s": phi_abs,
                "絶対phi_err": phi_err,
                "備考": "; ".join(notes),
            }
        )

    by_det_site: dict[str, dict[str, dict]] = {}
    for row in summary:
        by_det_site.setdefault(row["検出器"], {})[row["地点"]] = row

    ref_note = "; ".join(f"{d}基準={ref_site[d]}" for d in ("d1", "D1", "d2", "D2") if d in ref_site)
    ref_note += "; " + "; ".join(
        f"{d} εS_191-764={eps_wall[d]:.4g} cm²" for d in ("d1", "D1", "d2", "D2") if d in eps_wall
    )

    wide_rows: list[dict] = []
    for site in SITES_ORDER:
        wr: dict[str, str] = {"地点": site}
        any_hit = False
        for det in ("d1", "D1", "d2", "D2"):
            cell = by_det_site.get(det, {}).get(site)
            if cell:
                any_hit = True
                wr[f"{det}_NET"] = cell["NET_CPS_191_764keV"]
                wr[f"{det}_相対"] = cell["相対フラックス"]
                wr[f"{det}_絶対phi"] = cell["絶対phi_n_cm2_s"]
            else:
                wr[f"{det}_NET"] = ""
                wr[f"{det}_相対"] = ""
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
            fields += [f"{det}_NET", f"{det}_相対", f"{det}_絶対phi"]
        fields.append("注")
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(wide_rows)

    print("=" * 72)
    print("フラックス地点まとめ（主窓 191–764 keV · NET）")
    for d in ("d1", "D1", "d2", "D2"):
        if d in eps_wall:
            print(f"  {d} ε×S_191-764 = {eps_wall[d]:.4g} cm²")
    print(f"  相対基準: {ref_site}")
    print("=" * 72)
    print(f"{'検出器':4s} {'地点':12s} {'NET191-764':>12s} {'相対':>8s} {'φ[n/cm2/s]':>14s}")
    for row in summary:
        print(
            f"{row['検出器']:4s} {row['地点']:12s} "
            f"{(row['NET_CPS_191_764keV'] or '—'):>12s} "
            f"{(row['相対フラックス'] or '—'):>8s} "
            f"{(row['絶対phi_n_cm2_s'] or '—'):>14s}"
        )
    print(f"\n出力: {OUT_LONG}")
    print(f"出力: {OUT_WIDE}")


if __name__ == "__main__":
    main()
