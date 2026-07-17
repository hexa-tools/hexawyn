"""Unit tests for MCP tool: keda_scaledobjects_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestKedaScaledobjectsListTool:
    def test_keda_scaledobjects_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobjects_list import keda_scaledobjects_list

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_keda_adapter", return_value=MagicMock()),
        ):
            result = keda_scaledobjects_list()

        assert isinstance(result, dict)

    def test_keda_scaledobjects_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobjects_list import keda_scaledobjects_list

        with (
            patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("test error")),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = keda_scaledobjects_list()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.keda_scaledobjects_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
