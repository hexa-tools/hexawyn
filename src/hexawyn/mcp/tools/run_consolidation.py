"""MCP tool: run_consolidation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.run_consolidation.command import RunConsolidationCommand
from hexawyn.application.use_case.cluster.run_consolidation.run_consolidation_use_case import (
    RunConsolidationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def run_consolidation() -> dict[str, object]:
    from hexawyn.mcp.server import build_consolidation_adapter

    try:
        service = RunConsolidationUseCase(consolidation_port=build_consolidation_adapter())
        use_case = RunConsolidationUseCase(service=service)  # type: ignore
        _ = use_case.execute(RunConsolidationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(run_consolidation)
