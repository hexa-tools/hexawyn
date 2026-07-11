"""MCP tool: analyze_incident_cost — translates an incident's downtime into a
traceable business financial impact, in executive language."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_command import (  # noqa: E501
    AnalyzeIncidentCostCommand,
)
from hexawyn.application.use_case.analyze_incident_cost.analyze_incident_cost_use_case import (  # noqa: E501
    AnalyzeIncidentCostUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.incident_cost import CalculationBasis


def analyze_incident_cost(incident_ref: str = "yesterday") -> dict[str, object]:
    """Estimate the business financial impact of an incident.

    Returns the affected business service, downtime, revenue impact, support
    cost and SLA penalty (each in euros), the number of impacted business
    services, and the resolution time. Every euro amount is deterministic and
    traceable via ``calculation_basis``. When ``revenue_per_minute`` is not
    configured, no euro amount is produced — an explanation is returned instead.
    """
    from hexawyn.application.service.analyze_incident_cost_service import (
        AnalyzeIncidentCostService,
    )
    from hexawyn.mcp.server import build_incident_cost_adapter

    try:
        adapter = build_incident_cost_adapter()
        service = AnalyzeIncidentCostService(incident_cost_port=adapter)
        use_case = AnalyzeIncidentCostUseCase(service=service)
        response = use_case.execute(AnalyzeIncidentCostCommand(incident_ref=incident_ref))
        report = response.result
        return {
            "business_service_name": report.business_service_name,
            "downtime_minutes": report.downtime_minutes,
            "revenue_impact_eur": report.revenue_impact_eur,
            "support_cost_eur": report.support_cost_eur,
            "sla_penalty_eur": report.sla_penalty_eur,
            "total_cost_eur": report.total_cost_eur,
            "impacted_service_count": report.impacted_service_count,
            "resolved_at": report.resolved_at,
            "config_available": report.config_available,
            "explanation": report.explanation,
            "calculation_basis": _serialize_basis(report.calculation_basis),
            "error": None,
        }
    except Exception as exc:
        return {
            "business_service_name": "",
            "downtime_minutes": 0,
            "revenue_impact_eur": None,
            "support_cost_eur": None,
            "sla_penalty_eur": None,
            "total_cost_eur": None,
            "impacted_service_count": 0,
            "resolved_at": "",
            "config_available": False,
            "explanation": "",
            "calculation_basis": None,
            "error": str(exc),
        }


def _serialize_basis(basis: CalculationBasis | None) -> dict[str, object] | None:
    if basis is None:
        return None
    return {
        "formula": basis.formula,
        "config_values_used": basis.config_values_used,
        "source_metrics": basis.source_metrics,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_incident_cost)
