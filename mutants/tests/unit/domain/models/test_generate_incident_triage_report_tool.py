from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(reason: str = "FailedConnect") -> NamespaceEvent:
    return NamespaceEvent(
        event_type="Warning",
        reason=reason,
        message="connection pool exhausted for postgres",
        object="payment-db",
        count=1,
        last_seen="2024-06-01T14:15:00Z",
    )


class TestGenerateIncidentTriageReportTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.generate_incident_triage_report import (
            generate_incident_triage_report,
        )

        with (
            patch("hexawyn.mcp.server.build_namespace_events_adapter") as build_events,
            patch("hexawyn.mcp.server.build_k8s_adapter") as build_k8s,
            patch("hexawyn.mcp.server.build_pod_logs_adapter") as build_pod_logs,
            patch("hexawyn.mcp.server.build_tekton_adapter") as build_tekton,
            patch("hexawyn.mcp.server.build_pipeline_run_logs_adapter") as build_pipeline_logs,
        ):
            events_adapter = MagicMock()
            events_adapter.list_events.return_value = [_event()]
            build_events.return_value = events_adapter

            k8s_adapter = MagicMock()
            k8s_adapter.list_namespaces.return_value = [
                {"name": "payment", "status": "Active", "age": "10d"}
            ]
            k8s_adapter.list_pods.return_value = []
            build_k8s.return_value = k8s_adapter

            build_pod_logs.return_value = MagicMock()

            tekton_adapter = MagicMock()
            tekton_adapter.list_pipeline_runs_in_namespace.return_value = []
            build_tekton.return_value = tekton_adapter

            build_pipeline_logs.return_value = MagicMock()

            result = generate_incident_triage_report(namespace="payment")

        assert result["error"] is None
        assert result["namespace"] == "payment"
        assert len(result["root_causes"]) == 1
        assert "# Incident Report" in result["formatted_report"]

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.generate_incident_triage_report import (
            generate_incident_triage_report,
        )

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("Namespace 'ghost' not found"),
        ):
            result = generate_incident_triage_report(namespace="ghost")

        assert result["error"] == "Namespace 'ghost' not found"


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.generate_incident_triage_report")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
