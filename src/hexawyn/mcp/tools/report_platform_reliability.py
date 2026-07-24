"""MCP tool: report_platform_reliability."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.report_platform_reliability.command import (
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.use_case.report_platform_reliability.report_platform_reliability_use_case import (
    ReportPlatformReliabilityUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def report_platform_reliability(period="test") -> dict[str, object]:
    from hexawyn.mcp.server import build_platform_reliability_adapter

    try:
        use_case = ReportPlatformReliabilityUseCase(reliability_port=build_platform_reliability_adapter())
        _ = use_case.execute(ReportPlatformReliabilityCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_platform_reliability)
