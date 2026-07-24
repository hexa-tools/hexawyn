"""MCP tool: report_stale_credentials."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.report_stale_credentials.command import (
    ReportStaleCredentialsCommand,
)
from hexawyn.application.use_case.report_stale_credentials.report_stale_credentials_use_case import (
    ReportStaleCredentialsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def report_stale_credentials() -> dict[str, object]:
    from hexawyn.mcp.server import build_stale_credentials_adapter

    try:
        use_case = ReportStaleCredentialsUseCase(credentials_port=build_stale_credentials_adapter())
        _ = use_case.execute(ReportStaleCredentialsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_stale_credentials)
