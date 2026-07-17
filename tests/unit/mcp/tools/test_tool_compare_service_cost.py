"""Unit tests for MCP tool: compare_service_cost."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCompareServiceCostTool:
    def test_compare_service_cost_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compare_service_cost import compare_service_cost

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_service_cost_adapter", return_value=MagicMock()),
        ):
            result = compare_service_cost(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_compare_service_cost_handles_error(self) -> None:
        from hexawyn.mcp.tools.compare_service_cost import compare_service_cost

        with (
            patch(
                "hexawyn.mcp.server.build_service_cost_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compare_service_cost(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compare_service_cost")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
