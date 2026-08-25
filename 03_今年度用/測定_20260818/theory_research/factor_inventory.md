# 全要因インベントリ

最終更新: 2026-08-24（Phase 3 S7 統合）

| ID | 要因名 | 物理メカニズム | 文献 | 寄与（典型） | 信頼度 |
|----|--------|---------------|------|-------------|--------|
| A1 | 一次 CRN 減衰 | φ∝exp(−X/Λ_h), Λ_h≈120 g/cm² | Gudima 2006; EXPACS | 浅部支配、深部<1% | 高 |
| A2 | μ 均衡成分 | I_μ(x) 二指数; C_μ·I_μ | Gaisser-Stanev 2003 | 深部 60–85% | 中 |
| A3 | スペクトル硬化 | λ(E) 深度依存 | Shibata 2010 | wall/peak 逆転 30% | 中 |
| A4 | アルベド・幾何 | G_fast(site) | linac_cosmic; S0 | linacIRON 15–25% | 中 |
| A5 | 太陽変調 | solarmod=100 | NM データ | ≤5% | 低 |
| A6 | 環境放射能 | φ_rad 床値 | Malins 2013 | KEKB 10–20% | 中 |
| B1 | t_eq 密度 vs 組成 | 37A^0.3 混合則 | equiv_shielding | linacIRON 18% | 高 |
| B2 | 天頂角 t_eff | secθ 加重 | 文献一般 | 浅部 5–10% | 中 |
| B3 | 鉄換算 | Λ_Fe=124 g/cm² | 教材 | 組成補正に含む | 高 |
| B4 | linacIRON 開口 | f_open=0.20 | Q2 ユーザー | G_fast=1.25 | 中 |
| B5 | 屋内遮蔽 | x_eff=35/80 g/cm² | Q5 仮定 | 管理棟 0.6–0.9× | 中 |
| C1 | wall≠total | 反跳連続 191–764 keV | 米内 2002 | 窓比 0.2–6.8 | 高 |
| C2 | ε(E) 積分 | 1/v 重み | Knoll | 検出器間 40% | 中 |
| C3 | PE 応答 | d2/D2 epi 増 | S3 | wall/peak 2–7× | 高 |
| D1 | 熱場外挿 | Am-Be 較正 | 米内 2002 | 深部 +15–25% | 中 |
| D2 | 単一点転送 | d2/D1 地上 | build_flux_summary | ±10–20% | 中 |
| D3 | D1/d1 幾何 | 比 1.81 vs 3.3 | 実測 | ±30% スケール | 低 |
| E1 | 側帯背景 | 右/左右/GROSS | S5 | 負NET 100% 反転 | 高 |
| E2 | PF ファイル選択 | 8/20 vs 8/22 | S5 | 8× 差 | 高 |
| E3 | dead time | 1/(1−τ) | 測定記録 | d2 +2–3% | 低 |

詳細: `reports/S1_cosmic_muon.md` … `S6_phits.md`
