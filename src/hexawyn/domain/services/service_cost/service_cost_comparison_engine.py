from __future__ import annotations

from hexawyn.domain.models.service_cost_comparison import (
    MonthCost,
    ServiceCostBreakdown,
    ServiceCostComparison,
)

_SIGNIFICANT_TREND_PCT = 10.0


class ServiceCostComparisonEngine:
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


def current_month_str() -> str:
    from datetime import datetime

    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def previous_month_str() -> str:
    from datetime import datetime

    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0
