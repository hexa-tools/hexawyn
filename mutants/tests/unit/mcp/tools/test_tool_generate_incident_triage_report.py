"""Unit tests for MCP tool: generate_incident_triage_report."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGenerateIncidentTriageReportTool:
    def test_generate_incident_triage_report_returns_dict(self) -> None:
        from hexawyn.mcp.tools.generate_incident_triage_report import (
            generate_incident_triage_report,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_events_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pipeline_run_logs_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pod_logs_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
        ):
            result = generate_incident_triage_report(namespace="test-ns")

        assert isinstance(result, dict)

    def test_generate_incident_triage_report_handles_error(self) -> None:
        from hexawyn.mcp.tools.generate_incident_triage_report import (
            generate_incident_triage_report,
        )

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch(
                "hexawyn.mcp.server.build_namespace_events_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_pipeline_run_logs_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_pod_logs_adapter", side_effect=RuntimeError("test error")
            ),
            patch(
                "hexawyn.mcp.server.build_tekton_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = generate_incident_triage_report(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.generate_incident_triage_report")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
