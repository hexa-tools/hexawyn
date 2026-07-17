"""Unit tests for MCP tool: compute_team_cost."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeTeamCostTool:
    def test_compute_team_cost_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_team_cost import compute_team_cost

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_team_cost_adapter", return_value=MagicMock()),
        ):
            result = compute_team_cost()

        assert isinstance(result, dict)

    def test_compute_team_cost_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_team_cost import compute_team_cost

        with (
            patch(
                "hexawyn.mcp.server.build_team_cost_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compute_team_cost()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_team_cost")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
