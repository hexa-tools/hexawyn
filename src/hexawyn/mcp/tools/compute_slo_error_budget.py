"""MCP tool: compute_slo_error_budget — compute SLO error budget burn rate."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.compute_slo_error_budget.compute_slo_error_budget_command import (
    ComputeSLOErrorBudgetCommand,
)
from hexawyn.application.use_case.compute_slo_error_budget.compute_slo_error_budget_use_case import (
    ComputeSLOErrorBudgetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_slo_error_budget(
    service_name: str,
    slo_target: float = 0.999,
    rolling_window_days: int = 30,
) -> dict[str, object]:
    """Compute SLO error budget burn rate for a service.

    Queries Prometheus for actual success rate, computes total error budget,
    consumed budget, remaining budget, burn rate multiplier, and time-to-exhaustion.

    Args:
        service_name: Name of the service (e.g. 'payment-service').
        slo_target: SLO target as a decimal (e.g. 0.999 for 99.9%).
        rolling_window_days: Rolling window in days (default: 30).
    """
    from hexawyn.application.service.compute_slo_error_budget_service import (
        ComputeSLOErrorBudgetService,
    )
    from hexawyn.mcp.server import build_error_budget_adapter

    try:
        adapter = build_error_budget_adapter()
        service = ComputeSLOErrorBudgetService(error_budget_port=adapter)
        use_case = ComputeSLOErrorBudgetUseCase(service=service)
        response = use_case.execute(
            ComputeSLOErrorBudgetCommand(
                service_name=service_name,
                slo_target=slo_target,
                rolling_window_days=rolling_window_days,
            )
        )
        r = response.result
        return {
            "service_name": r.service_name,
            "slo_target": r.slo_target,
            "rolling_window_days": r.rolling_window_days,
            "total_budget_minutes": r.total_budget_minutes,
            "current_success_rate": r.current_success_rate,
            "error_rate": r.error_rate,
            "budget_consumed_minutes": r.budget_consumed_minutes,
            "budget_remaining_pct": r.budget_remaining_pct,
            "burn_rate": r.burn_rate,
            "time_to_exhaustion_days": r.time_to_exhaustion_days,
            "verdict": r.verdict,
            "recommendation": r.recommendation,
            "total_requests": r.total_requests,
            "successful_requests": r.successful_requests,
            "failed_requests": r.failed_requests,
            "error": None,
        }
    except Exception as exc:
        return {
            "service_name": service_name,
            "slo_target": slo_target,
            "rolling_window_days": rolling_window_days,
            "total_budget_minutes": 0.0,
            "current_success_rate": 0.0,
            "error_rate": 0.0,
            "budget_consumed_minutes": 0.0,
            "budget_remaining_pct": 0.0,
            "burn_rate": 0.0,
            "time_to_exhaustion_days": None,
            "verdict": "error",
            "recommendation": "",
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_slo_error_budget)
