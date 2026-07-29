"""Unit tests for MCP tool: advanced_namespace_event_analytics."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAdvancedNamespaceEventAnalyticsTool:
    def test_advanced_namespace_event_analytics_returns_dict(self) -> None:
        from hexawyn.mcp.tools.advanced_namespace_event_analytics import (
            advanced_namespace_event_analytics,
        )

        mock_response = MagicMock()
        mock_response.namespace = "test-ns"
        mock_response.events = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_events_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.advanced_namespace_event_analytics.AdvancedNamespaceEventAnalyticsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = advanced_namespace_event_analytics("test-ns")

        assert isinstance(result, dict)
        assert result["namespace"] == "test-ns"

    def test_advanced_namespace_event_analytics_handles_error(self) -> None:
        from hexawyn.mcp.tools.advanced_namespace_event_analytics import (
            advanced_namespace_event_analytics,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_k8s_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_namespace_events_adapter",
                side_effect=RuntimeError("test error"),
            ),
        ):
            result = advanced_namespace_event_analytics("test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.advanced_namespace_event_analytics")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
