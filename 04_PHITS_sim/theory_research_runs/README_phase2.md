# theory_research_runs — Phase 2 新規 run

既存 `10_deep_allsrc/` 等の出力は**上書きしない**。

## 10_deep_allsrc_v2

- 深部平坦化 MC（maxcas=5000, maxbch=20）
- 実行: `python3 ../../phits-agent-kit/phits_web_run.py deep_all.inp source.inp --version phits336`

## 30_linacIRON

- Q2 幾何: 土100 + コンクリ200 + 鉄150（上から）、1面開口
- `iron_tunnel.inp` — 簡易直方体モデル

## 20_he3_lin_x1 / x100

- He-3 密度線形性検証（既存 inp、未実行）
