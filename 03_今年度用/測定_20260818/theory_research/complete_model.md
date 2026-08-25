# 完全理論モデル — 最終式とパラメータ

最終更新: 2026-08-24（S7 統合 fit 後）

## 輸送モデル

深さ変数 \(x\) = 実効質量厚 [g/cm²]（`SITE_DB[site].x_eff`）

\[
\phi_{\mathrm{fast}}(x) = \left[ F_0 e^{-x/\Lambda_h} + C_\mu I_\mu(x) \right] G_{\mathrm{fast}}(\mathrm{site})
\]

\[
I_\mu(x) = (1-f_{\mathrm{stop}}) e^{-x/\Lambda_{\mu 2}} + f_{\mathrm{stop}} e^{-x/\Lambda_{\mu 1}}
\]

\[
\phi_{\mathrm{th}} = k_{\mathrm{th}}(\mathrm{class}) \cdot \phi_{\mathrm{fast}} + \phi_{\mathrm{rad}}
\]
\[
\phi_{\mathrm{epi}} = k_{\mathrm{epi}}(\mathrm{class}) \cdot \phi_{\mathrm{fast}}
\]

## 検出器応答（12 系統）

| 窓 | 式 |
|----|-----|
| wall | \(\phi_{\mathrm{wall}} = \phi_{\mathrm{th}} + r_{\mathrm{epi}}\phi_{\mathrm{epi}} + r_{\mathrm{fast,net}}\phi_{\mathrm{fast}}\) |
| peak | 同上（\(r_{\mathrm{fast,pk}}\)）× \(\varepsilon S_{\mathrm{wall}}/\varepsilon S_{\mathrm{peak}}\) |
| total | \(\phi_{\mathrm{total}} = \phi_{\mathrm{th}} + \phi_{\mathrm{epi}} + \phi_{\mathrm{fast}}\) |

## フィットパラメータ（`tables/theory_parameters.csv`）

| パラメータ | 値 | 単位 | prior 出典 |
|-----------|-----|------|-----------|
| F0_fast | 6.183×10⁻³ | n/cm²/s | PHITS 3.0×10⁻³ |
| Lambda_h | 118.5 | g/cm² | 文献 120 |
| C_mu | 2.46×10⁻⁴ | n/cm²/s | S1 6×10⁻⁵ |
| Lmu1 | 450 | g/cm² | Gaisser |
| fstop | ~0 (fit 下限) | — | prior 0.35 |
| Lmu2 | 7242 | g/cm² | Gaisser |
| phi_rad | 4.24×10⁻⁶ | n/cm²/s | Malins |

## 性能

| 指標 | 旧理論 | 完全理論 |
|------|--------|---------|
| log₁₀ RMS 残差 (wall+peak) | **2.84 dex** | **0.49 dex** |

## CLASS_DB

| class | k_th | k_epi | 根拠 |
|-------|------|-------|------|
| open | 0.070 | 0.150 | linac_cosmic 地上 |
| indoor | 0.575 | 0.516 | 管理棟 |
| hall_slab | 0.60 | 0.55 | PF |
| tunnel | 0.85 | 0.90 | Linac3/KEKB |
| iron_tunnel | 0.60 | 1.50 | linacIRON 鉄透過 |

## RESP（検出器）

| det | r_epi | r_fast_net | r_fast_pk |
|-----|-------|------------|-----------|
| D1 | 0.55 | −0.06 | 0.00 |
| D2 | 0.80 | −0.10 | 0.05 |
| d1 | 0.55 | +0.02 | 0.00 |
| d2 | 0.80 | +0.06 | 0.05 |

## 横軸選定（S2 統合後）

- **ハドロン減衰**: \(x_{\mathrm{eff}} = 1.5 \times X_v\)（cos²θ 加重, n=2）
- **μ 起源**: \(X_\mu = x_{\mathrm{eff}}\)（linacIRON のみ開口経路 → 2118 g/cm²）
- **旧理論プロット**: \(t_{\mathrm{eq,density}} = X_v/\rho_c\) を維持

AIC 比較（wall fit）: `x_v_only` vs `x_eff_S2` — 詳細は `reports/S2_axis_geometry.md`

## 参照レポート

- S1 宇宙線・μ 物理: `reports/S1_cosmic_muon.md`
- S2 横軸・幾何: `reports/S2_axis_geometry.md`
- S3 He-3 応答: `reports/S3_he3_response.md`
- S4 較正: `reports/S4_calibration.md`（チェーン系統 ±50–70%）
- S5 解析系統: `reports/S5_analysis_systematics.md`
- S6 PHITS: `reports/S6_phits.md`（地上 83% 整合）

## 実行

```bash
python3 theory_research/build_complete_theory.py --all
```
