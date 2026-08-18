#!/usr/bin/env python3
"""今年度 MCA（Amptek MCA8000D）スペクトルを CSV と Excel に変換する。

USB 上の .mca をリポジトリへ複製し、計数率正規化スペクトルを書き出す。
エネルギー較正は未実施のため、チャンネル番号のまま保存する。
昨年の熱中性子／MeV 窓の計数率とは直接比較しないこと。
"""

from __future__ import annotations

import csv
import re
import shutil
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import Reference, ScatterChart, Series
from openpyxl.chart.axis import ChartLines
from openpyxl.chart.marker import Marker
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "測定_20260818"
RAW = OUT / "raw"
TABLES = OUT / "tables"
USB = Path("/Volumes/NO NAME")

BLACK, GRAY, BLUE, RED = "000000", "666666", "1F77B4", "D62728"
PALE, WHITE, HEADER, YELLOW = "F5F5F5", "FFFFFF", "1F4E79", "FFF2CC"

thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
center = Alignment(horizontal="center", vertical="center", wrap_text=True)
left = Alignment(horizontal="left", vertical="center", wrap_text=True)

RUNS = [
    {
        "id": "kanri2f",
        "場所": "管理棟2F",
        "filename": "20260818_1552_管理棟2F.mca",
        "屋内_屋外": "屋内",
        "標高_m": 30,
        "メモ": "今年度・全スペクトル（未較正）。ch0はADCオーバーフロー。昨年の熱/MeV窓とは別定義。",
    },
    {
        "id": "linac",
        "場所": "linac",
        "filename": "20260818_1730_linac.mca",
        "屋内_屋外": "屋内",
        "標高_m": 30,
        "メモ": "今年度・全スペクトル（未較正）。ch0はADCオーバーフロー。昨年の熱/MeV窓とは別定義。",
    },
]


def parse_mca(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta: dict = {"path": path}
    for key in ("LIVE_TIME", "REAL_TIME", "START_TIME", "GAIN", "THRESHOLD"):
        m = re.search(rf"^{key} - (.+)$", text, re.M)
        if m:
            meta[key] = m.group(1).strip()
    roi = re.search(r"<<ROI>>\n(\d+) (\d+)", text)
    meta["roi"] = (int(roi.group(1)), int(roi.group(2))) if roi else (None, None)
    data = re.search(r"<<DATA>>\n([\s\S]*?)\n<<END>>", text)
    if not data:
        raise ValueError(f"DATA が見つかりません: {path}")
    counts = [int(x) for x in data.group(1).splitlines() if x.strip()]
    meta["counts"] = counts
    meta["n_channels"] = len(counts)
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


def summarize(run: dict, meta: dict) -> dict:
    counts = meta["counts"]
    live = float(meta["LIVE_TIME"])
    real = float(meta["REAL_TIME"])
    total = sum(counts)
    roi_lo, roi_hi = meta["roi"]
    roi_sum = sum(counts[roi_lo : roi_hi + 1]) if roi_lo is not None else 0
    ch0 = counts[0]
    ch1_20 = sum(counts[1:21])
    ch21_149 = sum(counts[21:150])
    ch451 = sum(counts[451:])
    excl0 = total - ch0
    dead = 1.0 - live / real if real else 0.0
    peak_ch = max(range(1, min(150, len(counts))), key=lambda i: counts[i])
    return {
        **run,
        "日付": "2026-08-18",
        "開始時刻": meta["START_TIME"],
        "live_s": live,
        "real_s": real,
        "dead_pct": 100.0 * dead,
        "n_channels": meta["n_channels"],
        "データ数": total,
        "測定時間_s": live,
        "計数率_s-1": total / live,
        "計数率_ch0除く_s-1": excl0 / live,
        "ch0": ch0,
        "ch0_cps": ch0 / live,
        "ch1_20": ch1_20,
        "ch1_20_cps": ch1_20 / live,
        "ch21_149": ch21_149,
        "ch21_149_cps": ch21_149 / live,
        "roi_lo": roi_lo,
        "roi_hi": roi_hi,
        "roi_counts": roi_sum,
        "roi_cps": roi_sum / live,
        "ch451_511": ch451,
        "peak_ch": peak_ch,
        "peak_counts": counts[peak_ch],
        "装置": meta["device"],
        "シリアル": meta["serial"],
        "ゲインGAIA": meta["gaia"],
        "ボード温度_C": meta["board_temp_C"],
        "slow_count": meta["slow_count"],
        "領域": "全スペクトル（未較正）",
        "フラックス_s-1_cm-2": "",
        "気圧_hPa": "",
        "気温_C": "",
        "覆土深さ_m": "",
        "覆土材質": "",
        "密度_g_cm-3_推定": "",
        "counts": counts,
    }


def find_mca(filename: str) -> Path | None:
    candidates = [
        USB / filename,
        RAW / filename,
    ]
    if Path("/Volumes").exists():
        for vol in Path("/Volumes").iterdir():
            candidates.append(vol / filename)
    for p in candidates:
        if p.is_file():
            return p
    return None


def copy_raw() -> list[dict]:
    RAW.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)
    rows = []
    missing = []
    for run in RUNS:
        src = find_mca(run["filename"])
        dst = RAW / run["filename"]
        if src is None:
            missing.append(run["filename"])
            continue
        if src.resolve() != dst.resolve():
            shutil.copy2(src, dst)
        meta = parse_mca(dst)
        rows.append(summarize(run, meta))
    if missing:
        raise FileNotFoundError(
            "MCA が見つかりません: "
            + ", ".join(missing)
            + "。USB を再接続するか raw/ に .mca を置いて再実行してください。"
        )
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_tables(rows: list[dict]) -> None:
    rec_fields = [
        "日付",
        "場所",
        "標高_m",
        "覆土深さ_m",
        "覆土材質",
        "密度_g_cm-3_推定",
        "屋内_屋外",
        "領域",
        "データ数",
        "測定時間_s",
        "計数率_s-1",
        "計数率_ch0除く_s-1",
        "フラックス_s-1_cm-2",
        "気圧_hPa",
        "気温_C",
        "開始時刻",
        "live_s",
        "real_s",
        "dead_pct",
        "ch0",
        "ch0_cps",
        "ch1_20",
        "ch1_20_cps",
        "ch21_149",
        "ch21_149_cps",
        "roi_lo",
        "roi_hi",
        "roi_counts",
        "roi_cps",
        "peak_ch",
        "装置",
        "シリアル",
        "ゲインGAIA",
        "ボード温度_C",
        "filename",
        "メモ",
    ]
    write_csv(TABLES / "測定記録.csv", rec_fields, rows)

    n = rows[0]["n_channels"]
    spec_rows = []
    for ch in range(n):
        rec = {"channel": ch}
        for r in rows:
            rec[f"counts_{r['id']}"] = r["counts"][ch]
            rec[f"cps_{r['id']}"] = r["counts"][ch] / r["live_s"]
        r0, r1 = rows[0], rows[1]
        c0 = r0["counts"][ch] / r0["live_s"]
        c1 = r1["counts"][ch] / r1["live_s"]
        rec["ratio_linac_over_kanri2f"] = (c1 / c0) if c0 > 0 else ""
        spec_rows.append(rec)
    spec_fields = (
        ["channel"]
        + [f"counts_{r['id']}" for r in rows]
        + [f"cps_{r['id']}" for r in rows]
        + ["ratio_linac_over_kanri2f"]
    )
    write_csv(TABLES / "スペクトル.csv", spec_fields, spec_rows)

    band_rows = []
    bands = [
        ("ch0（オーバーフロー）", lambda c: c[0:1]),
        ("ch1–20", lambda c: c[1:21]),
        ("ch21–149", lambda c: c[21:150]),
        ("ch150–450（ROI）", lambda c: c[150:451]),
        ("ch451–511", lambda c: c[451:]),
        ("全チャンネル", lambda c: c),
        ("ch0除く", lambda c: c[1:]),
    ]
    for label, fn in bands:
        rec = {"帯域": label}
        for r in rows:
            s = sum(fn(r["counts"]))
            rec[f"counts_{r['id']}"] = s
            rec[f"cps_{r['id']}"] = s / r["live_s"]
            rec[f"pct_{r['id']}"] = 100.0 * s / r["データ数"]
        band_rows.append(rec)
    band_fields = ["帯域"]
    for r in rows:
        band_fields += [f"counts_{r['id']}", f"cps_{r['id']}", f"pct_{r['id']}"]
    write_csv(TABLES / "チャンネル帯.csv", band_fields, band_rows)


def style_header(ws, row: int, n: int, start: int = 1) -> None:
    for c in range(start, start + n):
        cell = ws.cell(row, c)
        cell.font = Font(bold=True, color=WHITE, size=11)
        cell.fill = PatternFill("solid", fgColor=HEADER)
        cell.alignment = center
        cell.border = border
    ws.row_dimensions[row].height = 28


def apply_border(ws, r, c) -> None:
    cell = ws.cell(r, c)
    cell.border = border
    cell.alignment = left if c == 1 else center


def setup_axis(axis, title, major=None, nfmt="General", amin=None, amax=None, log=False):
    axis.title = title
    axis.delete = False
    axis.majorTickMark = "out"
    axis.tickLblPos = "nextTo"
    axis.numFmt = nfmt
    if major is not None:
        axis.majorUnit = major
    if amin is not None:
        axis.scaling.min = amin
    if amax is not None:
        axis.scaling.max = amax
    if log:
        axis.scaling.logBase = 10
    axis.majorGridlines = ChartLines(
        spPr=GraphicalProperties(ln=LineProperties(solidFill="D9D9D9", w=9525))
    )
    axis.spPr = GraphicalProperties(ln=LineProperties(solidFill=BLACK, w=15875))


def build_xlsx(rows: list[dict]) -> Path:
    wb = Workbook()

    # --- 概要 ---
    ws = wb.active
    ws.title = "測定概要"
    ws["A1"] = "今年度 MCA 測定（2026-08-18）"
    ws["A1"].font = Font(bold=True, size=16, color=HEADER)
    ws.merge_cells("A1:F1")
    ws["A2"] = (
        "Amptek MCA8000D（シリアル 1715）。USB から複製。エネルギー較正なし。"
        "昨年9班の熱中性子／MeV領域の計数率とは窓定義が違うので直接比較しない。"
    )
    ws["A2"].alignment = left
    ws.merge_cells("A2:F2")
    ws.row_dimensions[2].height = 36

    labels = [
        ("日付", "日付"),
        ("場所", "場所"),
        ("開始時刻", "開始時刻"),
        ("Live time [s]", "live_s"),
        ("Real time [s]", "real_s"),
        ("Dead time [%]", "dead_pct"),
        ("総カウント", "データ数"),
        ("全体 計数率 [s⁻¹]", "計数率_s-1"),
        ("ch0除く 計数率 [s⁻¹]", "計数率_ch0除く_s-1"),
        ("ROI (ch150–450) 計数率 [s⁻¹]", "roi_cps"),
        ("ch1–20 計数率 [s⁻¹]", "ch1_20_cps"),
        ("最大ピーク ch（1–149）", "peak_ch"),
        ("装置", "装置"),
        ("ゲイン GAIA", "ゲインGAIA"),
        ("ボード温度 [°C]", "ボード温度_C"),
        ("元ファイル", "filename"),
        ("メモ", "メモ"),
    ]
    ws["A4"] = "項目"
    ws["B4"] = rows[0]["場所"]
    ws["C4"] = rows[1]["場所"]
    ws["D4"] = "比 (linac / 管理棟2F)"
    style_header(ws, 4, 4)

    for i, (label, key) in enumerate(labels, start=5):
        ws.cell(i, 1, label)
        v0, v1 = rows[0][key], rows[1][key]
        ws.cell(i, 2, v0)
        ws.cell(i, 3, v1)
        if isinstance(v0, (int, float)) and isinstance(v1, (int, float)) and v0 not in (0,):
            ws.cell(i, 4, v1 / v0)
            ws.cell(i, 4).number_format = "0.00"
        for c in range(1, 5):
            apply_border(ws, i, c)
        if i % 2 == 0:
            for c in range(1, 5):
                ws.cell(i, c).fill = PatternFill("solid", fgColor=PALE)

    for r, fmt in ((8, "0.0"), (9, "0.0"), (10, "0.00"), (11, "0.00"), (12, "0.00"), (13, "0.000"), (14, "0.00")):
        ws.cell(r, 2).number_format = fmt
        ws.cell(r, 3).number_format = fmt

    ws["A23"] = "注意"
    ws["A23"].font = Font(bold=True, color=HEADER)
    notes = [
        "これは今年度（2026-08-18）の測定である。前年9班の公開表とは別データ。",
        "ch0 が総カウントの約半分。ADC オーバーフローとして解析では除外するのが安全。",
        "信号は ch 5–7 付近に集中。設定 ROI（ch150–450）のカウントはごく少ない。",
        "フラックス（φ）はエネルギー窓と効率 ε, S が未確定のため空欄。",
        "生データ: 03_今年度用/測定_20260818/raw/　表: tables/*.csv",
    ]
    for i, t in enumerate(notes, start=24):
        ws.cell(i, 1, f"• {t}")
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=6)
        ws.cell(i, 1).alignment = left
        ws.row_dimensions[i].height = 20

    ws.column_dimensions["A"].width = 32
    ws.column_dimensions["B"].width = 28
    ws.column_dimensions["C"].width = 28
    ws.column_dimensions["D"].width = 22
    ws.column_dimensions["E"].width = 18
    ws.column_dimensions["F"].width = 18
    ws.freeze_panes = "A5"

    # --- スペクトル ---
    ws2 = wb.create_sheet("スペクトル")
    n = rows[0]["n_channels"]
    headers = ["channel", "counts_管理棟2F", "cps_管理棟2F", "counts_linac", "cps_linac", "比_linac/管理棟2F"]
    for c, h in enumerate(headers, 1):
        ws2.cell(1, c, h)
    style_header(ws2, 1, len(headers))
    for ch in range(n):
        c0 = rows[0]["counts"][ch]
        c1 = rows[1]["counts"][ch]
        cps0 = c0 / rows[0]["live_s"]
        cps1 = c1 / rows[1]["live_s"]
        ws2.cell(ch + 2, 1, ch)
        ws2.cell(ch + 2, 2, c0)
        ws2.cell(ch + 2, 3, cps0)
        ws2.cell(ch + 2, 4, c1)
        ws2.cell(ch + 2, 5, cps1)
        if cps0 > 0:
            ws2.cell(ch + 2, 6, cps1 / cps0)
            ws2.cell(ch + 2, 6).number_format = "0.000"
        ws2.cell(ch + 2, 3).number_format = "0.0000"
        ws2.cell(ch + 2, 5).number_format = "0.0000"
        for c in range(1, 7):
            ws2.cell(ch + 2, c).border = border
    for col, w in enumerate([12, 16, 16, 14, 14, 18], 1):
        ws2.column_dimensions[get_column_letter(col)].width = w
    ws2.freeze_panes = "A2"
    ws2.auto_filter.ref = f"A1:F{n + 1}"

    chart1 = ScatterChart()
    chart1.title = "計数率スペクトル（ch 1–80、ch0除外）"
    chart1.style = 10
    chart1.y_axis.crosses = "min"
    chart1.legend.position = "r"
    chart1.height = 10
    chart1.width = 18
    setup_axis(chart1.x_axis, "チャンネル", major=10, amin=1, amax=80)
    setup_axis(chart1.y_axis, "計数率 [s⁻¹ / ch]", nfmt="0.0")
    # series from row1 titles; skip ch0 by using data starting row 3 (ch=1)
    x_zoom = Reference(ws2, min_col=1, min_row=3, max_row=82)
    y0 = Reference(ws2, min_col=3, min_row=3, max_row=82)
    y1 = Reference(ws2, min_col=5, min_row=3, max_row=82)
    s0 = Series(y0, xvalues=x_zoom, title="管理棟2F")
    s1 = Series(y1, xvalues=x_zoom, title="linac")
    s0.graphicalProperties.line.solidFill = BLUE
    s0.graphicalProperties.line.width = 15000
    s0.marker = Marker(symbol=None)
    s1.graphicalProperties.line.solidFill = RED
    s1.graphicalProperties.line.width = 15000
    s1.marker = Marker(symbol=None)
    chart1.series.append(s0)
    chart1.series.append(s1)
    ws["A30"] = ""
    ws.add_chart(chart1, "A31")

    chart2 = ScatterChart()
    chart2.title = "計数率スペクトル（全ch、対数）"
    chart2.style = 10
    chart2.legend.position = "r"
    chart2.height = 10
    chart2.width = 18
    setup_axis(chart2.x_axis, "チャンネル", major=50, amin=0, amax=511)
    setup_axis(chart2.y_axis, "計数率 [s⁻¹ / ch]", nfmt="0.000", amin=1e-4, amax=50, log=True)
    x_all = Reference(ws2, min_col=1, min_row=2, max_row=n + 1)
    ya = Reference(ws2, min_col=3, min_row=2, max_row=n + 1)
    yb = Reference(ws2, min_col=5, min_row=2, max_row=n + 1)
    sa = Series(ya, xvalues=x_all, title="管理棟2F")
    sb = Series(yb, xvalues=x_all, title="linac")
    sa.graphicalProperties.line.solidFill = BLUE
    sa.graphicalProperties.line.width = 12000
    sa.marker = Marker(symbol=None)
    sb.graphicalProperties.line.solidFill = RED
    sb.graphicalProperties.line.width = 12000
    sb.marker = Marker(symbol=None)
    chart2.series.append(sa)
    chart2.series.append(sb)
    ws.add_chart(chart2, "A50")

    # --- チャンネル帯 ---
    ws3 = wb.create_sheet("チャンネル帯")
    ws3["A1"] = "チャンネル帯ごとのカウントと計数率"
    ws3["A1"].font = Font(bold=True, size=14, color=HEADER)
    ws3.merge_cells("A1:G1")
    band_headers = [
        "帯域",
        "管理棟2F カウント",
        "管理棟2F [s⁻¹]",
        "管理棟2F [%]",
        "linac カウント",
        "linac [s⁻¹]",
        "linac [%]",
        "計数率比",
    ]
    for c, h in enumerate(band_headers, 1):
        ws3.cell(3, c, h)
    style_header(ws3, 3, len(band_headers))

    bands = [
        ("ch0（オーバーフロー）", 0, 1),
        ("ch1–20", 1, 21),
        ("ch21–149", 21, 150),
        ("ch150–450（ROI）", 150, 451),
        ("ch451–511", 451, 512),
        ("全チャンネル", 0, 512),
        ("ch0除く", 1, 512),
    ]
    for i, (label, lo, hi) in enumerate(bands, start=4):
        s0 = sum(rows[0]["counts"][lo:hi])
        s1 = sum(rows[1]["counts"][lo:hi])
        cps0 = s0 / rows[0]["live_s"]
        cps1 = s1 / rows[1]["live_s"]
        ws3.cell(i, 1, label)
        ws3.cell(i, 2, s0)
        ws3.cell(i, 3, cps0)
        ws3.cell(i, 4, 100.0 * s0 / rows[0]["データ数"])
        ws3.cell(i, 5, s1)
        ws3.cell(i, 6, cps1)
        ws3.cell(i, 7, 100.0 * s1 / rows[1]["データ数"])
        ws3.cell(i, 8, cps1 / cps0 if cps0 else "")
        ws3.cell(i, 3).number_format = "0.00"
        ws3.cell(i, 4).number_format = "0.0"
        ws3.cell(i, 6).number_format = "0.00"
        ws3.cell(i, 7).number_format = "0.0"
        ws3.cell(i, 8).number_format = "0.00"
        for c in range(1, 9):
            apply_border(ws3, i, c)
        if label == "ch0除く":
            for c in range(1, 9):
                ws3.cell(i, c).fill = PatternFill("solid", fgColor=YELLOW)
    for col, w in enumerate([22, 18, 16, 14, 16, 14, 12, 12], 1):
        ws3.column_dimensions[get_column_letter(col)].width = w

    xlsx = OUT / "測定_20260818_MCA.xlsx"
    wb.save(xlsx)
    return xlsx


def main() -> None:
    rows = copy_raw()
    write_tables(rows)
    xlsx = build_xlsx(rows)
    rec = TABLES / "測定記録.csv"
    spec = TABLES / "スペクトル.csv"
    print(f"raw     : {RAW}")
    print(f"記録    : {rec}")
    print(f"スペクトル: {spec}")
    print(f"Excel   : {xlsx}")
    try:
        from _plot_mca import main as plot_main

        plot_main()
    except Exception as exc:
        print(f"figures skipped: {exc}")
    for r in rows:
        print(
            f"  {r['場所']}: live={r['live_s']:.1f}s  "
            f"R={r['計数率_s-1']:.2f} cps  R(ch0除く)={r['計数率_ch0除く_s-1']:.2f} cps"
        )


if __name__ == "__main__":
    main()
