"""MCP tool: report_unauthorized_access — unauthorized access attempts in
business language with source attribution and alert level."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.report_unauthorized_access.report_unauthorized_access_use_case import (  # noqa: E501
    ReportUnauthorizedAccessUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def report_unauthorized_access() -> dict[str, object]:
    from hexawyn.application.service.report_unauthorized_access_service import (
        ReportUnauthorizedAccessService,
    )
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        adapter = build_unauthorized_access_adapter()
        service = ReportUnauthorizedAccessService(access_port=adapter)
        use_case = ReportUnauthorizedAccessUseCase(service=service)
        response = use_case.execute(ReportUnauthorizedAccessCommand())
        r = response.result
        return {
            "period_label": r.period_label,
            "attempt_count": r.attempt_count,
            "window_minutes": r.window_minutes,
            "source_type": r.source_type,
            "alert_level": r.alert_level,
            "has_data": r.has_data,
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Dernieres 30 minutes",
            "attempt_count": 0,
            "window_minutes": 30,
            "source_type": "unknown",
            "alert_level": "low",
            "has_data": False,
            "warning": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_unauthorized_access)
