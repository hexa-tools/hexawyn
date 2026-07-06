"""MCP tool: compare_service_cost — compare service cost month-over-month."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_command import (
    CompareServiceCostCommand,
)
from hexawyn.application.use_case.compare_service_cost.compare_service_cost_use_case import (
    CompareServiceCostUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compare_service_cost(
    service_name: str,
    cpu_price_per_core_hour: float = 0.03,
    memory_price_per_gb_hour: float = 0.01,
) -> dict[str, object]:
    """Compare infrastructure cost of a service: current month vs previous month.

    Computes total CPU + memory cost, provides pod-level breakdown,
    and a trend indicator (increasing/decreasing/stable).

    Args:
        service_name: Name of the service to analyze.
        cpu_price_per_core_hour: CPU pricing in currency per core per hour.
        memory_price_per_gb_hour: Memory pricing in currency per GB per hour.
    """
    from hexawyn.application.service.compare_service_cost_service import (
        CompareServiceCostService,
    )
    from hexawyn.mcp.server import build_service_cost_adapter

    try:
        adapter = build_service_cost_adapter()
        service = CompareServiceCostService(cost_port=adapter)
        use_case = CompareServiceCostUseCase(service=service)
        response = use_case.execute(
            CompareServiceCostCommand(
                service_name=service_name,
                cpu_price_per_core_hour=cpu_price_per_core_hour,
                memory_price_per_gb_hour=memory_price_per_gb_hour,
            )
        )
        r = response.result
        cm = r.current_month
        pm = r.previous_month
        return {
            "service_name": r.service_name,
            "trend": r.trend,
            "cost_delta": r.cost_delta,
            "cost_delta_pct": r.cost_delta_pct,
            "recommendation": r.recommendation,
            "current_month": {
                "month": cm.month if cm else "",
                "total_cost": cm.total_cost if cm else 0.0,
                "cpu_cost": cm.cpu_cost if cm else 0.0,
                "memory_cost": cm.memory_cost if cm else 0.0,
                "pod_breakdown": [
                    {
                        "pod_name": b.pod_name,
                        "namespace": b.namespace,
                        "cpu_cost": b.cpu_cost,
                        "memory_cost": b.memory_cost,
                        "total_cost": b.total_cost,
                    }
                    for b in (cm.pod_breakdown if cm else [])
                ],
            },
            "previous_month": {
                "month": pm.month if pm else "",
                "total_cost": pm.total_cost if pm else 0.0,
                "cpu_cost": pm.cpu_cost if pm else 0.0,
                "memory_cost": pm.memory_cost if pm else 0.0,
                "pod_breakdown": [
                    {
                        "pod_name": b.pod_name,
                        "namespace": b.namespace,
                        "cpu_cost": b.cpu_cost,
                        "memory_cost": b.memory_cost,
                        "total_cost": b.total_cost,
                    }
                    for b in (pm.pod_breakdown if pm else [])
                ],
            },
            "error": None,
        }
    except Exception as exc:
        return {
            "service_name": service_name,
            "trend": "error",
            "cost_delta": 0.0,
            "cost_delta_pct": 0.0,
            "recommendation": "",
            "current_month": None,
            "previous_month": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compare_service_cost)
