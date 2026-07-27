"""MCP tool: analyze_incident_cost — Analyze incident financial impact."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.analyze_incident_cost.analyze_incident_cost_use_case import (  # noqa: E501
    AnalyzeIncidentCostUseCase,
)
from hexawyn.application.use_case.finops.analyze_incident_cost.command import (
    AnalyzeIncidentCostCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def analyze_incident_cost(incident_ref: str = "yesterday") -> dict[str, object]:
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        service = AnalyzeIncidentCostUseCase(incident_cost_port=build_incident_cost_adapter())
        use_case = AnalyzeIncidentCostUseCase(service=service)  # type: ignore
        r = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = r.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "total_cost_eur": report.total_cost_eur,
            "error": None,
        }
    except Exception as exc:
        return {"business_service_name": "", "downtime_minutes": 0, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_incident_cost)
