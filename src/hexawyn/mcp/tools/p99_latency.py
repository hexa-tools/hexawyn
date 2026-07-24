"""MCP tool: p99_latency — Compute p99 latency for an HTTP endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.p99_latency.command import P99LatencyCommand
from hexawyn.application.use_case.p99_latency.p99_latency_use_case import P99LatencyUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


def p99_latency(
    endpoint: str, time_window_minutes: int = 120, slo_threshold_ms: float = 500.0
) -> dict[str, object]:
    from hexawyn.mcp.server import build_latency_percentile_adapter

    try:
        a = build_latency_percentile_adapter()
        r = P99LatencyUseCase(port=a).execute(
            P99LatencyCommand(
                endpoint=endpoint,
                time_window_minutes=time_window_minutes,
                slo_threshold_ms=slo_threshold_ms,
            )
        )
        return {
            "endpoint": r.endpoint,
            "p50_ms": r.p50_ms,
            "p95_ms": r.p95_ms,
            "p99_ms": r.p99_ms,
            "slo_threshold_ms": r.slo_threshold_ms,
            "slo_status": r.slo_status,
            "slo_delta_ms": r.slo_delta_ms,
            "sample_count": r.sample_count,
            "error": r.error,
        }
    except Exception as exc:
        return {"endpoint": endpoint, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(p99_latency)
