"""MCP tool: cluster_capacity_ceiling_forecast — Forecast cluster capacity ceiling."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_use_case import (
    ClusterCapacityCeilingForecastUseCase,
)
from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cluster_capacity_ceiling_forecast() -> dict[str, object]:
    from hexawyn.mcp.server import build_cost_forecast_adapter

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(port=build_cost_forecast_adapter())
        _ = use_case.execute(ClusterCapacityCeilingForecastCommand())
        return {"forecast": {}, "error": None}
    except Exception as exc:
        return {"forecast": {}, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(cluster_capacity_ceiling_forecast)
