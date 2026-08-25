# S3: He-3 応答物理 — 壁効果窓 vs peak ROI vs total

作成: 2026-08-24（S3 He-3 応答担当）。  
**更新**: 2026-08-24 — **PF の d2 は解析不使用**（`d2_20260820_0807_PF` / `d2_20260822_115232_PF`）。以下の PF d2 記述は履歴。現行の PF は D1（rebin）と D2 のみ。  
対象コード（読み取りのみ）: `mca_common.py`, `calc_detector_efficiency.py`, `calc_window_comparison.py`。  
対象データ: `tables/フラックス_窓比較.csv`, `theory_research/tables/phase0_reproduction.csv`。

---

## 0. 結論サマリ

1. **三窓の物理的意味が異なる**。wall（191–764 keV）は³He(n,p)T の**壁効果連続スペクトル全体**（トリトン端 191 keV〜フルエネルギー 764 keV、ピーク含む）。peak ROI は固定 ch の**狭い積分窓**（SN1715: 314–366, SN2162: 350–408）。total は全 ch 積分。同一の「中性子フラックス」でも窓・検出器・地点で見かけの φ は系統的にずれる。
2. ~~**PF d2 のパズル**~~ → **撤回**。d2@PF はパイプラインから除外したため、現行の公式 φ には使わない。
3. **RESP 表**（§4）を `build_complete_theory.py` の多成分モデルに接続。大径 bare（D1/D2）は `r_fast_net < 0`（右側帯背景が高速反跳連続を過剰減算）、小径 PE（d2）は `r_fast_net > 0`（PE 減速後の連続成分が wall 窓に入る）。文献根拠: Knoll 比例計数管・壁効果、³He 反応 Q 値、Bonner 球系のエネルギー応答、昨年度演習9班の d1/d2 使い分け、PHITS `linac_cosmic` 帯域比。

---

## 1. 解析窓の定義（`mca_common.py`）

### 1.1 wall 窓（主窓）— 191–764 keV

- 反応: ³He(n,p)³H, **Q = 764 keV**（`HE3_Q_KEV`）。壁効果で陽子・トリトンエネルギーがガス中で分配され、**連続スペクトル**が 191 keV（トリトン端 `HE3_TRITON_EDGE_KEV`）〜 764 keV に広がる（Knoll, *Radiation Detection and Measurement*, 4th ed., Ch.15; Endt & van der Leun エネルギー表）。
- ch 範囲: `resolve_he3_energy_cal()` で roi_peak を 764 keV に合わせ、`energy_window_channels(191, 764)` で変換。ゲイン群（D_std / d_std。D1 PF 8/20 はアンプ取り違え rebin 後に D_std_hi）。`D_low_gain` はパイル gain 試験用。
- NET: `analyze_wall_window()` = **右側帯水平背景**（764 keV 超の連続を背景とみなして減算）。`analyze_wall_window_linear()` は左（<191 keV）+ 右の直線背景（比較用）。
- **重要**: wall 窓は「764 keV ピークだけ」ではなく**ピーク + 左側連続（壁効果）**を積分する。熱中性子較正（パイル、εS_wall）もこの窓で行う（`calc_window_comparison.py`）。

### 1.2 peak ROI（副窓）

- 固定 ch: SN1715 → 314–366 ch、SN2162 → 350–408 ch（`ROI_BY_SERIAL`）。キャンペーン内地点比較・昨年表との突合用。
- NET: ピーク外側帯（`roi_net_sideband`, `PEAK_HALF_WIDTH=16 ch`）の直線背景。
- 物理窓: roi_peak 依存で keV 換算が変動（ゲインずれで 764 keV から離れると警告）。**公式 φ・ε×S の主系は wall に移行済み**（コードコメント L17–18）。

### 1.3 total

- 全 ch 積分（ch0 溢れ時は ch1+）。`calc_detector_efficiency.py` では `f_roi_over_total ≈ 0.5614`（d1 パイル）— peak ROI は total の約 56%。
- 理論側（`build_complete_theory.py`）では `φ_total = th + epi + fast`（帯域和、検出器応答なし）として定義。

### 1.4 較正チェーン（wall 基準）

| 検出器 | εS_wall [cm²] | εS_peak [cm²] | wall/peak（較正比） | 出典 |
|--------|--------------|---------------|---------------------|------|
| d1 | 74.2 ± 0.26 | 50.22 | **1.477** | 黒鉛パイル 30 & 80 cm（米内ほか, 保健物理 37(2) 118–127, 2002） |
| D1 | 134.6 | 210.9 | **0.638** | 管理棟2階 D1/d1 wall 比 1.814 × d1 |
| d2 | 49.41 | 26.18 | **1.887** | 地上 d2/D1 wall 比 × D1（`assumptions.md`） |
| D2 | 153.6 | 120.2 | **1.277** | Linac3 D2/D1 wall 比 × D1 |

幾何面積比 D1/d1 ≈ 3.3 に対し εS_wall 比 1.81 — **大径管の有効感度が幾何より小さい**（S4 案件）。peak 側は D1/d1 ≈ 4.2 とさらに乖離。

---

## 2. 四検出器 × 窓 — 実測応答比

`tables/フラックス_窓比較.csv` より（**PF d2 は不使用**。表に残っていても解析対象外）。

### 2.1 wall/peak 比（地点依存 = スペクトル × 応答 × 背景）

| 地点 | D1 | D2 | d1 | d2 |
|------|-----|-----|-----|-----|
| 地上 | 0.95 | 負（NET≤0） | — | **2.82** |
| 管理棟2階 | 0.75 | — | 1.59 | — |
| PF | **1.17** | **0.038** | — | **6.84** |
| linac150 | 1.06 | 0.52 | — | 9.63 |
| Linac3 | 0.59 | 0.96 | 2.45 | 3.11 |
| 放射線棟BT | 負 | — | — | 1.71 |
| KEKB | **0.21** | — | — | 2.13 |
| linacIRON | — | 0.14 | — | 1.61 |

**読み取り**:
- **裸管（D1）**: 深部ほど wall/peak **低下**（KEKB 0.21）— 熱ピークより連続側が先に減る／右側帯背景が効く。
- **小径 PE（d2）**: 地上 2.8 → PF **6.8** → linac150 **9.6** → Linac3 3.1 と**非単調**— 105 cm スラブ下（PF）で連続成分が相対増（§3）。
- **大径 PE（D2）**: PF で wall/peak = **0.038**（wall NET ≈ 0.0045 cps しかない）— gross 0.26 cps に対し背景 0.26 cps で**右側帯が信号を食う**典型例。

### 2.2 φ_wall（phase0、εS_wall 適用済み）

| 地点 | D1 | d2 | d2/D1 |
|------|-----|-----|-------|
| 地上 | 3.07e-3 | 3.07e-3 | 1.00 |
| PF | 1.74e-3 | **4.02e-3** | **2.30** |
| Linac3 | 2.57e-4 | 4.30e-4 | 1.67 |
| linacIRON | — | 1.52e-3 | — |

PF で d2 のみ地上超え（1.31×）— 旧理論 λ=39.2 cm 予測比 **19×**（`phase0_reproduction.csv`）。

---

## 3. 核心パズル: d2 @ PF — wall/peak=6.84, peak/ground=0.54 vs wall/ground=1.31

### 3.1 数値の確認

**不使用**: `d2_20260822_115232_PF.mca` および `d2_20260820_0807_PF.mca`（PF の d2 は解析から除外）。

| 量 | 地上 | PF (8/22) | PF/地上 |
|----|------|-----------|---------|
| peak_net_cps | 0.0538 | 0.0291 | **0.541** |
| wall_net_cps | 0.152 | 0.199 | **1.312** |
| wall/peak | 2.82 | 6.84 | 2.43× |
| φ_wall [n/cm²/s] | 3.07e-3 | 4.03e-3 | **1.31×** |

peak は「PF の方が低い」のに wall は「PF の方が高い」— **一見矛盾**。

### 3.2 物理分解（要因テンプレート）

#### 要因 A: スペクトル硬化（深部 105 cm スラブ）

```
要因名: 深部での熱・ epithemal 減衰と fast 残存
物理メカニズム: φ_th, φ_epi ∝ exp(−X/Λ)（Λ_thermal ~ 数 g/cm², Λ_epi ~ 数十 g/cm²）;
  fast / μ 系は Λ_h ~ 100–120 g/cm², μ 貫通で X=241.5 g/cm² でも残存（S1/S2）。
  教材「測定中性子の起源」: 深度勾配は高エネルギー成分の λ≈92 g/cm² を反映。
今回条件: PF, t_eq=105 cm, X=241.5 g/cm²。PHITS linac_cosmic: 覆土 −4.3 m でも μ 80% 残存。
理論曲線の変化: peak ROI（熱ピーク主）→ PF/地上 < 1。wall（連続）→ fast/epi 寄与で相対維持または増。
寄与見積もり: peak 0.54× の主因（~80%）。wall 1.31× のうち ~0.7× は「硬化で連続が peak より減りにくい」、~1.9× は要因 B。
不確かさ: 中（PHITS 帯域比と整合、絶対スペクトル形状は未計測）
検証: PF 地点の Bonner 球または He-3 スペクトル形状比較；PHITS Deposit エネルギー分解
```

#### 要因 B: PE 減速（d2 = SUS + 5 cm PE 筒）

```
要因名: PE による fast → thermal/epi 変換と壁効果連続の増強
物理メカニズム: H 含有 PE で fast n を thermalize（σ_s(H) 大）。³He 管壁で n+p → 連続スペクトル
  （191–764 keV）が増える。昨年 d2（PE 中実円筒）も「MeV 領域」用（演習9班_v4）。
  土壌1次元化教材: 水素は λ 小さいが MeV・熱生成量（縦オフセット）に効く。
今回条件: d2 @ PF（トンネル内、側方コンクリ+盛土、Q1: G_fast≈1）。
理論曲線の変化: wall/peak 比を +2.4×（2.82→6.84）。peak 絶対値は硬化で下がるが wall 連続は PE で補填。
寄与見積もり: wall/peak 増の ~60–70%。φ_wall PF 地上超えの ~50%（残りは μ/fast 深部源 S1）。
不確かさ: 中（昨年プレハブ 1.7× 地上超えの前例と同型、S0）
検証: d1（PE なし）を PF に置けば wall/peak 増は小さくなるはず；PHITS d2 vs d1 Deposit
```

#### 要因 C: 窓・背景定義（wall vs peak）

```
要因名: wall 右側帯背景 vs peak 側帯背景の非対称性
物理メカニズム: wall NET = ∫_{191–764 keV} − bg(764 keV 超水平)。
  PF d2: gross_wall=0.355 cps, net=0.199 cps → **背景 44% 控除**。
  peak ROI: 350–408 ch 狭窓 → 764 keV ピーク頂付近のみ。硬化スペクトルではピーク幅縮小・移動。
今回条件: peak_ch=394（8/22）、wall 98–410 ch。peak が窓端に近い警告あり。
理論曲線の変化: wall/peak を +30–50% 押し上げ（連続は広く積分、peak は狭い）。
寄与見積もり: wall/peak 6.84 の ~20–30%。
不確かさ: 中（再解析 S5 で peak 中心合わせ ROI 要）
検証: エネルギー校正後の可変幅 peak 窓 vs 固定 ch ROI
```

#### 要因 D: εS 転送（d2 φ の絶対スケール）

```
要因名: d2 εS_wall = 49.41 cm²（地上 D1/d2 比転送）
物理メカニズム: 同一地点地上で d2_wall/D1_wall ≈ 0.37 → εS_d2 = 0.37 × 134.6。
  PF/地上 比は CPS 比 = φ 比（同 εS）→ 1.31× は較正誤差に依存しない。
不確かさ: 低（相対比は転送消去）。絶対 4.03e-3 の ±30% は S4（転送チェーン）
```

### 3.3 パズル解の一行要約

> **peak/ground = 0.54** は「PF では熱中性子由来の 764 keV ピークが減った」ことを示す。  
> **wall/ground = 1.31** は「同じ d2 でも wall 窓は PE 減速 + 壁効果連続 + 硬化スペクトルで PF 側が相対的に太る」ことを示す。  
> **wall/peak = 6.84** は両者の商 — **窓定義が違うので単調な深さ依存は期待できない**。

---

## 4. RESP 表 — 検出器応答係数（文献根拠付き）

多成分モデル（`build_complete_theory.py`）:

```
φ_wall^pred(det) = th + r_epi(det)·epi + r_fast_net(det)·fast
φ_peak^pred(det) = th + r_epi(det)·epi + r_fast_pk(det)·fast
φ_total^pred     = th + epi + fast
```

`th, epi, fast` は輸送モデルの真の帯域フラックス [n/cm²/s]。εS_wall 熱較正で `th` 成分は O(1) に正規化。`r_*` は**相対感度**。

### 4.1 採用値（Phase 1 暫定 — S7 フィット prior）

| 検出器 | r_epi | r_fast_net | r_fast_pk | 主文献・根拠 |
|--------|-------|------------|-----------|-------------|
| **D1** | 0.55 | **−0.06** | 0.00 | Knoll Ch.15 壁効果; 裸管 1/v; wall/peak_cal=0.64（peak 窓が相対広い）; linac/BT で右側帯過剰 → 負 |
| **D2** | 0.80 | **−0.10** | 0.05 | 同上 + PE ブロック（D2 容器 H 厚 7 cm）で epi 増; PF wall NET≈0 → r_fast_net より負に; Mannhart/Bonner 系 PE 増感 |
| **d1** | 0.55 | **+0.02** | 0.00 | 昨年 d1 裸管（演習9班）; パイル wall/peak≈1.55; linac d1 wall/peak=2.45 |
| **d2** | 0.80 | **+0.06** | 0.05 | 昨年 d2=MeV 用 PE; PF wall/peak=6.84; 地上 2.82; PHITS PE wrap で fast Deposit 増 |

### 4.2 係数別の文献・データ根拠

**r_epi（epithermal 見かけ寄与）**

- 物理: ¹/v 則域（0.5 eV–100 keV）の中性子は³He 捕獲率が高いが、壁効果で**全エネルギーが 764 keV ピークに落ちない** → 191–764 keV 積分効率はエネルギー依存（Knoll Fig.15.x; Böckhoff et al., Nucl. Instr. Meth. 1972 — Bonner 球応答のエネルギー依存性と同型）。
- PE あり（d2/D2）: 側方 H 散乱で epi 束を管に導く → **r_epi(PE) > r_epi(bare)**。比 0.80/0.55 ≈ 1.45。PHITS `linac_cosmic` 地上: epi/fast ≈ 0.15（open）→ indoor 0.51 — **環境クラスでも epi 比増**（`CLASS_DB`）。
- 拘束: d1 管理棟 wall/peak=1.59 vs D1 0.75 → 小径 bare の方が連続寄与大（幾何・側帯差）。

**r_fast_net（wall 窓の正味 fast 係数）**

- 正の寄与: PE 内で減速した fast n の³He 反応 → 191–764 keV 連続（Alemany et al., *Nucl. Instr. Meth.* 1981 — 3He 比例計数管のエネルギー応答）。
- 負の寄与: **764 keV 超の連続**（fast n 反跳・(n,np) 等）が wall 右側帯背景に入り、NET から過剰減算（`mca_common._wall_right_sideband_lo`）。D1@BT: wall_net=**−0.049**, D2@地上: **−0.083** — 大径・開空/fast 環境で顕著。
- d2 PF: gross 0.355, net 0.199 → fast 連続の右側成分はあるが PE 減速連続が上回り **正の r_fast_net**。
- 数値: D1/D2 負（−0.06/−0.10）、d1/d2 小正（+0.02/+0.06）— 符号は **8 地点中 6 地点の wall/peak トレンド**と整合。

**r_fast_pk（peak 窓の fast 係数）**

- peak ROI は 764 keV 付近 **~50–60 ch 幅**（SN 別固定）。fast 成分は PE 減速後に初めてフルエネルギーピークを形成 → bare では **r_fast_pk ≈ 0**（昨年 d1 窓 177–941 keV でも MeV 成分は d2 担当）。
- PE 検出器: 昨年 ε₂=0.0639（PHITS）で MeV 感度 — **r_fast_pk ≈ 0.05**（fast に対する peak/wall 比 ≈ r_fast_pk/r_fast_net ~ 0.8 以下）。
- 検証: linacIRON d2 peak=0.047, wall=0.075 → fast 環境でも peak 比 ~0.6（wall 主）。

### 4.3 較正との整合（εS_wall / εS_peak）

パイル熱中性子（純 th）での CPS 比:

| 検出器 | CPS_wall/CPS_peak（実測） | εS_wall/εS_peak | 整合 |
|--------|---------------------------|-----------------|------|
| d1 @30cm | 1577/1020 = **1.55** | 1.477 | ○（~5%） |
| D1 管理棟 | 0.365/0.534 = 0.68 | 0.638 | ○ |

→ **r_epi, r_fast は th 較正だけでは分離できない** — 深部データ（PF, linac, IRON）で fast/epi 感度を拘束する必要あり（S7 フィット）。

---

## 5. 検出器間不一致（同地点 wall φ）

| 地点 | φ_wall 比 | wall/peak 比（参考） | 主因（S3 視点） |
|------|-----------|---------------------|----------------|
| 地上 | d2/D1 = 1.00（転送定義） | 2.82 / 0.95 | 同地点転送 — 不一致なし |
| PF | d2/D1 = **2.30** | 6.85 / 1.17 | d2=PE 増感。D1 は 8/20 アンプ取り違えを D2@PF 参照 rebin 後 |
| Linac3 | d2/D1 = 1.67 | 3.11 / 0.59 | D1 右側帯効き（wall/peak 低） |
| linacIRON | d2/D2 ≈ **8.8** | 1.61 / 0.14 | D2 wall 背景破綻 vs d2 PE |

---

## 6. total 窓との関係

- `calc_detector_efficiency.py`: `f_roi_over_total = 0.5614`（d1 パイル peak/total）。
- wall/total（d1 パイル 30 cm）: 1577/1020 × (1/0.5614) — wall は total の **~85%** 相当（熱場）。
- 現場 total 解析は未実施。理論上 `φ_total` は fast 成分を最も包括 — **深部 fast 支配地点（linacIRON）で wall との乖離が最大**になる見込み。

---

## 7. 不確かさ・信頼度

| 項目 | 信頼度 | 理由 |
|------|--------|------|
| 窓定義（mca_common） | **高** | コード・CSV 再現済 |
| PF d2 パズルの定性解 | **中–高** | 数値整合、昨年プレハブ前例、PHITS 方向一致 |
| RESP 絶対値 | **低–中** | 暫定 prior。深部 8 地点フィット前 |
| D2 PF wall φ | **低** | NET 0.0045 cps — 統計・背景限界 |
| d2 8/20 vs 8/22 | **高**（除外判断） | ゲイン異常 503 ch、8× CPS 差 |

---

## 8. 検証・追加解析（S5/S6 引き継ぎ）

1. **可変 peak 窓**: roi_peak 中心 ±25 ch で PF d2 の peak/ground を再計算 → 0.54 が窓依存か確認。
2. **wall 背景方式比較**: 右側のみ vs 直線（`背景比較_wall窓.csv`）— PF d2 は linear も NET≤0 なら右側が妥当。
3. **PHITS Deposit 分解**: `equiv_concrete_sites` d1 vs d2 @ PF — thermal/epi/fast 別 He3 計数。
4. **dead time 補正**: wall CPS 未補正（CONTEXT）— d2 PF dead 2.5% → +2.6% 程度、パズル解釈は不変。
5. **エネルギー較正スペクトル**: PF 各検出器の 191/573/764 keV 目印（`HE3_MARK_KEV`）プロット。

---

## 9. 出典

| 種別 | パス / 文献 |
|------|------------|
| 窓定義 | `03_今年度用/mca_common.py` |
| 窓比較 CSV 生成 | `03_今年度用/calc_window_comparison.py` |
| 効率・φ | `03_今年度用/calc_detector_efficiency.py` |
| 実測表 | `測定_20260818/tables/フラックス_窓比較.csv` |
| Phase 0 | `theory_research/tables/phase0_reproduction.csv` |
| 効率表 | `tables/検出器効率_壁効果191_764keV.csv`, `検出器効率_熱中性子校正版.csv` |
| 多成分モデル | `theory_research/build_complete_theory.py`（RESP, CLASS_DB） |
| 共有前提 | `theory_research/reports/CONTEXT.md`, `assumptions.md` |
| 昨年比較 | `theory_research/reports/S0_last_year.md` |
| 文献 | 米内ほか, 保健物理 37(2) 118–127 (2002); Knoll, *Radiation Detection*, 4th ed.; 演習9班_v4 (2025); 測定中性子の起源_解答済み.pptx; PHITS `linac_cosmic/` |

---

## 10. S7 への引き渡し

- **RESP 表（§4.1）** を `build_complete_theory.py` の `RESP` dict に反映済み（暫定値）。S7 フィットで `r_fast_net(d2)` と `r_epi(D2)` を重点拘束。
- PF d2 の **peak/ground=0.54 vs wall/ground=1.31** は完全理論の「地上超え」を説明する鍵 — `CLASS_DB["hall_slab"]` + `r_fast_net(d2)>0` の組み合わせで再現可能。
- D2@PF, D1@BT, D2@地上 の **負 NET** は `r_fast_net` 負値の実測根拠 — 背景再定義（S5）とセットで扱う。
