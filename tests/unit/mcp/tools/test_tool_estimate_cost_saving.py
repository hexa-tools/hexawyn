"""Unit tests for MCP tool: estimate_cost_saving."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestEstimateCostSavingTool:
    def test_estimate_cost_saving_returns_dict(self) -> None:
        from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_cost_saving_adapter", return_value=MagicMock()),
        ):
            result = estimate_cost_saving()

        assert isinstance(result, dict)

    def test_estimate_cost_saving_handles_error(self) -> None:
        from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

        with (
            patch(
                "hexawyn.mcp.server.build_cost_saving_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = estimate_cost_saving()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.estimate_cost_saving")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
