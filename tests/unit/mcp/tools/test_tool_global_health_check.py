"""Unit tests for MCP tool: global_health_check."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGlobalHealthCheckTool:
    def test_global_health_check_returns_dict(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_fleet_health_adapter", return_value=MagicMock()),
        ):
            result = global_health_check()

        assert isinstance(result, dict)

    def test_global_health_check_handles_error(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        with (
            patch(
                "hexawyn.mcp.server.build_fleet_health_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = global_health_check()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.global_health_check")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
