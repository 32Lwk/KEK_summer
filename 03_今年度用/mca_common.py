#!/usr/bin/env python3
"""MCA の検出・解析の共通処理。"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np

USB_ROOT = Path("/Volumes")

# 終夜参照で決めた共通 ROI（地点比較の積分窓）。背景はピーク外側帯（roi_net_sideband）。
ROI_BY_SERIAL: dict[str, dict[str, int]] = {
    "1715": {"lo": 314, "hi": 366, "search_lo": 80},   # D1 / D2
    "2162": {"lo": 350, "hi": 408, "search_lo": 300},  # d1 / d2（高 ch 山 ch≈389）
}
# 終夜 D1 の σ≈8 ch → ピーク除外 ≈±2σ。側帯は除外帯の外側。
PEAK_HALF_WIDTH = 16
SIDEBAND_WIDTH = 15
SIDEBAND_GAP = 0
ROI_EDGE = 6  # 参考用（旧・端点台形）
PEAK_OUTSIDE_WARN_CH = 15


def make_id(stem: str) -> str:
    s = (
        stem.replace("放射線棟BT", "hoshasenBT")
        .replace("放射線棟", "hoshasen")
        .replace("管理棟2階", "kanri2f")
        .replace("管理棟2F", "kanri2f")
        .replace("管理棟1階", "kanri1f")
        .replace("管理棟1F", "kanri1f")
        .replace("管理棟", "kanri")
        .replace("ライナック", "linac")
        .replace("地上", "ground")
    )
    s = re.sub(r"[^A-Za-z0-9_]+", "_", s).strip("_")
    if not s:
        s = "run_" + hashlib.md5(stem.encode()).hexdigest()[:8]
    return s


def make_label(stem: str) -> str:
    """表示名はファイル名（拡張子なし）。日時が残るので同地点の再測定も区別できる。"""
    return stem


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


def infer_serial(filename: str, meta_serial: str = "") -> str:
    """MCA ヘッダの Serial Number。無い場合はファイル名から 1715 / 2162 を推定。"""
    if meta_serial:
        return str(meta_serial)
    stem = Path(filename).stem
    # 大文字 D1/D2 → SN 1715（KEKB_D1 等）。小文字 d1/d2 → SN 2162。
    if re.search(r"(^|_)D1($|_)", stem):
        return "1715"
    if re.search(r"(^|_)D2($|_)", stem):
        return "1715"
    if re.search(r"(^|_)d1($|_)", stem):
        return "2162"
    if re.search(r"(^|_)d2($|_)", stem):
        return "2162"
    return ""


def search_lo_for_serial(serial: str) -> int:
    return ROI_BY_SERIAL.get(str(serial or ""), {}).get("search_lo", 80)


def fixed_roi_for_serial(serial: str) -> tuple[int, int] | None:
    preset = ROI_BY_SERIAL.get(str(serial or ""))
    if not preset:
        return None
    return int(preset["lo"]), int(preset["hi"])


def find_peak(counts, search_lo: int = 80) -> int:
    """平滑化スペクトルの argmax でピーク ch を返す（発見・監視用）。"""
    c = np.asarray(counts, dtype=float)
    n = len(c)
    search_lo = min(max(search_lo, 1), n - 20)
    sm = np.convolve(c, np.ones(5) / 5.0, mode="same")
    hi_lim = n - 5
    return int(search_lo + np.argmax(sm[search_lo:hi_lim]))


def find_roi(counts, search_lo: int = 80, pad: int = 8) -> tuple[int, int, int]:
    """低ch連続成分を除き、高ch側のピークを半値〜背景で切って ROI を返す（参考用）。"""
    c = np.asarray(counts, dtype=float)
    n = len(c)
    search_lo = min(max(search_lo, 1), n - 20)
    sm = np.convolve(c, np.ones(5) / 5.0, mode="same")
    hi_lim = n - 5
    peak = find_peak(c, search_lo)
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


@dataclass
class RoiAnalysis:
    roi_lo: int
    roi_hi: int
    roi_peak: int
    roi_auto_lo: int
    roi_auto_hi: int
    gross: float
    bg: float
    net: float
    err: float
    net_valid: bool
    warning: str
    search_lo: int
    serial: str
    sb_lo_lo: int = 0
    sb_lo_hi: int = 0
    sb_hi_lo: int = 0
    sb_hi_hi: int = 0
    bg_mode: str = "sideband"


def centered_roi(peak: int, width: int, n: int) -> tuple[int, int]:
    lo = max(1, peak - (width - 1) // 2)
    hi = lo + width - 1
    if hi > n - 1:
        hi = n - 1
        lo = max(1, hi - width + 1)
    return int(lo), int(hi)


def high_ch_peak(counts, serial: str) -> int:
    """ピーク ch。1715 は低 ch 斜面の argmax を避け高 ch 側も確認する。"""
    search_lo = search_lo_for_serial(serial)
    peak = find_peak(counts, search_lo)
    if serial != "1715":
        return peak
    peak_hi = find_peak(counts, 300)
    c = np.asarray(counts, dtype=float)
    if peak_hi >= 300 and (peak < 200 or c[peak_hi] >= 0.5 * c[peak]):
        return peak_hi
    return peak


def sideband_ranges(
    integrate_lo: int,
    integrate_hi: int,
    peak: int,
    n: int,
    peak_half: int = PEAK_HALF_WIDTH,
    width: int = SIDEBAND_WIDTH,
    gap: int = SIDEBAND_GAP,
) -> tuple[tuple[int, int], tuple[int, int]]:
    """積分窓の外側に左右側帯を置く（ピーク除外帯とも重ならないよう調整）。

    主目的はピーク裾を背景に混ぜないこと。共通 ROI の外に置き、
    さらに peak±peak_half に食い込む場合は外側へ押し出す。
    """
    excl_lo = peak - peak_half
    excl_hi = peak + peak_half

    left_hi = min(integrate_lo - gap - 1, excl_lo - gap - 1)
    left_lo = left_hi - width + 1
    right_lo = max(integrate_hi + gap + 1, excl_hi + gap + 1)
    right_hi = right_lo + width - 1

    left_lo = max(1, left_lo)
    left_hi = max(left_lo, min(left_hi, n - 1))
    right_lo = max(1, min(right_lo, n - 1))
    right_hi = max(right_lo, min(right_hi, n - 1))

    if left_hi >= integrate_lo or left_hi >= excl_lo:
        left_hi = max(1, min(integrate_lo, excl_lo) - gap - 1)
        left_lo = max(1, left_hi - width + 1)
    if right_lo <= integrate_hi or right_lo <= excl_hi:
        right_lo = min(n - 1, max(integrate_hi, excl_hi) + gap + 1)
        right_hi = min(n - 1, right_lo + width - 1)
    return (int(left_lo), int(left_hi)), (int(right_lo), int(right_hi))


def roi_net_sideband(
    counts,
    integrate_lo: int,
    integrate_hi: int,
    peak: int,
    peak_half: int = PEAK_HALF_WIDTH,
    sideband: int = SIDEBAND_WIDTH,
    gap: int = SIDEBAND_GAP,
) -> tuple[float, float, float, float, tuple[int, int], tuple[int, int], str]:
    """ピーク／ROI 外側帯で直線背景を決め、積分窓内の NET を返す。

    Returns
    -------
    gross, bg_sum, net, err, (sb_lo_lo, sb_lo_hi), (sb_hi_lo, sb_hi_hi), mode
    mode は \"sideband\"（両側）または \"sideband_left\"（右側帯が使えないとき）。
    """
    c = np.asarray(counts, dtype=float)
    n = len(c)
    lo = max(1, min(integrate_lo, n - 1))
    hi = max(lo, min(integrate_hi, n - 1))
    (sb0_lo, sb0_hi), (sb1_lo, sb1_hi) = sideband_ranges(
        lo, hi, peak, n, peak_half=peak_half, width=sideband, gap=gap
    )

    left = c[sb0_lo : sb0_hi + 1]
    right = c[sb1_lo : sb1_hi + 1]
    left_ok = len(left) >= 3
    right_ok = len(right) >= 3
    # 右側帯がピーク近傍や積分窓内に残っていたら使わない
    if right_ok and (sb1_lo <= hi or sb1_lo <= peak + peak_half):
        right_ok = False
    if right_ok and float(np.sum(right)) < 1.0 and left_ok and float(np.sum(left)) > 10.0:
        right_ok = False
    if left_ok and (sb0_hi >= lo or sb0_hi >= peak - peak_half):
        # 左側帯が窓／ピークに食い込むなら、さらに外側へ縮退できなければ左も無効→端点にフォールバックしないよう
        # 可能な範囲で再クリップ済み。食い込みが残るなら平均は取るが警告は analyze 側。
        pass

    bg0 = float(np.mean(left)) if left_ok else 0.0
    if right_ok:
        bg1 = float(np.mean(right))
        mode = "sideband"
        x0 = 0.5 * (sb0_lo + sb0_hi)
        x1 = 0.5 * (sb1_lo + sb1_hi)
    else:
        bg1 = bg0
        mode = "sideband_left"
        x0 = 0.5 * (sb0_lo + sb0_hi) if left_ok else float(lo)
        x1 = x0 + 1.0
        sb1_lo, sb1_hi = sb0_lo, sb0_hi

    x = np.arange(lo, hi + 1, dtype=float)
    y = c[lo : hi + 1]
    if abs(x1 - x0) < 1e-9:
        bg = np.full_like(x, bg0, dtype=float)
    else:
        bg = bg0 + (bg1 - bg0) / (x1 - x0) * (x - x0)
    tot = float(y.sum())
    bg_sum = float(np.clip(bg, 0, None).sum())
    net = tot - bg_sum
    err = float(np.sqrt(max(tot + bg_sum, 0.0)))
    return tot, bg_sum, net, err, (sb0_lo, sb0_hi), (sb1_lo, sb1_hi), mode


def analyze_roi(counts, serial: str = "") -> RoiAnalysis:
    """地点比較の主 ROI：シリアル別固定窓 + ピーク外側帯 NET。

    共通窓内にピークが収まる場合は lo/hi を固定。外れた場合のみ同じ幅で中心移動。
    背景は ROI 端ではなく、peak±PEAK_HALF_WIDTH の外側側帯で決める。
    """
    serial = str(serial or "")
    search_lo = search_lo_for_serial(serial)
    c = np.asarray(counts, dtype=float)
    n = len(c)
    peak = high_ch_peak(c, serial)
    auto_lo, auto_hi, _ = find_roi(c, search_lo=search_lo)
    fixed = fixed_roi_for_serial(serial)
    recentered = False
    width = 0
    if fixed:
        lo, hi = fixed
        width = hi - lo + 1
        if peak < lo - PEAK_OUTSIDE_WARN_CH or peak > hi + PEAK_OUTSIDE_WARN_CH:
            lo, hi = centered_roi(peak, width, n)
            recentered = True
    else:
        lo, hi = auto_lo, auto_hi

    gross, bg, net, err, (sb0_lo, sb0_hi), (sb1_lo, sb1_hi), bg_mode = roi_net_sideband(
        c, lo, hi, peak
    )
    warnings: list[str] = []
    if net <= 0:
        warnings.append("NET<=0（ROI または背景定義を確認）")
    if recentered:
        warnings.append(f"peak={peak} のため共通窓幅{width}chを {lo}-{hi} に中心移動")
    elif fixed and (peak < lo - PEAK_OUTSIDE_WARN_CH or peak > hi + PEAK_OUTSIDE_WARN_CH):
        warnings.append(f"peak={peak} が共通 ROI {lo}-{hi} から離れている")
    if bg_mode == "sideband_left":
        warnings.append("右側帯を使わず左側帯水平背景")
    if abs(peak - lo) < PEAK_HALF_WIDTH or abs(peak - hi) < PEAK_HALF_WIDTH:
        warnings.append(f"peak={peak} が積分窓端に近い（側帯定義を確認）")
    if serial == "2162" and auto_hi <= 150:
        warnings.append(
            f"参考: search_lo=80 だと低 ch 斜面 ROI {auto_lo}-{auto_hi} になるため使用しない"
        )

    warning = "; ".join(warnings)
    return RoiAnalysis(
        roi_lo=lo,
        roi_hi=hi,
        roi_peak=peak,
        roi_auto_lo=auto_lo,
        roi_auto_hi=auto_hi,
        gross=gross,
        bg=bg,
        net=net,
        err=err,
        net_valid=net > 0,
        warning=warning,
        search_lo=search_lo,
        serial=serial,
        sb_lo_lo=sb0_lo,
        sb_lo_hi=sb0_hi,
        sb_hi_lo=sb1_lo,
        sb_hi_hi=sb1_hi,
        bg_mode=bg_mode,
    )


def roi_net(counts, lo: int, hi: int, edge: int = 6) -> tuple[float, float, float, float]:
    """【参考】ROI 端 edge ch の台形背景。主値は roi_net_sideband / analyze_roi。"""
    c = np.asarray(counts, dtype=float)
    x = np.arange(lo, hi + 1, dtype=float)
    y = c[lo : hi + 1]
    if len(y) < 4:
        tot = float(y.sum())
        return tot, 0.0, tot, float(np.sqrt(max(tot, 0.0)))
    k = min(edge, max(2, len(y) // 5))
    bg0 = float(np.mean(y[:k]))
    bg1 = float(np.mean(y[-k:]))
    bg = bg0 + (bg1 - bg0) / (x[-1] - x[0]) * (x - x[0])
    tot = float(y.sum())
    bg_sum = float(np.clip(bg, 0, None).sum())
    net = tot - bg_sum
    err = float(np.sqrt(tot + bg_sum))
    return tot, bg_sum, net, err


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
