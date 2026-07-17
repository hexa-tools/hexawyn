"""Unit tests for MCP tool: compute_prediction_roi."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputePredictionRoiTool:
    def test_compute_prediction_roi_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_prediction_roi import compute_prediction_roi

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_prediction_roi_adapter", return_value=MagicMock()),
        ):
            result = compute_prediction_roi(period="test")

        assert isinstance(result, dict)

    def test_compute_prediction_roi_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_prediction_roi import compute_prediction_roi

        with (
            patch(
                "hexawyn.mcp.server.build_prediction_roi_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compute_prediction_roi(period="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_prediction_roi")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
