"""Общие функции экономических расчётов для решений экзаменационных задач.

Все функции работают с потоками, где индекс 0 соответствует моменту t = 0
(начало проекта, без дисконтирования), индекс t — концу периода t.
"""
from __future__ import annotations

import math
from typing import Iterable, Sequence

import numpy as np
from scipy.optimize import brentq


def discount_factors(rate: float, periods: int) -> np.ndarray:
    """Коэффициенты дисконтирования 1/(1+r)^t для t = 0..periods-1."""
    return 1.0 / (1.0 + rate) ** np.arange(periods)


def present_values(cash_flows: Sequence[float], rate: float) -> np.ndarray:
    """Приведённые (дисконтированные) значения каждого элемента потока."""
    cf = np.asarray(cash_flows, dtype=float)
    return cf * discount_factors(rate, len(cf))


def npv(cash_flows: Sequence[float], rate: float) -> float:
    """Чистая приведённая стоимость: NPV = Σ CF_t / (1 + r)^t."""
    return float(present_values(cash_flows, rate).sum())


def irr(cash_flows: Sequence[float], low: float = -0.99, high: float = 10.0) -> float:
    """Внутренняя норма доходности (численно, метод Брента).

    Возвращает nan, если на интервале [low, high] NPV не меняет знак.
    """
    f = lambda r: npv(cash_flows, r)
    try:
        return float(brentq(f, low, high))
    except ValueError:
        return float("nan")


def payback_period(cash_flows: Sequence[float]) -> float:
    """Простой срок окупаемости (лет) с линейной интерполяцией внутри года.

    Возвращает inf, если накопленный поток так и не становится неотрицательным.
    """
    cum = np.cumsum(np.asarray(cash_flows, dtype=float))
    for t in range(1, len(cum)):
        if cum[t] >= 0 > cum[t - 1]:
            return (t - 1) + (-cum[t - 1]) / (cum[t] - cum[t - 1])
    return 0.0 if cum[0] >= 0 else math.inf


def discounted_payback_period(cash_flows: Sequence[float], rate: float) -> float:
    """Дисконтированный срок окупаемости (лет)."""
    return payback_period(present_values(cash_flows, rate))


def annuity_factor(rate: float, periods: int) -> float:
    """Коэффициент аннуитета: Σ_{t=1..n} 1/(1+r)^t."""
    return (1 - (1 + rate) ** -periods) / rate if rate else float(periods)


def roi(total_benefit: float, total_cost: float) -> float:
    """ROI = (Выгоды − Затраты) / Затраты."""
    return (total_benefit - total_cost) / total_cost


def solve_for(func, target: float = 0.0, low: float = -1e12, high: float = 1e12) -> float:
    """Находит x, при котором func(x) = target (метод Брента)."""
    return float(brentq(lambda x: func(x) - target, low, high))


def fmt_rub(value: float, unit: str = "руб.", digits: int = 0) -> str:
    """Форматирование числа с пробелами-разделителями разрядов."""
    s = f"{value:,.{digits}f}".replace(",", " ")
    return f"{s} {unit}".strip()


def table(rows: Iterable[dict]):
    """Упрощённое создание DataFrame из списка словарей."""
    import pandas as pd

    return pd.DataFrame(list(rows))
