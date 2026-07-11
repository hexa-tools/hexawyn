"""MCP tool: report_stale_credentials — unrotated credentials older than N days,
grouped by risk level, in business language."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.use_case.report_stale_credentials.report_stale_credentials_use_case import (  # noqa: E501
    ReportStaleCredentialsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.stale_credentials import StaleCredential


def report_stale_credentials(min_days: int = 90) -> dict[str, object]:
    from hexawyn.application.service.report_stale_credentials_service import (
        ReportStaleCredentialsService,
    )
    from hexawyn.mcp.server import build_stale_credentials_adapter

    try:
        adapter = build_stale_credentials_adapter()
        service = ReportStaleCredentialsService(credentials_port=adapter)
        use_case = ReportStaleCredentialsUseCase(service=service)
        response = use_case.execute(ReportStaleCredentialsCommand(min_days=min_days))
        r = response.result
        return {
            "period_label": r.period_label,
            "total_stale": r.total_stale,
            "critical_count": r.critical_count,
            "credentials": [_serialize(cred) for cred in r.credentials],
            "has_data": r.has_data,
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Rotation en cours",
            "total_stale": 0,
            "critical_count": 0,
            "credentials": [],
            "has_data": False,
            "warning": "",
            "error": str(exc),
        }


def _serialize(cred: StaleCredential) -> dict[str, object]:
    return {"name": cred.name, "risk_level": cred.risk_level, "days_unrotated": cred.days_unrotated}


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_stale_credentials)
