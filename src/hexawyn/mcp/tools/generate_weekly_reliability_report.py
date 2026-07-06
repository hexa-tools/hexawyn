"""MCP tool: generate_weekly_reliability_report — weekly SRE report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.generate_weekly_reliability_report.generate_weekly_reliability_report_use_case import (
    GenerateWeeklyReliabilityReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def generate_weekly_reliability_report(
    window_days: int = 7,
) -> dict[str, object]:
    """Generate a weekly reliability report for all production services.

    Queries Prometheus for uptime, error rates, p99 latency, SLO compliance,
    and top incidents across the specified window.

    Args:
        window_days: Analysis window in days (default: 7).
    """
    from hexawyn.application.service.generate_weekly_reliability_report_service import (
        GenerateWeeklyReliabilityReportService,
    )
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        adapter = build_reliability_report_adapter()
        service = GenerateWeeklyReliabilityReportService(reliability_port=adapter)
        use_case = GenerateWeeklyReliabilityReportUseCase(service=service)
        response = use_case.execute(GenerateWeeklyReliabilityReportCommand(window_days=window_days))
        r = response.result
        return {
            "report_period_start": r.report_period_start,
            "report_period_end": r.report_period_end,
            "services": [
                {
                    "service_name": s.service_name,
                    "uptime_pct": s.uptime_pct,
                    "error_rate": s.error_rate,
                    "p99_latency_ms": s.p99_latency_ms,
                    "slo_target": s.slo_target,
                    "slo_status": s.slo_status,
                    "downtime_minutes": s.downtime_minutes,
                    "data_gap_minutes": s.data_gap_minutes,
                    "created_mid_week": s.created_mid_week,
                }
                for s in r.services
            ],
            "top_incidents": [
                {
                    "service_name": i.service_name,
                    "timestamp": i.timestamp,
                    "duration_minutes": i.duration_minutes,
                    "error_rate": i.error_rate,
                    "impact_score": i.impact_score,
                    "description": i.description,
                }
                for i in r.top_incidents
            ],
            "total_incident_count": r.total_incident_count,
            "health_score": r.health_score,
            "slo_pass_count": r.slo_pass_count,
            "slo_fail_count": r.slo_fail_count,
            "total_services": r.total_services,
            "error": None,
        }
    except Exception as exc:
        return {
            "report_period_start": "",
            "report_period_end": "",
            "services": [],
            "top_incidents": [],
            "total_incident_count": 0,
            "health_score": 0.0,
            "slo_pass_count": 0,
            "slo_fail_count": 0,
            "total_services": 0,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(generate_weekly_reliability_report)
