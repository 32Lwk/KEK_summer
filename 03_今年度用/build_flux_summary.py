#!/usr/bin/env python3
"""検出器ごとのフラックスまとめ表を作る。

方針（確定）:
  - 絶対 φ [n/cm²/s] は d1（黒鉛パイル）、D1（D1/d1 転送）、d2/D2（地上 d2/D1・D2/D1 転送）
  - 熱中性子管理棟・ゲイン調整は除外
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TABLES = ROOT / "測定_20260818" / "tables"
RECORD = TABLES / "測定記録.csv"
EFF = TABLES / "検出器効率_熱中性子校正版.csv"
OUT_LONG = TABLES / "フラックス_地点まとめ.csv"
OUT_WIDE = TABLES / "フラックス_検出器別相対.csv"

EPS_S_ROI_DEFAULTS = {
    "d1": 50.22,  # cm²（黒鉛パイル）
    "D1": 210.9,  # cm²（管理棟2階 D1/d1 転送）
    "d2": 26.17,  # cm²（地上 d2/D1 転送）
    "D2": 120.2,  # cm²（地上 D2/D1 転送・calc_D2_efficiency_transfer.py）
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


def load_eps_roi() -> dict[str, float]:
    out = dict(EPS_S_ROI_DEFAULTS)
    if EFF.exists():
        for r in csv.DictReader(EFF.open(encoding="utf-8")):
            det = (r.get("検出器") or "").strip()
            v = (r.get("epsilon_S_ROI_cm2") or "").strip()
            if det in ("d1", "D1", "d2", "D2") and v:
                out[det] = float(v)
    return out


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


def main() -> None:
    eps_roi = load_eps_roi()
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
            roi = float(r["roi_net_cps"])
            roi_err = float(r.get("roi_net_cps_err") or 0)
        except (KeyError, ValueError):
            continue
        live = float(r.get("live_s") or r.get("測定時間_s") or 0)
        valid = str(r.get("roi_net_valid", "1")) not in ("0", "False", "false")
        parsed.append(
            {
                "検出器": det,
                "シリアル": serial,
                "地点": site,
                "filename": fn,
                "roi_net_cps": roi,
                "roi_net_cps_err": roi_err,
                "roi_valid": valid,
                "live_s": live,
                "score": prefer_score(fn, live),
            }
        )

    best: dict[tuple[str, str], dict] = {}
    for p in parsed:
        key = (p["検出器"], p["地点"])
        if key not in best or p["score"] > best[key]["score"]:
            best[key] = p

    ref_cps: dict[str, float] = {}
    ref_site: dict[str, str] = {}
    for det in ("d1", "D1", "d2", "D2"):
        for site in ("地上", "管理棟2階"):
            hit = best.get((det, site))
            if hit and hit["roi_net_cps"] > 0:
                ref_cps[det] = hit["roi_net_cps"]
                ref_site[det] = site
                break

    def sort_key(item: tuple[str, str]) -> tuple:
        det, site = item
        si = SITES_ORDER.index(site) if site in SITES_ORDER else 99
        return (det, si)

    summary: list[dict] = []
    for det, site in sorted(best.keys(), key=sort_key):
        p = best[(det, site)]
        roi = p["roi_net_cps"]
        roi_err = p["roi_net_cps_err"]
        notes: list[str] = []

        if det in eps_roi:
            e = eps_roi[det]
            phi_abs = f"{roi / e:.6g}"
            phi_err = f"{roi_err / e:.6g}"
            tag = (
                "パイル"
                if det == "d1"
                else ("D1/d1転送" if det == "D1" else ("d2/D1転送" if det == "d2" else "D2/D1転送"))
            )
            notes.append(f"絶対φ=ROI/(εS_ROI={e:.4g} cm²,{tag})")
        else:
            phi_abs = ""
            phi_err = ""
            notes.append("絶対φなし（εS未較正）")

        if det in ref_cps:
            rel = f"{roi / ref_cps[det]:.4g}"
            rel_err = f"{roi_err / ref_cps[det]:.4g}"
            notes.append(f"相対基準={ref_site[det]}")
        else:
            rel = rel_err = ""
            notes.append("相対基準なし")

        if not p["roi_valid"] or roi <= 0:
            notes.append("ROI無効または≤0（参考）")

        summary.append(
            {
                "検出器": det,
                "地点": site,
                "filename": p["filename"],
                "シリアル": p["シリアル"],
                "ROI_net_CPS": f"{roi:.6g}",
                "ROI_net_CPS_err": f"{roi_err:.6g}",
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
        f"{d} εS_ROI={eps_roi[d]:.4g} cm²" for d in ("d1", "D1", "d2", "D2") if d in eps_roi
    )

    wide_rows: list[dict] = []
    for site in SITES_ORDER:
        wr: dict[str, str] = {"地点": site}
        any_hit = False
        for det in ("d1", "D1", "d2", "D2"):
            cell = by_det_site.get(det, {}).get(site)
            if cell:
                any_hit = True
                wr[f"{det}_ROI"] = cell["ROI_net_CPS"]
                wr[f"{det}_相対"] = cell["相対フラックス"]
                wr[f"{det}_絶対phi"] = cell["絶対phi_n_cm2_s"]
            else:
                wr[f"{det}_ROI"] = ""
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
            fields += [f"{det}_ROI", f"{det}_相対", f"{det}_絶対phi"]
        fields.append("注")
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(wide_rows)

    print("=" * 72)
    print("フラックス地点まとめ")
    print(
        f"  d1 ε×S_ROI = {eps_roi['d1']:.4g} cm²（パイル） / "
        f"D1 ε×S_ROI = {eps_roi['D1']:.4g} cm²（D1/d1転送） / "
        f"d2 ε×S_ROI = {eps_roi.get('d2', float('nan')):.4g} cm²（d2/D1転送） / "
        f"D2 ε×S_ROI = {eps_roi.get('D2', float('nan')):.4g} cm²（D2/D1転送）"
    )
    print(f"  相対基準: {ref_site}")
    print("=" * 72)
    print(f"{'検出器':4s} {'地点':12s} {'ROI':>10s} {'相対':>8s} {'φ[n/cm2/s]':>14s}")
    for row in summary:
        print(
            f"{row['検出器']:4s} {row['地点']:12s} {row['ROI_net_CPS']:>10s} "
            f"{(row['相対フラックス'] or '—'):>8s} {(row['絶対phi_n_cm2_s'] or '—'):>14s}"
        )
    print(f"\n出力: {OUT_LONG}")
    print(f"出力: {OUT_WIDE}")


if __name__ == "__main__":
    main()
