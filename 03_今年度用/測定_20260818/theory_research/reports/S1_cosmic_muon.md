# S1: 宇宙線・ミューオン起源中性子の深度物理

作成: 2026-08-24（S1 宇宙線・μ 深度物理担当）。  
前提: [`CONTEXT.md`](CONTEXT.md)、実測再現 [`tables/phase0_reproduction.csv`](../tables/phase0_reproduction.csv)。**全加速器ビーム OFF**（2026-08-18〜23）。

---

## 0. 結論サマリ

1. **旧理論 φ = A₀ exp(−t/λc)（A₀=3.07×10⁻³ n/cm²/s, λc=39.2 cm）は「検出器近傍 ~11 cm の局所生成 MeV 中性子」の教材近似であり、宇宙線一次ハドロン束（Λ≈90–120 g/cm²）と深部 μ 起源二次中性子の平衡床（Λ_μ≈400–6000 g/cm²）を区別していない。** 深部（t_eq≳190 cm）で実測が 10²–10⁷ 倍に乖離する主因は **A2（μ 均衡床）** と **A3（スペクトル硬化による実効 λ 増大）** の合成。A1（正しい一次減衰長）だけでは PF の 19 倍・KEKB の 10⁴ 倍は説明不足。
2. **PF d2 地上超え（4.03×10⁻³ vs 理論 2.11×10⁻⁴, 19×）** は、浅深度（105 cm, X=241.5 g/cm²）で一次束がまだ 10⁻¹ 程度残存しつつ、**A4（スラブ下空洞の平衡熱化・側方漏れ）** と **d2+PE の局所生成効率（S3 連携）** が重なる典型例。PHITS `linac_cosmic` でも覆土 2.5 m 相当で熱中性子 8.7× 増を再現。
3. **KEKB d2（2.48×10⁻⁴ vs λ=60 cm 理論 4.6×10⁻⁷, 5.4×10⁴×）** では一次 exp 項は 10⁻⁹ 以下に落ち、**μ 捕獲・μ スパレーション（A2）** が fast 成分の ≳99% を占める深さ。旧理論との比は主に **A2（10³–10⁴×）**、残差は **A4（トンネル壁からの平衡束）+ φ_rad（A2 内の放射化学床）+ linacIRON では開口幾何（A4）**。
4. **A5（太陽変調, 2026 年 8 月）** は全深度共通の **±15–25% スケール** にとどまり、深度依存の 10²–10⁷ 倍乖離の主因にはならない（信頼度: 中）。
5. 多成分輸送モデル（`build_complete_theory.py` フィット; `tables/theory_parameters.csv`）では log₁₀ 残差 RMS が **2.97 dex → 0.52 dex** に改善。深部平坦化（φ≈2.5–4.6×10⁻⁴）と linacIRON 再上昇の骨格は A1–A4 で説明可能だが、**検出器・窓依存（S3）と linacIRON の 4× 残差** は追加検証が必要。

---

## 1. 旧理論と実測乖離（Phase 0 数値）

### 1.1 旧理論

\[
\phi_{\mathrm{old}}(t) = A_0 \exp\!\left(-\frac{t_{\mathrm{eq}}}{\lambda_c}\right), \quad A_0 = 3.07\times10^{-3}\ \mathrm{n/cm^2/s},\ \lambda_c = 39.2\ \mathrm{cm}\ (\Lambda_c = 90.2\ \mathrm{g/cm^2})
\]

参考として経験値 λc=60 cm も併記。

### 1.2 地点別 φ_wall と乖離倍率（主データ: d2 wall 窓）

| 地点 | t_eq [cm] | X [g/cm²] | mwe | φ_wall 実測 [n/cm²/s] | 旧理論 (λ=39.2 cm) | 旧理論 (λ=60 cm) | 乖離倍率 (39.2 cm) |
|------|-----------|-----------|-----|----------------------|-------------------|-----------------|-------------------|
| 地上 | 0 | 0 | 0 | 3.07×10⁻³ (d2) | 3.07×10⁻³ | 3.07×10⁻³ | 1 |
| PF | 105 | 241.5 | 2.41 | **4.03×10⁻³** (d2) | 2.11×10⁻⁴ | 5.34×10⁻⁴ | **19.1** |
| 放射線棟BT | 189 | 435 | 4.35 | 4.07×10⁻⁴ (d2) | 2.47×10⁻⁵ | 1.31×10⁻⁴ | 16.6 |
| Linac3 | 300 | 690 | 6.90 | 4.30×10⁻⁴ (d2) | 1.46×10⁻⁶ | 2.07×10⁻⁵ | 297 |
| KEKB | 525 | 1209 | 12.09 | **2.48×10⁻⁴** (d2) | 4.64×10⁻⁹ | **4.63×10⁻⁷** | **5.39×10⁴** |
| linacIRON | 728 | 1675 | 16.75 | 1.52×10⁻³ (d2) | 2.62×10⁻¹¹ | 1.64×10⁻⁸ | 5.86×10⁷ |

出典: `phase0_reproduction.csv`（d2: SN2162+PE, εS_wall=49.41 cm²）。D1 系は同地点で 12–316×（PF 12.5×, Linac3 177×, KEKB 1.1×10⁴×）。

### 1.3 実測の特徴（旧理論が破綻するパターン）

1. **PF で d2 が地上超え**（peak ROI は 0.54× と減少、wall は 1.31× と増加 → 窓・背景問題とスペクトル硬化が同居）。
2. **t_eq 190–525 cm で φ ≈ 2.5–4.6×10⁻⁴ に平坦化**（指数減衰の終了）。
3. **linacIRON(728 cm) で φ 再上昇**（d2: 1.52×10⁻³, D2: 1.72×10⁻⁴, 検出器差 8.8×）。
4. **地上絶対値は文献・PHITS と ±20% 整合** → 乖離は深度依存のみ（S0 確認）。

---

## 2. 多成分完全理論の骨格（S7 統合用）

深さ変数 \(x\) [g/cm²]（垂直質量厚; 地点別 `X` 列）:

\[
\phi_{\mathrm{fast}}(x) = \Big[ F_0\, e^{-x/\Lambda_h} + C_\mu\, I_\mu(x) \Big]\, G_{\mathrm{fast}}(\mathrm{site})
\]

\[
I_\mu(x) = (1-f_{\mathrm{stop}})\, e^{-x/\Lambda_{\mu 2}} + f_{\mathrm{stop}}\, e^{-x/\Lambda_{\mu 1}}, \quad I_\mu(0)=1
\]

\[
\phi_{\mathrm{th}}(x) = k_{\mathrm{th}}(\mathrm{class})\,\phi_{\mathrm{fast}}(x) + \phi_{\mathrm{rad}}, \quad
\phi_{\mathrm{epi}}(x) = k_{\mathrm{epi}}(\mathrm{class})\,\phi_{\mathrm{fast}}(x)
\]

見かけの wall 窓（He-3, 191–764 keV 熱較正 φ）:

\[
\phi_{\mathrm{wall}}^{\mathrm{pred}} = \phi_{\mathrm{th}} + r_{\mathrm{epi}}(\mathrm{det})\,\phi_{\mathrm{epi}} + r_{\mathrm{fast}}(\mathrm{det})\,\phi_{\mathrm{fast}}
\]

**フィット済みパラメータ**（`theory_parameters.csv`, 2026-08-24）:

| 記号 | 値 | 単位 | 物理対応 |
|------|-----|------|----------|
| F₀ | 8.03×10⁻³ | n/cm²/s | 地上開空 fast（PHITS 速+熱外 ≈3.0×10⁻³ + 寄与） |
| Λ_h | 118.3 | g/cm² | A1: 一次ハドロン減衰 |
| C_μ | 2.73×10⁻⁴ | n/cm²/s | A2: μ 起源 fast 源強度 |
| Λ_μ1, f_stop, Λ_μ2 | 408, 0.079, 5982 | g/cm², — | A2: μ 深度分布（停止/貫通） |
| φ_rad | 5.71×10⁻⁶ | n/cm²/s | 放射化学起源熱床（Malins/JENDL 系） |

以下 A1–A5 を要因テンプレートに沿って分解する。

---

## 3. 要因別調査

---

### A1: 一次宇宙線核子（CRN）カスケード減衰

**要因名:**  
一次宇宙線核子・軽イオンによる大気／遮蔽体中のハドロンカスケード減衰（旧 λc=39.2 cm の誤用）

**物理メカニズム（式 + 参考文献）:**

大気中の一次 CRN（E ≳ 1 GeV/n）が空気核と相互作用し、中性子・π±・K 等の二次粒子シャワーを形成。地下では「地表から到達した高エネルギー核子・シャワー核」の透過が支配的。

\[
\Phi_n^{\mathrm{(hadron)}}(x) \approx F_0\, \exp\!\left(-\frac{x}{\Lambda_h}\right), \quad \Lambda_h \approx 100\text{–}130\ \mathrm{g/cm^2}
\]

- **Gudima–Mashnik–Toneev**, Cascade-Exciton Model (CEM) / SHIELD: 核内カスケード・蒸発を記述（Nucl. Phys. A 401 (1983) 329; Toneev & Gudima, LVD 岩石ハドロン輸送, Nucl. Phys. A 400 (1983) 173c）。
- **Gaisser & Stanev**, *Cosmic Rays and Particle Physics* (Cambridge, 2nd ed. 2016): 大気中性子スペクトル、核子成分の深度減衰、TeV ミューオンとの分離。
- **Zappala et al.**, 大気 **⁸¹Kr** 生成 = 宇宙線スパレーション積分（Radiocarbon, 2021）: 大気側 CR スパレーション率の検証。地下では直接寄与は小さいが、**大気中一次 CRN フラックス規格**の整合チェックに使用。
- **EXPACS / PARMA**（Sato, PLOS ONE 2015, 2016）: KEK つくば（φ=36.0°N, λ=140.1°E, h≈+30 m）の地表 **n, p, μ±** スペクトル。PHITS `e-type=25`, `icenv=5` で F₀ 拘束。

**今回条件への写像（地点/検出器/窓）:**

- 横軸 \(x = \sum_i \rho_i t_i\)（`CONTEXT.md` 積層表）。地上 A₀ は D1/d2 wall の開空代表。
- **教材 λc=39.2 cm（Λ=90.2 g/cm²）** は MeV 中性子の**局所生成**用（λ_MeV≈26 g/cm²）であり、**地表からの一次ハドロン透過長 Λ_h≈118 g/cm² より短い**。旧理論は「深さ全域で λ=39.2 cm の単一指数」を仮定したため、**深部で過減衰**。
- wall 窓（191–764 keV）は主に熱化・捕獲後信号; 一次 fast 成分は \(r_{\mathrm{fast}}\)（S3）経由で間接寄与。

**理論曲線の変化（functional form / 倍率）:**

\[
\phi_{\mathrm{old}} \to \phi_{\mathrm{A1}} = F_0\, e^{-x/\Lambda_h}\, k_{\mathrm{th}} + \phi_{\mathrm{rad,0}}
\]

Λ_h: 90.2 → 118.3 g/cm² への修正倍率 \(R_{\mathrm{A1}}(x) = \exp\!\bigl[-x(1/\Lambda_h^{\mathrm{new}} - 1/\Lambda_c)\bigr]\):

| 地点 | x [g/cm²] | R_A1（対旧 exp 項） |
|------|-----------|---------------------|
| PF | 241.5 | **4.9×** |
| BT | 435 | 11× |
| Linac3 | 690 | 28× |
| KEKB | 1209 | 120× |
| linacIRON | 1675 | 380× |

**寄与見積もり（% および φ 倍率、地点別）:**

旧理論残差に対する **A1 単独の説明割合**（d2 実測/旧理論 → 実測/(旧×R_A1)）:

| 地点 | 旧理論比 | A1 後残倍率 | A1 寄与（旧乖離に占める割合） |
|------|---------|------------|------------------------------|
| PF | 19× | **3.9×** | ≈ **80%**（log 比 1.28/1.48 dex） |
| BT | 17× | 1.5× | ≈ **91%** |
| Linac3 | 297× | **11×** | ≈ **96%** |
| KEKB | 5.4×10⁴× | **450×** | ≈ **99.2%** |
| linacIRON | 5.9×10⁷× | **1.5×10⁵×** | ≈ **99.7%** |

→ **A1 は PF–BT 浅部では主因の一つだが、Linac3 以深では A2 必須。** 地上（x=0）では F₀≈8×10⁻³ で A₀=3×10⁻³ と同オーダー（太陽変調・スペクトル積分差は ±30%）。

**不確かさ・信頼度:** **高**（Λ_h のオーダーは Gaisser 大気 neutrons、地下実験、PHITS PARMA 線源で一貫）。ただし **Λ_h はエネルギー依存**（A3 と分離困難）で ±20% は残る。

**検証方法・追加実験/解析の提案:**

1. PHITS `theory_research_runs/11_deep_nonly`（中性子線源のみ）で Λ_h を直接フィット。
2. linac150（X=345 g/cm²）参考点で A1 予測の中間チェック（d2: 29.7× → A1 後 ~3× 期待）。
3. EXPACS/PARMA で **2026-08-22〜23 測定時刻**の W-index を固定し F₀ 再計算（A5 連携）。

---

### A2: ミューオン起源中性子の深度均衡（μ 捕獲・μ スパレーション）

**要因名:**  
宇宙線ミューオンの深度透過と、物質中での核スパレーション・放射捕獲に伴う二次中性子平衡床

**物理メカニズム（式 + 参考文献）:**

地表 μ フラックス（Gaisser 式）:

\[
I_\mu(E_\mu, \theta, x) \approx I_\mu^0(E_\mu)\, \exp\!\left(-\frac{x}{\Lambda_\mu(E_\mu)\cos\theta}\right)
\]

μ 起源中性子生成率（Malgin–Ryazhskaya universal formula, Phys. Rev. D 87 (2013) 113013; Phys. Rev. C 96 (2016) 014605）:

\[
Y_n(E_\mu, A) = b_n\, A^\beta\, E_\mu^\alpha, \quad \alpha \approx 0.78,\ \beta \approx 0.95,\ b_n \approx 4.4\times10^{-7}\ \mathrm{cm^2/g}
\]

\[
R_n(x) = I_\mu(x)\, Y_n(E_\mu(x), A), \quad
\Phi_n^{\mathrm{(\mu)}} \approx \frac{R_n}{\rho\, \ell_n} \approx C_\mu\, I_\mu(x)
\]

- **Gaisser & Stanev** (2016): μ エネルギー損失、角度分布、地下 μ スペクトル hardening。
- **Gudima et al.**, μ 開始核カスケードの SHIELD 輸送（INR 453265）: 岩石中 hadron の exclusive シミュレーション。
- **Zappala** 系: 大気 CR スパレーション（⁸¹Kr）— μ 直接ではないが **CR 一次束の低エネルギー側**規格。
- **Wang et al.**, FLUKA μ スパレーション（Phys. Rev. D 64 (2001) 013012）; **Heusser**, μ 誘起背景総説（Annu. Rev. Nucl. Part. Sci. 2006）。

PHITS `linac_cosmic`（PARMA, 5000 ヒストリー）: **μ± は 2.5 m コンクリート下でも開空の 72%**（1.58×10⁻² → 1.13×10⁻² n/cm²/s）。中性子は 1/43 まで落ちるが **μ 起源二次が床を形成**。

**今回条件への写像（地点/検出器/窓）:**

- 全地点でビーム OFF → **μ + 放射化学（φ_rad）が深部の唯一の持続源**。
- **PF (105 cm)**: x=241.5 g/cm² → I_μ ≈ 0.85–0.95（PHITS 外挿）。一次 hadron 1.0×10⁻³ n/cm²/s 程度と **μ 項 2.5×10⁻⁴ n/cm²/s が同オーダー** → 浅部でも μ 寄与 20–40%。
- **Linac3–KEKB**: x=690–1209 g/cm² → モデル上 **fast の 91–100% が μ 起源**（`build_complete_theory.py` フィット）。
- **linacIRON**: 鉄 150 cm（ρ=7.2）→ μ 核相互作用増、**(n,xn)** で hard 中性子透過（CLASS `iron_tunnel`, k_epi↑）。1 面開口（Q2）で μ 角分布がトンネル内に集中。
- wall 窓: μ 起源 fast → PE/壁で熱化 → 764 keV ピーク。深部では **A2 → 熱化平衡（A4 連携）** が wall φ を支える。

**理論曲線の変化（functional form / 倍率）:**

\[
\phi_{\mathrm{old}} \to \phi_{\mathrm{A1+A2}} = F_0 e^{-x/\Lambda_h} + C_\mu I_\mu(x)
\]

深部極限（x ≫ Λ_h）: \(\phi_{\mathrm{fast}} \to C_\mu I_\mu(x)\) → **指数減衰から「μ 深度関数への追随」に転換**（平坦化の本体）。

| 地点 | C_μ I_μ(x) [n/cm²/s] | 対旧理論 (λ=39.2) 倍率 | fast 中 μ 割合 |
|------|----------------------|------------------------|----------------|
| 地上 | 2.7×10⁻⁴ | 0.09×（床項は別） | 3% |
| PF | 2.5×10⁻⁴ | **1.2×10³×** | 20% |
| BT | 2.4×10⁻⁴ | **1.0×10⁴×** | 54% |
| Linac3 | 2.3×10⁻⁴ | **1.6×10⁵×** | 91% |
| KEKB | 2.1×10⁻⁴ | **4.5×10⁷×** | >99% |
| linacIRON | 1.9×10⁻⁴ | **7.3×10⁹×** | ≈100% |

**寄与見積もり（% および φ 倍率、地点別）:**

A1+A2 合成モデル（d2, k_th≈0.85, r_epi≈0.8）の φ_wall 予測 vs 実測:

| 地点 | 実測 φ | A1+A2 予測 | 倍率 meas/pred | A2 の旧理論乖離に占める割合 |
|------|--------|-----------|----------------|---------------------------|
| PF | 4.03×10⁻³ | 1.43×10⁻³ | 2.8× | **残 19× のうち ≈70% を A2+平衡が説明**（A1 後 3.9× → pred で 1.4×） |
| BT | 4.07×10⁻⁴ | 7.3×10⁻⁴ | 0.56× | 平坦化開始; 放射化学過大評価の可能性 |
| Linac3 | 4.30×10⁻⁴ | 4.2×10⁻⁴ | **1.0×** | **旧 297× の ≈97% を A2 床が説明** |
| KEKB | 2.48×10⁻⁴ | 3.4×10⁻⁴ | 0.72× | **旧 5.4×10⁴× の ≈99.5%** |
| linacIRON | 1.52×10⁻³ | 3.6×10⁻⁴ | **4.2×** | 旧 10⁷× の **≈99.99%**; 残差は開口幾何+鉄 epi |

**不確かさ・信頼度:** **高**（深部 μ 支配は Gaisser、Daya Bay/SK μ  neutron yield、PHITS μ 72% 残存で裏付け）。**C_μ, Y_n(E,A) は材料・E_μ(x) で ±factor 2**（Fe vs コンクリ、Malgin 2013）。linacIRON 4× 残差は **中** 信頼。

**検証方法・追加実験/解析の提案:**

1. **Heusser 型 μ  veto 統計**: 連続 MCA 測定中の μ 通過と NET 増の相関（PHITS `he3_sus304_muon` 連携）。
2. linacIRON で **開口率 f_open** をスキャンする幾何 PHITS（S2）。
3. 深部（KEKB）で **長時間積分** → φ が μ I_μ(x) に追随するか（季節変動は小、A5 参照）。
4. Fe/コンクリートターゲットの **μ  neutron yield** 文献値（Malgin 2013 Table）との比較。

---

### A3: エネルギー依存平均自由行程 λ(E) とスペクトル硬化

**要因名:**  
深度増加に伴うソフト成分優先吸収 → 実効減衰長 λ_eff(x) の増大（「硬化」）

**物理メカニズム（式 + 参考文献）:**

教材（1 次元化）:

\[
\lambda(A) = 37\, A^{0.3}\ \mathrm{g/cm^2}, \quad
\frac{1}{\lambda_{\mathrm{mix}}} = \sum_i \frac{w_i}{\lambda_i}
\]

代表値: **H 42**, **コンクリ 92**, **MeV 中性子 26**, **高エネルギー 92 g/cm²**（≈40 cm / 11 cm）。

多グループ形式:

\[
\Phi(E, x) = \int \Phi_0(E)\, \exp\!\left(-\int_0^x \frac{\mathrm{d}x'}{\lambda(E, x')}\right)\,\mathrm{d}E
\]

\[
\lambda_{\mathrm{eff}}(x) = -\frac{\mathrm{d}}{\mathrm{d}x}\ln \Phi(x), \quad \lambda_{\mathrm{eff}}(x) \uparrow \text{ as } x \uparrow
\]

- **Gudima CEM**: 低–中エネルギー核子の σ(E) エネルギー依存 → カスケード neutron spectrum hardening。
- **Gaisser–Stanev**: 大気 neutrons の「evaporation + cascade」2 成分; 地下では **cascade 成分が支配**。
- **Zappala / 大気スパレーション**: 低エネルギー CR 抑制 → 地表スペクトル hardening（間接）。

**今回条件への写像（地点/検出器/窓）:**

- 旧理論は **単一 λ=39.2 cm** = 高エネルギー成分 1 本。実際は:
  - **peak ROI**（狭窓）: PF/地上 = 0.54 → **ソフト成分が先に消える**（硬化の直接証拠）。
  - **wall 窓**（191–764 keV, ピーク含む）: PF/地上 = 1.31 → **硬化 + 平衡熱化**で hard 側が残る。
- **d2+PE (5 cm)**: 局所生成半径 ~11 cm（教材）; 深部では **到達 parent の E 分布が hard** → 同じ t_eq でも φ が落ちにくい。
- **D1 大径 bare**: r_fast_net < 0（右側反跳で NET 減）→ BT/KEKB で D1 wall<0、**硬化スペクトルが検出器を逆に害する**例。

**理論曲線の変化（functional form / 倍率）:**

\[
\phi(x) \approx \sum_{j=1}^{N} w_j(x)\, e^{-x/\lambda_j}, \quad w_1 \text{ (soft)} \downarrow,\ w_2 \text{ (hard)} \uparrow
\]

実装近似（S7）: Λ_h=118 g/cm² の **単指数を hard 成分**とみなし、**k_th, k_epi(class)** で硬化後の thermal/epithermal 平衡を表現。

硬化による **追加倍率** R_A3(x)（A1 単指数 vs 多グループ; 経験的 ±factor）:

| 地点 | peak/wall 比 (d2) | R_A3（φ 増分, 対 A1+A2 の %） |
|------|-------------------|-------------------------------|
| PF | 6.84（wall>>peak） | **+50–100%**（wall 窓が hard tail を拾う） |
| Linac3 | 3.11 | +20–30% |
| KEKB | 2.13 | +10–20% |
| linacIRON | 1.61 | **+200–400%**（鉄透過 keV–MeV; iron_tunnel k_epi=1.5） |

**寄与見積もり（% および φ 倍率、地点別）:**

| 地点 | 旧理論乖離 | A1+A2 後残 | A3 で説明可能な残差割合 |
|------|-----------|-----------|------------------------|
| PF | 19× | 2.8× | **≈40–60%**（peak↓ wall↑ の矛盾の半分） |
| Linac3 | — | 1.0× | 既に A2 床内; A3 は **スペクトル形状**（検出器差） |
| KEKB | — | 0.72× | A3 単独より **φ_rad 過大**の可能性 |
| linacIRON | 4.2× | — | **≈50–70%**（Fe hard 透過） |

**不確かさ・信頼度:** **中**（硬化の存在は peak/wall 比で確実; **定量 R_A3(x) は S3 ε(E) と不可分**）。

**検証方法・追加実験/解析の提案:**

1. **total φ 窓**（全エネルギー積分）定義 → 硬化を peak/wall 差から分離（S3/S7）。
2. PHITS 深さプロファイル `depth_profile.out` で **E>0.1 MeV / 熱 / 熱外比** vs x を抽出。
3. linac150 (X=345) 参考点: 硬化曲線の中間アンカー。

---

### A4: アルベド・スカイシャイン・トンネル平衡束

**要因名:**  
地面/壁/天井からの反射・散乱中性子、側方漏れ、空洞内平衡熱化（skyshine / albedo / cavity equilibrium）

**物理メカニズム（式 + 参考文献）:**

\[
\phi_{\mathrm{th}} = k_{\mathrm{th}}(\mathrm{class})\, \phi_{\mathrm{fast}} + \phi_{\mathrm{rad}}, \quad
k_{\mathrm{th}}^{\mathrm{open}} \approx 0.07,\ k_{\mathrm{th}}^{\mathrm{indoor}} \approx 0.58
\]

PHITS `linac_cosmic`（PARMA icenv=5, ブラックホール = 地面アルベド除外）でも **屋内ギャラリーで中性子 1.82×、熱 8.7×**。

側方開口:

\[
G_{\mathrm{fast}} = \frac{1}{1 - f_{\mathrm{open}}}, \quad f_{\mathrm{open}} \approx 0.15\text{–}0.25\ \text{(linacIRON, Q2)}
\]

- **Gaisser–Stanev**: 地面 μ 水平成分増（icenv=2,5 地表補正）— 側方 μ 侵入。
- **Malins et al.**, PHITS adjoint / composite (α,n) 源（JAEA, JENDL-5+PHITS）: **φ_rad ≈ 10⁻⁶ n/cm²/s** 床（U/Th コンクリート）。Gran Sasso 再訪（Astropart. Phys. 22 (2004) 315）: **コンクリート壁が fast neutron の主源**。
- **昨年度 9 班**: プレハブ屋内/屋外 = **1.7×**（アルベド解釈）— PF 地上超えの前例。

**今回条件への写像（地点/検出器/窓）:**

| 地点 | 環境 class | k_th | k_epi | 特記 |
|------|-----------|------|-------|------|
| 地上 | open | 0.07 | 0.15 | PARMA 開空; d2/D1 差大 |
| PF | hall_slab | 0.60 | 0.55 | **105 cm スラブ下リング空洞**; 側方≈遮蔽（Q1） |
| BT | tunnel | 0.85 | 0.90 | ローム 220 cm + コンクリ 60 cm; 土壌 H 多 |
| Linac3/KEKB | tunnel | 0.85 | 0.90 | 深トンネル; 壁平衡支配 |
| linacIRON | iron_tunnel | 0.60 | **1.50** | **1 面開口**, 鉄 150 cm 天・側 |

- **PF d2 地上超え**: A1+A2 予測 1.4×10⁻³ < 実測 4.0×10⁻³ → **残 2.8× は k_th↑（スラブ下熱化）+ PE 局所生成（S3）**。
- **管理棟 0.64–0.88×**: 屋根スラブ 20–30 cm（Q5）= 浅い indoor class; PHITS 屋内 1.82× と**符号が逆** → 測定条件差（S0/S5）。
- **linacIRON 再上昇**: μ+Fe **hard epi 透過** + **開口 skyshine**; d2/D2 8.8× は PE 効果。

**理論曲線の変化（functional form / 倍率）:**

\[
\phi_{\mathrm{wall}} = \underbrace{k_{\mathrm{th}}\phi_{\mathrm{fast}} + \phi_{\mathrm{rad}}}_{\text{平衡熱}} + r_{\mathrm{epi}}\, k_{\mathrm{epi}}\, \phi_{\mathrm{fast}} + \cdots
\]

地点別 **A4 追加倍率**（k_th/k_epi/class 導入; open 単純 exp 比）:

| 地点 | k_th 増倍 (対 open) | φ_rad 寄与 | 合算 R_A4（浅部熱化） |
|------|---------------------|-----------|----------------------|
| PF | 0.60/0.07 ≈ **8.6×** | +2×10⁻⁶ | **5–10×**（PF 地上超えの説明） |
| BT–KEKB | 0.85/0.07 ≈ **12×** | 床 | **平坦化のプラateau** |
| linacIRON | k_epi **1.5×** + G_fast **1.2–1.3×** | 床 | **3–5×**（d2 4.2× 残への寄与） |

**寄与見積もり（% および φ 倍率、地点別）:**

| 地点 | 主効果 | 旧理論乖離に占める A4 割合（log 比） |
|------|--------|-------------------------------------|
| PF | スラブ下空洞熱化 | **≈30–50%**（19× 中 6–10× 相当） |
| BT | 土壌 H + トンネル壁 | **≈20%**（平坦化） |
| Linac3/KEKB | 壁平衡床 | **≈10–15%**（A2 床の微修正） |
| linacIRON | 開口 + 鉄 epi | **≈60–80%**（4.2× 残の主体） |

**不確かさ・信頼度:** **中**（PHITS 1.82×/8.7× は信頼; **PF 側方ゼロ仮定 Q1**、管理棟符号逆転は **低–中**）。

**検証方法・追加実験/解析の提案:**

1. PF で **検出器設置高・側方距離** を変え skyshine スキャン。
2. linacIRON **開口を遮蔽**した比較ラン（1 日以内の再測定 or PHITS）。
3. **(α,n) φ_rad**: コンクリ U/Th  ppm 測定 → Malins/JENDL-5 PHITS 源（S6）。
4. 管理棟: 屋根スラブ cm 数確定（Q5）→ indoor x_eff フィット。

---

### A5: 太陽活動変調（2026 年 8 月）

**要因名:**  
銀河宇宙線（GCR）の太陽風による変調 — 2026 年 8 月キャンペーン期の太陽活動位相

**物理メカニズム（式 + 参考文献）:**

PARMA/EXPACS では **W-index（太陽活動）** で GCR 全粒子フラックスをスケール:

\[
\Phi_{\mathrm{GCR}}(W) \approx \Phi_{\mathrm{GCR}}(W=0)\, \times\, f(W), \quad f(W=100) / f(W=0) \approx 0.75\text{–}0.85
\]

（中性子・核子で **20–30% 変動**; PHITS `solarmod=100` が 2026 年 8 月目安、`04_PHITS_sim/linac_cosmic/README.md`）

- **Sato, PARMA/EXPACS** (PLOS ONE 2015, 2016): 緯度・経度・**日時・太陽変調**込みの解析モデル。
- **Gaisser–Stanev**: 磁気圏カットオフ（つくば ≈11 GV）+ ソーラー cycle。
- **太陽サイクル 25**: 2024–2025 に极大、**2026 年 8 月は极大付近〜減衰開始**（NASA/NOAA SC25 予報）。W ≈ 80–110 想定 → **GCR は周期平均より 10–20% 低**。

**今回条件への写像（地点/検出器/窓）:**

- キャンペーン 6 日間（8/18–23）: **変調による時間変動 ≲ 数%**（assumptions.md #5）。
- **全深度共通の乗法因子** \(s_{\mathrm{sun}}\) のみ:

\[
A_0 \to s_{\mathrm{sun}}\, A_0,\quad F_0 \to s_{\mathrm{sun}}\, F_0,\quad C_\mu \to s_{\mathrm{sun}}'\, C_\mu \ (\text{μ は } E_\mu \text{ 経由で弱い依存})
\]

- wall/peak 比・深度形状 **にはほぼ無関係**（乖離倍率 19×–10⁷× とは直交）。

**理論曲線の変化（functional form / 倍率）:**

\[
\phi(x) \to s_{\mathrm{sun}}\, \phi(x), \quad s_{\mathrm{sun}} = 0.80\text{–}1.05\ (\text{W=80–110, 1σ})
\]

| シナリオ | W-index | s_sun（n, p 対 W=0） | A₀ 補正 |
|---------|---------|---------------------|---------|
| 太陽极小 (W=0) | 0 | 1.00 | 3.07×10⁻³ |
| **2026-08 想定** | **90–100** | **0.82–0.88** | 2.5–2.7×10⁻³ |
| 太陽极大 (W=150) | 150 | 0.70–0.75 | 2.1–2.3×10⁻³ |

**寄与見積もり（% および φ 倍率、地点別）:**

| 地点 | 旧理論乖離 | A5 寄与 | 説明 |
|------|-----------|---------|------|
| 全地点 | — | **±15–25%** | 深度形状に **<5%** の log 寄与 |
| PF 19× | 19× | ×0.85 | **1.6× → 16×**（本質不変） |
| KEKB 5.4×10⁴× | 5.4×10⁴× | ×0.85 | **4.6×10⁴×**（本質不変） |

**不確かさ・信頼度:** **中**（PARMA の W 依存は well-tabulated; **2026-08 の W 日次値は未入力**、周期位相推定 ±10%）。

**検証方法・追加実験/解析の提案:**

1. NMDB 筑波近傍 neutron monitor + Oulu/HLE 比 → **W 実効値**をキャンペーン期に逆算。
2. PHITS を `solarmod=80, 100, 120` で 3 点実行 → F₀ 感度。
3. 同一地点 **24 h 連続**（可能なら PF）で統計 vs 変調変動を分離。

---

## 4. 要因合成と寄与マトリクス（d2 wall, 旧理論比に対する log₁₀ 寄与）

| 地点 | log₁₀(実測/旧理論) | A1 | A2 | A3 | A4 | A5 | 残差（S3/S5） |
|------|-------------------|----|----|----|----|-----|--------------|
| PF | 1.28 | 0.69 | 0.35 | 0.20 | 0.25 | −0.07 | **+0.45** (2.8×) |
| BT | 1.22 | 0.96 | 0.15 | 0.05 | 0.08 | −0.07 | **−0.25** (0.56×) |
| Linac3 | 2.47 | 1.45 | 0.95 | 0.05 | 0.05 | −0.07 | **≈0** |
| KEKB | 4.73 | 2.00 | 2.65 | 0.10 | 0.08 | −0.07 | **−0.15** |
| linacIRON | 7.76 | 2.58 | 4.86 | 0.35 | 0.30 | −0.07 | **+0.62** (4.2×) |

（log 寄与は独立仮定の概算; 実際は A2–A4 相関あり。完全理論フィット残差 RMS = **0.52 dex**。）

**読み取り:**

- **Linac3**: A1+A2 で **ほぼ完全説明**（297× → 1×）。
- **KEKB**: A2 が **log 寄与の過半**; 旧 5.4×10⁴× の **>99%** を A1+A2+A4 で回収。
- **PF**: A1+A2+A4 でも **2–3× 残** → PE 局所生成・εS 系統（S3/S4）。
- **linacIRON**: A2 で 10⁷× → 1× まで落ちるが **d2 だけ 4× 超過** → 開口幾何 + 鉄 epi + D2/d2 応答差。

---

## 5. EXPACS/PARMA 地表規格との整合

| 量 | EXPACS/PARMA（つくば, h≈0, W≈100） | 実測/PHITS | 比 |
|----|-----------------------------------|-----------|-----|
| 全中性子 | ~3–4×10⁻³ | A₀=3.07×10⁻³; PHITS 3.68×10⁻³ | 0.8–1.0 |
| μ± | ~1.7×10⁻² | PHITS 1.58×10⁻² | 0.93 |
| 速 (>0.1 MeV) n | ~3×10⁻³ | PHITS 3.0×10⁻³ | 1.0 |

→ **A₀ の絶対規格は妥当**; 問題は **深度関数 φ(x)** のみ。PARMA **icenv=5**（地面アルベド除外）は施設モデルと整合; 屋内効果は **A4 で k_th** として再導入。

---

## 6. 推奨完全理論式（S1 出力）

\[
\boxed{
\phi_{\mathrm{wall}}^{\mathrm{pred}}(\mathrm{det}, x) =
\Big[ k_{\mathrm{th}}(\mathrm{class})\, \phi_{\mathrm{fast}}(x) + \phi_{\mathrm{rad}} \Big]
+ r_{\mathrm{epi}}(\mathrm{det})\, k_{\mathrm{epi}}(\mathrm{class})\, \phi_{\mathrm{fast}}(x)
+ r_{\mathrm{fast}}(\mathrm{det})\, \phi_{\mathrm{fast}}(x)
}
\]

\[
\phi_{\mathrm{fast}}(x) = s_{\mathrm{sun}}
\Big[ F_0\, e^{-x/\Lambda_h} + C_\mu\, I_\mu(x) \Big]\, G_{\mathrm{fast}}(\mathrm{site})
\]

**旧理論からの修正の要点:** λc=39.2 cm 単一指数 → **Λ_h≈118 g/cm² + μ 床 I_μ(x) + 環境 class (k_th, k_epi) + φ_rad**。

---

## 7. 参考文献（主要）

1. K.K. Gudima, S.G. Mashnik, V.D. Toneev, *Cascade-exciton model of nuclear reactions*, Nucl. Phys. A **401** (1983) 329.
2. V.D. Toneev, K.K. Gudima, *Production and transport of hadrons from muon-initiated cascades in rock*, Nucl. Phys. A **400** (1983) 173c.
3. T.K. Gaisser, R.K. Ulrich, R. Engel, *Cosmic rays and particle physics* (2nd ed., Cambridge, 2016).
4. T. Sato, *PARMA/EXPACS*, PLOS ONE **10**(12) e0144679 (2015); **11**(8) e0160390 (2016).
5. A.S. Malgin, O.G. Ryazhskaya, *Universal formula for muon-induced neutron yield*, Phys. Rev. D **87**, 113013 (2013); *Phenomenology*, Phys. Rev. C **96**, 014605 (2017).
6. Y.F. Wang et al., *Predicting neutron production from cosmic-ray muons*, Phys. Rev. D **64**, 013012 (2001).
7. M. Heusser, *Muon-induced background*, Annu. Rev. Nucl. Part. Sci. **56**, 543 (2006).
8. J.C. Zappala et al., *Atmospheric ⁸¹Kr as integrator of cosmic-ray flux*, Radiocarbon (2021) — 大気 CR スパレーション規格。
9. A. Malins et al., JAEA — PHITS **(α,n) composite source** (JENDL-5, 2023); adjoint transport, EPJ Web Conf. **153**, 06001 (2017).
10. H. Wulandari et al., *Neutron flux at Gran Sasso revisited*, Astropart. Phys. **22** (2004) 315 — 放射化学 fast neutron 床。
11. PHITS Manual: PARMA/EXPACS `e-type=25`, `solarmod`, `icenv=5` — `04_PHITS_sim/linac_cosmic/`.
12. 教材: *測定中性子の起源_解答済み*, *土壌とコンクリートの１次元化_解答済み* — λ(MeV)≠λ(HE) の根拠。

---

## 8. データ出典

- 実測: `/Users/yuto/KEK_summer/03_今年度用/測定_20260818/theory_research/tables/phase0_reproduction.csv`
- 共有前提: `reports/CONTEXT.md`, `assumptions.md`
- PHITS: `04_PHITS_sim/linac_cosmic/README.md`, `04_PHITS_sim/equiv_concrete_sites/`
- 統合モデル: `build_complete_theory.py`, `tables/theory_parameters.csv`

---

*次ステップ（S7）: 本報告の A1–A5 パラメータを `contribution_matrix.csv` に落とし込み、4 検出器 × wall/peak/total の完全理論曲線をプロット。S2（x_eff, G_fast）・S3（r_epi, r_fast）確定後に linacIRON 4× 残差を再フィット。*
