"""MCP tool: latency_diagnostic — Identify root cause of latency spikes via OTel traces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.latency_diagnostic.command import LatencyDiagnosticCommand
from hexawyn.application.use_case.latency_diagnostic.latency_diagnostic_use_case import (
    LatencyDiagnosticUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def latency_diagnostic(
    service_name: str, time_window_minutes: int = 15, threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_query_adapter

    try:
        a = build_trace_query_adapter()
        r = LatencyDiagnosticUseCase(port=a).execute(
            LatencyDiagnosticCommand(
                service_name=service_name,
                time_window_minutes=time_window_minutes,
                threshold_ms=threshold_ms,
            )
        )
        return {
            "service_name": r.service_name,
            "slow_trace_count": r.slow_trace_count,
            "total_traces": r.total_traces,
            "bottlenecks": r.bottlenecks,
            "slowest_span": r.slowest_span,
            "error": r.error,
        }
    except Exception as exc:
        return {"service_name": service_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(latency_diagnostic)
