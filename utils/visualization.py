"""Единый стиль графиков для всех решений."""
from __future__ import annotations

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

PALETTE = ["#2563eb", "#dc2626", "#16a34a", "#d97706", "#7c3aed", "#0891b2", "#64748b"]


def setup_style() -> None:
    """Базовые настройки matplotlib: шрифт с кириллицей, сетка, размеры."""
    plt.rcParams.update(
        {
            "figure.figsize": (10, 5.5),
            "figure.dpi": 110,
            "font.family": "DejaVu Sans",
            "font.size": 10.5,
            "axes.titlesize": 13,
            "axes.titleweight": "bold",
            "axes.grid": True,
            "grid.alpha": 0.3,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.prop_cycle": plt.cycler(color=PALETTE),
            "legend.frameon": False,
        }
    )


def thousands_axis(ax, axis: str = "y", unit: str = "") -> None:
    """Подписи оси с пробелами-разделителями тысяч."""
    fmt = mticker.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", " ") + unit)
    (ax.yaxis if axis == "y" else ax.xaxis).set_major_formatter(fmt)


def bar_labels(ax, bars, fmt: str = "{:.1f}", offset: float = 3) -> None:
    """Подписи значений над столбцами."""
    for b in bars:
        h = b.get_height()
        ax.annotate(
            fmt.format(h).replace(",", " "),
            (b.get_x() + b.get_width() / 2, h),
            xytext=(0, offset if h >= 0 else -offset - 9),
            textcoords="offset points",
            ha="center",
            fontsize=9,
        )


def tornado(ax, labels, low, high, base, title: str, xlabel: str) -> None:
    """Торнадо-диаграмма чувствительности."""
    import numpy as np

    low, high = np.asarray(low, float), np.asarray(high, float)
    order = np.argsort(np.abs(high - low))
    y = np.arange(len(labels))
    ax.barh(y, low[order] - base, left=base, color=PALETTE[1], label="Параметр −Δ")
    ax.barh(y, high[order] - base, left=base, color=PALETTE[2], label="Параметр +Δ")
    ax.axvline(base, color="black", lw=1)
    ax.set_yticks(y, [labels[i] for i in order])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.legend(loc="lower right")
