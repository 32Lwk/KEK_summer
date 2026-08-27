"""modufy_6_netu / modify_6_MeV の多成分理論曲線（y_sum_averaged）。"""

from __future__ import annotations

from typing import Literal

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from scipy.integrate import quad

RHO_CONCRETE = 2.3
I_0 = 100.0
D_0 = 11.5
GAMMA = 2.2
E_0 = 4.0
ALPHA = 0.73
A_COEFF = 4.0e-6
DELTA_X_BAR = 230.0
F0_N = 1.189e-3
DELTA_D = 0.1

THERMAL_A_MASS = [8.48, 9.52, 1.6, 0.81, 0.01]
THERMAL_BETA = 0.84
THERMAL_Y_CONST = 8.0e-6

MEV_A_MASS = [13.2, 8.4, 3.2, 1.35, 1.68, 0.01]
MEV_BETA = 0.9
MEV_Y_CONST = 3.88e-6

Kind = Literal["thermal", "mev"]

F123_STYLE = {
    "f1": {
        "color": "#C71585",
        "ls": "-.",
        "lw": 1.8,
        "alpha": 1.0,
        "label": r"$f_1$：ミューオン由来",
    },
    "f2": {
        "color": "#F58518",
        "ls": ":",
        "lw": 1.6,
        "alpha": 0.85,
        "label": r"$f_2$：大気中性子 ($e^{-d/60}$)",
    },
    "f3": {
        "color": "#54A24B",
        "ls": ":",
        "lw": 1.6,
        "alpha": 0.85,
        "label": r"$f_3$：定数成分（U238 等）",
    },
}

LEGEND_KW = {
    "frameon": True,
    "framealpha": 0.92,
    "loc": "upper right",
    "fontsize": 10.0,
    "borderaxespad": 0.8,
    "handlelength": 2.0,
    "labelspacing": 0.45,
}


def _calc_y_at_d(d_val: float, *, a_mass_list: list[float], beta: float) -> float:
    if d_val < 0:
        return 0.0
    i_mu = I_0 * (1.0 + d_val / D_0) ** (-GAMMA)
    e_bar = E_0 * (1.0 + d_val / D_0) ** ALPHA
    y_n_sum = sum(A_COEFF * (a_i**beta) * (e_bar**ALPHA) for a_i in a_mass_list)
    return (i_mu * y_n_sum * DELTA_X_BAR) / 1e4


def _integrate_y(d_center: float | np.ndarray, *, a_mass_list: list[float], beta: float):
    if isinstance(d_center, (list, np.ndarray)):
        return np.array(
            [_integrate_y(dc, a_mass_list=a_mass_list, beta=beta) for dc in d_center]
        )
    a = max(0.0, float(d_center) - DELTA_D)
    b = float(d_center) + DELTA_D
    if a >= b:
        return 0.0
    val, _ = quad(
        lambda dv: _calc_y_at_d(dv, a_mass_list=a_mass_list, beta=beta), a, b
    )
    return val


def _components(
    t_eq_cm: np.ndarray,
    *,
    a_mass_list: list[float],
    beta: float,
    y_const: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    d = (t_eq_cm / 100.0) * RHO_CONCRETE
    f1 = _integrate_y(d, a_mass_list=a_mass_list, beta=beta) / (2.0 * DELTA_D)
    f2 = F0_N * np.exp(-(t_eq_cm / 100.0) / 0.6)
    f3 = np.full_like(t_eq_cm, y_const, dtype=float)
    return f1, f2, f3


def _y_sum_averaged(
    t_eq_cm: np.ndarray,
    *,
    a_mass_list: list[float],
    beta: float,
    y_const: float,
) -> np.ndarray:
    f1, f2, f3 = _components(
        t_eq_cm, a_mass_list=a_mass_list, beta=beta, y_const=y_const
    )
    return f1 + f2 + f3


def thermal_components(t_eq_cm: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return _components(
        t_eq_cm,
        a_mass_list=THERMAL_A_MASS,
        beta=THERMAL_BETA,
        y_const=THERMAL_Y_CONST,
    )


def mev_components(t_eq_cm: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return _components(
        t_eq_cm,
        a_mass_list=MEV_A_MASS,
        beta=MEV_BETA,
        y_const=MEV_Y_CONST,
    )


def components_for(kind: Kind, t_eq_cm: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if kind == "thermal":
        return thermal_components(t_eq_cm)
    return mev_components(t_eq_cm)


def thermal_complete_theory(t_eq_cm: np.ndarray) -> np.ndarray:
    return _y_sum_averaged(
        t_eq_cm,
        a_mass_list=THERMAL_A_MASS,
        beta=THERMAL_BETA,
        y_const=THERMAL_Y_CONST,
    )


def mev_complete_theory(t_eq_cm: np.ndarray) -> np.ndarray:
    return _y_sum_averaged(
        t_eq_cm,
        a_mass_list=MEV_A_MASS,
        beta=MEV_BETA,
        y_const=MEV_Y_CONST,
    )


def plot_f123(
    ax: Axes,
    x_c: np.ndarray,
    f1: np.ndarray,
    f2: np.ndarray,
    f3: np.ndarray,
    *,
    zorder: float = 2.1,
    labeled: bool = True,
) -> None:
    for key, y in (("f1", f1), ("f2", f2), ("f3", f3)):
        st = F123_STYLE[key]
        kw = dict(
            color=st["color"],
            ls=st["ls"],
            lw=st["lw"],
            alpha=st["alpha"],
            zorder=zorder,
        )
        if labeled:
            kw["label"] = st["label"]
        ax.plot(x_c, y, **kw)


def legend_upper_right(ax: Axes, *, fontsize: float = 10.0) -> None:
    kw = dict(LEGEND_KW)
    kw["fontsize"] = fontsize
    ax.legend(**kw)
