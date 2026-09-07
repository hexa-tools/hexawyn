"""Unit tests for MCP tool: error_attribution."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestErrorAttributionTool:
    def test_error_attribution_returns_dict(self) -> None:
        from hexawyn.mcp.tools.error_attribution import error_attribution

        with patch("hexawyn.mcp.server.build_error_attribution_adapter", return_value=MagicMock()):
            result = error_attribution(gateway="test-gateway")

        assert isinstance(result, dict)
        assert "error" in result

    def test_error_attribution_handles_error(self) -> None:
        from hexawyn.mcp.tools.error_attribution import error_attribution

        with patch(
            "hexawyn.mcp.server.build_error_attribution_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = error_attribution(gateway="test-gateway")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.error_attribution")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
