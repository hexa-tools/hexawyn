"""MCP tool: cluster_capacity_ceiling_forecast — predicts when the cluster
will run out of allocatable node capacity (CPU and memory) at the current
growth rate."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_use_case import (
    ClusterCapacityCeilingForecastUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def cluster_capacity_ceiling_forecast(window_days: int = 14) -> dict[str, object]:
    from hexawyn.application.service.cluster_capacity_ceiling_forecast_service import (
        ClusterCapacityCeilingForecastService,
    )
    from hexawyn.mcp.server import (
        build_capacity_forecast_adapter,
        build_cluster_resource_metrics_adapter,
    )

    try:
        service = ClusterCapacityCeilingForecastService(
            metrics_port=build_cluster_resource_metrics_adapter(),
            capacity_port=build_capacity_forecast_adapter(),
        )
        r = ClusterCapacityCeilingForecastUseCase(service=service).execute(
            ClusterCapacityCeilingForecastCommand(window_days=window_days)
        )
        return {
            "cpu": r.cpu,
            "memory": r.memory,
            "critical_resource": r.critical_resource,
            "autoscaler_enabled": r.autoscaler_enabled,
            "recommendation": r.recommendation,
            "confidence": r.confidence,
            "window_days_used": r.window_days_used,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(cluster_capacity_ceiling_forecast)
