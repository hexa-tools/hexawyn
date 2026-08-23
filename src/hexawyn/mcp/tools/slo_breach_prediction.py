# mypy: ignore-errors
"""MCP tool: slo_breach_prediction."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.slo_breach_prediction.command import (  # type: ignore
    SLOBreachPredictionCommand,
)
from hexawyn.application.use_case.workloads.slo_breach_prediction.slo_breach_prediction_use_case import (  # noqa: E501  # type: ignore  # type: ignore
    SLOBreachPredictionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def slo_breach_prediction(prediction_window_minutes: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SLOBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(slo_breach_prediction)
