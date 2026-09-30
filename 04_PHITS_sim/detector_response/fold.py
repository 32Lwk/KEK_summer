#!/usr/bin/env python3
"""PHITS の応答関数 × 中性子スペクトルで、各地点の計数率（peak ROI）を実効面積を介さずに予測する。

予測計数率 = f_peak × Σ_E R_det(E) φ(E)
  R_det(E) : runs/E*_s* から求めた応答 [cm^2]（等方場、全反応数）
  φ(E)     : 中性子スペクトル [cm^-2 s^-1]（半無限コンクリート中の深さ分布、または地点ごとの部屋の中）
  f_peak   : 全計数に対する peak ROI の割合（黒鉛パイルで d1 から求めた 0.5695）

出力: results/response.csv, results/fold_at_sites.csv
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
MCS = HERE.parent / "muon_capture_study"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(MCS))

from resp_io import DET_ORDER, response  # noqa: E402

ENERGIES = [5.0e-9, 2.53e-8, 1.0e-7, 1.0e-6, 1.0e-5, 1.0e-4, 1.0e-3, 1.0e-2, 3.0e-2, 0.1, 0.3,
            1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 200.0, 1000.0]
F_PEAK = 0.5695
OUT = HERE / "results"

FLUX_CSV = HERE.parents[1] / "03_今年度用" / "測定_20260818" / "denoised_runs" / "peak764_cut200" / "tables" / "フラックス_地点まとめ.csv"
MEASURED_FILES = {
    ("D1", "地上"): "D1_20260819_1530_地上.mca", ("D1", "テストホール"): "D1_20260823_1510_linac_testhole.mca",
    ("D1", "PF"): "D1_20260820_0807_PF.mca", ("D1", "放射線棟BT"): "D1_20260819_1854_放射線棟BT.mca",
    ("D1", "Linac3"): "D1_20260823_1510_Linac3.mca", ("D1", "PS"): "D1_20260823_1510_PS.mca",
    ("D1", "KEKB"): "D1_20260820_1939_KEKB.mca",
    ("d1", "テストホール"): "d1_20260823_1509_linac_testhole.mca", ("d1", "Linac3"): "d1_20260823_1509_Linac3.mca",
    ("d1", "PS"): "d1_20260823_1509_PS.mca",
    ("D2", "地上"): "D2_20260822_155048_地上.mca", ("D2", "PF"): "D2_20260822_115234_PF.mca",
    ("D2", "Linac3"): "D2_20260823_0835_Linac3.mca", ("D2", "K2K"): "D2_20260826_0026_ep1.mca",
    ("d2", "地上"): "d2_20260822_155046_地上.mca", ("d2", "放射線棟BT"): "d2_20260819_1859_放射線棟BT.mca",
    ("d2", "Linac3"): "d2_20260823_0834_Linac3.mca", ("d2", "KEKB"): "d2_20260820_1939_KEKB.mca",
}


def load_measured() -> dict[tuple[str, str], tuple[float, float]]:
    """(det, site) -> (peak ROI の R_NET [s^-1], 誤差)。解析の地点まとめ表から読む。"""
    with FLUX_CSV.open(encoding="utf-8") as f:
        rows = {r["filename"]: r for r in csv.DictReader(f)}
    return {k: (float(rows[fn]["peak_ROI_net_CPS"]), float(rows[fn]["peak_ROI_net_CPS_err"]))
            for k, fn in MEASURED_FILES.items()}


MEASURED = load_measured()
SITE_TEQ = {"地上": 0.0, "テストホール": 57.0, "PF": 105.0, "放射線棟BT": 189.1, "Linac3": 300.0,
            "K2K": 444.0, "PS": 480.0, "KEKB": 525.4}


def response_table() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """return (E, R[E, det], sigma[E, det])。"""
    rs, ss = [], []
    for i in range(1, len(ENERGIES) + 1):
        dirs = sorted(HERE.glob(f"runs/E{i}_s*"))
        r, s = response(dirs)
        rs.append(r)
        ss.append(s)
    return np.array(ENERGIES), np.array(rs), np.array(ss)


def interp_response(e_tab, r_tab, e):
    """log-log 補間。表の範囲外は端の値で一定とする。"""
    le = np.log(np.clip(e, e_tab[0], e_tab[-1]))
    out = np.empty((len(e), r_tab.shape[1]))
    for j in range(r_tab.shape[1]):
        out[:, j] = np.exp(np.interp(le, np.log(e_tab), np.log(r_tab[:, j])))
    return out


def fold(e_lo, e_hi, spec, spec_rel, e_tab, r_tab):
    """spec[..., E] と応答から、全反応数の計数率 [s^-1] と統計誤差を返す（検出器の軸を最後に付ける）。"""
    ec = np.sqrt(e_lo * e_hi)
    r = interp_response(e_tab, r_tab, ec)
    rate = np.tensordot(spec, r, axes=([-1], [0]))
    err = np.sqrt(np.tensordot((spec * spec_rel) ** 2, r**2, axes=([-1], [0])))
    return rate, err


def write_response(e_tab, r_tab, s_tab) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "response.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["E_MeV"] + [f"R_{d}_cm2" for d in DET_ORDER] + [f"err_{d}_cm2" for d in DET_ORDER])
        for e, r, s in zip(e_tab, r_tab, s_tab):
            w.writerow([f"{e:.3e}"] + [f"{x:.3f}" for x in r] + [f"{x:.3f}" for x in s])


def _finished(run: Path, tally: str) -> bool:
    log = run / "run.log"
    return log.exists() and "finished normally" in log.read_text() and (run / tally).exists()


def load_case(runs_dir: Path, case: str, tally: str):
    from phits_io import accumulate
    runs = sorted(r for r in runs_dir.glob(f"{case}_s*") if _finished(r, tally))
    if not runs:
        raise SystemExit(f"no finished runs for {case} in {runs_dir}")
    e_lo, e_hi, val, rel = accumulate([r / tally for r in runs])
    return e_lo, e_hi, val[:, :, 0], rel[:, :, 0], len(runs)


def source_ratio(runs_dir: Path) -> float:
    import re
    def total(case):
        vals = []
        for r in sorted(runs_dir.glob(f"{case}_s*")):
            if not (r / "phits.out").exists():
                continue
            m = re.search(r"^\$\s*totfact\s*=\s*(\S+)\s*# revised", (r / "phits.out").read_text(), re.M)
            if m:
                vals.append(abs(float(m.group(1))))
        return float(np.mean(vals))
    return total("mum") / total("mup")


def components(runs_dir: Path, tally: str, e_tab, r_tab, cases=("had", "mum", "mup")):
    """成分ごとの予測計数率（全反応数）[page, det] と誤差を返す。"""
    ratio = source_ratio(runs_dir)
    out = {}
    for key in cases:
        e_lo, e_hi, v, s, n = load_case(runs_dir, key, tally)
        out[key] = fold(e_lo, e_hi, v, s, e_tab, r_tab)
    h, hs = out[cases[0]]
    m, ms = out[cases[1]]
    p, ps = out[cases[2]]
    comp = {
        "had": (h, hs),
        "cap": (m - ratio * p, np.hypot(ms, ratio * ps)),
        "fast": (p * (1 + ratio), ps * (1 + ratio)),
    }
    comp["total"] = (h + m + p, np.sqrt(hs**2 + ms**2 + ps**2))
    return comp, ratio


SITE_RUNS = HERE.parent / "site_models" / "runs"
ROOM_VOL = np.array([1.2e8, 6.0e7])


def room_components(site: str, e_tab, r_tab, page: str = "all"):
    """地点モデルの部屋の中の成分ごとの予測計数率（全反応数）[det]。
    page="all" は部屋全体（体積平均）、"floor" は床から 1 m。KEKBdry のハドロンは KEKB で代用する。"""
    ratio = source_ratio(SITE_RUNS / site)
    out = {}
    for key in ("had", "mum", "mup"):
        d = SITE_RUNS / site
        if key == "had" and not any(d.glob("had_s*")):
            d = SITE_RUNS / "KEKB"
        e_lo, e_hi, v, s, _ = load_case(d, key, "room_spec.out")
        rate, err = fold(e_lo, e_hi, v, s, e_tab, r_tab)
        if page == "floor":
            out[key] = (rate[1], err[1])
        else:
            w = ROOM_VOL[:, None] / ROOM_VOL.sum()
            out[key] = ((w * rate).sum(axis=0), np.sqrt(((w * err) ** 2).sum(axis=0)))
    h, hs = out["had"]
    m, ms = out["mum"]
    p, ps = out["mup"]
    comp = {
        "had": (h, hs),
        "cap": (m - ratio * p, np.hypot(ms, ratio * ps)),
        "fast": (p * (1 + ratio), ps * (1 + ratio)),
    }
    comp["total"] = (h + m + p, np.sqrt(hs**2 + ms**2 + ps**2))
    return comp


def tunnel_components(e_tab, r_tab):
    """天井 300 cm のトンネル（幅・高さ 3 m、長さ 20 m）の中の成分ごとの予測計数率 [det]。
    mu+ は計算していないので、同じ体系のコンクリート中（300--600 cm）の mu+/mu- 比で補う。"""
    runs = MCS / "runs"
    ratio = source_ratio(runs)
    e_lo, e_hi, v, s, _ = load_case(runs, "hadT", "tunnel_spec.out")
    h, hs = (a[0] for a in fold(e_lo, e_hi, v, s, e_tab, r_tab))
    e_lo, e_hi, v, s, _ = load_case(runs, "mumT", "tunnel_spec.out")
    m, ms = (a[0] for a in fold(e_lo, e_hi, v, s, e_tab, r_tab))
    slab = {}
    for key in ("mum", "mup"):
        e_lo, e_hi, v, s, _ = load_case(runs, key, "depth_spec.out")
        rate, _ = fold(e_lo, e_hi, v, s, e_tab, r_tab)
        teq = -(-700.0 + 20.0 * (np.arange(rate.shape[0]) + 0.5))
        slab[key] = rate[(teq >= 300.0) & (teq <= 600.0)].mean(axis=0)
    p = m * slab["mup"] / slab["mum"]
    ps = ms * slab["mup"] / slab["mum"]
    comp = {
        "had": (h, hs),
        "cap": (m - ratio * p, np.hypot(ms, ratio * ps)),
        "fast": (p * (1 + ratio), ps * (1 + ratio)),
    }
    comp["total"] = (h + m + p, np.sqrt(hs**2 + ms**2 + ps**2))
    return comp


def slab_site_values(comp, teq_c, x, half=40.0):
    m = np.abs(teq_c - x) <= half
    return {k: (float(v[m].mean(axis=0)[0]) if v.ndim == 1 else v[m].mean(axis=0),
                np.sqrt((s[m] ** 2).sum(axis=0)) / m.sum()) for k, (v, s) in comp.items()}


def main() -> None:
    e_tab, r_tab, s_tab = response_table()
    write_response(e_tab, r_tab, s_tab)
    print(OUT / "response.csv")

    depth, ratio = components(MCS / "runs", "depth_spec.out", e_tab, r_tab)
    air, _ = components(MCS / "runs", "air_spec.out", e_tab, r_tab)
    nz = depth["total"][0].shape[0]
    teq_c = -(-700.0 + 20.0 * (np.arange(nz) + 0.5))
    print(f"mu-/mu+ = {ratio:.3f}")

    rows = []
    for (det, site), (meas, meas_e) in MEASURED.items():
        j = DET_ORDER.index(det)
        if site == "地上":
            vals = {k: (v[0, j], s[0, j]) for k, (v, s) in air.items()}
        else:
            sv = slab_site_values(depth, teq_c, SITE_TEQ[site])
            vals = {k: (v[j], s[j]) for k, (v, s) in sv.items()}
        pred = {k: F_PEAK * v for k, (v, _) in vals.items()}
        pred_e = F_PEAK * vals["total"][1]
        rows.append({
            "検出器": det, "地点": site, "teq_cm": f"{SITE_TEQ[site]:.0f}",
            "実測_RNET": f"{meas:.4f}", "実測_誤差": f"{meas_e:.4f}",
            "予測_大気ハドロン": f"{pred['had']:.4e}", "予測_負μ捕獲": f"{pred['cap']:.4e}",
            "予測_高速μ": f"{pred['fast']:.4e}", "予測_合計": f"{pred['total']:.4e}",
            "予測_統計誤差": f"{pred_e:.1e}",
            "実測/予測": f"{meas / pred['total']:.2f}",
            "μ起源の割合": f"{(pred['cap'] + pred['fast']) / pred['total']:.2f}",
        })
    with (OUT / "fold_at_sites.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(f"{r['検出器']:3s} {r['地点']:8s} teq={r['teq_cm']:>4s}  meas={r['実測_RNET']:>7s}  "
              f"pred={float(r['予測_合計']):.4f}  meas/pred={r['実測/予測']:>5s}  mu={r['μ起源の割合']}")
    print(OUT / "fold_at_sites.csv")


if __name__ == "__main__":
    main()
