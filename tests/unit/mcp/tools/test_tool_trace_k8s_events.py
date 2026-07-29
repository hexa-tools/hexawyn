"""Unit tests for MCP tool: trace_k8s_events."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestTraceK8sEventsTool:
    def test_trace_k8s_events_returns_dict(self) -> None:
        from hexawyn.mcp.tools.trace_k8s_events import trace_k8s_events

        mock_response = MagicMock()
        mock_response.trace_id = "abc123"
        mock_response.matching_events = []
        mock_response.slowest_span = "test-span"
        mock_response.conclusion = "none"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_trace_event_correlation_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.trace_k8s_events.TraceK8sEventsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = trace_k8s_events("abc123")

        assert isinstance(result, dict)
        assert result["trace_id"] == "abc123"

    def test_trace_k8s_events_handles_error(self) -> None:
        from hexawyn.mcp.tools.trace_k8s_events import trace_k8s_events

        with patch(
            "hexawyn.mcp.server.build_trace_event_correlation_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = trace_k8s_events("abc123")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.trace_k8s_events")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
