"""MCP tool: generate_sla_report — executive quarterly SLA report for all
customer-facing services (uptime vs target, breaches, and reliability trend)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_command import (
    GenerateSlaReportCommand,
)
from hexawyn.application.use_case.generate_sla_report.generate_sla_report_use_case import (
    GenerateSlaReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.sla_report import ServiceSla, SlaBreach


def generate_sla_report(quarter: str) -> dict[str, object]:
    """Generate an executive SLA report for a quarter.

    Returns per-service uptime vs SLA target, all breaches (date, duration,
    impacted users, root-cause reference), mid-quarter proration for services
    onboarded late, and the quarter-over-quarter reliability trend. Output is
    chart-ready — no raw logs. Warns when incident data is missing rather than
    reporting a misleading 100% uptime.
    """
    from hexawyn.application.service.generate_sla_report_service import (
        GenerateSlaReportService,
    )
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        adapter = build_sla_report_adapter()
        service = GenerateSlaReportService(sla_port=adapter)
        use_case = GenerateSlaReportUseCase(service=service)
        response = use_case.execute(GenerateSlaReportCommand(quarter=quarter))
        report = response.result
        return {
            "quarter_label": report.quarter_label,
            "has_data": report.has_data,
            "overall_met_count": report.overall_met_count,
            "overall_breached_count": report.overall_breached_count,
            "trend": report.trend,
            "previous_avg_uptime_pct": report.previous_avg_uptime_pct,
            "current_avg_uptime_pct": report.current_avg_uptime_pct,
            "services": [_serialize_service(service_sla) for service_sla in report.services],
            "warning": report.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "quarter_label": quarter,
            "has_data": True,
            "overall_met_count": 0,
            "overall_breached_count": 0,
            "trend": "stable",
            "previous_avg_uptime_pct": None,
            "current_avg_uptime_pct": 0.0,
            "services": [],
            "warning": "",
            "error": str(exc),
        }


def _serialize_service(service: ServiceSla) -> dict[str, object]:
    return {
        "service_name": service.service_name,
        "sla_target_pct": service.sla_target_pct,
        "actual_uptime_pct": service.actual_uptime_pct,
        "met": service.met,
        "exceeded": service.exceeded,
        "breach_count": service.breach_count,
        "prorated": service.prorated,
        "coverage_days": service.coverage_days,
        "breaches": [_serialize_breach(breach) for breach in service.breaches],
    }


def _serialize_breach(breach: SlaBreach) -> dict[str, object]:
    return {
        "date": breach.date,
        "duration_minutes": breach.duration_minutes,
        "impacted_users": breach.impacted_users,
        "root_cause_ref": breach.root_cause_ref,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(generate_sla_report)
