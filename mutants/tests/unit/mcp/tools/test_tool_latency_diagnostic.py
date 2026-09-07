"""Unit tests for MCP tool: latency_diagnostic."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestLatencyDiagnosticTool:
    def test_latency_diagnostic_returns_dict(self) -> None:
        from hexawyn.mcp.tools.latency_diagnostic import latency_diagnostic

        mock_response = MagicMock()
        mock_response.service_name = "test-svc"
        mock_response.slow_trace_count = 3
        mock_response.total_traces = 100
        mock_response.bottlenecks = []
        mock_response.slowest_span = "test-span"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_trace_query_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.latency_diagnostic.LatencyDiagnosticUseCase",
                return_value=mock_uc,
            ),
        ):
            result = latency_diagnostic("test-svc")

        assert isinstance(result, dict)
        assert result["service_name"] == "test-svc"

    def test_latency_diagnostic_handles_error(self) -> None:
        from hexawyn.mcp.tools.latency_diagnostic import latency_diagnostic

        with patch(
            "hexawyn.mcp.server.build_trace_query_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = latency_diagnostic("test-svc")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.latency_diagnostic")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
