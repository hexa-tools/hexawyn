"""MCP tool: get_namespace_events — Warning/Error events triage for a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.use_case.get_namespace_events.get_namespace_events_use_case import (
    GetNamespaceEventsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def get_namespace_events(
    namespace: str,
    time_window_minutes: int = 15,
    top_n: int = 20,
) -> dict[str, object]:
    from hexawyn.application.service.get_namespace_events_service import GetNamespaceEventsService
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        service = GetNamespaceEventsService(events_port=events_adapter, k8s_port=k8s_adapter)
        r = GetNamespaceEventsUseCase(service=service).execute(
            GetNamespaceEventsCommand(
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                top_n=top_n,
            )
        )
        return {
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "total_events": r.total_events,
            "has_more": r.has_more,
            "remaining_count": r.remaining_count,
            "summary": r.summary,
            "events": r.events,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(get_namespace_events)
