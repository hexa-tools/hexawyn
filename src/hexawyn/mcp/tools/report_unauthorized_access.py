"""MCP tool: report_unauthorized_access."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.report_unauthorized_access.command import (
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.report_unauthorized_access.report_unauthorized_access_use_case import (
    ReportUnauthorizedAccessUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def report_unauthorized_access() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        use_case = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_unauthorized_access)
