"""Unit tests for MCP tool: compute_slo_error_budget."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeSloErrorBudgetTool:
    def test_compute_slo_error_budget_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_slo_error_budget import compute_slo_error_budget

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_error_budget_adapter", return_value=MagicMock()),
        ):
            result = compute_slo_error_budget(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_compute_slo_error_budget_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_slo_error_budget import compute_slo_error_budget

        with (
            patch(
                "hexawyn.mcp.server.build_error_budget_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compute_slo_error_budget(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_slo_error_budget")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
