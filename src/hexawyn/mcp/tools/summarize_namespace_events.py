"""MCP tool: summarize_namespace_events — Phase 1 progressive disclosure (high-level overview)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.summarize_namespace_events.command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.use_case.summarize_namespace_events.summarize_namespace_events_use_case import (
    SummarizeNamespaceEventsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def summarize_namespace_events(namespace: str, time_window_minutes: int = 15) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        r = SummarizeNamespaceEventsUseCase(
            events_port=events_adapter, k8s_port=k8s_adapter
        ).execute(
            r=SummarizeNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "severity_breakdown": r.severity_breakdown,
            "top_affected_pods": r.top_affected_pods,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(summarize_namespace_events)
