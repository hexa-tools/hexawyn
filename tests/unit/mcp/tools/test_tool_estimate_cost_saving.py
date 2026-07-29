"""Unit tests for MCP tool: estimate_cost_saving."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestEstimateCostSavingTool:
    def test_estimate_cost_saving_returns_dict(self) -> None:
        from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

        with patch("hexawyn.mcp.server.build_cost_saving_adapter", return_value=MagicMock()):
            result = estimate_cost_saving()

        assert isinstance(result, dict)
        assert "error" in result

    def test_estimate_cost_saving_handles_error(self) -> None:
        from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

        with patch(
            "hexawyn.mcp.server.build_cost_saving_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = estimate_cost_saving()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_estimate_cost_saving_success_path(self) -> None:
        from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

        mock_opp = MagicMock()
        mock_opp.pod_name = "test-pod"
        mock_opp.namespace = "test-ns"
        mock_opp.current_cpu_request = 2.0
        mock_opp.recommended_cpu_request = 0.5
        mock_opp.current_memory_request_mi = 1024
        mock_opp.recommended_memory_request_mi = 512.0
        mock_opp.delta_cores = 1.5
        mock_opp.delta_memory_mi = 512.0
        mock_opp.monthly_saving_usd = 50.0
        mock_opp.hpa_enabled = False
        mock_opp.is_bursty = False
        mock_opp.caveats = None
        mock_ns = MagicMock()
        mock_ns.namespace = "test-ns"
        mock_ns.pod_count = 1
        mock_ns.total_delta_cores = 1.5
        mock_ns.total_delta_memory_mi = 512.0
        mock_ns.total_monthly_saving_usd = 50.0
        mock_report = MagicMock()
        mock_report.top_opportunities = [mock_opp]
        mock_report.namespace_savings = [mock_ns]
        mock_report.total_monthly_saving_usd = 50.0
        mock_report.total_delta_cores = 1.5
        mock_report.total_delta_memory_mi = 512.0
        mock_report.pods_analyzed = 10
        mock_report.pods_excluded = 2
        mock_report.pricing_configured = True
        mock_response = MagicMock()
        mock_response.report = mock_report
        mock_response.previous_total_saving_usd = 45.0
        mock_response.saving_trend = "increasing"
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_cost_saving_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.estimate_cost_saving.EstimateCostSavingUseCase",
                return_value=mock_uc,
            ),
        ):
            result = estimate_cost_saving()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.estimate_cost_saving")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
