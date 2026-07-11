"""MCP tool: compute_budget_intelligence — monitors projected cloud spend
against a configured monthly budget with alerting and recommendations."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.use_case.compute_budget_intelligence.compute_budget_intelligence_use_case import (  # noqa: E501
    ComputeBudgetIntelligenceUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.budget_intelligence import BudgetAlertRecommendation


def compute_budget_intelligence(period: str = "current") -> dict[str, object]:
    from hexawyn.application.service.compute_budget_intelligence_service import (
        ComputeBudgetIntelligenceService,
    )
    from hexawyn.mcp.server import build_budget_intelligence_adapter

    try:
        adapter = build_budget_intelligence_adapter()
        service = ComputeBudgetIntelligenceService(budget_intelligence_port=adapter)
        use_case = ComputeBudgetIntelligenceUseCase(service=service)
        response = use_case.execute(ComputeBudgetIntelligenceCommand(period=period))
        report = response.result
        return {
            "period_label": report.period_label,
            "current_spend_eur": report.current_spend_eur,
            "projected_spend_eur": report.projected_spend_eur,
            "budget_monthly_eur": report.budget_monthly_eur,
            "overshoot_pct": report.overshoot_pct,
            "budget_exceeded": report.budget_exceeded,
            "recommendations": [_serialize_rec(rec) for rec in report.recommendations],
            "config_available": report.config_available,
            "explanation": report.explanation,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": period,
            "current_spend_eur": 0.0,
            "projected_spend_eur": 0.0,
            "budget_monthly_eur": 0.0,
            "overshoot_pct": 0.0,
            "budget_exceeded": False,
            "recommendations": [],
            "config_available": False,
            "explanation": "",
            "error": str(exc),
        }


def _serialize_rec(rec: BudgetAlertRecommendation) -> dict[str, object]:
    return {"action": rec.action, "description": rec.description}


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_budget_intelligence)
