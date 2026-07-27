"""MCP tool: advanced_namespace_event_analytics — event analytics."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.advanced_namespace_event_analytics_use_case import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsUseCase,
)
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.command import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def advanced_namespace_event_analytics(namespace: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        use_case = AdvancedNamespaceEventAnalyticsUseCase(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
        )
        r = use_case.execute(AdvancedNamespaceEventAnalyticsCommand(namespace=namespace))
        return {"namespace": r.namespace, "events": r.events, "error": r.error}
    except Exception as exc:
        return {"namespace": namespace, "events": [], "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(advanced_namespace_event_analytics)
