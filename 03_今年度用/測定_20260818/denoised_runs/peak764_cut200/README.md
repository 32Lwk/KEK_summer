# peak764_cut200（peak ROI 側帯 NET f · 02 地点別ロジック）

親ディレクトリ: `denoised_runs/peak764_cut200/`（他 run とは独立）

入力はいまの `raw/`（方式B済み4件含む）。
対象 29 件（small_d 12 + large_D 17）。

## 方針

- **S2**: part/full ≥ 0.84 かつ左漏れ弱い地点は**未補正**
- **C4**: 左漏れ r2≥0.45 のとき cut=300、それ以外 cut=200
- **F5**: ch<cut を熱中性子テンプレ、ch≥cut は観測維持で wall 合計 = N_ge/f
- **T1**: f = D1/d1 熱中性子 **peak ROI 側帯 NET 比**（4ファイル平均）

- f_large @ 200 = 0.707959
- f_small @ 200 = 0.667979
- 適用 0 件 / skip 13 件
- **hybrid**: PS → D skip + d legacy F2 (cut=300, f=0.769)
- **testhole**: 大小とも legacy F2
- **BT**: D1 適応 F5、d2 本番
- **Linac3**: d2 本番、他適応 F5
- **preserve**: PF, linac（トンネル linac 系）→ 本番維持
- 除外: 熱中性子・gain・D1/d2 PF・`_error`
- 本解析は未変更（`--merge` するまで）

## 中身

- `raw/` … 補正 MCA
- `review_raw/` … 再集計用
- `tables/`
- `figures/地点別/`
- `evaluation_adaptive.csv` … 同地点 D/d 評価

| ファイル | 族 | mode | cut | wall | part/full | r2 | f | N_wall補正後 |
|---|---|---|---:|---|---:|---:|---:|---:|
| `D1_20260818_1552_管理棟2階.mca` | large_D | peak_skip_clean | 200 | 86-366 | 0.850 | - | 0.7080 | 1028 |
| `D1_20260818_1730_linac.mca` | large_D | skip_preserve | 200 | 85-366 | 0.746 | - | 0.7080 | 512 |
| `D1_20260819_0832_管理棟2階.mca` | large_D | peak_skip_clean | 200 | 85-366 | 0.851 | - | 0.7080 | 41810 |
| `D1_20260819_1344_管理棟1階.mca` | large_D | peak_skip_clean | 200 | 85-366 | 0.843 | - | 0.7080 | 10230 |
| `D1_20260819_1530_地上.mca` | large_D | peak_skip_clean | 200 | 85-366 | 0.855 | - | 0.7080 | 3089 |
| `D1_20260819_1854_放射線棟BT.mca` | large_D | peak_partial | 200 | 370-422 | 0.867 | 0.357 | 0.7080 | 1093 |
| `D1_20260820_1939_KEKB.mca` | large_D | peak_partial | 300 | 359-411 | 0.958 | 0.612 | 0.7080 | 2071 |
| `D1_20260823_1510_Linac3.mca` | large_D | peak_partial | 300 | 357-409 | 0.959 | 1.142 | 0.7080 | 2066 |
| `D1_20260823_1510_PS.mca` | large_D | peak_partial | 300 | 359-411 | 0.947 | 1.440 | 0.7080 | 3328 |
| `D1_20260823_1510_linac_testhole.mca` | large_D | peak_partial | 300 | 361-413 | 0.913 | 0.540 | 0.7080 | 4068 |
| `D2_20260821_080728_linac.mca` | large_D | skip_preserve | 200 | 97-404 | 0.679 | - | 0.7080 | 5349 |
| `D2_20260821_170217_linacIRON.mca` | large_D | peak_skip_clean | 200 | 95-398 | 0.804 | - | 0.7080 | 9402 |
| `D2_20260822_115234_PF.mca` | large_D | skip_preserve | 200 | 96-402 | 0.770 | - | 0.7080 | 16355 |
| `D2_20260822_155048_地上.mca` | large_D | peak_skip_clean | 200 | 98-408 | 0.845 | - | 0.7080 | 5333 |
| `D2_20260823_0835_Linac3.mca` | large_D | peak_partial | 300 | 356-408 | 0.957 | 1.232 | 0.7080 | 3203 |
| `D2_20260824_1440_linac_testhole.mca` | large_D | peak_partial | 300 | 361-413 | 0.913 | 0.540 | 0.7080 | 4068 |
| `D2_20260826_0026_ep1.mca` | large_D | peak_partial | 300 | 314-366 | 0.960 | 5.559 | 0.7080 | 1440 |
| `d1_20260819_1520_管理棟2階.mca` | small_d | peak_skip_clean | 200 | 97-408 | 0.866 | - | 0.6680 | 15554 |
| `d1_20260823_1509_Linac3.mca` | small_d | peak_partial | 300 | 350-408 | 0.694 | 0.946 | 0.6680 | 388 |
| `d1_20260823_1509_PS.mca` | small_d | peak_partial | 300 | 350-408 | 0.686 | 1.532 | 0.6680 | 862 |
| `d1_20260823_1509_linac_testhole.mca` | small_d | peak_partial | 300 | 350-408 | 0.781 | 3.777 | 0.6680 | 1398 |
| `d1_20260825_1439_linac_testhole.mca` | small_d | peak_partial | 300 | 350-408 | 0.706 | 3.063 | 0.6680 | 2262 |
| `d2_20260819_1859_放射線棟BT.mca` | small_d | peak_partial | 200 | 350-408 | 0.762 | 0.398 | 0.6680 | 131 |
| `d2_20260820_1939_KEKB.mca` | small_d | peak_partial | 300 | 350-408 | 0.710 | 0.755 | 0.6680 | 256 |
| `d2_20260821_080725_linac.mca` | small_d | skip_preserve | 200 | 97-408 | 0.441 | - | 0.6680 | 4791 |
| `d2_20260821_170219_linacIRON.mca` | small_d | peak_skip_clean | 200 | 97-408 | 0.830 | - | 0.6680 | 2291 |
| `d2_20260822_115232_PF.mca` | small_d | skip_preserve | 200 | 99-412 | 0.566 | - | 0.6680 | 21720 |
| `d2_20260822_155046_地上.mca` | small_d | peak_partial | 300 | 350-408 | 0.774 | 0.994 | 0.6680 | 928 |
| `d2_20260823_0834_Linac3.mca` | small_d | peak_partial | 300 | 350-408 | 0.827 | 1.289 | 0.6680 | 545 |
