# denoised 確認用成果物（ch≥300 割合補正）

本解析（`tables/`・`figures/`）は**未変更**（`--merge` するまで）。

## 方式

1. 入力: 方式 B（側帯フロア引き）済みの `raw/`
2. 対象 4 件のみ: wall 窓内で ch<300 を捨て、ch>=300 を `1/f` 倍
3. f = 0.769（指定）。熱中性子 d1 30/80cm 再計算平均 = 0.774771
4. wall 窓の定義（191–764 keV）自体は変えない

## 図の見方

→ `figures/地点別_denoised/README.md`

## 出力場所

- MCA: `raw_denoised/`
- 地点別スペクトル: `figures/地点別_denoised/<stem>/`
- fig16–19: `figures/地点別_denoised/theory_16_19/`
- 再集計表: `denoised_review/tables/`

## 対象ファイル

| ファイル | wall | N_full | N>=300 | part/full | cps前 | cps後 |
|---|---|---:|---:|---:|---:|---:|
| `d1_20260823_1509_linac_testhole.mca` | 97-408 | 7528 | 1650 | 0.219 | 0.396783 | 0.113374 |
| `d2_20260821_080725_linac.mca` | 97-408 | 4791 | 982 | 0.205 | 0.114352 | 0.0306943 |
| `d1_20260823_1509_PS.mca` | 98-409 | 2470 | 969 | 0.392 | 0.0321227 | 0.0164385 |
| `d2_20260822_155046_地上.mca` | 96-408 | 2175 | 1012 | 0.465 | 0.17968 | 0.109626 |

## 本解析への反映

```bash
python3 03_今年度用/build_denoised_review.py --merge
```

- 現在の `raw/`（方式B済み）4件は `raw_pre_partial_corr/` に退避
- `raw_denoised/` の補正 MCA を `raw/` に同名配置
- tables / figures / theory を再計算
