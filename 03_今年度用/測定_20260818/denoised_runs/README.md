# denoised_runs（確認用・追記型）

条件を変えるたびに **新しいフォルダ** を追加する。既存 run は上書きしない運用。

| run_id | 説明 |
|--------|------|
| `large_d_cut200` | large_d_cut200（適応型補正・d/D 統合・確認用） |
| `peak764_cut200` | peak764_cut200（764 keV peak ROI フラックス・確認用） |
| `small_d_cut300` | small_d_cut300（d/D 統合・ch>=300 割合補正・確認用） |

例:

```bash
python3 03_今年度用/build_denoised_review.py --run-id large_d_cut200
python3 03_今年度用/build_denoised_review.py --run-id large_d_cut200 --merge
```
