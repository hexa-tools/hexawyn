"""MCP tool: compute_optimization_roi."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.compute_optimization_roi.command import (
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.use_case.compute_optimization_roi.compute_optimization_roi_use_case import (
    ComputeOptimizationRoiUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_optimization_roi(sprint_id="test") -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeOptimizationRoiUseCase(roi_port=build_optimization_roi_adapter())
        _ = use_case.execute(ComputeOptimizationRoiCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_optimization_roi)
