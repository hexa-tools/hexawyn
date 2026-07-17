"""Unit tests for MCP tool: analyze_pod_logs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAnalyzePodLogsTool:
    def test_analyze_pod_logs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.analyze_pod_logs import analyze_pod_logs

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pod_logs_adapter", return_value=MagicMock()),
        ):
            result = analyze_pod_logs(pod_name="test-pod_name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_analyze_pod_logs_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_pod_logs import analyze_pod_logs

        with (
            patch(
                "hexawyn.mcp.server.build_pod_logs_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = analyze_pod_logs(pod_name="test-pod_name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_pod_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
