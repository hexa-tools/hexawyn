"""Unit tests for MCP tool: cost_profiling."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCostProfilingTool:
    def test_cost_profiling_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cost_profiling import cost_profiling

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_cost_profiling_adapter", return_value=MagicMock()),
        ):
            result = cost_profiling()

        assert isinstance(result, dict)

    def test_cost_profiling_handles_error(self) -> None:
        from hexawyn.mcp.tools.cost_profiling import cost_profiling

        with (
            patch(
                "hexawyn.mcp.server.build_cost_profiling_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = cost_profiling()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cost_profiling")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
