#!/usr/bin/env python3
"""MCA の検出・解析の共通処理。"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np

USB_ROOT = Path("/Volumes")


def is_pf_d2_mca(name: str) -> bool:
    """小径 d2 の PF 測定か。解析・図・フラックスから除外する（生ファイルは raw/ に残す）。

    大径 D2@PF は対象外。8/20（ゲイン異常）と 8/22 の両方を含める。
    """
    stem = Path(name).stem
    if re.search(r"(^|_)D2($|_)", stem) or stem.startswith("D2"):
        return False
    is_d2 = (
        stem.startswith("d2")
        or "smalld2" in stem.lower()
        or bool(re.search(r"(^|_)d2($|_)", stem))
    )
    is_pf = bool(re.search(r"(^|_)PF($|_)", stem) or stem.endswith("_PF") or "_PF" in stem)
    return is_d2 and is_pf


# --- 解析窓（2026–）---
# 主窓: 191–764 keV … ピーク麓より右の全 ch を水平背景 → NET（ROI あり）
# 副窓: 固定 ch peak ROI … キャンペーン内地点比較・昨年表との突合用（analyze_roi）
# 公式 φ・ε×S は主窓へ移行。peak ROI はゲイン変動で物理窓とずれるため参照用。

# 終夜参照で決めた共通 ROI（地点比較の積分窓）。背景はピーク外側帯（roi_net_sideband）。
ROI_BY_SERIAL: dict[str, dict[str, int]] = {
    "1715": {"lo": 314, "hi": 366, "search_lo": 80},   # D1 / D2
    "2162": {"lo": 350, "hi": 408, "search_lo": 300},  # d1 / d2（高 ch 山 ch≈389）
}
# 終夜 D1 の σ≈8 ch → ピーク除外 ≈±2σ。側帯は除外帯の外側。
PEAK_HALF_WIDTH = 16
SIDEBAND_WIDTH = 15  # peak ROI の左右側帯幅。壁窓右側背景は麓より右の全 ch
SIDEBAND_GAP = 0
WALL_PLATEAU_MIN_WIDTH = 20  # 平坦部背景推定に必要な最小幅 [ch]
WALL_NET_GROSS_MIN = 0.25  # 右側帯 NET/gross がこれ未満なら平坦部背景を検討
WALL_LEFT_SB_MIN_CH = 10  # 壁窓左側帯の下限（ch0 付近を避ける）
ROI_EDGE = 6  # 参考用（旧・端点台形）
PEAK_OUTSIDE_WARN_CH = 15

# ³He(n,p)³H: Q=764 keV。壁効果で連続成分はトリトン端〜フルエネルギーに分布。
HE3_Q_KEV = 764.0
HE3_PROTON_EDGE_KEV = 573.0
HE3_TRITON_EDGE_KEV = 191.0
HE3_WALL_LO_KEV = HE3_TRITON_EDGE_KEV  # 積分窓下端 = トリトン端
HE3_MARK_KEV = (HE3_Q_KEV, HE3_PROTON_EDGE_KEV, HE3_TRITON_EDGE_KEV)

# シリアル別の 764 keV 基準（large D=1715 と small d=2162 はゲイン応答が違う）。
# 1715 はキャンペーン内で実効ゲインが二群ある（≈342 と ≈387）。
# peak_ref: その群の代表 ch（764 keV）。lo/hi: 群判定帯（roi_peak がこの中なら当該群）。
HE3_CAL_BY_SERIAL: dict[str, list[dict]] = {
    "1715": [
        {
            "id": "D_low_gain",
            "peak_ref": 245,
            "lo": 220,
            "hi": 280,
            "note": "D1 PF 8/20 アンプ取り違え（ch≈242）→ rebin 補正後は D_std_hi 相当",
        },
        {
            "id": "D_std_lo",
            "peak_ref": 342,
            "lo": 325,
            "hi": 360,
            "note": "D1 初期・管理棟系（ch≈340）",
        },
        {
            "id": "D_std_hi",
            "peak_ref": 387,
            "lo": 365,
            "hi": 430,
            "note": "D1 後半 / D2（ch≈387）",
        },
    ],
    "2162": [
        {
            "id": "d_std",
            "peak_ref": 389,
            "lo": 360,
            "hi": 420,
            "note": "d1/d2 標準（ch≈389）",
        },
    ],
}


@dataclass(frozen=True)
class He3EnergyCal:
    """³He エネルギー目印用の較正結果。"""

    peak_ch: int  # 764 keV に対応させるチャンネル
    serial: str
    mode: str  # HE3_CAL id / run_gain / fallback
    source: str  # peak_run | peak_ref
    note: str

    @property
    def kev_per_ch(self) -> float:
        return HE3_Q_KEV / float(self.peak_ch) if self.peak_ch > 0 else float("nan")

    def channel_of(self, energy_kev: float) -> float:
        return float(self.peak_ch) * (float(energy_kev) / HE3_Q_KEV)


def _place_is_gain_trial(place: str) -> bool:
    p = (place or "").lower()
    return ("gain" in p) or ("corse" in p) or ("coarse" in p)


def resolve_he3_energy_cal(
    serial: str,
    roi_peak: int,
    place: str = "",
) -> He3EnergyCal | None:
    """シリアル×ゲイン群で 764 keV チャンネルを決める。

    - 群帯内: そのスペクトルの roi_peak を 764 keV とする（群ラベルは SN 別）
    - ファイル名が gain 試験: 当該 roi_peak（設定変更セッション）
    - 帯外（誤ピーク疑い）: その SN の代表 peak_ref にフォールバック
    """
    ser = str(serial or "").strip()
    peak = int(roi_peak or 0)
    profiles = HE3_CAL_BY_SERIAL.get(ser)
    if not profiles:
        if peak <= 0:
            return None
        return He3EnergyCal(peak, ser or "?", "unknown", "peak_run", "シリアル未登録")

    if _place_is_gain_trial(place) and peak > 0:
        return He3EnergyCal(
            peak,
            ser,
            "run_gain",
            "peak_run",
            "ゲイン試験: 当該ピークを 764 keV",
        )

    for prof in profiles:
        if peak > 0 and int(prof["lo"]) <= peak <= int(prof["hi"]):
            return He3EnergyCal(
                peak,
                ser,
                str(prof["id"]),
                "peak_run",
                str(prof["note"]),
            )

    # 帯外 → 代表値（roi_peak が壁効果・誤検出のとき）
    # 近い群の peak_ref を選ぶ。peak が無い/0 なら先頭群。
    if peak > 0:
        prof = min(profiles, key=lambda p: abs(int(p["peak_ref"]) - peak))
    else:
        prof = profiles[0]
    return He3EnergyCal(
        int(prof["peak_ref"]),
        ser,
        f"fallback_{prof['id']}",
        "peak_ref",
        f"ピーク帯外(roi_peak={peak})→{prof['note']}",
    )

# 図・CSV 接尾辞（macOS 既定 FS はケース非区別 → _d2 と _D2 は同一ファイル）
DETECTOR_FS_TAG: dict[str, str] = {
    "D1": "",
    "d1": "small_d1",
    "d2": "small_d2",
    "D2": "large_D2",
}


def detector_fs_suffix(detector: str) -> str:
    """検出器キーからファイル名接尾辞を返す（D1 は空 = 従来の無接尾辞）。"""
    tag = DETECTOR_FS_TAG.get(detector, detector)
    return f"_{tag}" if tag else ""


def equiv_decay_csv_name(detector: str) -> str:
    suf = detector_fs_suffix(detector)
    return f"等価コンクリート_減衰{suf}.csv" if suf else "等価コンクリート_減衰.csv"


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


def live_count_rate(net: float, live_s: float) -> float:
    """計数率 [cps]。MCA の LIVE_TIME は dead time 除外済みなので、これ以上補正しない。"""
    live = float(live_s)
    if live <= 0:
        return float("nan")
    return float(net) / live


def parse_mca(path: Path, *, apply_gain_correction: bool = True) -> dict:
    """MCA を読む。解析用は既定で GAIN_AMP_CORRECTIONS の rebin を適用する。"""
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
    if apply_gain_correction:
        corrected, info = apply_gain_amp_correction(
            Path(path).name, meta["counts"], Path(path).parent
        )
        if info:
            meta["counts_raw"] = meta["counts"]
            meta["counts"] = corrected
            meta["gain_correction"] = info
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
    # エネルギー窓メタ（ピーク ROI では空。壁効果窓では 191–764 keV）
    window_kind: str = "peak_roi"
    e_lo_kev: float = 0.0
    e_hi_kev: float = 0.0
    kev_per_ch: float = 0.0


def kev_to_channel(e_kev: float, peak_ch_764: int) -> float:
    """roi_peak を 764 keV フルエネルギーピークとする線形校正。"""
    if peak_ch_764 <= 0:
        return float("nan")
    return float(peak_ch_764) * (e_kev / HE3_Q_KEV)


def channel_to_kev(ch: float, peak_ch_764: int) -> float:
    if peak_ch_764 <= 0:
        return float("nan")
    return float(ch) * HE3_Q_KEV / float(peak_ch_764)


def energy_window_channels(
    peak_ch_764: int,
    n: int,
    e_lo_kev: float = HE3_WALL_LO_KEV,
    e_hi_kev: float = HE3_Q_KEV,
) -> tuple[int, int]:
    """エネルギー窓 [e_lo, e_hi] keV をチャンネル整数範囲へ。"""
    lo = int(np.floor(kev_to_channel(e_lo_kev, peak_ch_764)))
    hi = int(np.ceil(kev_to_channel(e_hi_kev, peak_ch_764)))
    lo = max(1, min(lo, n - 1))
    hi = max(lo, min(hi, n - 1))
    return lo, hi


def he3_wall_channels(
    serial: str,
    roi_peak: int,
    place: str = "",
    n: int = 512,
) -> tuple[int, int] | None:
    """壁効果連続帯 191–764 keV の ch 範囲（プロット・クリップ用）。"""
    cal = resolve_he3_energy_cal(str(serial or ""), int(roi_peak or 0), str(place or ""))
    if cal is None or cal.peak_ch <= 0:
        return None
    peak = cal.peak_ch
    lo_e, hi_e = energy_window_channels(peak, n)
    lo = lo_e
    hi = max(hi_e, min(n - 1, peak + PEAK_HALF_WIDTH))
    fixed = fixed_roi_for_serial(serial)
    if fixed is not None:
        hi = max(hi, fixed[1])
    return lo, hi


def centered_roi(peak: int, width: int, n: int) -> tuple[int, int]:
    lo = max(1, peak - (width - 1) // 2)
    hi = lo + width - 1
    if hi > n - 1:
        hi = n - 1
        lo = max(1, hi - width + 1)
    return int(lo), int(hi)


def refine_peak_local(counts, peak: int, *, half: int = 20, min_ch: int = 1) -> int:
    """平滑 argmax 付近で生スペクトルの局所 argmax に refine する（広い山用）。"""
    c = np.asarray(counts, dtype=float)
    n = len(c)
    if peak <= 0 or n < 3:
        return peak
    lo = max(min_ch, peak - half)
    hi = min(n - 1, peak + half)
    if hi <= lo:
        return peak
    return int(lo + np.argmax(c[lo : hi + 1]))


def high_ch_peak(counts, serial: str) -> int:
    """ピーク ch。1715 / 2162 は低 ch 斜面の argmax を避け高 ch 側も確認する。"""
    search_lo = search_lo_for_serial(serial)
    peak = find_peak(counts, search_lo)
    c = np.asarray(counts, dtype=float)
    if serial in ("1715", "2162"):
        peak_hi = find_peak(counts, 300)
        if peak_hi >= 300 and (peak < 200 or c[peak_hi] >= 0.5 * c[peak]):
            peak = peak_hi
    if serial in ("1715", "2162") and peak >= 300:
        peak = refine_peak_local(c, peak, half=20, min_ch=300)
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
    kev_per = HE3_Q_KEV / peak if peak > 0 else 0.0
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
        window_kind="peak_roi",
        e_lo_kev=channel_to_kev(lo, peak) if peak > 0 else 0.0,
        e_hi_kev=channel_to_kev(hi, peak) if peak > 0 else 0.0,
        kev_per_ch=kev_per,
    )


def _wall_right_sideband_lo(
    counts,
    integrate_lo: int,
    integrate_hi: int,
    peak: int,
    n: int,
    *,
    peak_half: int = PEAK_HALF_WIDTH,
    width: int = SIDEBAND_WIDTH,
    gap: int = SIDEBAND_GAP,
) -> tuple[int, int, int]:
    """壁窓の右側帯。ピーク麓（peak+peak_half）より右の全チャンネル。

    width は peak ROI 側帯との呼び出し互換のため残し、壁窓では使わない。
    戻り値の第3要素（旧シフト量）は常に 0。
    """
    del counts, width
    lo = max(1, min(integrate_lo, n - 1))
    hi = max(lo, min(integrate_hi, n - 1))
    excl_hi = peak + peak_half
    sb_lo = min(n - 1, max(hi, excl_hi) + gap + 1)
    sb_hi = n - 1
    return int(sb_lo), int(sb_hi), 0


def _wall_plateau_bg_per_ch(
    counts,
    lo: int,
    hi: int,
    peak: int,
    *,
    peak_half: int = PEAK_HALF_WIDTH,
    min_width: int = WALL_PLATEAU_MIN_WIDTH,
) -> float | None:
    """壁窓内ピーク下側の平坦連続部（中央値）を背景 cps/ch 相当で返す。"""
    c = np.asarray(counts, dtype=float)
    excl_lo = peak - peak_half
    plat_hi = max(lo, excl_lo - 5)
    plat_lo = lo + 10
    if plat_hi - plat_lo + 1 < min_width:
        plat_lo = lo
        plat_hi = max(lo, min(hi, peak - peak_half - 1))
    if plat_hi <= plat_lo + 2:
        return None
    return float(np.median(c[plat_lo : plat_hi + 1]))


def _peak_near_wall_hi(peak: int, hi: int, *, peak_half: int = PEAK_HALF_WIDTH) -> bool:
    return peak + peak_half >= hi - 3


def wall_sideband_ranges(
    integrate_lo: int,
    integrate_hi: int,
    peak: int,
    n: int,
    peak_half: int = PEAK_HALF_WIDTH,
    width: int = SIDEBAND_WIDTH,
    gap: int = SIDEBAND_GAP,
    counts=None,
) -> tuple[tuple[int, int], tuple[int, int]]:
    """壁効果窓用側帯: 左は 191 keV 窓下端より低 ch、右はピーク麓より右の全 ch。"""
    lo = max(1, min(integrate_lo, n - 1))
    hi = max(lo, min(integrate_hi, n - 1))
    excl_hi = peak + peak_half

    left_hi = lo - gap - 1
    left_lo = left_hi - width + 1
    left_lo = max(WALL_LEFT_SB_MIN_CH, left_lo)
    left_hi = max(left_lo, min(left_hi, n - 1))

    if counts is not None:
        right_lo, right_hi, _ = _wall_right_sideband_lo(
            counts, lo, hi, peak, n, peak_half=peak_half, width=width, gap=gap
        )
    else:
        right_lo = min(n - 1, max(hi, excl_hi) + gap + 1)
        right_hi = n - 1

    if left_hi < left_lo + 2:
        left_lo, left_hi = 0, 0
    if right_hi < right_lo + 2:
        right_lo, right_hi = 0, 0
    return (int(left_lo), int(left_hi)), (int(right_lo), int(right_hi))


def wall_net_sideband(
    counts,
    integrate_lo: int,
    integrate_hi: int,
    peak: int,
    peak_half: int = PEAK_HALF_WIDTH,
    sideband: int = SIDEBAND_WIDTH,
    gap: int = SIDEBAND_GAP,
) -> tuple[float, float, float, float, tuple[int, int], tuple[int, int], str]:
    """191 keV 未満（左）＋ピーク右（右）の直線背景で壁窓 NET を返す。"""
    c = np.asarray(counts, dtype=float)
    n = len(c)
    lo = max(1, min(integrate_lo, n - 1))
    hi = max(lo, min(integrate_hi, n - 1))
    (sb0_lo, sb0_hi), (sb1_lo, sb1_hi) = wall_sideband_ranges(
        lo, hi, peak, n, peak_half=peak_half, width=sideband, gap=gap, counts=c
    )

    left = c[sb0_lo : sb0_hi + 1] if sb0_hi >= sb0_lo > 0 else np.array([])
    right = c[sb1_lo : sb1_hi + 1] if sb1_hi >= sb1_lo > 0 else np.array([])
    left_ok = len(left) >= 3
    right_ok = len(right) >= 3

    y = c[lo : hi + 1]
    gross = float(y.sum())
    x = np.arange(lo, hi + 1, dtype=float)

    if left_ok and right_ok:
        bg0 = float(np.mean(left))
        bg1 = float(np.mean(right))
        x0 = 0.5 * (sb0_lo + sb0_hi)
        x1 = 0.5 * (sb1_lo + sb1_hi)
        if abs(x1 - x0) < 1e-9:
            bg = np.full_like(x, bg0, dtype=float)
        else:
            bg = bg0 + (bg1 - bg0) / (x1 - x0) * (x - x0)
        mode = "sideband"
    elif right_ok:
        bg1 = float(np.mean(right))
        bg = np.full_like(x, bg1, dtype=float)
        mode = "sideband_right"
    elif left_ok:
        bg0 = float(np.mean(left))
        bg = np.full_like(x, bg0, dtype=float)
        mode = "sideband_left"
    else:
        bg = np.zeros_like(x, dtype=float)
        mode = "none_gross"

    bg_sum = float(np.clip(bg, 0, None).sum())
    net = gross - bg_sum
    err = float(np.sqrt(max(gross + bg_sum, 0.0)))
    return gross, bg_sum, net, err, (sb0_lo, sb0_hi), (sb1_lo, sb1_hi), mode


def _wall_window_bounds(
    counts,
    serial: str,
    e_lo_kev: float,
    e_hi_kev: float,
) -> tuple[int, int, int, int, int, int]:
    """壁窓 ch 範囲とピーク・search_lo を返す。"""
    serial = str(serial or "")
    search_lo = search_lo_for_serial(serial)
    c = np.asarray(counts, dtype=float)
    n = len(c)
    peak = high_ch_peak(c, serial)
    auto_lo, auto_hi, _ = find_roi(c, search_lo=search_lo)
    lo_e, hi_e = energy_window_channels(peak, n, e_lo_kev=e_lo_kev, e_hi_kev=e_hi_kev)
    lo = lo_e
    hi = max(hi_e, min(n - 1, peak + PEAK_HALF_WIDTH))
    fixed = fixed_roi_for_serial(serial)
    if fixed is not None:
        hi = max(hi, fixed[1])
    return lo, hi, peak, auto_lo, auto_hi, search_lo


def analyze_wall_window(
    counts,
    serial: str = "",
    e_lo_kev: float = HE3_WALL_LO_KEV,
    e_hi_kev: float = HE3_Q_KEV,
    sideband: int = SIDEBAND_WIDTH,
) -> RoiAnalysis:
    """壁効果連続帯 NET（191–764 keV）。背景はピーク麓より右の全 ch の水平平均（主値）。

    191 keV 未満左＋右の直線背景は analyze_wall_window_linear（比較用）。
    """
    return analyze_wall_window_right_only(counts, serial, e_lo_kev, e_hi_kev, sideband)


def analyze_wall_window_linear(
    counts,
    serial: str = "",
    e_lo_kev: float = HE3_WALL_LO_KEV,
    e_hi_kev: float = HE3_Q_KEV,
    sideband: int = SIDEBAND_WIDTH,
) -> RoiAnalysis:
    """壁窓 NET（191 keV 未満左＋ピーク右の直線背景）。比較・検証用。"""
    serial = str(serial or "")
    lo, hi, peak, auto_lo, auto_hi, search_lo = _wall_window_bounds(
        counts, serial, e_lo_kev, e_hi_kev
    )
    gross, bg, net, err, (sb0_lo, sb0_hi), (sb1_lo, sb1_hi), bg_mode = wall_net_sideband(
        counts, lo, hi, peak, sideband=sideband
    )

    warnings: list[str] = []
    if peak <= 0:
        warnings.append("ピーク未検出のためエネルギー校正不可")
    if net <= 0:
        warnings.append("NET<=0（直線背景・側帯を確認）")
    if bg_mode == "none_gross":
        warnings.append("左右側帯が取れず GROSS を NET として使用")
    elif bg_mode == "sideband_right":
        warnings.append("左側帯不可→右側水平背景")
    elif bg_mode == "sideband_left":
        warnings.append("右側帯不可→左側水平背景")

    kev_per = HE3_Q_KEV / peak if peak > 0 else 0.0
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
        warning="; ".join(warnings),
        search_lo=search_lo,
        serial=serial,
        sb_lo_lo=sb0_lo,
        sb_lo_hi=sb0_hi,
        sb_hi_lo=sb1_lo,
        sb_hi_hi=sb1_hi,
        bg_mode=bg_mode,
        window_kind="wall_191_764",
        e_lo_kev=float(e_lo_kev),
        e_hi_kev=float(e_hi_kev),
        kev_per_ch=kev_per,
    )


def analyze_wall_window_right_only(
    counts,
    serial: str = "",
    e_lo_kev: float = HE3_WALL_LO_KEV,
    e_hi_kev: float = HE3_Q_KEV,
    sideband: int = SIDEBAND_WIDTH,
) -> RoiAnalysis:
    """壁窓 NET。背景はピーク麓より右の全 ch の水平平均；ピーク上端付近は平坦部へフォールバック。"""
    serial = str(serial or "")
    lo, hi, peak, auto_lo, auto_hi, search_lo = _wall_window_bounds(
        counts, serial, e_lo_kev, e_hi_kev
    )
    c = np.asarray(counts, dtype=float)
    n = len(c)
    y = c[lo : hi + 1]
    gross = float(y.sum())
    n_win = hi - lo + 1

    sb1_lo, sb1_hi, sb_shift = _wall_right_sideband_lo(
        c, lo, hi, peak, n, width=sideband
    )
    right = c[sb1_lo : sb1_hi + 1]
    right_ok = len(right) >= 3
    if right_ok:
        bg_per_ch = float(np.mean(right))
        bg_mode = "sideband_right"
    else:
        bg_per_ch = 0.0
        bg_mode = "none_gross"
    bg = bg_per_ch * n_win
    net = gross - bg
    err = float(np.sqrt(max(gross + bg, 0.0)))

    warnings: list[str] = []
    if peak <= 0:
        warnings.append("ピーク未検出のためエネルギー校正不可")
    if sb_shift > 0:
        warnings.append(f"右側帯を+{sb_shift}ch 右へずらし（ピーク裾回避）")

    plateau_bg = _wall_plateau_bg_per_ch(c, lo, hi, peak)
    peak_near_hi = _peak_near_wall_hi(peak, hi)
    if plateau_bg is not None:
        net_plateau = gross - plateau_bg * n_win
        use_plateau = False
        if bg_mode == "none_gross" and net_plateau > 0:
            use_plateau = True
        elif peak_near_hi and net_plateau > 0 and (
            net <= 0 or net_plateau > net or (gross > 0 and net / gross < WALL_NET_GROSS_MIN)
        ):
            use_plateau = True
        if use_plateau:
            bg_per_ch = plateau_bg
            bg = bg_per_ch * n_win
            net = net_plateau
            err = float(np.sqrt(max(gross + bg, 0.0)))
            bg_mode = "plateau"
            warnings.append("平坦部背景に切替（ピーク上端・側帯不可）")

    if net <= 0:
        warnings.append("NET<=0（壁効果窓または右側帯背景を確認）")
    if bg_mode == "none_gross":
        warnings.append("右側帯が取れず GROSS を NET として使用")

    kev_per = HE3_Q_KEV / peak if peak > 0 else 0.0
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
        warning="; ".join(warnings),
        search_lo=search_lo,
        serial=serial,
        sb_lo_lo=0,
        sb_lo_hi=0,
        sb_hi_lo=sb1_lo,
        sb_hi_hi=sb1_hi,
        bg_mode=bg_mode,
        window_kind="wall_191_764",
        e_lo_kev=float(e_lo_kev),
        e_hi_kev=float(e_hi_kev),
        kev_per_ch=kev_per,
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


# アンプ D/d 取り違え等: 参照 MCA の 764 keV ピーク位置で線形 rebin 補正
GAIN_AMP_CORRECTIONS: dict[str, str] = {
    "D1_20260820_0807_PF.mca": "D2_20260822_115234_PF.mca",
}


def rebin_counts_linear(counts, scale: float) -> list[int]:
    """面積保存の線形チャンネル rebin（scale>1 で右方向へ伸長）。"""
    if scale <= 0 or abs(scale - 1.0) < 1e-6:
        return list(counts)
    src = np.asarray(counts, dtype=float)
    n = len(src)
    dst = np.zeros(n, dtype=float)
    for i, v in enumerate(src):
        if v == 0:
            continue
        j = i * scale
        j0 = int(np.floor(j))
        j1 = j0 + 1
        w1 = j - j0
        w0 = 1.0 - w1
        if 0 <= j0 < n:
            dst[j0] += v * w0
        if 0 <= j1 < n:
            dst[j1] += v * w1
    return dst.astype(np.int64).tolist()


def apply_gain_amp_correction(
    filename: str,
    counts: list[int],
    raw_dir: Path,
) -> tuple[list[int], dict]:
    """参照 MCA のピーク ch でゲイン rebin。補正不要なら (counts, {})。"""
    ref_name = GAIN_AMP_CORRECTIONS.get(filename)
    if not ref_name:
        return counts, {}
    ref_path = raw_dir / ref_name
    if not ref_path.exists():
        raise FileNotFoundError(f"ゲイン補正参照 MCA がありません: {ref_path}")
    ref_meta = parse_mca(ref_path, apply_gain_correction=False)
    serial = infer_serial(filename, "")
    search = search_lo_for_serial(serial)
    peak_src = find_peak(counts, search_lo=search)
    peak_ref = find_peak(ref_meta["counts"], search_lo=search)
    if peak_src <= 0 or peak_ref <= 0:
        raise ValueError(f"ゲイン補正: ピーク未検出 ({filename}: {peak_src}, ref: {peak_ref})")
    scale = peak_ref / peak_src
    corrected = rebin_counts_linear(counts, scale)
    note = (
        f"アンプD/d取り違え補正: rebin×{scale:.4f} "
        f"(peak {peak_src}→{peak_ref}, 参照={ref_name})"
    )
    return corrected, {
        "reference": ref_name,
        "peak_src": peak_src,
        "peak_ref": peak_ref,
        "scale": scale,
        "note": note,
    }


def parse_mca_for_analysis(path: Path) -> dict:
    """parse_mca の別名（ゲイン補正込み）。"""
    return parse_mca(path, apply_gain_correction=True)


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
