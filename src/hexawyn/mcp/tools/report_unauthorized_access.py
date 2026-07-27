"""MCP tool: report_unauthorized_access."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.report_unauthorized_access.command import (
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.security.report_unauthorized_access.report_unauthorized_access_use_case import (  # noqa: E501
    ReportUnauthorizedAccessUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def report_unauthorized_access() -> dict[str, object]:
    from hexawyn.mcp.server import build_unauthorized_access_adapter

    try:
        service = ReportUnauthorizedAccessUseCase(access_port=build_unauthorized_access_adapter())
        use_case = ReportUnauthorizedAccessUseCase(service=service)  # type: ignore
        _ = use_case.execute(ReportUnauthorizedAccessCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_unauthorized_access)
