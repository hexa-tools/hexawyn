"""MCP tool: report_night_interventions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.report_night_interventions.command import (
    ReportNightInterventionsCommand,
)
from hexawyn.application.use_case.report_night_interventions.report_night_interventions_use_case import (
    ReportNightInterventionsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def report_night_interventions() -> dict[str, object]:
    from hexawyn.mcp.server import build_night_intervention_adapter

    try:
        use_case = ReportNightInterventionsUseCase(workload_port=build_night_intervention_adapter())
        _ = use_case.execute(ReportNightInterventionsCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_night_interventions)
