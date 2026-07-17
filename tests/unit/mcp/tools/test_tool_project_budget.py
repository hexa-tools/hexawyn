"""Unit tests for MCP tool: project_budget."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestProjectBudgetTool:
    def test_project_budget_returns_dict(self) -> None:
        from hexawyn.mcp.tools.project_budget import project_budget

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_budget_projection_adapter", return_value=MagicMock()),
        ):
            result = project_budget()

        assert isinstance(result, dict)

    def test_project_budget_handles_error(self) -> None:
        from hexawyn.mcp.tools.project_budget import project_budget

        with (
            patch(
                "hexawyn.mcp.server.build_budget_projection_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = project_budget()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.project_budget")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
