"""MCP tool: advanced_namespace_event_analytics — 6h event storm/timeline/correlation report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_command import (
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.use_case.advanced_namespace_event_analytics.advanced_namespace_event_analytics_use_case import (
    AdvancedNamespaceEventAnalyticsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def advanced_namespace_event_analytics(
    namespace: str, time_window_minutes: int = 360
) -> dict[str, object]:
    from hexawyn.application.service.advanced_namespace_event_analytics_service import (
        AdvancedNamespaceEventAnalyticsService,
    )
    from hexawyn.mcp.server import build_k8s_adapter, build_namespace_events_adapter

    try:
        events_adapter = build_namespace_events_adapter()
        k8s_adapter = build_k8s_adapter()
        service = AdvancedNamespaceEventAnalyticsService(
            events_port=events_adapter, k8s_port=k8s_adapter
        )
        r = AdvancedNamespaceEventAnalyticsUseCase(service=service).execute(
            AdvancedNamespaceEventAnalyticsCommand(
                namespace=namespace, time_window_minutes=time_window_minutes
            )
        )
        return {
            "namespace": r.namespace,
            "total_events": r.total_events,
            "timeline": r.timeline,
            "storms": r.storms,
            "top_reasons": r.top_reasons,
            "correlated_incidents": r.correlated_incidents,
            "sampling_applied": r.sampling_applied,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(advanced_namespace_event_analytics)
