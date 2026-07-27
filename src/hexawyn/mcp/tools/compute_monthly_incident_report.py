"""MCP tool: compute_monthly_incident_report — monthly incident summary report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compute_monthly_incident_report.command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.use_case.finops.compute_monthly_incident_report.compute_monthly_incident_report_use_case import (  # noqa: E501
    ComputeMonthlyIncidentReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_monthly_incident_report(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_monthly_incident_report)
