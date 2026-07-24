"""MCP tool: run_what_if_simulation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.run_what_if_simulation.command import RunWhatIfSimulationCommand
from hexawyn.application.use_case.run_what_if_simulation.run_what_if_simulation_use_case import (
    RunWhatIfSimulationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def run_what_if_simulation(
    target_service="test-target_service", namespace="test-ns", proposed_replicas="test"
) -> dict[str, object]:
    from hexawyn.mcp.server import build_what_if_simulation_adapter

    try:
        use_case = RunWhatIfSimulationUseCase(port=build_what_if_simulation_adapter())
        _ = use_case.execute(RunWhatIfSimulationCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(run_what_if_simulation)
