#!/usr/bin/env python3
"""同一 main.inp を Web PHITS で N 回回し、de.out / neutron_he3.out を加重平均する。

Web PHITS は 1 ジョブ約 3 分制限のため、遮蔽地点の Deposit スペクトルを
複数ランで積算して統計を稼ぐ。
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
RUNNER = ROOT.parents[1] / "phits-agent-kit" / "phits_web_run.py"
SOURCE = ROOT / "source_ceiling.inp"


def parse_hist_spectrum(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """return lo, y, y2_for_err, n_hist from PHITS spectrum file."""
    text = path.read_text()
    n_hist = 0.0
    m = re.search(r"resc3\s*=\s*([0-9.Ee+-]+)", text)
    if m:
        n_hist = float(m.group(1))
    lo: list[float] = []
    y: list[float] = []
    err: list[float] = []
    start = False
    for line in text.splitlines():
        if "e-lower" in line:
            start = True
            continue
        if start:
            if line.startswith("#") or not line.strip():
                if lo:
                    break
                continue
            parts = line.split()
            if len(parts) >= 4:
                try:
                    lo.append(float(parts[0]))
                    y.append(float(parts[2]))
                    err.append(float(parts[3]))
                except ValueError:
                    pass
    arr_y = np.array(y)
    arr_err = np.array(err)
    # PHITS r.err ≈ 1/sqrt(N); recover counts-like weight
    with np.errstate(divide="ignore", invalid="ignore"):
        counts = np.where((arr_y > 0) & (arr_err > 0), 1.0 / (arr_err**2), 0.0)
    return np.array(lo), arr_y, counts, n_hist


def write_merged(template: Path, out: Path, lo: np.ndarray, y: np.ndarray, err: np.ndarray) -> None:
    """Overwrite data block of template with merged y/err (keep headers)."""
    lines = template.read_text().splitlines(keepends=True)
    out_lines: list[str] = []
    start = False
    i_bin = 0
    for line in lines:
        if "e-lower" in line:
            start = True
            out_lines.append(line)
            continue
        if start and i_bin < len(lo):
            parts = line.split()
            if len(parts) >= 4:
                try:
                    float(parts[0])
                    e_lo = float(parts[0])
                    e_hi = float(parts[1])
                    out_lines.append(
                        f"   {e_lo:.4E}   {e_hi:.4E}   {y[i_bin]:.4E}  {err[i_bin]:.4f}\n"
                    )
                    i_bin += 1
                    continue
                except ValueError:
                    pass
        if start and i_bin >= len(lo) and line.strip().startswith("#"):
            start = False
            # update sum line if present
        out_lines.append(line)
    # patch sum over
    total = float(np.sum(y))
    patched: list[str] = []
    for line in out_lines:
        if "sum over" in line:
            patched.append(f"#   sum over                 {total:.4E}  0.0000\n")
        else:
            patched.append(line)
    out.write_text("".join(patched))


def run_once(workdir: Path, run_index: int) -> None:
    # Web PHITS は同一入力をキャッシュするため、毎回 rseed を変える
    main = workdir / "main.inp"
    text = main.read_text()
    seed_line = f" rseed    = {1000 + run_index * 9973 + int(time.time()) % 100000}\n"
    if re.search(r"^\s*rseed\s*=", text, flags=re.M):
        text = re.sub(r"^\s*rseed\s*=.*$", seed_line.rstrip(), text, flags=re.M)
    else:
        text = text.replace(" itall    =   1\n", " itall    =   1\n" + seed_line)
    main.write_text(text)
    cmd = [
        sys.executable,
        str(RUNNER),
        "main.inp",
        str(SOURCE),
        "--version",
        "phits336",
        "--new-session",
    ]
    for name in (".phits_web_session", ".phits_web_result.zip"):
        p = workdir / name
        if p.exists():
            p.unlink()
    subprocess.run(cmd, cwd=workdir, check=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("workdir", type=Path, help="例: small/d1/01_PF")
    ap.add_argument("-n", type=int, default=5, help="繰り返し回数")
    args = ap.parse_args()
    workdir = args.workdir if args.workdir.is_absolute() else ROOT / args.workdir
    if not (workdir / "main.inp").is_file():
        raise SystemExit(f"main.inp not found in {workdir}")

    stash = workdir / "_accumulate"
    stash.mkdir(exist_ok=True)

    ys: list[np.ndarray] = []
    cs: list[np.ndarray] = []
    lo_ref: np.ndarray | None = None
    for i in range(args.n):
        print(f"=== run {i+1}/{args.n} ===", flush=True)
        run_once(workdir, i)
        de = workdir / "de.out"
        lo, y, counts, n_hist = parse_hist_spectrum(de)
        print(f"  n_hist={n_hist:.0f} deposit_sum={y.sum():.4e} nz={(y>0).sum()}", flush=True)
        shutil.copy2(de, stash / f"de_{i+1:02d}.out")
        if lo_ref is None:
            lo_ref = lo
        ys.append(y)
        cs.append(counts)

    y_stack = np.vstack(ys)
    c_stack = np.vstack(cs)
    c_sum = c_stack.sum(axis=0)
    # weighted mean by recovered counts; fall back to arithmetic mean
    with np.errstate(divide="ignore", invalid="ignore"):
        y_mean = np.where(
            c_sum > 0,
            (y_stack * c_stack).sum(axis=0) / c_sum,
            y_stack.mean(axis=0),
        )
        err = np.where(c_sum > 0, 1.0 / np.sqrt(c_sum), 0.0)

    template = stash / "de_01.out"
    write_merged(template, workdir / "de.out", lo_ref, y_mean, err)
    print(f"merged deposit_sum={y_mean.sum():.4e} nz={(y_mean>0).sum()} -> {workdir/'de.out'}")


if __name__ == "__main__":
    main()
