"""Unit tests for MCP tool: metric_correlation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestMetricCorrelationTool:
    def test_metric_correlation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.metric_correlation import metric_correlation

        mock_response = MagicMock()
        mock_response.primary_service = "svc-a"
        mock_response.correlated_service = "svc-b"
        mock_response.status = "correlated"
        mock_response.coefficient = 0.85
        mock_response.lag_index = 0
        mock_response.hypothesis = "test"
        mock_response.data_point_count = 100
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_metric_correlation_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.metric_correlation.MetricCorrelationUseCase",
                return_value=mock_uc,
            ),
        ):
            result = metric_correlation("svc-a", "svc-b")

        assert isinstance(result, dict)
        assert result["primary_service"] == "svc-a"

    def test_metric_correlation_handles_error(self) -> None:
        from hexawyn.mcp.tools.metric_correlation import metric_correlation

        with patch(
            "hexawyn.mcp.server.build_metric_correlation_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = metric_correlation("svc-a", "svc-b")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.metric_correlation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
