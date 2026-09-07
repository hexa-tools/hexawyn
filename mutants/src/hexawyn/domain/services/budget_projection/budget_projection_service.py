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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁBudgetProjectionServiceǁproject__mutmut: MutantDict = {}  # type: ignore


class BudgetProjectionService:
    """Domain service — projects infrastructure cost over a multi-month horizon
    with optimistic / realistic / pessimistic scenarios, a per-category
    breakdown, confidence based on data volume, and budget-threshold alerting."""

    @_mutmut_mutated(mutants_xǁBudgetProjectionServiceǁproject__mutmut)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_orig(  # noqa: PLR0913
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

    def xǁBudgetProjectionServiceǁproject__mutmut_1(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = None
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

    def xǁBudgetProjectionServiceǁproject__mutmut_2(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(None, exclude_months or [])
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

    def xǁBudgetProjectionServiceǁproject__mutmut_3(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, None)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_4(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(exclude_months or [])
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

    def xǁBudgetProjectionServiceǁproject__mutmut_5(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, )
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

    def xǁBudgetProjectionServiceǁproject__mutmut_6(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months and [])
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

    def xǁBudgetProjectionServiceǁproject__mutmut_7(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = None
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

    def xǁBudgetProjectionServiceǁproject__mutmut_8(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = estimate_growth(None)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_9(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = estimate_growth(usable)
        start_month = None
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

    def xǁBudgetProjectionServiceǁproject__mutmut_10(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = estimate_growth(usable)
        start_month = usable[+1]["month"] if usable else "1970-01"
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

    def xǁBudgetProjectionServiceǁproject__mutmut_11(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = estimate_growth(usable)
        start_month = usable[-2]["month"] if usable else "1970-01"
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

    def xǁBudgetProjectionServiceǁproject__mutmut_12(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = estimate_growth(usable)
        start_month = usable[-1]["XXmonthXX"] if usable else "1970-01"
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

    def xǁBudgetProjectionServiceǁproject__mutmut_13(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = estimate_growth(usable)
        start_month = usable[-1]["MONTH"] if usable else "1970-01"
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

    def xǁBudgetProjectionServiceǁproject__mutmut_14(  # noqa: PLR0913
        self,
        history: list[MonthlyCostRaw],
        horizon_months: int,
        budget_threshold_usd: float | None,
        exclude_months: list[str] | None = None,
        seasonal_factors: dict[int, float] | None = None,
    ) -> BudgetProjectionReport:
        usable = _exclude(history, exclude_months or [])
        estimate = estimate_growth(usable)
        start_month = usable[-1]["month"] if usable else "XX1970-01XX"
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

    def xǁBudgetProjectionServiceǁproject__mutmut_15(  # noqa: PLR0913
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
        category_mix = None

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

    def xǁBudgetProjectionServiceǁproject__mutmut_16(  # noqa: PLR0913
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
        category_mix = _category_mix(None)

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

    def xǁBudgetProjectionServiceǁproject__mutmut_17(  # noqa: PLR0913
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

        months = None
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

    def xǁBudgetProjectionServiceǁproject__mutmut_18(  # noqa: PLR0913
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

        months = project_months(None, horizon_months, category_mix, start_month)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_19(  # noqa: PLR0913
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

        months = project_months(estimate, None, category_mix, start_month)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_20(  # noqa: PLR0913
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

        months = project_months(estimate, horizon_months, None, start_month)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_21(  # noqa: PLR0913
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

        months = project_months(estimate, horizon_months, category_mix, None)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_22(  # noqa: PLR0913
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

        months = project_months(horizon_months, category_mix, start_month)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_23(  # noqa: PLR0913
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

        months = project_months(estimate, category_mix, start_month)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_24(  # noqa: PLR0913
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

        months = project_months(estimate, horizon_months, start_month)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_25(  # noqa: PLR0913
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

        months = project_months(estimate, horizon_months, category_mix, )
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

    def xǁBudgetProjectionServiceǁproject__mutmut_26(  # noqa: PLR0913
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
        months = None

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

    def xǁBudgetProjectionServiceǁproject__mutmut_27(  # noqa: PLR0913
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
        months = _apply_seasonality(None, seasonal_factors or {})

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

    def xǁBudgetProjectionServiceǁproject__mutmut_28(  # noqa: PLR0913
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
        months = _apply_seasonality(months, None)

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

    def xǁBudgetProjectionServiceǁproject__mutmut_29(  # noqa: PLR0913
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
        months = _apply_seasonality(seasonal_factors or {})

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

    def xǁBudgetProjectionServiceǁproject__mutmut_30(  # noqa: PLR0913
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
        months = _apply_seasonality(months, )

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

    def xǁBudgetProjectionServiceǁproject__mutmut_31(  # noqa: PLR0913
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
        months = _apply_seasonality(months, seasonal_factors and {})

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

    def xǁBudgetProjectionServiceǁproject__mutmut_32(  # noqa: PLR0913
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

        confidence = None
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

    def xǁBudgetProjectionServiceǁproject__mutmut_33(  # noqa: PLR0913
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

        confidence = _confidence(None)
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

    def xǁBudgetProjectionServiceǁproject__mutmut_34(  # noqa: PLR0913
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
        budget_exceeded, breach_month = None

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

    def xǁBudgetProjectionServiceǁproject__mutmut_35(  # noqa: PLR0913
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
        budget_exceeded, breach_month = _budget_breach(None, budget_threshold_usd)

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

    def xǁBudgetProjectionServiceǁproject__mutmut_36(  # noqa: PLR0913
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
        budget_exceeded, breach_month = _budget_breach(months, None)

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

    def xǁBudgetProjectionServiceǁproject__mutmut_37(  # noqa: PLR0913
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
        budget_exceeded, breach_month = _budget_breach(budget_threshold_usd)

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

    def xǁBudgetProjectionServiceǁproject__mutmut_38(  # noqa: PLR0913
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
        budget_exceeded, breach_month = _budget_breach(months, )

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

    def xǁBudgetProjectionServiceǁproject__mutmut_39(  # noqa: PLR0913
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
            current_monthly_usd=None,
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

    def xǁBudgetProjectionServiceǁproject__mutmut_40(  # noqa: PLR0913
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
            growth_rate_pct=None,
            growth_model=estimate.model,
            projected_months=months,
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_41(  # noqa: PLR0913
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
            growth_model=None,
            projected_months=months,
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_42(  # noqa: PLR0913
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
            projected_months=None,
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_43(  # noqa: PLR0913
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
            six_month_total_realistic=None,
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_44(  # noqa: PLR0913
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
            confidence=None,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_45(  # noqa: PLR0913
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
            budget_threshold_usd=None,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_46(  # noqa: PLR0913
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
            budget_exceeded=None,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_47(  # noqa: PLR0913
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
            budget_breach_month=None,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_48(  # noqa: PLR0913
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
            warning=None,
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_49(  # noqa: PLR0913
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

    def xǁBudgetProjectionServiceǁproject__mutmut_50(  # noqa: PLR0913
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
            growth_model=estimate.model,
            projected_months=months,
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_51(  # noqa: PLR0913
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
            projected_months=months,
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_52(  # noqa: PLR0913
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
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_53(  # noqa: PLR0913
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
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_54(  # noqa: PLR0913
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
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_55(  # noqa: PLR0913
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
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_56(  # noqa: PLR0913
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
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_57(  # noqa: PLR0913
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
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_58(  # noqa: PLR0913
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
            )

    def xǁBudgetProjectionServiceǁproject__mutmut_59(  # noqa: PLR0913
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
            six_month_total_realistic=round(None, 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_60(  # noqa: PLR0913
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
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), None),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_61(  # noqa: PLR0913
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
            six_month_total_realistic=round(2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_62(  # noqa: PLR0913
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
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), ),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_63(  # noqa: PLR0913
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
            six_month_total_realistic=round(sum(None), 2),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_64(  # noqa: PLR0913
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
            six_month_total_realistic=round(sum(m.realistic_usd for m in months), 3),
            confidence=confidence,
            budget_threshold_usd=budget_threshold_usd,
            budget_exceeded=budget_exceeded,
            budget_breach_month=breach_month,
            warning=_warning(confidence, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_65(  # noqa: PLR0913
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
            warning=_warning(None, estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_66(  # noqa: PLR0913
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
            warning=_warning(confidence, None),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_67(  # noqa: PLR0913
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
            warning=_warning(estimate.model),
        )

    def xǁBudgetProjectionServiceǁproject__mutmut_68(  # noqa: PLR0913
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
            warning=_warning(confidence, ),
        )

mutants_xǁBudgetProjectionServiceǁproject__mutmut['_mutmut_orig'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_orig # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_1'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_1 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_2'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_2 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_3'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_3 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_4'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_4 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_5'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_5 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_6'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_6 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_7'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_7 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_8'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_8 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_9'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_9 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_10'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_10 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_11'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_11 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_12'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_12 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_13'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_13 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_14'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_14 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_15'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_15 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_16'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_16 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_17'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_17 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_18'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_18 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_19'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_19 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_20'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_20 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_21'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_21 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_22'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_22 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_23'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_23 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_24'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_24 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_25'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_25 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_26'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_26 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_27'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_27 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_28'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_28 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_29'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_29 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_30'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_30 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_31'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_31 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_32'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_32 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_33'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_33 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_34'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_34 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_35'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_35 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_36'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_36 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_37'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_37 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_38'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_38 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_39'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_39 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_40'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_40 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_41'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_41 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_42'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_42 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_43'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_43 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_44'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_44 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_45'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_45 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_46'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_46 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_47'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_47 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_48'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_48 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_49'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_49 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_50'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_50 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_51'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_51 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_52'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_52 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_53'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_53 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_54'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_54 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_55'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_55 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_56'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_56 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_57'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_57 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_58'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_58 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_59'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_59 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_60'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_60 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_61'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_61 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_62'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_62 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_63'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_63 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_64'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_64 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_65'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_65 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_66'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_66 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_67'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_67 # type: ignore # mutmut generated
mutants_xǁBudgetProjectionServiceǁproject__mutmut['xǁBudgetProjectionServiceǁproject__mutmut_68'] = BudgetProjectionService.xǁBudgetProjectionServiceǁproject__mutmut_68 # type: ignore # mutmut generated
mutants_x__exclude__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__exclude__mutmut)
def _exclude(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if not excluded:
        return history
    excluded_set = set(excluded)
    return [month for month in history if month["month"] not in excluded_set]


def x__exclude__mutmut_orig(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if not excluded:
        return history
    excluded_set = set(excluded)
    return [month for month in history if month["month"] not in excluded_set]


def x__exclude__mutmut_1(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if excluded:
        return history
    excluded_set = set(excluded)
    return [month for month in history if month["month"] not in excluded_set]


def x__exclude__mutmut_2(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if not excluded:
        return history
    excluded_set = None
    return [month for month in history if month["month"] not in excluded_set]


def x__exclude__mutmut_3(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if not excluded:
        return history
    excluded_set = set(None)
    return [month for month in history if month["month"] not in excluded_set]


def x__exclude__mutmut_4(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if not excluded:
        return history
    excluded_set = set(excluded)
    return [month for month in history if month["XXmonthXX"] not in excluded_set]


def x__exclude__mutmut_5(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if not excluded:
        return history
    excluded_set = set(excluded)
    return [month for month in history if month["MONTH"] not in excluded_set]


def x__exclude__mutmut_6(history: list[MonthlyCostRaw], excluded: list[str]) -> list[MonthlyCostRaw]:
    if not excluded:
        return history
    excluded_set = set(excluded)
    return [month for month in history if month["month"] in excluded_set]

mutants_x__exclude__mutmut['_mutmut_orig'] = x__exclude__mutmut_orig # type: ignore # mutmut generated
mutants_x__exclude__mutmut['x__exclude__mutmut_1'] = x__exclude__mutmut_1 # type: ignore # mutmut generated
mutants_x__exclude__mutmut['x__exclude__mutmut_2'] = x__exclude__mutmut_2 # type: ignore # mutmut generated
mutants_x__exclude__mutmut['x__exclude__mutmut_3'] = x__exclude__mutmut_3 # type: ignore # mutmut generated
mutants_x__exclude__mutmut['x__exclude__mutmut_4'] = x__exclude__mutmut_4 # type: ignore # mutmut generated
mutants_x__exclude__mutmut['x__exclude__mutmut_5'] = x__exclude__mutmut_5 # type: ignore # mutmut generated
mutants_x__exclude__mutmut['x__exclude__mutmut_6'] = x__exclude__mutmut_6 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__category_mix__mutmut)
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


def x__category_mix__mutmut_orig(history: list[MonthlyCostRaw]) -> dict[str, float]:
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


def x__category_mix__mutmut_1(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if history:
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


def x__category_mix__mutmut_2(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(None)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_3(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = None
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_4(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[+1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_5(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-2]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_6(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = None
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_7(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["XXtotal_usdXX"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_8(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["TOTAL_USD"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_9(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total < 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_10(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 1:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_11(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(None)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_12(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "XXcomputeXX": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_13(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "COMPUTE": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_14(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] * total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_15(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["XXcompute_usdXX"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_16(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["COMPUTE_USD"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_17(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "XXstorageXX": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_18(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "STORAGE": latest["storage_usd"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_19(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] * total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_20(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["XXstorage_usdXX"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_21(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["STORAGE_USD"] / total,
        "network": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_22(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "XXnetworkXX": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_23(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "NETWORK": latest["network_usd"] / total,
    }


def x__category_mix__mutmut_24(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["network_usd"] * total,
    }


def x__category_mix__mutmut_25(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["XXnetwork_usdXX"] / total,
    }


def x__category_mix__mutmut_26(history: list[MonthlyCostRaw]) -> dict[str, float]:
    if not history:
        return dict(_DEFAULT_CATEGORY_MIX)
    latest = history[-1]
    total = latest["total_usd"]
    if total <= 0:
        return dict(_DEFAULT_CATEGORY_MIX)
    return {
        "compute": latest["compute_usd"] / total,
        "storage": latest["storage_usd"] / total,
        "network": latest["NETWORK_USD"] / total,
    }

mutants_x__category_mix__mutmut['_mutmut_orig'] = x__category_mix__mutmut_orig # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_1'] = x__category_mix__mutmut_1 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_2'] = x__category_mix__mutmut_2 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_3'] = x__category_mix__mutmut_3 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_4'] = x__category_mix__mutmut_4 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_5'] = x__category_mix__mutmut_5 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_6'] = x__category_mix__mutmut_6 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_7'] = x__category_mix__mutmut_7 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_8'] = x__category_mix__mutmut_8 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_9'] = x__category_mix__mutmut_9 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_10'] = x__category_mix__mutmut_10 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_11'] = x__category_mix__mutmut_11 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_12'] = x__category_mix__mutmut_12 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_13'] = x__category_mix__mutmut_13 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_14'] = x__category_mix__mutmut_14 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_15'] = x__category_mix__mutmut_15 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_16'] = x__category_mix__mutmut_16 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_17'] = x__category_mix__mutmut_17 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_18'] = x__category_mix__mutmut_18 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_19'] = x__category_mix__mutmut_19 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_20'] = x__category_mix__mutmut_20 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_21'] = x__category_mix__mutmut_21 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_22'] = x__category_mix__mutmut_22 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_23'] = x__category_mix__mutmut_23 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_24'] = x__category_mix__mutmut_24 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_25'] = x__category_mix__mutmut_25 # type: ignore # mutmut generated
mutants_x__category_mix__mutmut['x__category_mix__mutmut_26'] = x__category_mix__mutmut_26 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__apply_seasonality__mutmut)
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


def x__apply_seasonality__mutmut_orig(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_1(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_2(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = None
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_3(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = None
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_4(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(None, 1.0)
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_5(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, None)
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_6(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(1.0)
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_7(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, )
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_8(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 2.0)
        adjusted.append(_scale(month, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_9(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(None)
    return adjusted


def x__apply_seasonality__mutmut_10(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(None, factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_11(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(month, None) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_12(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(factor) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_13(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(month, ) if factor != 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_14(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(month, factor) if factor == 1.0 else month)
    return adjusted


def x__apply_seasonality__mutmut_15(
    months: list[ProjectedMonth], seasonal_factors: dict[int, float]
) -> list[ProjectedMonth]:
    if not seasonal_factors:
        return months
    adjusted: list[ProjectedMonth] = []
    for month in months:
        factor = seasonal_factors.get(month.month_offset, 1.0)
        adjusted.append(_scale(month, factor) if factor != 2.0 else month)
    return adjusted

mutants_x__apply_seasonality__mutmut['_mutmut_orig'] = x__apply_seasonality__mutmut_orig # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_1'] = x__apply_seasonality__mutmut_1 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_2'] = x__apply_seasonality__mutmut_2 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_3'] = x__apply_seasonality__mutmut_3 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_4'] = x__apply_seasonality__mutmut_4 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_5'] = x__apply_seasonality__mutmut_5 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_6'] = x__apply_seasonality__mutmut_6 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_7'] = x__apply_seasonality__mutmut_7 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_8'] = x__apply_seasonality__mutmut_8 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_9'] = x__apply_seasonality__mutmut_9 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_10'] = x__apply_seasonality__mutmut_10 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_11'] = x__apply_seasonality__mutmut_11 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_12'] = x__apply_seasonality__mutmut_12 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_13'] = x__apply_seasonality__mutmut_13 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_14'] = x__apply_seasonality__mutmut_14 # type: ignore # mutmut generated
mutants_x__apply_seasonality__mutmut['x__apply_seasonality__mutmut_15'] = x__apply_seasonality__mutmut_15 # type: ignore # mutmut generated
mutants_x__scale__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__scale__mutmut)
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


def x__scale__mutmut_orig(month: ProjectedMonth, factor: float) -> ProjectedMonth:
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


def x__scale__mutmut_1(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=None,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_2(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=None,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_3(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=None,
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_4(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=None,
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_5(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=None,
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_6(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category=None,
    )


def x__scale__mutmut_7(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_8(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_9(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_10(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_11(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_12(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        )


def x__scale__mutmut_13(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(None, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_14(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, None),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_15(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_16(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, ),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_17(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd / factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_18(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 3),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_19(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(None, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_20(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, None),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_21(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_22(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, ),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_23(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd / factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_24(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 3),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_25(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(None, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_26(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, None),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_27(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_28(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, ),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_29(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd / factor, 2),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_30(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 3),
        by_category={
            category: round(value * factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_31(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(None, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_32(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, None) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_33(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_34(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, ) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_35(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value / factor, 2) for category, value in month.by_category.items()
        },
    )


def x__scale__mutmut_36(month: ProjectedMonth, factor: float) -> ProjectedMonth:
    return ProjectedMonth(
        month_offset=month.month_offset,
        month_label=month.month_label,
        realistic_usd=round(month.realistic_usd * factor, 2),
        optimistic_usd=round(month.optimistic_usd * factor, 2),
        pessimistic_usd=round(month.pessimistic_usd * factor, 2),
        by_category={
            category: round(value * factor, 3) for category, value in month.by_category.items()
        },
    )

mutants_x__scale__mutmut['_mutmut_orig'] = x__scale__mutmut_orig # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_1'] = x__scale__mutmut_1 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_2'] = x__scale__mutmut_2 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_3'] = x__scale__mutmut_3 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_4'] = x__scale__mutmut_4 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_5'] = x__scale__mutmut_5 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_6'] = x__scale__mutmut_6 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_7'] = x__scale__mutmut_7 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_8'] = x__scale__mutmut_8 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_9'] = x__scale__mutmut_9 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_10'] = x__scale__mutmut_10 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_11'] = x__scale__mutmut_11 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_12'] = x__scale__mutmut_12 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_13'] = x__scale__mutmut_13 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_14'] = x__scale__mutmut_14 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_15'] = x__scale__mutmut_15 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_16'] = x__scale__mutmut_16 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_17'] = x__scale__mutmut_17 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_18'] = x__scale__mutmut_18 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_19'] = x__scale__mutmut_19 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_20'] = x__scale__mutmut_20 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_21'] = x__scale__mutmut_21 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_22'] = x__scale__mutmut_22 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_23'] = x__scale__mutmut_23 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_24'] = x__scale__mutmut_24 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_25'] = x__scale__mutmut_25 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_26'] = x__scale__mutmut_26 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_27'] = x__scale__mutmut_27 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_28'] = x__scale__mutmut_28 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_29'] = x__scale__mutmut_29 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_30'] = x__scale__mutmut_30 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_31'] = x__scale__mutmut_31 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_32'] = x__scale__mutmut_32 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_33'] = x__scale__mutmut_33 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_34'] = x__scale__mutmut_34 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_35'] = x__scale__mutmut_35 # type: ignore # mutmut generated
mutants_x__scale__mutmut['x__scale__mutmut_36'] = x__scale__mutmut_36 # type: ignore # mutmut generated
mutants_x__confidence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__confidence__mutmut)
def _confidence(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "low"


def x__confidence__mutmut_orig(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "low"


def x__confidence__mutmut_1(month_count: int) -> str:
    if month_count > _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "low"


def x__confidence__mutmut_2(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "XXhighXX"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "low"


def x__confidence__mutmut_3(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "HIGH"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "low"


def x__confidence__mutmut_4(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count > _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "low"


def x__confidence__mutmut_5(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "XXmediumXX"
    return "low"


def x__confidence__mutmut_6(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "MEDIUM"
    return "low"


def x__confidence__mutmut_7(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "XXlowXX"


def x__confidence__mutmut_8(month_count: int) -> str:
    if month_count >= _HIGH_CONFIDENCE_MONTHS:
        return "high"
    if month_count >= _MEDIUM_CONFIDENCE_MONTHS:
        return "medium"
    return "LOW"

mutants_x__confidence__mutmut['_mutmut_orig'] = x__confidence__mutmut_orig # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_1'] = x__confidence__mutmut_1 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_2'] = x__confidence__mutmut_2 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_3'] = x__confidence__mutmut_3 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_4'] = x__confidence__mutmut_4 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_5'] = x__confidence__mutmut_5 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_6'] = x__confidence__mutmut_6 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_7'] = x__confidence__mutmut_7 # type: ignore # mutmut generated
mutants_x__confidence__mutmut['x__confidence__mutmut_8'] = x__confidence__mutmut_8 # type: ignore # mutmut generated
mutants_x__budget_breach__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__budget_breach__mutmut)
def _budget_breach(
    months: list[ProjectedMonth], threshold: float | None
) -> tuple[bool, str | None]:
    if threshold is None:
        return False, None
    for month in months:
        if month.realistic_usd > threshold:
            return True, month.month_label
    return False, None


def x__budget_breach__mutmut_orig(
    months: list[ProjectedMonth], threshold: float | None
) -> tuple[bool, str | None]:
    if threshold is None:
        return False, None
    for month in months:
        if month.realistic_usd > threshold:
            return True, month.month_label
    return False, None


def x__budget_breach__mutmut_1(
    months: list[ProjectedMonth], threshold: float | None
) -> tuple[bool, str | None]:
    if threshold is not None:
        return False, None
    for month in months:
        if month.realistic_usd > threshold:
            return True, month.month_label
    return False, None


def x__budget_breach__mutmut_2(
    months: list[ProjectedMonth], threshold: float | None
) -> tuple[bool, str | None]:
    if threshold is None:
        return True, None
    for month in months:
        if month.realistic_usd > threshold:
            return True, month.month_label
    return False, None


def x__budget_breach__mutmut_3(
    months: list[ProjectedMonth], threshold: float | None
) -> tuple[bool, str | None]:
    if threshold is None:
        return False, None
    for month in months:
        if month.realistic_usd >= threshold:
            return True, month.month_label
    return False, None


def x__budget_breach__mutmut_4(
    months: list[ProjectedMonth], threshold: float | None
) -> tuple[bool, str | None]:
    if threshold is None:
        return False, None
    for month in months:
        if month.realistic_usd > threshold:
            return False, month.month_label
    return False, None


def x__budget_breach__mutmut_5(
    months: list[ProjectedMonth], threshold: float | None
) -> tuple[bool, str | None]:
    if threshold is None:
        return False, None
    for month in months:
        if month.realistic_usd > threshold:
            return True, month.month_label
    return True, None

mutants_x__budget_breach__mutmut['_mutmut_orig'] = x__budget_breach__mutmut_orig # type: ignore # mutmut generated
mutants_x__budget_breach__mutmut['x__budget_breach__mutmut_1'] = x__budget_breach__mutmut_1 # type: ignore # mutmut generated
mutants_x__budget_breach__mutmut['x__budget_breach__mutmut_2'] = x__budget_breach__mutmut_2 # type: ignore # mutmut generated
mutants_x__budget_breach__mutmut['x__budget_breach__mutmut_3'] = x__budget_breach__mutmut_3 # type: ignore # mutmut generated
mutants_x__budget_breach__mutmut['x__budget_breach__mutmut_4'] = x__budget_breach__mutmut_4 # type: ignore # mutmut generated
mutants_x__budget_breach__mutmut['x__budget_breach__mutmut_5'] = x__budget_breach__mutmut_5 # type: ignore # mutmut generated
mutants_x__warning__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__warning__mutmut)
def _warning(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_orig(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_1(confidence: str, model: str) -> str:
    parts: list[str] = None
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_2(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence != "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_3(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "XXlowXX":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_4(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "LOW":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_5(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(None)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_6(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model != "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_7(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "XXexponentialXX":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_8(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "EXPONENTIAL":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(parts)


def x__warning__mutmut_9(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(None)
    return " ".join(parts)


def x__warning__mutmut_10(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return " ".join(None)


def x__warning__mutmut_11(confidence: str, model: str) -> str:
    parts: list[str] = []
    if confidence == "low":
        parts.append(_LOW_CONFIDENCE_WARNING)
    if model == "exponential":
        parts.append(_EXPONENTIAL_WARNING)
    return "XX XX".join(parts)

mutants_x__warning__mutmut['_mutmut_orig'] = x__warning__mutmut_orig # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_1'] = x__warning__mutmut_1 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_2'] = x__warning__mutmut_2 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_3'] = x__warning__mutmut_3 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_4'] = x__warning__mutmut_4 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_5'] = x__warning__mutmut_5 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_6'] = x__warning__mutmut_6 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_7'] = x__warning__mutmut_7 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_8'] = x__warning__mutmut_8 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_9'] = x__warning__mutmut_9 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_10'] = x__warning__mutmut_10 # type: ignore # mutmut generated
mutants_x__warning__mutmut['x__warning__mutmut_11'] = x__warning__mutmut_11 # type: ignore # mutmut generated
