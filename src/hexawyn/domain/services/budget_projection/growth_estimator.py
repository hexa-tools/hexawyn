from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.budget_projection_port import MonthlyCostRaw

_FLAT_TOLERANCE_PCT = 0.5
_EXPONENTIAL_ACCELERATION_PCT = 2.0


@dataclass(frozen=True)
class GrowthEstimate:
    current_monthly_usd: float
    monthly_rate_pct: float
    model: str


def estimate_growth(history: list[MonthlyCostRaw]) -> GrowthEstimate:
    """Estimate the monthly growth rate and classify the growth model.

    The rate is the mean of consecutive month-over-month percentage changes.
    The model is exponential when those changes keep accelerating, decreasing
    when the rate is negative, flat when it is within +/-0.5%, otherwise linear.
    """
    if len(history) < 2:  # noqa: PLR2004
        current = history[-1]["total_usd"] if history else 0.0
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")

    changes = _month_over_month_changes(history)
    if not changes:
        current = history[-1]["total_usd"]
        return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=0.0, model="flat")
    mean_rate = round(sum(changes) / len(changes), 2)
    current = history[-1]["total_usd"]
    model = _classify_model(mean_rate, changes)
    return GrowthEstimate(current_monthly_usd=current, monthly_rate_pct=mean_rate, model=model)


def _month_over_month_changes(history: list[MonthlyCostRaw]) -> list[float]:
    changes: list[float] = []
    for previous, current in zip(history, history[1:], strict=False):
        previous_total = previous["total_usd"]
        if previous_total == 0:
            continue
        changes.append((current["total_usd"] - previous_total) / previous_total * 100)
    return changes


def _classify_model(mean_rate: float, changes: list[float]) -> str:
    if abs(mean_rate) <= _FLAT_TOLERANCE_PCT:
        return "flat"
    if mean_rate < 0:
        return "decreasing"
    if _is_accelerating(changes):
        return "exponential"
    return "linear"


def _is_accelerating(changes: list[float]) -> bool:
    if len(changes) < 2:  # noqa: PLR2004
        return False
    return all(
        later - earlier > _EXPONENTIAL_ACCELERATION_PCT
        for earlier, later in zip(changes, changes[1:], strict=False)
    )
