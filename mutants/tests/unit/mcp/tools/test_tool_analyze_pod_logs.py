"""Unit tests for MCP tool: analyze_pod_logs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAnalyzePodLogsTool:
    def test_analyze_pod_logs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.analyze_pod_logs import analyze_pod_logs

        mock_response = MagicMock()
        mock_response.pod_name = "test-pod"
        mock_response.namespace = "test-ns"
        mock_response.time_window_minutes = 30
        mock_response.strategy_used = "pattern"
        mock_response.total_lines = 100
        mock_response.error_count = 0
        mock_response.warning_count = 1
        mock_response.confidence = 0.9
        mock_response.summary = "ok"
        mock_response.restarts_detected = False
        mock_response.sanitized_binary = False
        mock_response.token_reduction_percentage = 50.0
        mock_response.degraded = False
        mock_response.patterns = []
        mock_response.connection_timeouts = 0
        mock_response.connection_refused = 0
        mock_response.runs = []
        mock_response.ranked_events = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_pod_logs_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.analyze_pod_logs.AnalyzePodLogsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = analyze_pod_logs("test-pod", "test-ns")

        assert isinstance(result, dict)
        assert result["pod_name"] == "test-pod"

    def test_analyze_pod_logs_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_pod_logs import analyze_pod_logs

        with patch(
            "hexawyn.mcp.server.build_pod_logs_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = analyze_pod_logs("test-pod", "test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_pod_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
