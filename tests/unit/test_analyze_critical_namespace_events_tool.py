from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(event_type: str = "Warning", reason: str = "OOMKilling") -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=reason,
        object="pod/payment-api",
        count=1,
        last_seen="2024-01-01T15:00:00Z",
    )


class TestAnalyzeCriticalNamespaceEventsTool:
    def test_returns_critical_incidents_with_runbooks(self) -> None:
        from hexawyn.mcp.tools.analyze_critical_namespace_events import (
            analyze_critical_namespace_events,
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
                {"name": "staging", "status": "Active", "age": "1d"}
            ]
            build_k8s.return_value = k8s_adapter

            result = analyze_critical_namespace_events(namespace="staging")

        assert result["error"] is None
        assert len(result["critical_incidents"]) == 1
        incident = result["critical_incidents"][0]
        assert incident["reason"] == "OOMKilling"
        assert incident["runbook_id"] == "runbook-memory-001"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_critical_namespace_events import (
            analyze_critical_namespace_events,
        )

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("Namespace 'ghost' not found"),
        ):
            result = analyze_critical_namespace_events(namespace="ghost")

        assert result["error"] == "Namespace 'ghost' not found"


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_critical_namespace_events")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
