from __future__ import annotations

from datetime import datetime

from hexawyn.application.ports.driven.service_cost_port import (
    PodResourceSnapshotData,
    ServiceCostPort,
)
from hexawyn.application.use_case.compare_service_cost.command import CompareServiceCostCommand
from hexawyn.application.use_case.compare_service_cost.response import CompareServiceCostResponse
from hexawyn.domain.models.service_cost_comparison import (
    MonthCost,
    ServiceCostBreakdown,
    ServiceCostComparison,
)


def _current_month_str() -> str:
    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def _previous_month_str() -> str:
    now = datetime.now()
    if now.month == 1:
        return f"{now.year - 1}-12"
    return f"{now.year}-{now.month - 1:02d}"


def _compute_month_cost(
    snapshots: list[PodResourceSnapshotData], cpu_price: float, memory_price: float
) -> MonthCost:
    breakdowns: list[ServiceCostBreakdown] = []
    total_cpu = 0.0
    total_mem = 0.0
    for s in snapshots:
        cpu_c = s["cpu_cores"] * cpu_price
        mem_c = s["memory_gb"] * memory_price
        total_cpu += cpu_c
        total_mem += mem_c
        breakdowns.append(
            ServiceCostBreakdown(
                pod_name=s["pod_name"],
                namespace=s["namespace"],
                cpu_cost=cpu_c,
                memory_cost=mem_c,
                total_cost=cpu_c + mem_c,
            )
        )
    return MonthCost(
        month=snapshots[0]["month"] if snapshots else "",
        total_cost=total_cpu + total_mem,
        cpu_cost=total_cpu,
        memory_cost=total_mem,
        pod_breakdown=breakdowns,
    )


class CompareServiceCostUseCase:
    def __init__(self, port: ServiceCostPort) -> None:
        self._port = port

    def execute(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        service_name = command.service_name
        cpu_price = command.cpu_price_per_core_hour
        mem_price = command.memory_price_per_gb_hour

        current_month = _current_month_str()
        previous_month = _previous_month_str()

        current_snapshots = self._port.fetch_pod_resources(service_name, current_month)
        previous_snapshots = self._port.fetch_pod_resources(service_name, previous_month)

        cm = _compute_month_cost(current_snapshots, cpu_price, mem_price)
        pm = _compute_month_cost(previous_snapshots, cpu_price, mem_price)

        delta = cm.total_cost - pm.total_cost
        delta_pct = (delta / pm.total_cost * 100.0) if pm.total_cost > 0 else 0.0

        if delta_pct > 5:
            trend = "increasing"
            recommendation = "Cost is trending up — investigate pod resource requests"
        elif delta_pct < -5:
            trend = "decreasing"
            recommendation = "Cost is trending down — verify no missing services"
        else:
            trend = "stable"
            recommendation = "Cost is stable — no action needed"

        comparison = ServiceCostComparison(
            service_name=service_name,
            current_month=cm,
            previous_month=pm,
            cost_delta=round(delta, 2),
            cost_delta_pct=round(delta_pct, 1),
            trend=trend,
            recommendation=recommendation,
        )
        return CompareServiceCostResponse(result=comparison)
