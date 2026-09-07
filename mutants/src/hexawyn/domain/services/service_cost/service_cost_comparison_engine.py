from __future__ import annotations

from hexawyn.domain.models.service_cost_comparison import (
    MonthCost,
    ServiceCostBreakdown,
    ServiceCostComparison,
)

_SIGNIFICANT_TREND_PCT = 10.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut: MutantDict = {}  # type: ignore


class ServiceCostComparisonEngine:
    @_mutmut_mutated(mutants_xǁServiceCostComparisonEngineǁcompute__mutmut)
    def compute(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_orig(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_1(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = None
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_2(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            None,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_3(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            None,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_4(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            None,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_5(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            None,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_6(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            None,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_7(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_8(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_9(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_10(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_11(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_12(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = None

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_13(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            None,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_14(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            None,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_15(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            None,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_16(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            None,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_17(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            None,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_18(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_19(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_20(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_21(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_22(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_23(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 or previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_24(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost != 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_25(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 1.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_26(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost != 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_27(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 1.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_28(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=None,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_29(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=None,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_30(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=None,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_31(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend=None,
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_32(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation=None,
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_33(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_34(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_35(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_36(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_37(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_38(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="XXno_dataXX",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_39(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="NO_DATA",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_40(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="XXNo metrics data available — check Prometheus connectivityXX",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_41(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="no metrics data available — check prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_42(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="NO METRICS DATA AVAILABLE — CHECK PROMETHEUS CONNECTIVITY",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_43(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = None
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_44(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(None, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_45(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, None)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_46(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_47(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, )
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_48(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost + previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_49(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 3)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_50(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost >= 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_51(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 1:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_52(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = None
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_53(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round(None, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_54(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, None)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_55(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round(1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_56(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, )
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_57(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) / 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_58(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta * previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_59(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 101.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_60(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 2)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_61(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = None

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_62(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 101.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_63(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost >= 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_64(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 1 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_65(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 1.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_66(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(None) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_67(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) <= _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_68(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = None
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_69(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "XXstableXX"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_70(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "STABLE"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_71(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = None
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_72(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "XXCost is stable month-over-monthXX"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_73(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_74(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "COST IS STABLE MONTH-OVER-MONTH"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_75(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct > _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_76(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = None
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_77(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "XXincreasingXX"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_78(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "INCREASING"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_79(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = None
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_80(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(None):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_81(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = None
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_82(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "XXdecreasingXX"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_83(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "DECREASING"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_84(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = None

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_85(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(None):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_86(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=None,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_87(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=None,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_88(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=None,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_89(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=None,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_90(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=None,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_91(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=None,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_92(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=None,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_93(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_94(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_95(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_96(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta_pct=delta_pct,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_97(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            trend=trend,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_98(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            recommendation=recommendation,
        )
    def xǁServiceCostComparisonEngineǁcompute__mutmut_99(  # noqa: PLR0913
        self,
        service_name: str,
        current_month: str,
        current_days: int,
        previous_month: str,
        previous_days: int,
        current_pods: list[dict[str, object]],
        previous_pods: list[dict[str, object]],
        cpu_price_per_core_hour: float,
        memory_price_per_gb_hour: float,
    ) -> ServiceCostComparison:
        current = _compute_month_cost(
            current_month,
            current_days,
            current_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )
        previous = _compute_month_cost(
            previous_month,
            previous_days,
            previous_pods,
            cpu_price_per_core_hour,
            memory_price_per_gb_hour,
        )

        if current.total_cost == 0.0 and previous.total_cost == 0.0:
            return ServiceCostComparison(
                service_name=service_name,
                current_month=current,
                previous_month=previous,
                trend="no_data",
                recommendation="No metrics data available — check Prometheus connectivity",
            )

        delta = round(current.total_cost - previous.total_cost, 2)
        if previous.total_cost > 0:
            delta_pct = round((delta / previous.total_cost) * 100.0, 1)
        else:
            delta_pct = 100.0 if current.total_cost > 0 else 0.0

        if abs(delta_pct) < _SIGNIFICANT_TREND_PCT:
            trend = "stable"
            recommendation = "Cost is stable month-over-month"
        elif delta_pct >= _SIGNIFICANT_TREND_PCT:
            trend = "increasing"
            recommendation = f"Cost increased by {abs(delta_pct):.0f}% — review scaling decisions"
        else:
            trend = "decreasing"
            recommendation = (
                f"Cost decreased by {abs(delta_pct):.0f}% — optimization efforts paying off"
            )

        return ServiceCostComparison(
            service_name=service_name,
            current_month=current,
            previous_month=previous,
            cost_delta=delta,
            cost_delta_pct=delta_pct,
            trend=trend,
            )

mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['_mutmut_orig'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_1'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_2'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_3'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_4'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_5'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_6'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_7'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_8'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_9'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_10'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_11'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_12'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_13'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_14'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_15'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_16'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_17'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_18'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_19'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_20'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_21'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_22'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_23'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_24'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_25'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_26'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_27'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_28'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_29'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_30'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_31'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_32'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_33'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_34'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_35'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_36'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_37'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_38'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_39'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_40'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_41'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_42'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_43'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_44'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_45'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_46'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_47'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_48'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_49'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_50'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_51'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_52'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_53'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_54'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_55'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_56'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_57'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_58'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_59'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_60'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_61'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_62'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_63'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_64'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_65'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_66'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_67'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_68'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_69'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_70'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_71'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_72'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_73'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_74'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_75'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_76'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_77'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_78'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_79'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_80'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_81'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_82'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_83'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_84'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_85'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_86'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_87'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_88'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_89'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_90'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_91'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_92'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_93'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_94'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_94 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_95'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_95 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_96'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_96 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_97'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_97 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_98'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_98 # type: ignore # mutmut generated
mutants_xǁServiceCostComparisonEngineǁcompute__mutmut['xǁServiceCostComparisonEngineǁcompute__mutmut_99'] = ServiceCostComparisonEngine.xǁServiceCostComparisonEngineǁcompute__mutmut_99 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_month_cost__mutmut)
def _compute_month_cost(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_orig(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_1(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_2(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=None,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_3(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=None,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_4(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=None,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_5(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=None,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_6(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=None,
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_7(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_8(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_9(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_10(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_11(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_12(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=1.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_13(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=1.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_14(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=1.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_15(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = None
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_16(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days / 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_17(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 25
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_18(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = None
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_19(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = None
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_20(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 1.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_21(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = None

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_22(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 1.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_23(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = None
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_24(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(None)
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_25(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get(None))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_26(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("XXcpu_coresXX"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_27(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("CPU_CORES"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_28(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = None
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_29(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(None)
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_30(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get(None))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_31(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("XXmemory_gbXX"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_32(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("MEMORY_GB"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_33(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = None
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_34(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(None, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_35(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, None)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_36(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_37(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, )
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_38(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price / hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_39(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu / cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_40(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 3)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_41(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = None
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_42(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(None, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_43(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, None)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_44(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_45(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, )
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_46(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price / hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_47(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem / mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_48(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 3)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_49(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu = cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_50(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu -= cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_51(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem = mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_52(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem -= mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_53(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            None
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_54(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=None,
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_55(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=None,
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_56(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=None,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_57(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=None,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_58(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=None,
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_59(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_60(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_61(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_62(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_63(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_64(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(None),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_65(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get(None, "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_66(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", None)),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_67(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_68(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", )),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_69(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("XXpod_nameXX", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_70(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("POD_NAME", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_71(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "XXXX")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_72(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(None),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_73(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get(None, "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_74(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", None)),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_75(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_76(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", )),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_77(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("XXnamespaceXX", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_78(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("NAMESPACE", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_79(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "XXXX")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_80(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(None, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_81(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, None),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_82(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_83(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, ),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_84(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost - mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_85(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 3),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_86(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=None,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_87(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=None,
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_88(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=None,
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_89(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=None,
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_90(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=None,
    )


def x__compute_month_cost__mutmut_91(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_92(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_93(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_94(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_95(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        )


def x__compute_month_cost__mutmut_96(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(None, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_97(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, None),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_98(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_99(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, ),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_100(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu - total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_101(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 3),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_102(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(None, 2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_103(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, None),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_104(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(2),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_105(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, ),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_106(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 3),
        memory_cost=round(total_mem, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_107(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(None, 2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_108(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, None),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_109(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(2),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_110(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, ),
        pod_breakdown=breakdown,
    )


def x__compute_month_cost__mutmut_111(
    month: str,
    days: int,
    pods: list[dict[str, object]],
    cpu_price: float,
    mem_price: float,
) -> MonthCost:
    if not pods:
        return MonthCost(
            month=month,
            total_cost=0.0,
            cpu_cost=0.0,
            memory_cost=0.0,
            pod_breakdown=[],
        )

    hours = days * 24
    breakdown: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0

    for p in pods:
        cpu = _as_float(p.get("cpu_cores"))
        mem = _as_float(p.get("memory_gb"))
        cpu_cost = round(cpu * cpu_price * hours, 2)
        mem_cost = round(mem * mem_price * hours, 2)
        total_cpu += cpu_cost
        total_mem += mem_cost
        breakdown.append(
            ServiceCostBreakdown(
                pod_name=str(p.get("pod_name", "")),
                namespace=str(p.get("namespace", "")),
                cpu_cost=cpu_cost,
                memory_cost=mem_cost,
                total_cost=round(cpu_cost + mem_cost, 2),
            )
        )

    return MonthCost(
        month=month,
        total_cost=round(total_cpu + total_mem, 2),
        cpu_cost=round(total_cpu, 2),
        memory_cost=round(total_mem, 3),
        pod_breakdown=breakdown,
    )

mutants_x__compute_month_cost__mutmut['_mutmut_orig'] = x__compute_month_cost__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_1'] = x__compute_month_cost__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_2'] = x__compute_month_cost__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_3'] = x__compute_month_cost__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_4'] = x__compute_month_cost__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_5'] = x__compute_month_cost__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_6'] = x__compute_month_cost__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_7'] = x__compute_month_cost__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_8'] = x__compute_month_cost__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_9'] = x__compute_month_cost__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_10'] = x__compute_month_cost__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_11'] = x__compute_month_cost__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_12'] = x__compute_month_cost__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_13'] = x__compute_month_cost__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_14'] = x__compute_month_cost__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_15'] = x__compute_month_cost__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_16'] = x__compute_month_cost__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_17'] = x__compute_month_cost__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_18'] = x__compute_month_cost__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_19'] = x__compute_month_cost__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_20'] = x__compute_month_cost__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_21'] = x__compute_month_cost__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_22'] = x__compute_month_cost__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_23'] = x__compute_month_cost__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_24'] = x__compute_month_cost__mutmut_24 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_25'] = x__compute_month_cost__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_26'] = x__compute_month_cost__mutmut_26 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_27'] = x__compute_month_cost__mutmut_27 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_28'] = x__compute_month_cost__mutmut_28 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_29'] = x__compute_month_cost__mutmut_29 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_30'] = x__compute_month_cost__mutmut_30 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_31'] = x__compute_month_cost__mutmut_31 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_32'] = x__compute_month_cost__mutmut_32 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_33'] = x__compute_month_cost__mutmut_33 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_34'] = x__compute_month_cost__mutmut_34 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_35'] = x__compute_month_cost__mutmut_35 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_36'] = x__compute_month_cost__mutmut_36 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_37'] = x__compute_month_cost__mutmut_37 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_38'] = x__compute_month_cost__mutmut_38 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_39'] = x__compute_month_cost__mutmut_39 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_40'] = x__compute_month_cost__mutmut_40 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_41'] = x__compute_month_cost__mutmut_41 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_42'] = x__compute_month_cost__mutmut_42 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_43'] = x__compute_month_cost__mutmut_43 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_44'] = x__compute_month_cost__mutmut_44 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_45'] = x__compute_month_cost__mutmut_45 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_46'] = x__compute_month_cost__mutmut_46 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_47'] = x__compute_month_cost__mutmut_47 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_48'] = x__compute_month_cost__mutmut_48 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_49'] = x__compute_month_cost__mutmut_49 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_50'] = x__compute_month_cost__mutmut_50 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_51'] = x__compute_month_cost__mutmut_51 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_52'] = x__compute_month_cost__mutmut_52 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_53'] = x__compute_month_cost__mutmut_53 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_54'] = x__compute_month_cost__mutmut_54 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_55'] = x__compute_month_cost__mutmut_55 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_56'] = x__compute_month_cost__mutmut_56 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_57'] = x__compute_month_cost__mutmut_57 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_58'] = x__compute_month_cost__mutmut_58 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_59'] = x__compute_month_cost__mutmut_59 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_60'] = x__compute_month_cost__mutmut_60 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_61'] = x__compute_month_cost__mutmut_61 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_62'] = x__compute_month_cost__mutmut_62 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_63'] = x__compute_month_cost__mutmut_63 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_64'] = x__compute_month_cost__mutmut_64 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_65'] = x__compute_month_cost__mutmut_65 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_66'] = x__compute_month_cost__mutmut_66 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_67'] = x__compute_month_cost__mutmut_67 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_68'] = x__compute_month_cost__mutmut_68 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_69'] = x__compute_month_cost__mutmut_69 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_70'] = x__compute_month_cost__mutmut_70 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_71'] = x__compute_month_cost__mutmut_71 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_72'] = x__compute_month_cost__mutmut_72 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_73'] = x__compute_month_cost__mutmut_73 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_74'] = x__compute_month_cost__mutmut_74 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_75'] = x__compute_month_cost__mutmut_75 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_76'] = x__compute_month_cost__mutmut_76 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_77'] = x__compute_month_cost__mutmut_77 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_78'] = x__compute_month_cost__mutmut_78 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_79'] = x__compute_month_cost__mutmut_79 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_80'] = x__compute_month_cost__mutmut_80 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_81'] = x__compute_month_cost__mutmut_81 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_82'] = x__compute_month_cost__mutmut_82 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_83'] = x__compute_month_cost__mutmut_83 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_84'] = x__compute_month_cost__mutmut_84 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_85'] = x__compute_month_cost__mutmut_85 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_86'] = x__compute_month_cost__mutmut_86 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_87'] = x__compute_month_cost__mutmut_87 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_88'] = x__compute_month_cost__mutmut_88 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_89'] = x__compute_month_cost__mutmut_89 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_90'] = x__compute_month_cost__mutmut_90 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_91'] = x__compute_month_cost__mutmut_91 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_92'] = x__compute_month_cost__mutmut_92 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_93'] = x__compute_month_cost__mutmut_93 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_94'] = x__compute_month_cost__mutmut_94 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_95'] = x__compute_month_cost__mutmut_95 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_96'] = x__compute_month_cost__mutmut_96 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_97'] = x__compute_month_cost__mutmut_97 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_98'] = x__compute_month_cost__mutmut_98 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_99'] = x__compute_month_cost__mutmut_99 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_100'] = x__compute_month_cost__mutmut_100 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_101'] = x__compute_month_cost__mutmut_101 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_102'] = x__compute_month_cost__mutmut_102 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_103'] = x__compute_month_cost__mutmut_103 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_104'] = x__compute_month_cost__mutmut_104 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_105'] = x__compute_month_cost__mutmut_105 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_106'] = x__compute_month_cost__mutmut_106 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_107'] = x__compute_month_cost__mutmut_107 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_108'] = x__compute_month_cost__mutmut_108 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_109'] = x__compute_month_cost__mutmut_109 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_110'] = x__compute_month_cost__mutmut_110 # type: ignore # mutmut generated
mutants_x__compute_month_cost__mutmut['x__compute_month_cost__mutmut_111'] = x__compute_month_cost__mutmut_111 # type: ignore # mutmut generated
mutants_x_current_month_str__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_current_month_str__mutmut)
def current_month_str() -> str:
    from datetime import datetime

    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def x_current_month_str__mutmut_orig() -> str:
    from datetime import datetime

    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def x_current_month_str__mutmut_1() -> str:
    from datetime import datetime

    now = None
    return f"{now.year}-{now.month:02d}"

mutants_x_current_month_str__mutmut['_mutmut_orig'] = x_current_month_str__mutmut_orig # type: ignore # mutmut generated
mutants_x_current_month_str__mutmut['x_current_month_str__mutmut_1'] = x_current_month_str__mutmut_1 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_previous_month_str__mutmut)
def previous_month_str() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_orig() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_1() -> str:
    from datetime import datetime

    now = None
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_2() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month != 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_3() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 2:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_4() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 1:
        return f"{now.year + 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_5() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 2}-12"
    return f"{now.year}-{now.month - 1:02d}"


def x_previous_month_str__mutmut_6() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month + 1:02d}"


def x_previous_month_str__mutmut_7() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 2:02d}"

mutants_x_previous_month_str__mutmut['_mutmut_orig'] = x_previous_month_str__mutmut_orig # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_1'] = x_previous_month_str__mutmut_1 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_2'] = x_previous_month_str__mutmut_2 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_3'] = x_previous_month_str__mutmut_3 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_4'] = x_previous_month_str__mutmut_4 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_5'] = x_previous_month_str__mutmut_5 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_6'] = x_previous_month_str__mutmut_6 # type: ignore # mutmut generated
mutants_x_previous_month_str__mutmut['x_previous_month_str__mutmut_7'] = x_previous_month_str__mutmut_7 # type: ignore # mutmut generated
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
