"""Unit tests for MCP tool: advanced_namespace_event_analytics."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAdvancedNamespaceEventAnalyticsTool:
    def test_advanced_namespace_event_analytics_returns_dict(self) -> None:
        from hexawyn.mcp.tools.advanced_namespace_event_analytics import (
            advanced_namespace_event_analytics,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_events_adapter", return_value=MagicMock()),
        ):
            result = advanced_namespace_event_analytics(namespace="test-ns")

        assert isinstance(result, dict)

    def test_advanced_namespace_event_analytics_handles_error(self) -> None:
        from hexawyn.mcp.tools.advanced_namespace_event_analytics import (
            advanced_namespace_event_analytics,
        )

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch(
                "hexawyn.mcp.server.build_namespace_events_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = advanced_namespace_event_analytics(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.advanced_namespace_event_analytics")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
