"""MCP tool: cluster_headroom_simulation — Simulate cluster headroom."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster_headroom_simulation.cluster_headroom_simulation_use_case import (
    ClusterHeadroomSimulationUseCase,
)
from hexawyn.application.use_case.cluster_headroom_simulation.command import (
    ClusterHeadroomSimulationCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cluster_headroom_simulation() -> dict[str, object]:
    from hexawyn.mcp.server import build_headroom_simulation_adapter

    try:
        use_case = ClusterHeadroomSimulationUseCase(port=build_headroom_simulation_adapter())
        _ = use_case.execute(ClusterHeadroomSimulationCommand())
        return {"simulation": {}, "error": None}
    except Exception as exc:
        return {"simulation": {}, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(cluster_headroom_simulation)
