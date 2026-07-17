"""Unit tests for MCP tool: trace_k8s_events."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestTraceK8sEventsTool:
    def test_trace_k8s_events_returns_dict(self) -> None:
        from hexawyn.mcp.tools.trace_k8s_events import trace_k8s_events

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_trace_event_correlation_adapter", return_value=MagicMock()
            ),
        ):
            result = trace_k8s_events(trace_id="test")

        assert isinstance(result, dict)

    def test_trace_k8s_events_handles_error(self) -> None:
        from hexawyn.mcp.tools.trace_k8s_events import trace_k8s_events

        with (
            patch(
                "hexawyn.mcp.server.build_trace_event_correlation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = trace_k8s_events(trace_id="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.trace_k8s_events")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
