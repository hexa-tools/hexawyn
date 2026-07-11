"""MCP tool: project_budget — projects infrastructure cost over a multi-month
horizon with optimistic / realistic / pessimistic scenarios and budget alerts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.project_budget.project_budget_command import (
    ProjectBudgetCommand,
)
from hexawyn.application.use_case.project_budget.project_budget_use_case import (
    ProjectBudgetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.budget_projection import ProjectedMonth


def project_budget(
    horizon_months: int = 6,
    history_months: int = 6,
    budget_threshold_usd: float | None = None,
    exclude_months: list[str] | None = None,
) -> dict[str, object]:
    """Project infrastructure cost for the next N months at the current growth.

    Returns the projected monthly cost with optimistic / realistic / pessimistic
    scenarios, a per-category breakdown (compute / storage / network), the
    detected growth model (linear / exponential / decreasing), a confidence
    level based on available history, and a budget-threshold alert with the
    month the budget is first exceeded.
    """
    from hexawyn.application.service.project_budget_service import ProjectBudgetService
    from hexawyn.mcp.server import build_budget_projection_adapter

    try:
        adapter = build_budget_projection_adapter()
        service = ProjectBudgetService(budget_port=adapter)
        use_case = ProjectBudgetUseCase(service=service)
        response = use_case.execute(
            ProjectBudgetCommand(
                horizon_months=horizon_months,
                history_months=history_months,
                budget_threshold_usd=budget_threshold_usd,
                exclude_months=exclude_months or [],
            )
        )
        report = response.result
        return {
            "current_monthly_usd": report.current_monthly_usd,
            "growth_rate_pct": report.growth_rate_pct,
            "growth_model": report.growth_model,
            "confidence": report.confidence,
            "six_month_total_realistic": report.six_month_total_realistic,
            "budget_threshold_usd": report.budget_threshold_usd,
            "budget_exceeded": report.budget_exceeded,
            "budget_breach_month": report.budget_breach_month,
            "warning": report.warning,
            "projected_months": [_serialize(month) for month in report.projected_months],
            "error": None,
        }
    except Exception as exc:
        return {
            "current_monthly_usd": 0.0,
            "growth_rate_pct": 0.0,
            "growth_model": "flat",
            "confidence": "low",
            "six_month_total_realistic": 0.0,
            "budget_threshold_usd": budget_threshold_usd,
            "budget_exceeded": False,
            "budget_breach_month": None,
            "warning": "",
            "projected_months": [],
            "error": str(exc),
        }


def _serialize(month: ProjectedMonth) -> dict[str, object]:
    return {
        "month_offset": month.month_offset,
        "month_label": month.month_label,
        "realistic_usd": month.realistic_usd,
        "optimistic_usd": month.optimistic_usd,
        "pessimistic_usd": month.pessimistic_usd,
        "by_category": month.by_category,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(project_budget)
