"""Unit tests for MCP tool: prometheus_query."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPrometheusQueryTool:
    def test_prometheus_query_returns_dict(self) -> None:
        from hexawyn.mcp.tools.prometheus_query import prometheus_query

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_metrics_query_adapter", return_value=MagicMock()),
        ):
            result = prometheus_query(promql="test")

        assert isinstance(result, dict)

    def test_prometheus_query_handles_error(self) -> None:
        from hexawyn.mcp.tools.prometheus_query import prometheus_query

        with (
            patch(
                "hexawyn.mcp.server.build_metrics_query_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = prometheus_query(promql="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.prometheus_query")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
