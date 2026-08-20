"""KEK 公式案内図（Campus_Map Ver.2026.05）上の座標変換。

案内図左下のスケールバー 400 m を地図幅とし、画像アスペクト比から高さを決める。
原点は地図中心。X=東, Y=上, Z=南（画像の下方向）。
"""

from __future__ import annotations

MAP_WIDTH_M = 400.0
MAP_HEIGHT_M = 566.0  # 3508/4961 × 400


def pct_to_scene(x_pct: float, y_pct: float) -> tuple[float, float]:
    """案内図上の百分率 → シーン座標 (x, z) [m]。"""
    x = x_pct / 100.0 * MAP_WIDTH_M - MAP_WIDTH_M / 2.0
    z = y_pct / 100.0 * MAP_HEIGHT_M - MAP_HEIGHT_M / 2.0
    return x, z


def grid_to_pct(col: str, row: int) -> tuple[float, float]:
    """番地グリッド (a-d, 1-7) → 百分率（おおよそ）。"""
    cols = {"a": 0, "b": 1, "c": 2, "d": 3}
    c = cols[col[0]]
    x_pct = (c + 0.5) / 4.0 * 100.0
    y_pct = (row - 0.5) / 7.0 * 100.0
    return x_pct, y_pct
