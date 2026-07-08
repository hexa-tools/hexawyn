"""MCP tool: slo_breach_prediction — Predict which services will violate SLO."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_command import (
    SLOBreachPredictionCommand,
)
from hexawyn.application.use_case.slo_breach_prediction.slo_breach_prediction_use_case import (
    SLOBreachPredictionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def slo_breach_prediction(prediction_window_minutes: int = 60) -> dict[str, object]:
    from hexawyn.application.service.slo_breach_prediction_service import SLOBreachPredictionService
    from hexawyn.mcp.server import build_slo_breach_prediction_adapter

    try:
        a = build_slo_breach_prediction_adapter()
        r = SLOBreachPredictionUseCase(service=SLOBreachPredictionService(port=a)).execute(
            SLOBreachPredictionCommand(prediction_window_minutes=prediction_window_minutes)
        )
        return {"at_risk": r.at_risk, "safe_count": r.safe_count, "error": r.error}
    except Exception as exc:
        return {"at_risk": [], "safe_count": 0, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(slo_breach_prediction)
