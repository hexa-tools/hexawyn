"""Unit tests for MCP tool: span_bottleneck_analysis."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSpanBottleneckAnalysisTool:
    def test_span_bottleneck_analysis_returns_dict(self) -> None:
        from hexawyn.mcp.tools.span_bottleneck_analysis import span_bottleneck_analysis

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_span_bottleneck_adapter", return_value=MagicMock()),
        ):
            result = span_bottleneck_analysis()

        assert isinstance(result, dict)

    def test_span_bottleneck_analysis_handles_error(self) -> None:
        from hexawyn.mcp.tools.span_bottleneck_analysis import span_bottleneck_analysis

        with (
            patch(
                "hexawyn.mcp.server.build_span_bottleneck_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = span_bottleneck_analysis()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.span_bottleneck_analysis")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
