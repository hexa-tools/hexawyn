from __future__ import annotations

from hexawyn.application.ports.driven.budget_projection_port import MonthlyCostRaw
from hexawyn.domain.models.budget_projection import (
    BudgetProjectionReport,
    ProjectedMonth,
)
from hexawyn.domain.services.budget_projection.growth_estimator import estimate_growth
from hexawyn.domain.services.budget_projection.scenario_projector import project_months

_HIGH_CONFIDENCE_MONTHS = 6
_MEDIUM_CONFIDENCE_MONTHS = 3
_DEFAULT_CATEGORY_MIX = {"compute": 0.6, "storage": 0.25, "network": 0.15}
_LOW_CONFIDENCE_WARNING = (
    "Low confidence: fewer than three months of cost history. Treat this "
    "projection as indicative only."
)
_EXPONENTIAL_WARNING = (
    "Exponential cost growth detected — review the pessimistic scenario; spend "
    "may accelerate faster than a linear trend suggests."
)


class BudgetProjectionService:
    """Domain service — projects infrastructure cost over a multi-month horizon
    with optimistic / realistic / pessimistic scenarios, a per-category
    breakdown, confidence based on data volume, and budget-threshold alerting."""

    def project(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = estimate_growth(usable)
        start_month = usable[-1]["month"] if usable else "1970-01"
        category_mix = _category_mix(usable)

        months = project_months(estimate, horizon_months, category_mix, start_month)
        months = _apply_seasonality(months, seasonal_factors or {})

        confidence = _confidence(len(usable))
        budget_exceeded, breach_month = _budget_breach(months, budget_threshold_usd)

        return BudgetProjectionReport(
            current_monthly_usd=estimate.current_monthly_usd,
            growth_rate_pct=estimate.monthly_rate_pct,
            growth_model=estimate.model,
            projected_months=months,
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )


def _exclude(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if not excluded:
        return history
    excluded_set = set(excluded)
    return [month for month in history if month["month"] not in excluded_set]


def _category_mix(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def _apply_seasonality(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def _scale(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def _confidence(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "low"


def _budget_breach(
    months: list[ProjectedMonth], threshold: float | None
) -> tuple[bool, str | None]:
    if threshold is None:
        return False, None
    for month in months:
        if month.realistic_usd > threshold:
            return True, month.month_label
    return False, None


def _warning(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)
