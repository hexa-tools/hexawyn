"""Unit tests for MCP tool: canary_comparison."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCanaryComparisonTool:
    def test_canary_comparison_returns_dict(self) -> None:
        from hexawyn.mcp.tools.canary_comparison import canary_comparison

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_canary_comparison_adapter", return_value=MagicMock()),
        ):
            result = canary_comparison(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_canary_comparison_handles_error(self) -> None:
        from hexawyn.mcp.tools.canary_comparison import canary_comparison

        with (
            patch(
                "hexawyn.mcp.server.build_canary_comparison_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = canary_comparison(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.canary_comparison")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
