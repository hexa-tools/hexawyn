"""Unit tests for MCP tool: prometheus_query."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPrometheusQueryTool:
    def test_prometheus_query_returns_dict(self) -> None:
        from hexawyn.mcp.tools.prometheus_query import prometheus_query

        with patch(
            "hexawyn.mcp.server.build_metrics_query_adapter",
            return_value=MagicMock(),
        ):
            result = prometheus_query()

        assert isinstance(result, dict)
        assert "error" in result

    def test_prometheus_query_handles_error(self) -> None:
        from hexawyn.mcp.tools.prometheus_query import prometheus_query

        with patch(
            "hexawyn.mcp.server.build_metrics_query_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = prometheus_query()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_prometheus_query_success_path(self) -> None:
        from hexawyn.mcp.tools.prometheus_query import prometheus_query

        with (
            patch(
                "hexawyn.mcp.server.build_metrics_query_adapter",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.tools.prometheus_query.PrometheusQueryUseCase") as mock_uc,
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = prometheus_query()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.prometheus_query")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
