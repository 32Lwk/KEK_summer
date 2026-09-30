"""PHITS T-Track 出力（axis=eng、複数ページ）の読み込みと複数ランの積算。"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np

PARTS = ["neutron", "muon-", "muon+", "proton"]


def read_pages(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """return (e_lo, e_hi, val[page, e, part], relerr[page, e, part])."""
    pages: list[list[list[float]]] = []
    cur: list[list[float]] | None = None
    for line in path.read_text().splitlines():
        if re.match(r"^\s*#\s*e-lower", line):
            cur = []
            pages.append(cur)
            continue
        if cur is None:
            continue
        s = line.split()
        if not s or line.lstrip().startswith("#"):
            continue
        try:
            row = [float(x) for x in s]
        except ValueError:
            continue
        if len(row) == 2 + 2 * len(PARTS):
            cur.append(row)
    arr = np.array([p for p in pages if p])
    e_lo = arr[0, :, 0]
    e_hi = arr[0, :, 1]
    val = arr[:, :, 2::2]
    err = arr[:, :, 3::2]
    return e_lo, e_hi, val, err


def n_histories(run_dir: Path) -> int:
    text = (run_dir / "phits.out").read_text()
    cas = int(re.search(r"^\s*maxcas\s*=\s*(\d+)", text, re.M).group(1))
    bch = int(re.search(r"^\s*maxbch\s*=\s*(\d+)", text, re.M).group(1))
    return cas * bch


def accumulate(paths: list[Path]) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """ヒストリー数で重み付けした平均。相対誤差は二乗和から合成する。"""
    vals, sig, wts = [], [], []
    for p in paths:
        e_lo, e_hi, v, r = read_pages(p)
        vals.append(v)
        sig.append(v * r)
        wts.append(n_histories(p.parent))
    w = np.array(wts, dtype=float)[:, None, None, None]
    mean = np.sum(w * np.array(vals), axis=0) / w.sum()
    sig = np.sqrt(np.sum((w * np.array(sig)) ** 2, axis=0)) / w.sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.where(mean > 0, sig / mean, 0.0)
    return e_lo, e_hi, mean, rel


def group(e_lo, e_hi, val, rel, lo: float, hi: float, weight=None):
    """エネルギー範囲 [lo, hi) MeV で積分したフラックスと絶対誤差（ページごと）。"""
    m = (e_lo >= lo * 0.999) & (e_hi <= hi * 1.001)
    w = np.ones_like(e_lo) if weight is None else weight
    v = np.sum(val[:, m, :] * w[m, None], axis=1)
    s = np.sqrt(np.sum((val[:, m, :] * rel[:, m, :] * w[m, None]) ** 2, axis=1))
    return v, s


def one_over_v_weight(e_lo, e_hi):
    """裸の He-3 管の応答（1/v）に対応する熱中性子等価の重み sqrt(0.0253 eV / E)。"""
    ec = np.sqrt(e_lo * e_hi)
    return np.sqrt(2.53e-8 / ec)
