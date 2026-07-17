"""Unit tests for MCP tool: detect_log_anomalies."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectLogAnomaliesTool:
    def test_detect_log_anomalies_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_log_anomalies import detect_log_anomalies

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pod_logs_adapter", return_value=MagicMock()),
        ):
            result = detect_log_anomalies(pod_name="test-pod_name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_detect_log_anomalies_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_log_anomalies import detect_log_anomalies

        with (
            patch(
                "hexawyn.mcp.server.build_pod_logs_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_log_anomalies(pod_name="test-pod_name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_log_anomalies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
