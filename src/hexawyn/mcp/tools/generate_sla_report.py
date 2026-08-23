# mypy: ignore-errors
"""MCP tool: generate_sla_report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.generate_sla_report.command import (  # type: ignore
    GenerateSLAReportCommand,
)
from hexawyn.application.use_case.workloads.generate_sla_report.generate_sla_report_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    GenerateSLAReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def generate_sla_report(quarter: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_sla_report_adapter

    try:
        use_case = GenerateSLAReportUseCase(sla_port=build_sla_report_adapter())
        _ = use_case.execute(GenerateSLAReportCommand(quarter=quarter))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(generate_sla_report)
