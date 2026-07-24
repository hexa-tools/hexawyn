"""MCP tool: generate_sla_report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.generate_sla_report.command import GenerateSlaReportCommand
from hexawyn.application.use_case.generate_sla_report.generate_sla_report_use_case import (
    GenerateSlaReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def generate_sla_report(quarter="test") -> dict[str, object]:
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSlaReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSlaReportCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(generate_sla_report)
