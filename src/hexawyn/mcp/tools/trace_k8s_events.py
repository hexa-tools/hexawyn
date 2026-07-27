"""MCP tool: trace_k8s_events — Show k8s events during a slow trace window."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.trace_k8s_events.command import (
    TraceK8sEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.trace_k8s_events_use_case import (  # noqa: E501
    TraceK8sEventsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def trace_k8s_events(trace_id: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_trace_event_correlation_adapter

    try:
        a = build_trace_event_correlation_adapter()
        r = TraceK8sEventsUseCase(port=a).execute(TraceK8sEventsCommand(trace_id=trace_id))
        return {
            "trace_id": r.trace_id,
            "matching_events": r.matching_events,
            "slowest_span": r.slowest_span,
            "conclusion": r.conclusion,
            "error": r.error,
        }
    except Exception as exc:
        return {"trace_id": trace_id, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(trace_k8s_events)
