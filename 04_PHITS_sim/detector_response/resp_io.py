"""応答関数計算の出力（gas_track.out）を読み、検出器ごとの反応率 [cm^2] に直す。"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np

DET_ORDER = ["D1", "D2", "d1", "d2"]
R_SRC = {"D1": 35.0, "D2": 44.0, "d1": 22.0, "d2": 27.0}

N_A = 6.02214e23
RHO_HE3 = 1.254e-3
N_HE3 = RHO_HE3 * N_A / 3.01603
SIGMA0_CM2 = 5333e-24
E0_MEV = 2.53e-8


def sigma_he3(e_mev: np.ndarray) -> np.ndarray:
    """He-3(n,p) 断面積 [cm^2]。1/v 則（熱で 5333 b）。"""
    return SIGMA0_CM2 * np.sqrt(E0_MEV / e_mev)


def read_track(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """return (e_lo, e_hi, val[det, e], relerr[det, e])。val は有効ガス内の飛跡長 [cm/source]。"""
    pages: list[list[list[float]]] = []
    cur = None
    for line in path.read_text().splitlines():
        if re.match(r"^\s*#\s*e-lower", line):
            cur = []
            pages.append(cur)
            continue
        if cur is None or line.lstrip().startswith("#"):
            continue
        s = line.split()
        if len(s) != 4:
            continue
        try:
            cur.append([float(x) for x in s])
        except ValueError:
            continue
    arr = np.array([p for p in pages if p])
    return arr[0, :, 0], arr[0, :, 1], arr[:, :, 2], arr[:, :, 3]


def n_histories(run_dir: Path) -> int:
    text = (run_dir / "phits.out").read_text()
    return int(re.search(r"^\s*maxcas\s*=\s*(\d+)", text, re.M).group(1))


def response(run_dirs: list[Path]) -> tuple[np.ndarray, np.ndarray]:
    """複数シードをヒストリー数で重み付けして平均し、応答 [cm^2] と絶対誤差を返す（DET_ORDER 順）。"""
    rates, sig, wts = [], [], []
    for d in run_dirs:
        e_lo, e_hi, tl, rel = read_track(d / "gas_track.out")
        ec = np.sqrt(e_lo * e_hi)
        w = N_HE3 * sigma_he3(ec)
        r = np.sum(tl * w, axis=1)
        s = np.sqrt(np.sum((tl * rel * w) ** 2, axis=1))
        rates.append(r)
        sig.append(s)
        wts.append(n_histories(d))
    wt = np.array(wts, dtype=float)[:, None]
    mean = np.sum(wt * np.array(rates), axis=0) / wt.sum()
    err = np.sqrt(np.sum((wt * np.array(sig)) ** 2, axis=0)) / wt.sum()
    area = np.array([np.pi * R_SRC[k] ** 2 for k in DET_ORDER])
    n_src = len(DET_ORDER)
    return mean * area * n_src, err * area * n_src
