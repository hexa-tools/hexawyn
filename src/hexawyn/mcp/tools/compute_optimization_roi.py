# mypy: ignore-errors
"""MCP tool: compute_optimization_roi."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compute_optimization_roi.command import (
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.use_case.finops.compute_optimization_roi.compute_optimization_roi_use_case import (  # noqa: E501
    ComputeOptimizationRoiUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_optimization_roi(sprint_id: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputeOptimizationRoiUseCase(roi_port=build_optimization_roi_adapter())
        use_case = ComputeOptimizationRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputeOptimizationRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(compute_optimization_roi)
