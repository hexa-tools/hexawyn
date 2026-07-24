"""MCP tool: analyze_critical_namespace_events — Analyze critical namespace events."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.analyze_critical_namespace_events.analyze_critical_namespace_events_use_case import (
    AnalyzeCriticalNamespaceEventsUseCase,
)
from hexawyn.application.use_case.analyze_critical_namespace_events.command import (
    AnalyzeCriticalNamespaceEventsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def analyze_critical_namespace_events(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace=namespace))
        return {"critical_events": r.critical_events, "error": r.error}
    except Exception as exc:
        return {"critical_events": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(analyze_critical_namespace_events)
