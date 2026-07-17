"""Unit tests for MCP tool: summarize_namespace_events."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSummarizeNamespaceEventsTool:
    def test_summarize_namespace_events_returns_dict(self) -> None:
        from hexawyn.mcp.tools.summarize_namespace_events import summarize_namespace_events

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_events_adapter", return_value=MagicMock()),
        ):
            result = summarize_namespace_events(namespace="test-ns")

        assert isinstance(result, dict)

    def test_summarize_namespace_events_handles_error(self) -> None:
        from hexawyn.mcp.tools.summarize_namespace_events import summarize_namespace_events

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch(
                "hexawyn.mcp.server.build_namespace_events_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = summarize_namespace_events(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.summarize_namespace_events")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
