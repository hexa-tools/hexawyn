"""MCP tool: cluster_capacity_ceiling_forecast — Forecast cluster capacity ceiling."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_use_case import (  # noqa: E501
    ClusterCapacityCeilingForecastUseCase,
)
from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cluster_capacity_ceiling_forecast() -> dict[str, object]:
    from hexawyn.mcp.server import (  # noqa: E501
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        use_case = ClusterCapacityCeilingForecastUseCase(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        response = use_case.forecast(ClusterCapacityCeilingForecastCommand())
        return {
            "cpu": response.cpu,
            "memory": response.memory,
            "critical_resource": response.critical_resource,
            "autoscaler_enabled": response.autoscaler_enabled,
            "recommendation": response.recommendation,
            "confidence": response.confidence,
            "window_days_used": response.window_days_used,
            "error": None,
        }
    except Exception as exc:
        return {
            "cpu": None,
            "memory": None,
            "critical_resource": "",
            "autoscaler_enabled": False,
            "recommendation": "",
            "confidence": "",
            "window_days_used": 0,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(cluster_capacity_ceiling_forecast)
