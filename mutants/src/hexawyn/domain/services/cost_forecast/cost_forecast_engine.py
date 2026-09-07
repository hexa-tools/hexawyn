from __future__ import annotations

from hexawyn.domain.models.cost_forecast import CostForecast, ResourceCost

_TREND_WINDOW = 3  # days used to compute recent trend


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCostForecastEngineǁforecast__mutmut: MutantDict = {}  # type: ignore


class CostForecastEngine:
    """Pure domain service — no infra deps, no try/catch."""

    @_mutmut_mutated(mutants_xǁCostForecastEngineǁforecast__mutmut)
    def forecast(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_orig(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_1(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 4,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_2(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "XXestimatedXX",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_3(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "ESTIMATED",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_4(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "XXlowXX",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_5(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "LOW",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_6(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = None
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_7(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = None
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_8(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(None, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_9(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, None)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_10(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_11(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, )
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_12(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = None
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_13(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend * days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_14(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed >= 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_15(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 1 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_16(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 1.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_17(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = None
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_18(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(None)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_19(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = None
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_20(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month + days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_21(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = None
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_22(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(None, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_23(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, None)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_24(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_25(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, )
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_26(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend - daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_27(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor / days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_28(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg / trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_29(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 3)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_30(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = None
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_31(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(None, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_32(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, None)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_33(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_34(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, )
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_35(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = None

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_36(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(None, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_37(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, None, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_38(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, None)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_39(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_40(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_41(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, )

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_42(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=None,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_43(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=None,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_44(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=None,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_45(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=None,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_46(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=None,
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_47(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=None,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_48(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=None,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_49(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=None,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_50(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=None,
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_51(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=None,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_52(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=None,
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_53(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=None,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_54(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=None,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_55(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=None,
        )

    def xǁCostForecastEngineǁforecast__mutmut_56(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_57(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_58(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_59(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_60(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_61(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_62(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_63(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_64(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_65(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_66(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_67(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_68(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_69(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            )

    def xǁCostForecastEngineǁforecast__mutmut_70(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(None, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_71(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, None),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_72(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_73(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, ),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_74(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 3),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_75(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(None, 4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_76(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, None),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_77(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(4),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_78(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, ),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

    def xǁCostForecastEngineǁforecast__mutmut_79(  # noqa: PLR0913
        self,
        daily_costs: list[dict[str, object]],
        cluster_name: str,
        month: str,
        days_elapsed: int,
        days_in_month: int,
        top_n: int = 3,
        previous_month_usd: float | None = None,
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> CostForecast:
        historical_days = len(daily_costs)
        current_spend = _compute_current_spend(daily_costs, days_elapsed)
        daily_avg = current_spend / days_elapsed if days_elapsed > 0 else 0.0
        trend_factor = _compute_trend(daily_costs)
        days_remaining = days_in_month - days_elapsed
        projected_total = round(current_spend + daily_avg * trend_factor * days_remaining, 2)
        mom_delta = _month_over_month_delta(projected_total, previous_month_usd)
        top_drivers = _top_drivers(daily_costs, projected_total, top_n)

        return CostForecast(
            cluster_name=cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_remaining=days_remaining,
            current_spend_usd=round(current_spend, 2),
            projected_total_usd=projected_total,
            previous_month_usd=previous_month_usd,
            month_over_month_delta=mom_delta,
            trend_factor=round(trend_factor, 5),
            top_cost_drivers=top_drivers,
            billing_events=[],
            forecast_confidence=forecast_confidence,
            historical_days_used=historical_days,
            data_source=data_source,
        )

mutants_xǁCostForecastEngineǁforecast__mutmut['_mutmut_orig'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_1'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_2'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_3'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_4'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_5'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_6'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_7'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_8'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_9'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_10'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_11'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_12'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_13'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_14'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_15'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_16'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_17'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_18'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_19'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_20'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_21'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_22'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_23'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_24'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_25'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_26'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_27'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_28'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_29'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_30'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_31'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_32'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_33'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_34'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_35'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_36'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_37'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_38'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_39'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_40'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_41'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_42'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_43'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_44'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_45'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_46'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_47'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_48'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_48 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_49'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_49 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_50'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_50 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_51'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_51 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_52'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_52 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_53'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_53 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_54'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_54 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_55'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_55 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_56'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_56 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_57'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_57 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_58'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_58 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_59'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_59 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_60'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_60 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_61'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_61 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_62'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_62 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_63'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_63 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_64'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_64 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_65'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_65 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_66'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_66 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_67'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_67 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_68'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_68 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_69'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_69 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_70'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_70 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_71'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_71 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_72'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_72 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_73'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_73 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_74'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_74 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_75'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_75 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_76'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_76 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_77'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_77 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_78'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_78 # type: ignore # mutmut generated
mutants_xǁCostForecastEngineǁforecast__mutmut['xǁCostForecastEngineǁforecast__mutmut_79'] = CostForecastEngine.xǁCostForecastEngineǁforecast__mutmut_79 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_current_spend__mutmut)
def _compute_current_spend(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_orig(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_1(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_2(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 1.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_3(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = None
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_4(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(None)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_5(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(None) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_6(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get(None)) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_7(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("XXtotal_usdXX")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_8(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("TOTAL_USD")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_9(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = None
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_10(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n > days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_11(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = None
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_12(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total * n
    return daily_avg * days_elapsed


def x__compute_current_spend__mutmut_13(daily_costs: list[dict[str, object]], days_elapsed: int) -> float:
    if not daily_costs:
        return 0.0
    total = sum(_as_float(d.get("total_usd")) for d in daily_costs)
    n = len(daily_costs)
    if n >= days_elapsed:
        return total
    # Fewer data points than days elapsed — extrapolate from average
    daily_avg = total / n
    return daily_avg / days_elapsed

mutants_x__compute_current_spend__mutmut['_mutmut_orig'] = x__compute_current_spend__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_1'] = x__compute_current_spend__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_2'] = x__compute_current_spend__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_3'] = x__compute_current_spend__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_4'] = x__compute_current_spend__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_5'] = x__compute_current_spend__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_6'] = x__compute_current_spend__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_7'] = x__compute_current_spend__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_8'] = x__compute_current_spend__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_9'] = x__compute_current_spend__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_10'] = x__compute_current_spend__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_11'] = x__compute_current_spend__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_12'] = x__compute_current_spend__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_current_spend__mutmut['x__compute_current_spend__mutmut_13'] = x__compute_current_spend__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_trend__mutmut)
def _compute_trend(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_orig(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_1(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) <= 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_2(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 3:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_3(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 2.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_4(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = None
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_5(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(None) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_6(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get(None)) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_7(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("XXtotal_usdXX")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_8(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("TOTAL_USD")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_9(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = None
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_10(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) * len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_11(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(None) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_12(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg != 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_13(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 1.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_14(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 2.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_15(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = None
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_16(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[+_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_17(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = None
    return recent_avg / overall_avg


def x__compute_trend__mutmut_18(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) * len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_19(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(None) / len(recent)
    return recent_avg / overall_avg


def x__compute_trend__mutmut_20(daily_costs: list[dict[str, object]]) -> float:
    if len(daily_costs) < 2:  # noqa: PLR2004
        return 1.0
    totals = [_as_float(d.get("total_usd")) for d in daily_costs]
    overall_avg = sum(totals) / len(totals)
    if overall_avg == 0.0:
        return 1.0
    recent = totals[-_TREND_WINDOW:]
    recent_avg = sum(recent) / len(recent)
    return recent_avg * overall_avg

mutants_x__compute_trend__mutmut['_mutmut_orig'] = x__compute_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_1'] = x__compute_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_2'] = x__compute_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_3'] = x__compute_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_4'] = x__compute_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_5'] = x__compute_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_6'] = x__compute_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_7'] = x__compute_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_8'] = x__compute_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_9'] = x__compute_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_10'] = x__compute_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_11'] = x__compute_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_12'] = x__compute_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_13'] = x__compute_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_14'] = x__compute_trend__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_15'] = x__compute_trend__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_16'] = x__compute_trend__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_17'] = x__compute_trend__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_18'] = x__compute_trend__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_19'] = x__compute_trend__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_20'] = x__compute_trend__mutmut_20 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__month_over_month_delta__mutmut)
def _month_over_month_delta(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, 2)


def x__month_over_month_delta__mutmut_orig(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, 2)


def x__month_over_month_delta__mutmut_1(projected: float, previous: float | None) -> float:
    if previous is None and previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, 2)


def x__month_over_month_delta__mutmut_2(projected: float, previous: float | None) -> float:
    if previous is not None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, 2)


def x__month_over_month_delta__mutmut_3(projected: float, previous: float | None) -> float:
    if previous is None or previous != 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, 2)


def x__month_over_month_delta__mutmut_4(projected: float, previous: float | None) -> float:
    if previous is None or previous == 1.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, 2)


def x__month_over_month_delta__mutmut_5(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 1.0
    return round((projected - previous) / previous * 100.0, 2)


def x__month_over_month_delta__mutmut_6(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round(None, 2)


def x__month_over_month_delta__mutmut_7(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, None)


def x__month_over_month_delta__mutmut_8(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round(2)


def x__month_over_month_delta__mutmut_9(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, )


def x__month_over_month_delta__mutmut_10(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous / 100.0, 2)


def x__month_over_month_delta__mutmut_11(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) * previous * 100.0, 2)


def x__month_over_month_delta__mutmut_12(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected + previous) / previous * 100.0, 2)


def x__month_over_month_delta__mutmut_13(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 101.0, 2)


def x__month_over_month_delta__mutmut_14(projected: float, previous: float | None) -> float:
    if previous is None or previous == 0.0:
        return 0.0
    return round((projected - previous) / previous * 100.0, 3)

mutants_x__month_over_month_delta__mutmut['_mutmut_orig'] = x__month_over_month_delta__mutmut_orig # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_1'] = x__month_over_month_delta__mutmut_1 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_2'] = x__month_over_month_delta__mutmut_2 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_3'] = x__month_over_month_delta__mutmut_3 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_4'] = x__month_over_month_delta__mutmut_4 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_5'] = x__month_over_month_delta__mutmut_5 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_6'] = x__month_over_month_delta__mutmut_6 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_7'] = x__month_over_month_delta__mutmut_7 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_8'] = x__month_over_month_delta__mutmut_8 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_9'] = x__month_over_month_delta__mutmut_9 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_10'] = x__month_over_month_delta__mutmut_10 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_11'] = x__month_over_month_delta__mutmut_11 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_12'] = x__month_over_month_delta__mutmut_12 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_13'] = x__month_over_month_delta__mutmut_13 # type: ignore # mutmut generated
mutants_x__month_over_month_delta__mutmut['x__month_over_month_delta__mutmut_14'] = x__month_over_month_delta__mutmut_14 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__top_drivers__mutmut)
def _top_drivers(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_orig(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_1(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_2(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = None
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_3(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = None
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_4(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get(None)
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_5(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("XXnamespace_costsXX")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_6(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("NAMESPACE_COSTS")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_7(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_8(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            break
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_9(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_10(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                break
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_11(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = None
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_12(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(None)
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_13(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get(None, ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_14(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", None))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_15(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get(""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_16(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_17(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("XXnameXX", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_18(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("NAME", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_19(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", "XXXX"))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_20(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = None
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_21(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(None)
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_22(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get(None))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_23(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("XXcost_usdXX"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_24(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("COST_USD"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_25(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = None

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_26(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) - cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_27(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(None, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_28(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, None) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_29(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_30(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, ) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_31(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 1.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_32(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_33(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = None
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_34(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = None
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_35(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(None)
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_36(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = None

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_37(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total >= 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_38(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 1 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_39(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days / 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_40(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily * n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_41(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 31

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_42(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = None
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_43(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(None, key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_44(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=None, reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_45(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=None)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_46(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_47(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_48(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], )[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_49(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: None, reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_50(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[2], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_51(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=False)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_52(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = None
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_53(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = None
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_54(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) / 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_55(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total * n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_56(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 31
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_57(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = None
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_58(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily / 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_59(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total * total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_60(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 101.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_61(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily >= 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_62(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 1 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_63(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 1.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_64(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            None
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_65(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=None,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_66(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind=None,
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_67(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=None,
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_68(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=None,
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_69(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_70(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_71(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_72(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_73(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="XXnamespaceXX",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_74(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="NAMESPACE",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_75(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(None, 2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_76(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, None),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_77(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(2),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_78(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, ),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_79(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 3),
                percentage=round(pct, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_80(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(None, 1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_81(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, None),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_82(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(1),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_83(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, ),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_84(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 2),
            )
        )
    _ = cluster_monthly  # used for context, not directly needed per driver
    return result


def x__top_drivers__mutmut_85(
    daily_costs: list[dict[str, object]],
    projected_total: float,
    top_n: int,
) -> list[ResourceCost]:
    if not daily_costs:
        return []

    # Aggregate namespace costs across all data points
    ns_agg: dict[str, float] = {}
    for day in daily_costs:
        ns_list = day.get("namespace_costs")
        if not isinstance(ns_list, list):
            continue
        for ns in ns_list:
            if not isinstance(ns, dict):
                continue
            name = str(ns.get("name", ""))
            cost = _as_float(ns.get("cost_usd"))
            ns_agg[name] = ns_agg.get(name, 0.0) + cost

    if not ns_agg:
        return []

    # Convert daily aggregate to monthly estimate
    n_days = len(daily_costs)
    total_daily = sum(ns_agg.values())
    cluster_monthly = projected_total if projected_total > 0 else total_daily / n_days * 30

    ranked = sorted(ns_agg.items(), key=lambda x: x[1], reverse=True)[:top_n]
    result: list[ResourceCost] = []
    for name, daily_total in ranked:
        monthly = (daily_total / n_days) * 30
        pct = (daily_total / total_daily * 100.0) if total_daily > 0 else 0.0
        result.append(
            ResourceCost(
                name=name,
                kind="namespace",
                monthly_cost_usd=round(monthly, 2),
                percentage=round(pct, 1),
            )
        )
    _ = None  # used for context, not directly needed per driver
    return result

mutants_x__top_drivers__mutmut['_mutmut_orig'] = x__top_drivers__mutmut_orig # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_1'] = x__top_drivers__mutmut_1 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_2'] = x__top_drivers__mutmut_2 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_3'] = x__top_drivers__mutmut_3 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_4'] = x__top_drivers__mutmut_4 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_5'] = x__top_drivers__mutmut_5 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_6'] = x__top_drivers__mutmut_6 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_7'] = x__top_drivers__mutmut_7 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_8'] = x__top_drivers__mutmut_8 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_9'] = x__top_drivers__mutmut_9 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_10'] = x__top_drivers__mutmut_10 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_11'] = x__top_drivers__mutmut_11 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_12'] = x__top_drivers__mutmut_12 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_13'] = x__top_drivers__mutmut_13 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_14'] = x__top_drivers__mutmut_14 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_15'] = x__top_drivers__mutmut_15 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_16'] = x__top_drivers__mutmut_16 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_17'] = x__top_drivers__mutmut_17 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_18'] = x__top_drivers__mutmut_18 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_19'] = x__top_drivers__mutmut_19 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_20'] = x__top_drivers__mutmut_20 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_21'] = x__top_drivers__mutmut_21 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_22'] = x__top_drivers__mutmut_22 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_23'] = x__top_drivers__mutmut_23 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_24'] = x__top_drivers__mutmut_24 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_25'] = x__top_drivers__mutmut_25 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_26'] = x__top_drivers__mutmut_26 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_27'] = x__top_drivers__mutmut_27 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_28'] = x__top_drivers__mutmut_28 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_29'] = x__top_drivers__mutmut_29 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_30'] = x__top_drivers__mutmut_30 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_31'] = x__top_drivers__mutmut_31 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_32'] = x__top_drivers__mutmut_32 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_33'] = x__top_drivers__mutmut_33 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_34'] = x__top_drivers__mutmut_34 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_35'] = x__top_drivers__mutmut_35 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_36'] = x__top_drivers__mutmut_36 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_37'] = x__top_drivers__mutmut_37 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_38'] = x__top_drivers__mutmut_38 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_39'] = x__top_drivers__mutmut_39 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_40'] = x__top_drivers__mutmut_40 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_41'] = x__top_drivers__mutmut_41 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_42'] = x__top_drivers__mutmut_42 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_43'] = x__top_drivers__mutmut_43 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_44'] = x__top_drivers__mutmut_44 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_45'] = x__top_drivers__mutmut_45 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_46'] = x__top_drivers__mutmut_46 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_47'] = x__top_drivers__mutmut_47 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_48'] = x__top_drivers__mutmut_48 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_49'] = x__top_drivers__mutmut_49 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_50'] = x__top_drivers__mutmut_50 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_51'] = x__top_drivers__mutmut_51 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_52'] = x__top_drivers__mutmut_52 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_53'] = x__top_drivers__mutmut_53 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_54'] = x__top_drivers__mutmut_54 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_55'] = x__top_drivers__mutmut_55 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_56'] = x__top_drivers__mutmut_56 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_57'] = x__top_drivers__mutmut_57 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_58'] = x__top_drivers__mutmut_58 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_59'] = x__top_drivers__mutmut_59 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_60'] = x__top_drivers__mutmut_60 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_61'] = x__top_drivers__mutmut_61 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_62'] = x__top_drivers__mutmut_62 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_63'] = x__top_drivers__mutmut_63 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_64'] = x__top_drivers__mutmut_64 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_65'] = x__top_drivers__mutmut_65 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_66'] = x__top_drivers__mutmut_66 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_67'] = x__top_drivers__mutmut_67 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_68'] = x__top_drivers__mutmut_68 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_69'] = x__top_drivers__mutmut_69 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_70'] = x__top_drivers__mutmut_70 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_71'] = x__top_drivers__mutmut_71 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_72'] = x__top_drivers__mutmut_72 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_73'] = x__top_drivers__mutmut_73 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_74'] = x__top_drivers__mutmut_74 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_75'] = x__top_drivers__mutmut_75 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_76'] = x__top_drivers__mutmut_76 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_77'] = x__top_drivers__mutmut_77 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_78'] = x__top_drivers__mutmut_78 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_79'] = x__top_drivers__mutmut_79 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_80'] = x__top_drivers__mutmut_80 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_81'] = x__top_drivers__mutmut_81 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_82'] = x__top_drivers__mutmut_82 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_83'] = x__top_drivers__mutmut_83 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_84'] = x__top_drivers__mutmut_84 # type: ignore # mutmut generated
mutants_x__top_drivers__mutmut['x__top_drivers__mutmut_85'] = x__top_drivers__mutmut_85 # type: ignore # mutmut generated
mutants_x__as_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float__mutmut)
def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_orig(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_1(value: object) -> float:
    if value is not None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_2(value: object) -> float:
    if value is None:
        return 1.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_3(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_4(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1.0

mutants_x__as_float__mutmut['_mutmut_orig'] = x__as_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_1'] = x__as_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_2'] = x__as_float__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_3'] = x__as_float__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_4'] = x__as_float__mutmut_4 # type: ignore # mutmut generated
