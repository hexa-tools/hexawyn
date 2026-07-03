from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(count: int = 12) -> NamespaceEvent:
    return NamespaceEvent(
        event_type="Warning",
        reason="BackOff",
        message="Back-off restarting failed container",
        object="pod/payment-api",
        count=count,
        last_seen="2024-01-01T15:00:00Z",
    )


class TestGetNamespaceEventsTool:
    def test_returns_events(self) -> None:
        from hexawyn.mcp.tools.get_namespace_events import get_namespace_events

        with (
            patch("hexawyn.mcp.server.build_namespace_events_adapter") as build_events,
            patch("hexawyn.mcp.server.build_k8s_adapter") as build_k8s,
        ):
            events_adapter = MagicMock(spec=NamespaceEventsPort)
            events_adapter.list_events.return_value = [_event()]
            build_events.return_value = events_adapter

            k8s_adapter = MagicMock()
            k8s_adapter.list_namespaces.return_value = [
                {"name": "production", "status": "Active", "age": "10d"}
            ]
            build_k8s.return_value = k8s_adapter

            result = get_namespace_events(namespace="production")

        assert result["error"] is None
        assert result["namespace"] == "production"
        assert result["total_events"] == 1
        assert result["events"][0]["recurring"] is True

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.get_namespace_events import get_namespace_events

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("Namespace 'ghost' not found"),
        ):
            result = get_namespace_events(namespace="ghost")

        assert result["error"] == "Namespace 'ghost' not found"


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_namespace_events")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
