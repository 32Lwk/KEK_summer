# peak764_cut200（764 keV peak ROI フラックス・確認用）

本解析の `tables/`・`figures/` は**未変更**（`--merge` するまで）。
この成果は `denoised_runs/peak764_cut200/` にあり、他 run とは独立。

## 方針

1. 入力: いまの `raw/`
2. 対象: d1/d2/D1/D2 計 29 件（small 12 + large 17）
3. **フラックス**: φ = peak ROI NET / εS_peak（側帯背景）
4. **スペクトル補正**: peak ROI 部分補正（S2: part/full≥0.84 かつ左漏れ弱 → skip）
5. **Linac3**: wall F5 を使わず peak 部分補正のみ
6. 除外: 熱中性子・gain・D1/d2 PF・`_error`

- f_large（参考・peak ROI 側帯 NET）@ 200 = 0.707959
- f_small（参考）@ 200 = 0.667979

## 評価

- `evaluation_adaptive.csv` … 同地点 D/d |log比|（E1）

## 図の見方

→ `denoised_runs/peak764_cut200/figures/地点別/README.md`
→ 時系列: `figures/地点別_denoised/stages/03_peak764_cut200/`

## 出力場所

- MCA: `denoised_runs/peak764_cut200/raw/`
- 地点別: `denoised_runs/peak764_cut200/figures/地点別/<stem>/`
- fig16–19: `denoised_runs/peak764_cut200/figures/地点別/theory_16_19/`
- 再集計表: `denoised_runs/peak764_cut200/tables/`

## 対象ファイル

| ファイル | 族 | mode | cut | wall | part/full | r2 | f | cps前 | cps後 |
|---|---|---|---:|---|---:|---:|---:|---:|---:|
| `D1_20260818_1552_管理棟2階.mca` | large_D | peak_skip_clean | 200 | 86-366 | 0.850 | - | 0.7080 | 0.769826 | 0.769826 |
| `D1_20260818_1730_linac.mca` | large_D | skip_preserve | 200 | 85-366 | 0.746 | - | 0.7080 | 0.121647 | 0.121647 |
| `D1_20260819_0832_管理棟2階.mca` | large_D | peak_skip_clean | 200 | 85-366 | 0.851 | - | 0.7080 | 0.800238 | 0.800238 |
| `D1_20260819_1344_管理棟1階.mca` | large_D | peak_skip_clean | 200 | 85-366 | 0.843 | - | 0.7080 | 0.585162 | 0.585162 |
| `D1_20260819_1530_地上.mca` | large_D | peak_skip_clean | 200 | 85-366 | 0.855 | - | 0.7080 | 0.650582 | 0.650582 |
| `D1_20260819_1854_放射線棟BT.mca` | large_D | peak_skip_clean | 200 | 99-412 | 0.804 | - | 0.7080 | 0.169556 | 0.169556 |
| `D1_20260820_1939_KEKB.mca` | large_D | peak_partial | 300 | 359-411 | 1.000 | 0.454 | 0.7080 | 0.0530924 | 0.0749087 |
| `D1_20260823_1510_Linac3.mca` | large_D | peak_partial | 300 | 357-409 | 1.000 | 0.847 | 0.7080 | 0.0889647 | 0.125524 |
| `D1_20260823_1510_PS.mca` | large_D | peak_partial | 300 | 359-411 | 1.000 | 1.089 | 0.7080 | 0.0423613 | 0.0598124 |
| `D1_20260823_1510_linac_testhole.mca` | large_D | peak_partial | 200 | 361-413 | 1.000 | 0.424 | 0.7080 | 0.201 | 0.283959 |
| `D2_20260821_080728_linac.mca` | large_D | skip_preserve | 200 | 97-404 | 0.679 | - | 0.7080 | 0.12563 | 0.12563 |
| `D2_20260821_170217_linacIRON.mca` | large_D | peak_skip_clean | 200 | 95-398 | 0.804 | - | 0.7080 | 0.304632 | 0.304632 |
| `D2_20260822_115234_PF.mca` | large_D | skip_preserve | 200 | 96-402 | 0.770 | - | 0.7080 | 0.260231 | 0.260231 |
| `D2_20260822_155048_地上.mca` | large_D | peak_skip_clean | 200 | 98-408 | 0.845 | - | 0.7080 | 0.433508 | 0.433508 |
| `D2_20260823_0835_Linac3.mca` | large_D | peak_partial | 300 | 356-408 | 1.000 | 0.918 | 0.7080 | 0.0624772 | 0.0881859 |
| `D2_20260824_1440_linac_testhole.mca` | large_D | peak_partial | 200 | 361-413 | 1.000 | 0.424 | 0.7080 | 0.201 | 0.283959 |
| `D2_20260826_0026_ep1.mca` | large_D | peak_partial | 300 | 314-366 | 0.960 | 5.559 | 0.7080 | 0.0331592 | 0.0449616 |
| `d1_20260819_1520_管理棟2階.mca` | small_d | peak_skip_clean | 200 | 97-408 | 0.866 | - | 0.6680 | 0.202457 | 0.202457 |
| `d1_20260823_1509_Linac3.mca` | small_d | peak_partial | 300 | 350-408 | 1.000 | 0.853 | 0.6680 | 0.0166622 | 0.0246497 |
| `d1_20260823_1509_PS.mca` | small_d | peak_partial | 300 | 350-408 | 1.000 | 1.367 | 0.6680 | 0.0112104 | 0.0167246 |
| `d1_20260823_1509_linac_testhole.mca` | small_d | peak_partial | 300 | 350-408 | 1.000 | 3.036 | 0.6680 | 0.0736853 | 0.110001 |
| `d1_20260825_1439_linac_testhole.mca` | small_d | peak_partial | 300 | 350-408 | 1.000 | 2.605 | 0.6680 | 0.119225 | 0.17831 |
| `d2_20260819_1859_放射線棟BT.mca` | small_d | peak_skip_clean | 200 | 97-408 | 0.781 | - | 0.6680 | 0.0205441 | 0.0205441 |
| `d2_20260820_1939_KEKB.mca` | small_d | peak_partial | 300 | 350-408 | 1.000 | 0.676 | 0.6680 | 0.00655773 | 0.00965728 |
| `d2_20260821_080725_linac.mca` | small_d | skip_preserve | 200 | 97-408 | 0.441 | - | 0.6680 | 0.114352 | 0.114352 |
| `d2_20260821_170219_linacIRON.mca` | small_d | peak_skip_clean | 200 | 97-408 | 0.830 | - | 0.6680 | 0.0761463 | 0.0761463 |
| `d2_20260822_115232_PF.mca` | small_d | skip_preserve | 200 | 99-412 | 0.566 | - | 0.6680 | 0.353928 | 0.353928 |
| `d2_20260822_155046_地上.mca` | small_d | peak_partial | 300 | 350-408 | 1.000 | 0.832 | 0.6680 | 0.0766636 | 0.114252 |
| `d2_20260823_0834_Linac3.mca` | small_d | peak_partial | 300 | 350-408 | 1.000 | 1.022 | 0.6680 | 0.0106075 | 0.0157653 |

## 本解析への反映

```bash
python3 03_今年度用/build_denoised_review.py --run-id peak764_cut200 --merge
```

- 対象ファイルは `raw_pre_partial_corr/peak764_cut200/` に退避してから `raw/` を置換
- tables / figures / theory を再計算
