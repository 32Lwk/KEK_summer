# theory_research — Executive Summary

**更新**: 2026-08-24（Phase 0–5 完了）

## 目的

2026-08 KEK 測定の中性子フラックスが旧理論 \(\phi=A_0 e^{-t/\lambda}\) から最大 \(10^7\) 倍乖離する要因を物理分解し、多成分完全理論曲線を策定。

## 主要結果

| 指標 | 旧理論 | 完全理論 |
|------|--------|---------|
| log₁₀ RMS 残差 | 2.84 dex | **0.49 dex** |
| PF d2 地上比 | — | **d2@PF は解析不使用**（D1/D2 のみ） |
| KEKB 平坦化 | 旧理論 \(10^4\times\) 過小 | μ 均衡+φ_rad 床値 |

## モデル

\[
\phi_{\mathrm{fast}} = [F_0 e^{-x/\Lambda_h} + C_\mu I_\mu(x)] G_{\mathrm{fast}}
\]
+ 検出器応答（wall/peak/total × D1/D2/d1/d2 = **12 系統**）

## 成果物

| ファイル | 内容 |
|----------|------|
| `complete_model.md` | 最終式 |
| `factor_inventory.md` | 全要因一覧 |
| `contribution_matrix.csv` | 地点×要因×% |
| `build_complete_theory.py` | fit + 図 + CSV + LaTeX |
| `reports/S0–S6_*.md` | Subagent 報告 |
| `figures/*.png` | 理論 vs 実測（独立出力） |
| `latex/theory_section.tex` | レポート追記用 |

## 変更禁止

既存 `_plot_mca.py`, `figures/11–18`, `tables/`, `フラックス解析レポート.tex` は**未変更**。

## 実行

```bash
cd 03_今年度用/測定_20260818/theory_research
python3 s5_reanalyze.py          # S5 補正 NET 再生成
python3 build_complete_theory.py --all   # fit + 12系統図 + CSV + LaTeX
```

### 生成図（`figures/`）

| ファイル | 内容 |
|----------|------|
| `theory_vs_meas_all_detectors.png` | 4 det × wall + 旧理論 overlay |
| `theory_vs_meas_peak_total.png` | **4 det × 3 窓 = 12 系統** |
| `component_decomposition.png` | ハドロン/μ/放射能成分 |
| `residual_by_site.png` | 地点別 log 残差 |
| `axis_comparison_teq_vs_teff.png` | 横軸候補比較 |

## 検証（Phase 4）

- PF 8/22 採用: 8/20 比 **8.2×** 差（S5）
- 横軸: x_eff ≈ x_v（差 marginal）
- linacIRON d2/D2: 8.8× → RESP+較正で分担
- PHITS: 1D スラブ **使用不可**; linac_cosmic 地上 **120%** 整合

## 未解決（assumptions.md Q3–Q7）

Q5 管理棟上階構造、Q6 He-3 圧、Q7 パイル構成 — 感度 ≤30%
