"""Unit tests for MCP tool: compute_optimization_roi."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeOptimizationRoiTool:
    def test_compute_optimization_roi_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_optimization_roi import compute_optimization_roi

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_optimization_roi_adapter", return_value=MagicMock()),
        ):
            result = compute_optimization_roi(sprint_id="test")

        assert isinstance(result, dict)

    def test_compute_optimization_roi_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_optimization_roi import compute_optimization_roi

        with (
            patch(
                "hexawyn.mcp.server.build_optimization_roi_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compute_optimization_roi(sprint_id="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_optimization_roi")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
