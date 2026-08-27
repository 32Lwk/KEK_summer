# large_d_cut200（適応型補正・d/D 統合・確認用）

本解析の `tables/`・`figures/` は**未変更**（`--merge` するまで）。
この成果は `denoised_runs/large_d_cut200/` にあり、他 run とは独立。

## 方針

1. 入力: いまの `raw/`（方式B済み4件含む）
2. 対象: d1/d2/D1/D2 計 28 件（small 12 + large 16）
3. **S2**: part/full ≥ 0.84 かつ左漏れ弱 → **未補正**
4. **C4**: 左漏れ r2≥0.45 → cut=300、それ以外 cut=200
5. **F5**: ch<cut を熱中性子テンプレ、ch≥cut は観測維持（wall 合計 = N_ge/f）
6. **T1**: f_large = D1熱中性子、f_small = d1熱中性子（cut ごと）
7. 適用 12 件 / skip 16 件
8. **hybrid**: PS → D skip + d legacy F2
9. **testhole**: 大小 legacy F2 / **BT**: D1 adapt + d2 skip / **Linac3**: d2 skip + 他 adapt
10. **preserve**: PF, linac
11. 除外: 熱中性子・gain・D1/d2 PF(0807)・`_error`

- f_large @ 200 = 0.872813
- f_small @ 200 = 0.871608

## 評価

- `evaluation_adaptive.csv` … 同地点 D/d |log比|（E1）

## 図の見方

→ `denoised_runs/large_d_cut200/figures/地点別/README.md`
→ 時系列: `figures/地点別_denoised/stages/02_large_d_cut200/`

## 出力場所

- MCA: `denoised_runs/large_d_cut200/raw/`
- 地点別: `denoised_runs/large_d_cut200/figures/地点別/<stem>/`
- fig16–19: `denoised_runs/large_d_cut200/figures/地点別/theory_16_19/`
- 再集計表: `denoised_runs/large_d_cut200/tables/`

## 対象ファイル

| ファイル | 族 | mode | cut | wall | part/full | r2 | f | cps前 | cps後 |
|---|---|---|---:|---|---:|---:|---:|---:|---:|
| `D1_20260818_1552_管理棟2階.mca` | large_D | skip | 200 | 86-366 | 0.850 | 0.203 | 0.8728 | 0.769826 | 0.769826 |
| `D1_20260818_1730_linac.mca` | large_D | skip_preserve | 200 | 85-366 | 0.746 | - | 0.8728 | 0.121647 | 0.121647 |
| `D1_20260819_0832_管理棟2階.mca` | large_D | skip | 200 | 85-366 | 0.851 | 0.198 | 0.8728 | 0.800238 | 0.800238 |
| `D1_20260819_1344_管理棟1階.mca` | large_D | skip | 200 | 85-366 | 0.843 | 0.210 | 0.8728 | 0.585162 | 0.585162 |
| `D1_20260819_1530_地上.mca` | large_D | skip | 200 | 85-366 | 0.855 | 0.195 | 0.8728 | 0.650582 | 0.650582 |
| `D1_20260819_1854_放射線棟BT.mca` | large_D | adaptive_f5 | 200 | 99-412 | 0.779 | 0.357 | 0.8728 | 0.14994 | 0.136375 |
| `D1_20260820_1939_KEKB.mca` | large_D | adaptive_f5 | 300 | 96-401 | 0.599 | 0.718 | 0.7343 | 0.0662181 | 0.0542204 |
| `D1_20260823_1510_Linac3.mca` | large_D | adaptive_f5 | 300 | 95-399 | 0.460 | 1.241 | 0.7343 | 0.140251 | 0.0876298 |
| `D1_20260823_1510_PS.mca` | large_D | skip_hybrid | 200 | 96-401 | 0.497 | - | 0.8728 | 0.0822659 | 0.0822659 |
| `D1_20260823_1510_linac_testhole.mca` | large_D | legacy_f2 | 300 | 96-403 | 0.559 | 0.931 | 0.7690 | 0.315581 | 0.229657 |
| `D2_20260821_080728_linac.mca` | large_D | skip_preserve | 200 | 97-404 | 0.679 | - | 0.8728 | 0.12563 | 0.12563 |
| `D2_20260821_170217_linacIRON.mca` | large_D | skip | 200 | 95-398 | 0.804 | 0.292 | 0.8728 | 0.304632 | 0.304632 |
| `D2_20260822_115234_PF.mca` | large_D | skip_preserve | 200 | 96-402 | 0.770 | - | 0.8728 | 0.260231 | 0.260231 |
| `D2_20260822_155048_地上.mca` | large_D | skip | 200 | 98-408 | 0.845 | 0.236 | 0.8728 | 0.433508 | 0.433508 |
| `D2_20260823_0835_Linac3.mca` | large_D | adaptive_f5 | 300 | 95-398 | 0.442 | 1.365 | 0.7343 | 0.102835 | 0.0619116 |
| `D2_20260824_1440_linac_testhole.mca` | large_D | legacy_f2 | 300 | 96-403 | 0.559 | 0.931 | 0.7690 | 0.315581 | 0.229657 |
| `d1_20260819_1520_管理棟2階.mca` | small_d | skip | 200 | 97-408 | 0.866 | 0.204 | 0.8716 | 0.202457 | 0.202457 |
| `d1_20260823_1509_Linac3.mca` | small_d | adaptive_f5 | 300 | 98-409 | 0.531 | 1.063 | 0.7748 | 0.0340544 | 0.0247786 |
| `d1_20260823_1509_PS.mca` | small_d | legacy_f2 | 300 | 98-409 | 0.392 | 1.949 | 0.7690 | 0.0321227 | 0.0164385 |
| `d1_20260823_1509_linac_testhole.mca` | small_d | legacy_f2 | 300 | 97-408 | 0.219 | 5.230 | 0.7690 | 0.396783 | 0.113374 |
| `d1_20260825_1439_linac_testhole.mca` | small_d | legacy_f2 | 300 | 97-408 | 0.271 | 4.743 | 0.7690 | 0.659478 | 0.232441 |
| `d2_20260819_1859_放射線棟BT.mca` | small_d | skip_site | 200 | 97-408 | 0.770 | - | 0.8716 | 0.0196007 | 0.0196007 |
| `d2_20260820_1939_KEKB.mca` | small_d | adaptive_f5 | 300 | 98-411 | 0.574 | 0.904 | 0.7748 | 0.0124494 | 0.00799223 |
| `d2_20260821_080725_linac.mca` | small_d | skip_preserve | 200 | 97-408 | 0.441 | - | 0.8716 | 0.114352 | 0.114352 |
| `d2_20260821_170219_linacIRON.mca` | small_d | skip | 200 | 97-408 | 0.830 | 0.263 | 0.8716 | 0.0761463 | 0.0761463 |
| `d2_20260822_115232_PF.mca` | small_d | skip_preserve | 200 | 99-412 | 0.566 | - | 0.8716 | 0.353928 | 0.353928 |
| `d2_20260822_155046_地上.mca` | small_d | legacy_f2 | 300 | 96-408 | 0.465 | 1.497 | 0.7690 | 0.17968 | 0.109626 |
| `d2_20260823_0834_Linac3.mca` | small_d | skip_site | 200 | 96-408 | 0.509 | - | 0.8716 | 0.0220714 | 0.0220714 |

## 本解析への反映

```bash
python3 03_今年度用/build_denoised_review.py --run-id large_d_cut200 --merge
```

- 対象ファイルは `raw_pre_partial_corr/large_d_cut200/` に退避してから `raw/` を置換
- tables / figures / theory を再計算
