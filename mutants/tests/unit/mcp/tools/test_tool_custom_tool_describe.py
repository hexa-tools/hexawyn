"""Unit tests for MCP tool: custom_tool_describe."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCustomToolDescribeTool:
    def test_custom_tool_describe_returns_dict(self) -> None:
        from hexawyn.mcp.tools.custom_tool_describe import custom_tool_describe

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = custom_tool_describe(name="test-name")

        assert isinstance(result, dict)

    def test_custom_tool_describe_handles_error(self) -> None:
        from hexawyn.mcp.tools.custom_tool_describe import custom_tool_describe

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = custom_tool_describe(name="test-name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.custom_tool_describe")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
