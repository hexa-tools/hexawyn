"""Unit tests for MCP tool: redundant_calls."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRedundantCallsTool:
    def test_redundant_calls_returns_dict(self) -> None:
        from hexawyn.mcp.tools.redundant_calls import redundant_calls

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_redundant_call_detection_adapter",
                return_value=MagicMock(),
            ),
        ):
            result = redundant_calls(flow="test")

        assert isinstance(result, dict)

    def test_redundant_calls_handles_error(self) -> None:
        from hexawyn.mcp.tools.redundant_calls import redundant_calls

        with (
            patch(
                "hexawyn.mcp.server.build_redundant_call_detection_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = redundant_calls(flow="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.redundant_calls")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
