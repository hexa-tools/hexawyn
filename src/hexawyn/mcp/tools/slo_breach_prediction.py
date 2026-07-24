"""MCP tool: slo_breach_prediction."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.slo_breach_prediction.command import SloBreachPredictionCommand
from hexawyn.application.use_case.slo_breach_prediction.slo_breach_prediction_use_case import (
    SloBreachPredictionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def slo_breach_prediction(slo_name: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        use_case = SloBreachPredictionUseCase(port=build_slo_breach_prediction_adapter())
        _ = use_case.execute(SloBreachPredictionCommand(slo_name=slo_name))
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(slo_breach_prediction)
