"""Unit tests for MCP tool: detect_pod_anomalies."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectPodAnomaliesTool:
    def test_detect_pod_anomalies_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_pod_anomalies import detect_pod_anomalies

        with (
            patch(
                "hexawyn.mcp.server.build_pod_metrics_baseline_adapter",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
        ):
            result = detect_pod_anomalies(namespace="test-ns")

        assert isinstance(result, dict)
        assert "error" in result

    def test_detect_pod_anomalies_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_pod_anomalies import detect_pod_anomalies

        with patch(
            "hexawyn.mcp.server.build_pod_metrics_baseline_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_pod_anomalies(namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_detect_pod_anomalies_success_path(self) -> None:
        from hexawyn.mcp.tools.detect_pod_anomalies import detect_pod_anomalies

        mock_response = MagicMock()
        mock_response.namespace = "test-ns"
        mock_response.total_pods = 10
        mock_response.anomalies = []
        mock_response.excluded_pods = []
        mock_response.summary = "No anomalies"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_pod_metrics_baseline_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.server.build_k8s_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.detect_pod_anomalies.DetectPodAnomaliesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = detect_pod_anomalies(namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_pod_anomalies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
