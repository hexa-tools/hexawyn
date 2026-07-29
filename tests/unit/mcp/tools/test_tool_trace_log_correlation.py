"""Unit tests for MCP tool: trace_log_correlation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestTraceLogCorrelationTool:
    def test_trace_log_correlation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.trace_log_correlation import trace_log_correlation

        mock_response = MagicMock()
        mock_response.trace_id = "abc123"
        mock_response.operation = "test-op"
        mock_response.error_span_count = 2
        mock_response.correlated_log_count = 3
        mock_response.summary = "test"
        mock_response.error_spans = []
        mock_response.correlated_logs = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_trace_log_correlation_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.trace_log_correlation.TraceLogCorrelationUseCase",
                return_value=mock_uc,
            ),
        ):
            result = trace_log_correlation("test-op")

        assert isinstance(result, dict)
        assert result["operation"] == "test-op"

    def test_trace_log_correlation_handles_error(self) -> None:
        from hexawyn.mcp.tools.trace_log_correlation import trace_log_correlation

        with patch(
            "hexawyn.mcp.server.build_trace_log_correlation_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = trace_log_correlation("test-op")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.trace_log_correlation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
