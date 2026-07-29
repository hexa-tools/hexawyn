"""Unit tests for MCP tool: estimate_rightsizing_savings."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestEstimateRightsizingSavingsTool:
    def test_estimate_rightsizing_savings_returns_dict(self) -> None:
        from hexawyn.mcp.tools.estimate_rightsizing_savings import (
            estimate_rightsizing_savings,
        )

        with patch("hexawyn.mcp.server.build_rightsizing_adapter", return_value=MagicMock()):
            result = estimate_rightsizing_savings()

        assert isinstance(result, dict)
        assert "error" in result

    def test_estimate_rightsizing_savings_handles_error(self) -> None:
        from hexawyn.mcp.tools.estimate_rightsizing_savings import (
            estimate_rightsizing_savings,
        )

        with patch(
            "hexawyn.mcp.server.build_rightsizing_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = estimate_rightsizing_savings()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_estimate_rightsizing_savings_success_path(self) -> None:
        from hexawyn.mcp.tools.estimate_rightsizing_savings import (
            estimate_rightsizing_savings,
        )

        mock_rec = MagicMock()
        mock_rec.resource_name = "test-deploy"
        mock_rec.namespace = "test-ns"
        mock_rec.kind = "Deployment"
        mock_rec.rightsizing_type = MagicMock()
        mock_rec.rightsizing_type.value = "cpu_memory"
        mock_rec.current_cpu_cores = 2.0
        mock_rec.recommended_cpu_cores = 1.5
        mock_rec.current_memory_mi = 1024
        mock_rec.recommended_memory_mi = 768.0
        mock_rec.monthly_savings_usd = 30.0
        mock_rec.waste_percentage = 25.0
        mock_rec.reason = "over-provisioned"
        mock_rec.priority = "high"
        mock_report = MagicMock()
        mock_report.recommendations = [mock_rec]
        mock_report.total_monthly_savings_usd = 30.0
        mock_report.skipped_count = 1
        mock_response = MagicMock()
        mock_response.report = mock_report
        mock_response.metrics_server_available = True
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_rightsizing_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.estimate_rightsizing_savings.EstimateRightsizingSavingsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = estimate_rightsizing_savings()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.estimate_rightsizing_savings")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
