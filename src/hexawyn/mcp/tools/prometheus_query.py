"""MCP tool: prometheus_query — execute PromQL instant/range queries against Prometheus."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.use_case.execute_prometheus_query.execute_prometheus_query_use_case import (
    ExecutePrometheusQueryUseCase,
)
from hexawyn.domain.models.metrics_query import QueryType, UnitHint

if TYPE_CHECKING:
    from fastmcp import FastMCP


def prometheus_query(
    promql: str,
    query_type: QueryType = "instant",
    start: str | None = None,
    end: str | None = None,
    step: str = "15s",
    unit_hint: UnitHint = "raw",
    timeout_seconds: float = 15.0,
) -> dict[str, object]:
    from hexawyn.application.service.prometheus_query_service import PrometheusQueryService
    from hexawyn.mcp.server import build_metrics_query_adapter

    try:
        service = PrometheusQueryService(port=build_metrics_query_adapter())
        r = ExecutePrometheusQueryUseCase(service=service).execute(
            ExecutePrometheusQueryCommand(
                promql=promql,
                query_type=query_type,
                start=start,
                end=end,
                step=step,
                unit_hint=unit_hint,
                timeout_seconds=timeout_seconds,
            )
        )
        return {
            "query": r.query,
            "query_type": r.query_type,
            "results": r.results,
            "result_count": r.result_count,
            "truncated": r.truncated,
            "no_data": r.no_data,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"query": promql, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(prometheus_query)
