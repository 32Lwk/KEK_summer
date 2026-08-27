# small_d_cut300（d/D 統合・ch>=300 割合補正・確認用）

本解析の `tables/`・`figures/` は**未変更**（`--merge` するまで）。
この成果は `denoised_runs/small_d_cut300/` にあり、他 run とは独立。

## 方式

1. 入力: いまの `raw/`（small_d 強ノイズ4件は方式B済み、他は未B）
2. 対象: d1/d2/D1/D2 計 12 件（small 12 + large 0）。 wall 内 ch<300 を捨て、ch>=300 を `1/f` 倍
3. f_large (D1/D2) = 0.769000（D1 熱中性子 30cm/80cm 平均）
4. f_small (d1/d2) = 0.769000（d1 熱中性子 30cm/80cm 平均）
5. 除外: 熱中性子・gain・D1 PF・`_error`
6. wall 窓の定義（191–764 keV）自体は変えない

## 図の見方

→ `denoised_runs/small_d_cut300/figures/地点別/README.md`
→ 時系列: `figures/地点別_denoised/`

## 出力場所

- MCA: `denoised_runs/small_d_cut300/raw/`
- 地点別スペクトル: `denoised_runs/small_d_cut300/figures/地点別/<stem>/`
- fig16–19: `denoised_runs/small_d_cut300/figures/地点別/theory_16_19/`
- 再集計表: `denoised_runs/small_d_cut300/tables/`

## 対象ファイル

| ファイル | 族 | wall | N_full | N>=300 | part/full | f | cps前 | cps後 |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `d1_20260819_1520_管理棟2階.mca` | small_d | 97-408 | 15554 | 12022 | 0.773 | 0.7690 | 0.202457 | 0.203589 |
| `d1_20260823_1509_Linac3.mca` | small_d | 98-409 | 793 | 421 | 0.531 | 0.7690 | 0.0340544 | 0.0235761 |
| `d1_20260823_1509_PS.mca` | small_d | 98-409 | 2470 | 969 | 0.392 | 0.7690 | 0.0321227 | 0.0164385 |
| `d1_20260823_1509_linac_testhole.mca` | small_d | 97-408 | 7528 | 1650 | 0.219 | 0.7690 | 0.396783 | 0.113374 |
| `d1_20260825_1439_linac_testhole.mca` | small_d | 97-408 | 12512 | 3386 | 0.271 | 0.7690 | 0.659478 | 0.232441 |
| `d2_20260819_1859_放射線棟BT.mca` | small_d | 97-408 | 187 | 137 | 0.733 | 0.7690 | 0.0196007 | 0.0185525 |
| `d2_20260820_1939_KEKB.mca` | small_d | 98-411 | 486 | 279 | 0.574 | 0.7690 | 0.0124494 | 0.00922181 |
| `d2_20260821_080725_linac.mca` | small_d | 97-408 | 4791 | 982 | 0.205 | 0.7690 | 0.114352 | 0.0306943 |
| `d2_20260821_170219_linacIRON.mca` | small_d | 97-408 | 2291 | 1702 | 0.743 | 0.7690 | 0.0761463 | 0.0738197 |
| `d2_20260822_115232_PF.mca` | small_d | 99-412 | 21720 | 6573 | 0.303 | 0.7690 | 0.353928 | 0.13929 |
| `d2_20260822_155046_地上.mca` | small_d | 96-408 | 2175 | 1012 | 0.465 | 0.7690 | 0.17968 | 0.109626 |
| `d2_20260823_0834_Linac3.mca` | small_d | 96-408 | 1134 | 509 | 0.449 | 0.7690 | 0.0220714 | 0.0128847 |

## 本解析への反映

```bash
python3 03_今年度用/build_denoised_review.py --run-id small_d_cut300 --merge
```

- 対象ファイルは `raw_pre_partial_corr/small_d_cut300/` に退避してから `raw/` を置換
- tables / figures / theory を再計算
