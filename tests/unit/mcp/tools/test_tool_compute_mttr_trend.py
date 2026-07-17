"""Unit tests for MCP tool: compute_mttr_trend."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeMttrTrendTool:
    def test_compute_mttr_trend_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_mttr_trend import compute_mttr_trend

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_mttr_trend_adapter", return_value=MagicMock()),
        ):
            result = compute_mttr_trend()

        assert isinstance(result, dict)

    def test_compute_mttr_trend_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_mttr_trend import compute_mttr_trend

        with (
            patch(
                "hexawyn.mcp.server.build_mttr_trend_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compute_mttr_trend()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_mttr_trend")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
