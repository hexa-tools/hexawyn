from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(reason: str = "BackOff") -> NamespaceEvent:
    return NamespaceEvent(
        event_type="Warning",
        reason=reason,
        message=reason,
        object="pod/payment-api",
        count=1,
        last_seen="2024-01-01T15:00:00Z",
    )


class TestAdvancedNamespaceEventAnalyticsTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.advanced_namespace_event_analytics import (
            advanced_namespace_event_analytics,
        )

        with (
            patch("hexawyn.mcp.server.build_namespace_events_adapter") as build_events,
            patch("hexawyn.mcp.server.build_k8s_adapter") as build_k8s,
        ):
            events_adapter = MagicMock(spec=NamespaceEventsPort)
            events_adapter.list_events.return_value = [_event(), _event(), _event()]
            build_events.return_value = events_adapter

            k8s_adapter = MagicMock()
            k8s_adapter.list_namespaces.return_value = [
                {"name": "data-pipeline", "status": "Active", "age": "10d"}
            ]
            build_k8s.return_value = k8s_adapter

            result = advanced_namespace_event_analytics(namespace="data-pipeline")

        assert result["error"] is None
        assert result["namespace"] == "data-pipeline"
        assert result["total_events"] == 3
        assert len(result["correlated_incidents"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.advanced_namespace_event_analytics import (
            advanced_namespace_event_analytics,
        )

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("Namespace 'ghost' not found"),
        ):
            result = advanced_namespace_event_analytics(namespace="ghost")

        assert result["error"] == "Namespace 'ghost' not found"


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.advanced_namespace_event_analytics")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
