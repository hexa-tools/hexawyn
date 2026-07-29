"""Unit tests for MCP tool: canary_comparison."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCanaryComparisonTool:
    def test_canary_comparison_returns_dict(self) -> None:
        from hexawyn.mcp.tools.canary_comparison import canary_comparison

        mock_response = MagicMock()
        mock_response.service_name = "test-svc"
        mock_response.canary_version = "v2"
        mock_response.stable_version = "v1"
        mock_response.verdict = "safe"
        mock_response.confidence = 0.9
        mock_response.p99_delta_pct = 1.0
        mock_response.error_rate_delta_pct = 0.0
        mock_response.canary_count = 10
        mock_response.stable_count = 90
        mock_response.traffic_split_pct = 10.0
        mock_response.reasons = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_canary_comparison_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.canary_comparison.CanaryComparisonUseCase",
                return_value=mock_uc,
            ),
        ):
            result = canary_comparison("test-svc")

        assert isinstance(result, dict)
        assert result["service_name"] == "test-svc"

    def test_canary_comparison_handles_error(self) -> None:
        from hexawyn.mcp.tools.canary_comparison import canary_comparison

        with patch(
            "hexawyn.mcp.server.build_canary_comparison_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = canary_comparison("test-svc")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.canary_comparison")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
