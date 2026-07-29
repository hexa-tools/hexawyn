"""Unit tests for MCP tool: cost_profiling."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCostProfilingTool:
    def test_cost_profiling_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cost_profiling import cost_profiling

        mock_response = MagicMock()
        mock_response.time_window_minutes = 60
        mock_response.ranked_endpoints = []
        mock_response.optimisation_candidates = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cost_profiling_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.cost_profiling.CostProfilingUseCase",
                return_value=mock_uc,
            ),
        ):
            result = cost_profiling()

        assert isinstance(result, dict)
        assert "ranked_endpoints" in result

    def test_cost_profiling_handles_error(self) -> None:
        from hexawyn.mcp.tools.cost_profiling import cost_profiling

        with patch(
            "hexawyn.mcp.server.build_cost_profiling_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = cost_profiling()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cost_profiling")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
