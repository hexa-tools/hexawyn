"""MCP tool: metric_correlation — Correlate error/latency spikes between services."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.metric_correlation.metric_correlation_command import (
    MetricCorrelationCommand,
)
from hexawyn.application.use_case.metric_correlation.metric_correlation_use_case import (
    MetricCorrelationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def metric_correlation(
    primary_service: str, correlated_service: str, time_window_minutes: int = 30
) -> dict[str, object]:
    from hexawyn.application.service.metric_correlation_service import MetricCorrelationService
    from hexawyn.mcp.server import build_metric_correlation_adapter

    try:
        a = build_metric_correlation_adapter()
        r = MetricCorrelationUseCase(service=MetricCorrelationService(port=a)).execute(
            MetricCorrelationCommand(
                primary_service=primary_service,
                correlated_service=correlated_service,
                time_window_minutes=time_window_minutes,
            )
        )
        return {
            "primary_service": r.primary_service,
            "correlated_service": r.correlated_service,
            "status": r.status,
            "coefficient": r.coefficient,
            "lag_index": r.lag_index,
            "hypothesis": r.hypothesis,
            "data_point_count": r.data_point_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"primary_service": primary_service, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(metric_correlation)
