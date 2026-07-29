"""Unit tests for MCP tool: analyze_critical_namespace_events."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAnalyzeCriticalNamespaceEventsTool:
    def test_analyze_critical_namespace_events_returns_dict(self) -> None:
        from hexawyn.mcp.tools.analyze_critical_namespace_events import (
            analyze_critical_namespace_events,
        )

        mock_response = MagicMock()
        mock_response.critical_events = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_events_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.analyze_critical_namespace_events.AnalyzeCriticalNamespaceEventsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = analyze_critical_namespace_events()

        assert isinstance(result, dict)
        assert "critical_events" in result

    def test_analyze_critical_namespace_events_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_critical_namespace_events import (
            analyze_critical_namespace_events,
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
            result = analyze_critical_namespace_events()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_critical_namespace_events")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
