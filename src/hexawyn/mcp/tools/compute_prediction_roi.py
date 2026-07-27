# mypy: ignore-errors
"""MCP tool: compute_prediction_roi."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compute_prediction_roi.command import (
    ComputePredictionRoiCommand,
)
from hexawyn.application.use_case.finops.compute_prediction_roi.compute_prediction_roi_use_case import (  # noqa: E501
    ComputePredictionRoiUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_prediction_roi(period: str = "test") -> dict[str, object]:  # type: ignore[no-untyped-def]
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        service = ComputePredictionRoiUseCase(prediction_roi_port=build_optimization_roi_adapter())  # type: ignore
        use_case = ComputePredictionRoiUseCase(service=service)  # type: ignore
        _ = use_case.execute(ComputePredictionRoiCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:  # type: ignore[no-untyped-def]
    mcp.tool()(compute_prediction_roi)
