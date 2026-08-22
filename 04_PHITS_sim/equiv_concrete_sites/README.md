# 各地点・等価コンクリート層 PHITS シミュレーション

図11と同じ遮蔽層厚で、宇宙線中性子 + **He-3 比例計数管（信管付き）**の応答を
[Web PHITS](https://phits.kek.jp/web/cli.html) 上で計算し、地上比を測定・理論と比較する。

## 検出器 4 種（測定ファイル名規則と同じ）

| キー | サイズ | PE 緩衝 | 系列 | 出力フォルダ |
|------|--------|---------|------|--------------|
| **d1** | 小径 | なし | SN 2162 系 | `small/d1/` |
| **d2** | 小径 | 5 cm | SN 2162 系 | `small/d2/` |
| **D1** | 大径 | なし | SN 1715 系 | `large/D1/` |
| **D2** | 大径 | 5 cm | SN 1715 系 | `large/D2/` |

- **小文字 d** = 小径、**大文字 D** = 大径（混同しない）
- **末尾 1** = PE なし、**末尾 2** = PE あり

`small/` と `large/` に分けているのは、macOS 等で `d1` と `D1` が同一フォルダ扱いになるのを避けるためです。

### 寸法（推定）

| 項目 | 小径 d | 大径 D |
|------|--------|--------|
| 高さ | 39.5 cm | 66 cm |
| 外径 | ~5.5 cm | 10 cm |
| SUS 肉厚 | 2 mm | 2 mm |
| 信管（上端） | ~8.5 cm | 14 cm |
| 有効 He-3 | 信管除く | 信管除く |
| タリー | cell 1 = 有効 He-3 のみ | 同左 |

## 方針

| 項目 | 内容 |
|------|------|
| 線源 | 天井上方 `s-type=2`, `dir=-1`, `e-type=25`, `icenv=5`（c11=30 cm） |
| 遮蔽 | 水平天井スラブ（z=0 床、上向き） |
| 比較 | 測定 CPS / 理論 / He-3 Deposit 相対 / フラックス相対 |

## 地点

| フォルダ | 地点 | コンクリート | 土 |
|----------|------|--------------|-----|
| `00_ground` | 地上 | 0 | 0 |
| `01_PF` | PF | 105 cm | 0 |
| `02_linac` | linac | 150 cm | 0 |
| `03_BT` | BT | 60 cm | ローム 220 cm |
| `04_KEKB` | KEKB | 80 cm | ローム 400 + 常総 270 cm |

## 実行方法

```bash
python3 build_ceiling_main.py                    # 4 検出器すべて生成
python3 build_ceiling_main.py --detector D1      # 1 種類だけ

./run_all_phits.sh                               # 全検出器・全地点

RUNNER=../../phits-agent-kit/phits_web_run.py
cd large/D1/00_ground
python3 "$RUNNER" main.inp ../../source_ceiling.inp --version phits336 --new-session

python3 summarize_relative.py --detector d1
python3 plot_3d_sites.py --detector D2
```

## 成果物

- `small/d1/`, `small/d2/`, `large/D1/`, `large/D2/` 配下に各地点の `main.inp`, `de.out`
- `tables/PHITS_等価コンクリート_相対_<検出器>.csv`
- `figures/15_PHITS_等価コンクリート_比較_<検出器>.png`

仕様の詳細は [`detector_specs.py`](detector_specs.py)。
