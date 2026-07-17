"""Unit tests for MCP tool: metric_correlation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestMetricCorrelationTool:
    def test_metric_correlation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.metric_correlation import metric_correlation

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_metric_correlation_adapter", return_value=MagicMock()),
        ):
            result = metric_correlation(
                primary_service="test-primary_service", correlated_service="test-correlated_service"
            )

        assert isinstance(result, dict)

    def test_metric_correlation_handles_error(self) -> None:
        from hexawyn.mcp.tools.metric_correlation import metric_correlation

        with (
            patch(
                "hexawyn.mcp.server.build_metric_correlation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = metric_correlation(
                primary_service="test-primary_service", correlated_service="test-correlated_service"
            )

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.metric_correlation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
