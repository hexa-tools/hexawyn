"""Unit tests for MCP tool: detect_log_anomalies."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectLogAnomaliesTool:
    def test_detect_log_anomalies_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_log_anomalies import detect_log_anomalies

        with patch("hexawyn.mcp.server.build_pod_logs_adapter", return_value=MagicMock()):
            result = detect_log_anomalies(pod_name="test-pod", namespace="test-ns")

        assert isinstance(result, dict)
        assert "error" in result

    def test_detect_log_anomalies_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_log_anomalies import detect_log_anomalies

        with patch(
            "hexawyn.mcp.server.build_pod_logs_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_log_anomalies(pod_name="test-pod", namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_detect_log_anomalies_success_path(self) -> None:
        from hexawyn.mcp.tools.detect_log_anomalies import detect_log_anomalies

        mock_response = MagicMock()
        mock_response.pod_name = "test-pod"
        mock_response.namespace = "test-ns"
        mock_response.time_window_minutes = 240
        mock_response.total_lines = 1000
        mock_response.baseline_mean_lines_per_minute = 4.0
        mock_response.baseline_std_dev = 1.0
        mock_response.summary = "No anomalies"
        mock_response.insufficient_data = False
        mock_response.formats_analyzed_separately = False
        mock_response.anomalies = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_pod_logs_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.detect_log_anomalies.DetectLogAnomaliesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = detect_log_anomalies(pod_name="test-pod", namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_log_anomalies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
