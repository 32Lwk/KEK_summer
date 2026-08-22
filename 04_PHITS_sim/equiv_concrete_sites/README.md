# 各地点・等価コンクリート層 PHITS シミュレーション

図11と同じ遮蔽層厚で、宇宙線中性子 + **He-3/SUS304 検出器**の応答を
[Web PHITS](https://phits.kek.jp/web/cli.html) 上で計算し、地上比を測定・理論と比較する。

## 方針

| 項目 | 内容 |
|------|------|
| 線源 | `e-type=25`, `icenv=5`, `proj=neutron`, KEK つくば |
| 遮蔽 | 同心球殻（コンクリート ± ローム ± 常総、図11層厚） |
| 検出器 | 既存 [`he3_sus304`](../he3_sus304/he3_sus304.inp) と同寸法・同組成を中心に配置 |
|  | He-3 ガス R=2.54 cm, L=39.53 cm, ρ=0.00124 g/cm³ |
|  | SUS304 外壁 R=2.74 cm, L=39.93 cm, ρ=8.0 g/cm³ |
| タリー | `T-Deposit` → `de.out`（波高＝検出器応答） |
|  | He-3 内 `T-Track` → `neutron_he3.out` |
| 比較 | 測定 CPS / 理論 / Deposit 相対 / He-3 内フラックス相対 |

**解釈メモ**

- He-3 は熱中性子に高感度。コンクリート背後でスペクトルが軟化すると、**Deposit が地上より増える**ことがある（熱化効果）。減衰トレンドの比較には **He-3 内フラックス相対**の方が安定。
- BT / KEKB は検出器体積が小さく、現行ヒストリでは Deposit・フラックスとも統計ゼロ（上限）。

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
RUNNER=../../phits-agent-kit/phits_web_run.py
SRC=../source.inp

cd 00_ground && python3 "$RUNNER" main.inp "$SRC" --version phits336 --new-session
# 同様に 01_PF … 04_KEKB

python3 summarize_relative.py
python3 plot_3d_sites.py
```

## 成果物

- 各地点: `de.out`, `neutron_he3.out`, `phits.out`, `figures/3d_*.{html,png}`
- [`tables/PHITS_等価コンクリート_相対.csv`](../../03_今年度用/測定_20260818/tables/PHITS_等価コンクリート_相対.csv)
- [`figures/15_PHITS_等価コンクリート_比較.png`](../../03_今年度用/測定_20260818/figures/15_PHITS_等価コンクリート_比較.png)
- [`figures/index.html`](figures/index.html) — 3D 一覧
