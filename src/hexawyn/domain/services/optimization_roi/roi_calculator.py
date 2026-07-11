from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRaw
from hexawyn.domain.models.optimization_roi import OptimizationItem

_MONTHS_PER_YEAR = 12


@dataclass(frozen=True)
class SavingsResult:
    monthly_saving_eur: float
    annual_saving_eur: float
    savings_pct: float
    normalized_current_eur: float
    traffic_normalized: bool


def compute_savings(baseline: float, current: float, traffic_growth_pct: float) -> SavingsResult:
    """Compute monthly / annual savings and percentage.

    When traffic grew during the sprint, the current cost is normalized down to
    what it would have been at baseline traffic, so savings are not overstated
    by attributing organic growth to the optimization.
    """
    normalized_current = _normalize(current, traffic_growth_pct)
    monthly_saving = round(baseline - normalized_current, 2)
    return SavingsResult(
        monthly_saving_eur=monthly_saving,
        annual_saving_eur=round(monthly_saving * _MONTHS_PER_YEAR, 2),
        savings_pct=_pct(monthly_saving, baseline),
        normalized_current_eur=round(normalized_current, 2),
        traffic_normalized=traffic_growth_pct > 0,
    )


def rank_optimizations(optimizations: list[OptimizationRaw]) -> list[OptimizationItem]:
    """Return optimizations as domain items, highest monthly saving first."""
    items = [
        OptimizationItem(
            name=raw["name"],
            category=raw["category"],
            monthly_saving_eur=raw["monthly_saving_eur"],
            description=raw.get("description", ""),
        )
        for raw in optimizations
    ]
    return sorted(items, key=lambda item: item.monthly_saving_eur, reverse=True)


def _normalize(current: float, traffic_growth_pct: float) -> float:
    if traffic_growth_pct <= 0:
        return current
    return current / (1 + traffic_growth_pct / 100)


def _pct(monthly_saving: float, baseline: float) -> float:
    if baseline <= 0:
        return 0.0
    return round(monthly_saving / baseline * 100, 1)
