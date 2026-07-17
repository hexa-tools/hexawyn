"""Unit tests for MCP tool: detect_recurring_incidents."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectRecurringIncidentsTool:
    def test_detect_recurring_incidents_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_recurring_incidents import detect_recurring_incidents

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_recurring_incident_adapter", return_value=MagicMock()),
        ):
            result = detect_recurring_incidents()

        assert isinstance(result, dict)

    def test_detect_recurring_incidents_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_recurring_incidents import detect_recurring_incidents

        with (
            patch(
                "hexawyn.mcp.server.build_recurring_incident_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_recurring_incidents()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_recurring_incidents")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
