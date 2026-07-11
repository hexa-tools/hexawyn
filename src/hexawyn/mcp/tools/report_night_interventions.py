"""MCP tool: report_night_interventions — average night interventions and
trend for Head of Engineering team workload assessment."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_command import (  # noqa: E501
    ReportNightInterventionsCommand,
)
from hexawyn.application.use_case.report_night_interventions.report_night_interventions_use_case import (  # noqa: E501
    ReportNightInterventionsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def report_night_interventions(history_months: int = 6) -> dict[str, object]:
    from hexawyn.application.service.report_night_interventions_service import (
        ReportNightInterventionsService,
    )
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        adapter = build_night_intervention_adapter()
        service = ReportNightInterventionsService(workload_port=adapter)
        use_case = ReportNightInterventionsUseCase(service=service)
        response = use_case.execute(ReportNightInterventionsCommand(history_months=history_months))
        r = response.result
        return {
            "period_label": r.period_label,
            "avg_interventions_per_night": r.avg_interventions_per_night,
            "previous_avg_per_night": r.previous_avg_per_night,
            "delta_pct": r.delta_pct,
            "trend": r.trend,
            "summary": r.summary,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Ce mois",
            "avg_interventions_per_night": 0.0,
            "previous_avg_per_night": None,
            "delta_pct": 0.0,
            "trend": "stable",
            "summary": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_night_interventions)
