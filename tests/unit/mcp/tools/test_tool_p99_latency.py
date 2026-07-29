"""Unit tests for MCP tool: p99_latency."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestP99LatencyTool:
    def test_p99_latency_returns_dict(self) -> None:
        from hexawyn.mcp.tools.p99_latency import p99_latency

        mock_response = MagicMock()
        mock_response.endpoint = "/api/test"
        mock_response.p50_ms = 10.0
        mock_response.p95_ms = 50.0
        mock_response.p99_ms = 100.0
        mock_response.slo_threshold_ms = 500.0
        mock_response.slo_status = "ok"
        mock_response.slo_delta_ms = 400.0
        mock_response.sample_count = 1000
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_latency_percentile_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.p99_latency.P99LatencyUseCase",
                return_value=mock_uc,
            ),
        ):
            result = p99_latency("/api/test")

        assert isinstance(result, dict)
        assert result["endpoint"] == "/api/test"

    def test_p99_latency_handles_error(self) -> None:
        from hexawyn.mcp.tools.p99_latency import p99_latency

        with patch(
            "hexawyn.mcp.server.build_latency_percentile_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = p99_latency("/api/test")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.p99_latency")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
