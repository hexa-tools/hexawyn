"""Unit tests for MCP tool: estimate_rightsizing_savings."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestEstimateRightsizingSavingsTool:
    def test_estimate_rightsizing_savings_returns_dict(self) -> None:
        from hexawyn.mcp.tools.estimate_rightsizing_savings import estimate_rightsizing_savings

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_rightsizing_adapter", return_value=MagicMock()),
        ):
            result = estimate_rightsizing_savings()

        assert isinstance(result, dict)

    def test_estimate_rightsizing_savings_handles_error(self) -> None:
        from hexawyn.mcp.tools.estimate_rightsizing_savings import estimate_rightsizing_savings

        with (
            patch(
                "hexawyn.mcp.server.build_rightsizing_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = estimate_rightsizing_savings()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.estimate_rightsizing_savings")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
