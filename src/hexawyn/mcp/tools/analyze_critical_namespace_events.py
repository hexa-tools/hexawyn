"""MCP tool: analyze_critical_namespace_events — Phase 2 progressive disclosure
(critical events correlated into incidents with runbook suggestions)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.use_case.analyze_critical_namespace_events.analyze_critical_namespace_events_use_case import (
    AnalyzeCriticalNamespaceEventsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def analyze_critical_namespace_events(
    namespace: str, time_window_minutes: int = 15
) -> dict[str, object]:
    from hexawyn.application.service.analyze_critical_namespace_events_service import (
        AnalyzeCriticalNamespaceEventsService,
    )
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        service = AnalyzeCriticalNamespaceEventsService(
            events_port=events_adapter, k8s_port=k8s_adapter
        )
        r = AnalyzeCriticalNamespaceEventsUseCase(service=service).execute(
            AnalyzeCriticalNamespaceEventsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "critical_incidents": r.critical_incidents,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_critical_namespace_events)
