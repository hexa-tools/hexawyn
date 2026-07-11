from __future__ import annotations

from hexawyn.domain.models.budget_projection import ProjectedMonth
from hexawyn.domain.services.budget_projection.growth_estimator import GrowthEstimate

_OPTIMISTIC_FACTOR = 0.5
_PESSIMISTIC_FACTOR = 1.5
_EXPONENTIAL_PESSIMISTIC_FACTOR = 2.0


def project_months(
    estimate: GrowthEstimate,
    horizon: int,
    category_mix: dict[str, float],
    start_month: str,
) -> list[ProjectedMonth]:
    """Project *horizon* months forward in three scenarios.

    Realistic applies the estimated monthly rate as compound growth. Optimistic
    halves the rate; pessimistic widens it (further for exponential models,
    where the downside risk is larger). Each month's realistic total is split
    across categories using the historical mix.
    """
    realistic_rate = estimate.monthly_rate_pct / 100
    optimistic_rate = realistic_rate * _OPTIMISTIC_FACTOR
    pessimistic_rate = realistic_rate * _pessimistic_factor(estimate.model)
    base = estimate.current_monthly_usd

    months: list[ProjectedMonth] = []
    for offset in range(1, horizon + 1):
        realistic = _compound(base, realistic_rate, offset)
        months.append(
            ProjectedMonth(
                month_offset=offset,
                month_label=_add_months(start_month, offset),
                realistic_usd=realistic,
                optimistic_usd=_compound(base, optimistic_rate, offset),
                pessimistic_usd=_compound(base, pessimistic_rate, offset),
                by_category=_split_categories(realistic, category_mix),
            )
        )
    return months


def _pessimistic_factor(model: str) -> float:
    if model == "exponential":
        return _EXPONENTIAL_PESSIMISTIC_FACTOR
    return _PESSIMISTIC_FACTOR


def _compound(base: float, rate: float, offset: int) -> float:
    return round(base * (1 + rate) ** offset, 2)


def _split_categories(total: float, category_mix: dict[str, float]) -> dict[str, float]:
    return {category: round(total * share, 2) for category, share in category_mix.items()}


def _add_months(start_month: str, offset: int) -> str:
    year, month = (int(part) for part in start_month.split("-"))
    zero_based = (month - 1) + offset
    new_year = year + zero_based // 12
    new_month = zero_based % 12 + 1
    return f"{new_year:04d}-{new_month:02d}"
