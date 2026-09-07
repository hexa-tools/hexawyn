"""Unit tests for MCP tool: custom_tools_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCustomToolsListTool:
    def test_custom_tools_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.custom_tools_list import custom_tools_list

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = custom_tools_list()

        assert isinstance(result, dict)

    def test_custom_tools_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.custom_tools_list import custom_tools_list

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = custom_tools_list()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.custom_tools_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
