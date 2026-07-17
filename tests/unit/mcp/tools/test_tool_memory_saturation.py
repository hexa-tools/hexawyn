"""Unit tests for MCP tool: memory_saturation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestMemorySaturationTool:
    def test_memory_saturation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.memory_saturation import memory_saturation

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_memory_saturation_adapter", return_value=MagicMock()),
        ):
            result = memory_saturation()

        assert isinstance(result, dict)

    def test_memory_saturation_handles_error(self) -> None:
        from hexawyn.mcp.tools.memory_saturation import memory_saturation

        with (
            patch(
                "hexawyn.mcp.server.build_memory_saturation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = memory_saturation()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.memory_saturation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
