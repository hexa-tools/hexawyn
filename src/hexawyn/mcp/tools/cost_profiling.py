"""MCP tool: cost_profiling — Identify the most CPU-intensive HTTP endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.cost_profiling.cost_profiling_command import (
    CostProfilingCommand,
)
from hexawyn.application.use_case.cost_profiling.cost_profiling_use_case import CostProfilingUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cost_profiling(time_window_minutes: int = 60, top_n: int = 5) -> dict[str, object]:
    from hexawyn.application.service.cost_profiling_service import CostProfilingService
    from hexawyn.mcp.server import build_cost_profiling_adapter

    try:
        a = build_cost_profiling_adapter()
        r = CostProfilingUseCase(service=CostProfilingService(port=a)).execute(
            CostProfilingCommand(time_window_minutes=time_window_minutes, top_n=top_n)
        )
        return {
            "time_window_minutes": r.time_window_minutes,
            "ranked_endpoints": r.ranked_endpoints,
            "optimisation_candidates": r.optimisation_candidates,
            "error": r.error,
        }
    except Exception as exc:
        return {"ranked_endpoints": [], "optimisation_candidates": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(cost_profiling)
