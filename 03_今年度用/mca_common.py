#!/usr/bin/env python3
"""MCA の検出・解析の共通処理。"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import numpy as np

USB_ROOT = Path("/Volumes")


def make_id(stem: str) -> str:
    s = (
        stem.replace("管理棟2階", "kanri2f")
        .replace("管理棟2F", "kanri2f")
        .replace("管理棟1階", "kanri1f")
        .replace("管理棟1F", "kanri1f")
        .replace("管理棟", "kanri")
    )
    s = re.sub(r"[^A-Za-z0-9_]+", "_", s).strip("_")
    if not s:
        s = "run_" + hashlib.md5(stem.encode()).hexdigest()[:8]
    return s


def make_label(stem: str) -> str:
    return re.sub(r"^\d{8}_\d{4}_", "", stem)


def parse_mca(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta: dict = {"path": path}
    for key in ("LIVE_TIME", "REAL_TIME", "START_TIME", "GAIN", "THRESHOLD"):
        m = re.search(rf"^{key} - (.+)$", text, re.M)
        if m:
            meta[key] = m.group(1).strip()
    data = re.search(r"<<DATA>>\n([\s\S]*?)\n<<END>>", text)
    if not data:
        raise ValueError(f"DATA が見つかりません: {path}")
    counts = [int(x) for x in data.group(1).splitlines() if x.strip()]
    meta["counts"] = counts
    meta["n_channels"] = len(counts)
    file_roi = re.search(r"<<ROI>>\n(\d+) (\d+)", text)
    meta["file_roi"] = (int(file_roi.group(1)), int(file_roi.group(2))) if file_roi else None
    sc = re.search(r"Slow Count: (\d+)", text)
    meta["slow_count"] = int(sc.group(1)) if sc else sum(counts)
    sn = re.search(r"Serial Number: (\d+)", text)
    meta["serial"] = sn.group(1) if sn else ""
    dt = re.search(r"Device Type: (.+)", text)
    meta["device"] = dt.group(1).strip() if dt else "MCA8000D"
    bt = re.search(r"Board Temp: (\d+)", text)
    meta["board_temp_C"] = int(bt.group(1)) if bt else None
    mcac = re.search(r"MCAC=(\d+);", text)
    meta["mcac"] = int(mcac.group(1)) if mcac else len(counts)
    gaia = re.search(r"GAIA=(\d+);", text)
    meta["gaia"] = int(gaia.group(1)) if gaia else None
    return meta


def find_roi(counts, search_lo: int = 80, pad: int = 8) -> tuple[int, int, int]:
    """低ch連続成分を除き、高ch側のピークを半値〜背景で切って ROI を返す。"""
    c = np.asarray(counts, dtype=float)
    n = len(c)
    search_lo = min(max(search_lo, 1), n - 20)
    sm = np.convolve(c, np.ones(5) / 5.0, mode="same")
    hi_lim = n - 5
    peak = search_lo + int(np.argmax(sm[search_lo:hi_lim]))
    h = float(sm[peak])
    bg_mask = np.zeros(n, dtype=bool)
    bg_mask[search_lo:hi_lim] = True
    bg_mask[max(search_lo, peak - 40) : min(hi_lim, peak + 41)] = False
    bg = float(np.median(sm[bg_mask])) if np.any(bg_mask) else 0.0
    thresh = bg + 0.15 * max(h - bg, 0.0)
    lo, hi = peak, peak
    while lo > search_lo and sm[lo] > thresh:
        lo -= 1
    while hi < hi_lim - 1 and sm[hi] > thresh:
        hi += 1
    lo = max(search_lo, lo - pad)
    hi = min(n - 1, hi + pad)
    if hi - lo < 10:
        lo, hi = max(search_lo, peak - 25), min(n - 1, peak + 25)
    return int(lo), int(hi), int(peak)


def peak_clip(counts, lo: int, hi: int, pad: float = 10.0) -> float:
    c = np.asarray(counts, dtype=float)
    return float(np.max(c[lo : hi + 1]) + pad) if hi >= lo else pad


def discover_usb_mca() -> list[Path]:
    found: list[Path] = []
    if not USB_ROOT.exists():
        return found
    for vol in USB_ROOT.iterdir():
        if vol.name in ("Macintosh HD",) or not vol.is_dir():
            continue
        try:
            found.extend(sorted(vol.glob("*.mca")))
        except OSError:
            continue
    return found


def discover_raw_mca(raw: Path) -> list[Path]:
    if not raw.exists():
        return []
    return sorted(raw.glob("*.mca"))
