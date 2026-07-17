"""Unit tests for MCP tool: analyze_incident_cost."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAnalyzeIncidentCostTool:
    def test_analyze_incident_cost_returns_dict(self) -> None:
        from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_incident_cost_adapter", return_value=MagicMock()),
        ):
            result = analyze_incident_cost()

        assert isinstance(result, dict)

    def test_analyze_incident_cost_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

        with (
            patch(
                "hexawyn.mcp.server.build_incident_cost_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = analyze_incident_cost()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_incident_cost")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
