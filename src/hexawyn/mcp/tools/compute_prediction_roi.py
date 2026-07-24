"""MCP tool: compute_prediction_roi."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.compute_prediction_roi.command import ComputePredictionRoiCommand
from hexawyn.application.use_case.compute_prediction_roi.compute_prediction_roi_use_case import (
    ComputePredictionRoiUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_prediction_roi(period="test") -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())
        _ = use_case.execute(ComputePredictionRoiCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_prediction_roi)
