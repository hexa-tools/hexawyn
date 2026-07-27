"""MCP tool: generate_weekly_reliability_report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.generate_weekly_reliability_report_use_case import (  # noqa: E501
    GenerateWeeklyReliabilityReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def generate_weekly_reliability_report() -> dict[str, object]:
    from hexawyn.mcp.server import build_reliability_report_adapter

    try:
        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=build_reliability_report_adapter()
        )
        _ = use_case.execute(GenerateWeeklyReliabilityReportCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(generate_weekly_reliability_report)
