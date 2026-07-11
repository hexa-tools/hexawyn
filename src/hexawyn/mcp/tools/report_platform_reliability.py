"""MCP tool: report_platform_reliability — CTO-facing platform reliability
report in plain business language, with a technical drill-down available."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.use_case.report_platform_reliability.report_platform_reliability_use_case import (  # noqa: E501
    ReportPlatformReliabilityUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.platform_reliability import IncidentSummary


def report_platform_reliability(period: str) -> dict[str, object]:
    """Report platform reliability for a period in plain business language.

    Returns availability in human terms, the number of incidents by severity,
    the average resolution time with its trend vs the previous period, and an
    honest financial impact (only when pricing is configured). ``executive_summary``
    is a jargon-free, sub-five-sentence summary; ``incidents`` provides the
    technical drill-down on demand.
    """
    from hexawyn.application.service.report_platform_reliability_service import (
        ReportPlatformReliabilityService,
    )
    from hexawyn.mcp.server import build_platform_reliability_adapter

    try:
        adapter = build_platform_reliability_adapter()
        service = ReportPlatformReliabilityService(reliability_port=adapter)
        use_case = ReportPlatformReliabilityUseCase(service=service)
        response = use_case.execute(ReportPlatformReliabilityCommand(period=period))
        report = response.result
        return {
            "period_label": report.period_label,
            "uptime_pct": report.uptime_pct,
            "total_incidents": report.total_incidents,
            "major_count": report.major_count,
            "minor_count": report.minor_count,
            "avg_resolution_minutes": report.avg_resolution_minutes,
            "resolution_trend": report.resolution_trend,
            "resolution_delta_pct": report.resolution_delta_pct,
            "previous_avg_resolution_minutes": report.previous_avg_resolution_minutes,
            "financial_impact_eur": report.financial_impact_eur,
            "pricing_configured": report.pricing_configured,
            "has_major_incident": report.has_major_incident,
            "executive_summary": report.executive_summary,
            "incidents": [_serialize_incident(incident) for incident in report.incidents],
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": period,
            "uptime_pct": 0.0,
            "total_incidents": 0,
            "major_count": 0,
            "minor_count": 0,
            "avg_resolution_minutes": 0,
            "resolution_trend": "stable",
            "resolution_delta_pct": 0.0,
            "previous_avg_resolution_minutes": None,
            "financial_impact_eur": None,
            "pricing_configured": False,
            "has_major_incident": False,
            "executive_summary": "",
            "incidents": [],
            "error": str(exc),
        }


def _serialize_incident(incident: IncidentSummary) -> dict[str, object]:
    return {
        "date": incident.date,
        "severity": incident.severity,
        "downtime_minutes": incident.downtime_minutes,
        "root_cause": incident.root_cause,
        "resolved": incident.resolved,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_platform_reliability)
