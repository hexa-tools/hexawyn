"""MCP tool: trace_log_correlation — Correlate error logs with failed OTel traces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.trace_log_correlation.command import TraceLogCorrelationCommand
from hexawyn.application.use_case.trace_log_correlation.trace_log_correlation_use_case import (
    TraceLogCorrelationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def trace_log_correlation(operation: str, trace_id: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_log_correlation_adapter

    try:
        a = build_trace_log_correlation_adapter()
        r = TraceLogCorrelationUseCase(port=a).execute(
            TraceLogCorrelationCommand(operation=operation, trace_id=trace_id)
        )
        return {
            "trace_id": r.trace_id,
            "operation": r.operation,
            "error_span_count": r.error_span_count,
            "correlated_log_count": r.correlated_log_count,
            "summary": r.summary,
            "error_spans": r.error_spans,
            "correlated_logs": r.correlated_logs,
            "error": r.error,
        }
    except Exception as exc:
        return {"operation": operation, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(trace_log_correlation)
