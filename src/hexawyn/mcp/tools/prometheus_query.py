"""MCP tool: prometheus_query."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.observability.prometheus_query.command import (
    PrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.prometheus_query.prometheus_query_use_case import (
    PrometheusQueryUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def prometheus_query(promql: str = "") -> dict[str, object]:
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        use_case = PrometheusQueryUseCase(port=build_metrics_query_adapter())
        _ = use_case.execute(PrometheusQueryCommand())  # type: ignore
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(prometheus_query)
