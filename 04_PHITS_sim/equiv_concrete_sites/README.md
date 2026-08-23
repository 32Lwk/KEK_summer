# 各地点・等価コンクリート層 PHITS シミュレーション

図11と同じ遮蔽層厚で、宇宙線中性子 + **He-3 比例計数管（信管付き）**の応答を
[Web PHITS](https://phits.kek.jp/web/cli.html) 上で計算し、地上比を測定・理論と比較する。

## 検出器 4 種（測定ファイル名規則と同じ）

| キー | サイズ | PE 緩衝 | 系列 | 出力フォルダ | 成果物タグ |
|------|--------|---------|------|--------------|-----------|
| **d1** | 小径 | なし | SN 2162 系 | `small/d1/` | `small_d1` |
| **d2** | 小径 | 薄肉筒 5 cm | SN 2162 系 | `small/d2/` | `small_d2` |
| **D1** | 大径 | なし | SN 1715 系 | `large/D1/` | `large_D1` |
| **D2** | 大径 | PE 容器 | SN 1715 系 | `large/D2/` | `large_D2` |

- **小文字 d** = 小径、**大文字 D** = 大径
- **末尾 1** = PE なし、**末尾 2** = PE あり
- macOS 大文字小文字非区別対策で `small/` と `large/` に分離
- CSV/図ファイル名も `small_d1` / `large_D1` と区別（`_d1` だけだと上書きされる）

### 寸法（`detector_specs.py`）

| 項目 | 小径 d | 大径 D |
|------|--------|--------|
| 高さ | 39.5 cm | 66 cm |
| 外径 (SUS) | 5.5 cm | 10 cm |
| SUS 肉厚 | 2 mm | 2 mm |
| 信管 (R580 級) | r=1.25 cm, L=8.5 cm | r=1.9 cm, L=10 cm |
| 有効 He-3 | 信管除く ~31 cm | 信管除く ~56 cm |
| He-3 内部圧 | 10 atm（ρ = 0.0124 g/cm³） | 同左 |
| d2 PE | SUS 外 +5 cm 筒 | — |
| D2 PE 容器 | — | OD29 / ID15 / H80 / 内高74 cm |

## 方針

| 項目 | 内容 |
|------|------|
| 線源 | 天井上方 `s-type=2`, `dir=-1`, `e-type=25`, `icenv=5`（地上 c11=30 cm、遮蔽 c11=10 cm） |
| 遮蔽 | 水平天井スラブ（z=0 床、上向き）、室内は空気 |
| 地上 | 信管分割なし（802 lost 回避） |
| 遮蔽の Deposit | PE なし検出器は熱化用 PE 筒 +25 cm を自動付与。He-3 密度 ×100（相対比は ÷100）。足りなければ `accumulate_runs.py` |
| 比較 | 測定 CPS / 理論 / He-3 Deposit 相対 / フラックス相対 |

### Deposit スペクトルが空になる場合

105 cm 級コンクリート下で **PE なし He-3** は熱中性子がほぼ到達せず、`de.out` / `de.pdf` が全ビン 0 になります（バグではなく物理）。
対策は `build_ceiling_main.py` の熱化用 PE 筒と、必要なら:

```bash
python3 accumulate_runs.py small/d1/01_PF -n 8
```

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
- `tables/PHITS_等価コンクリート_相対_{small_d1,large_D1,...}.csv`
- `figures/15_PHITS_等価コンクリート_比較_{tag}.png`

仕様の詳細は [`detector_specs.py`](detector_specs.py)。
