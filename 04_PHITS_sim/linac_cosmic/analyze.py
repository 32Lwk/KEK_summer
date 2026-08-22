#!/usr/bin/env python3
"""linac_cosmic の PHITS 結果を要約する。

  python3 analyze.py                 … 2ケースの spectrum_reg.out を読んで表を出す
  python3 analyze.py --csv out.csv   … 機械可読の表も書き出す

出力は totfact = pi*c1**2 規格化なので絶対値 [/cm2/s]。
"""
import argparse
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# 領域番号 → 表示名（2ケース共通の対応）
REG_LABEL = {
    "01_open_sky": {
        "111": "地上 開空 GL+1.3m",
        "300": "地上 開空 GL+1.3m (横)",
        "221": "覆土のみ 空洞 -4.3m",
        "220": "覆土のみ 空洞（室平均）",
    },
    "02_linac": {
        "111": "ギャラリー 床上1.3m",
        "300": "建屋脇 屋外 GL+1.3m",
        "221": "トンネル ビーム高さ",
        "110": "ギャラリー（室平均）",
        "220": "トンネル（室平均）",
    },
}

# PHITS のグループ名 → 表示名
PART_LABEL = {"p3-group": "muon±", "p2-group": "muon±"}

# エネルギー区分（中性子の帯域別に積分する）
BANDS = [("thermal", 0.0, 5.0e-7), ("epi", 5.0e-7, 0.1), ("fast", 0.1, 1.0e4)]


def parse_spectrum(path):
    """spectrum_reg.out → {reg: {part: [(elo, ehi, val, rerr), ...]}}"""
    if not os.path.exists(path):
        return None
    parts, out, reg, cols = [], {}, None, None
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            s = line.strip()
            m = re.match(r"#\s*no\.\s*=\s*\d+\s+reg\s*=\s*(\S+)", s)
            if m:
                reg = m.group(1)
                out.setdefault(reg, {})
                continue
            if s.startswith("#  e-lower"):
                cols = re.findall(r"(\S+)\s+r\.err", s)
                if not parts:
                    parts = cols
                continue
            if not s or s.startswith(("#", "h:", "x:", "y:", "p:", "$")):
                continue
            f = s.split()
            if reg is None or cols is None or len(f) < 2 + 2 * len(cols):
                continue
            try:
                v = [float(x) for x in f]
            except ValueError:
                continue
            elo, ehi = v[0], v[1]
            for i, p in enumerate(cols):
                val, rerr = v[2 + 2 * i], v[3 + 2 * i]
                out[reg].setdefault(p, []).append((elo, ehi, val, rerr))
    return out


def integrate(rows, lo=0.0, hi=1.0e30):
    """ビン積分値の和と統計誤差（二乗和）。rows は既にビン積分値 [1/cm2/source]"""
    tot, var = 0.0, 0.0
    for elo, ehi, val, rerr in rows:
        ec = math.sqrt(max(elo, 1e-30) * ehi)
        if not (lo <= ec < hi):
            continue
        tot += val
        var += (val * rerr) ** 2
    return tot, math.sqrt(var)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=None)
    args = ap.parse_args()

    data, rows_csv = {}, []
    for case in ("01_open_sky", "02_linac"):
        path = os.path.join(HERE, case, "spectrum_reg.out")
        d = parse_spectrum(path)
        if d is None:
            print(f"!! {path} がない（まだ計算していない）", file=sys.stderr)
            continue
        data[case] = d
        print(f"\n=== {case} : {path.replace(HERE + os.sep, '')} ===")
        head = f"{'領域':28s} {'粒子':10s} {'全エネルギー':>13s} {'熱':>11s} {'熱外':>11s} {'速中性子':>11s}"
        print(head)
        print("-" * len(head))
        for reg in d:
            label = REG_LABEL.get(case, {}).get(reg, f"reg {reg}")
            for part, rows in d[reg].items():
                part = PART_LABEL.get(part, part)
                tot, err = integrate(rows)
                bands = [integrate(rows, lo, hi)[0] for _, lo, hi in BANDS]
                rel = f"±{100*err/tot:4.1f}%" if tot > 0 else "      "
                print(f"{label:28s} {part:10s} {tot:10.3e} {rel} "
                      f"{bands[0]:10.3e} {bands[1]:10.3e} {bands[2]:10.3e}")
                rows_csv.append([case, reg, label, part, tot, err] + bands)

    # ---- 比（linac / 開空）----
    if len(data) == 2:
        print("\n=== 建屋による減衰（02_linac ÷ 01_open_sky の同一粒子）===")
        base = {}
        for part in data["01_open_sky"].get("111", {}):
            base[PART_LABEL.get(part, part)] = integrate(data["01_open_sky"]["111"][part])
        print(f"{'点':28s} {'粒子':10s} {'flux [/cm2/s]':>13s} {'開空比':>10s}")
        print("-" * 66)
        for reg in ("111", "221", "300", "110", "220"):
            if reg not in data["02_linac"]:
                continue
            for part, rows in data["02_linac"][reg].items():
                part = PART_LABEL.get(part, part)
                tot, err = integrate(rows)
                b, berr = base.get(part, (0.0, 0.0))
                if b <= 0:
                    continue
                r = tot / b
                rerr = r * math.sqrt((err / tot) ** 2 + (berr / b) ** 2) if tot > 0 else 0.0
                lab = REG_LABEL["02_linac"].get(reg, reg)
                print(f"{lab:28s} {part:10s} {tot:10.3e}   {r:8.4f} ± {rerr:.4f}")
        # 覆土のみの場合も
        print("\n=== 参考：覆土のみ（01_open_sky の空洞 ÷ 同ケース地上）===")
        for reg in ("221", "220"):
            if reg not in data["01_open_sky"]:
                continue
            for part, rows in data["01_open_sky"][reg].items():
                part = PART_LABEL.get(part, part)
                tot, err = integrate(rows)
                b, berr = base.get(part, (0.0, 0.0))
                if b <= 0 or tot <= 0:
                    continue
                r = tot / b
                lab = REG_LABEL["01_open_sky"].get(reg, reg)
                print(f"{lab:28s} {part:10s} {tot:10.3e}   {r:8.4f}")

    if args.csv and rows_csv:
        import csv
        with open(args.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["case", "reg", "label", "particle", "flux_total_cm-2s-1",
                        "err", "thermal", "epithermal", "fast"])
            w.writerows(rows_csv)
        print(f"\n書き出し: {args.csv}")


if __name__ == "__main__":
    main()
