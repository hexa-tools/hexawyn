"""Unit tests for MCP tool: global_health_check."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGlobalHealthCheckTool:
    def test_global_health_check_returns_dict(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        mock_cluster_report = MagicMock()
        mock_cluster_report.context_name = "test-ctx"
        mock_cluster_report.reachable = True
        mock_cluster_report.unreachable_reason = None
        mock_cluster_report.health_score = 85.0
        mock_cluster_report.health_status = "healthy"
        mock_cluster_report.categories = {}
        mock_cluster_report.checked_at = MagicMock()
        mock_cluster_report.checked_at.isoformat.return_value = "2024-01-01T00:00:00"

        mock_report = MagicMock()
        mock_report.cluster_reports = [mock_cluster_report]
        mock_report.fleet_score = 85.0
        mock_report.fleet_status = "healthy"
        mock_report.reachable_count = 1
        mock_report.unreachable_count = 0
        mock_report.checked_at = MagicMock()
        mock_report.checked_at.isoformat.return_value = "2024-01-01T00:00:00"

        mock_response = MagicMock()
        mock_response.report = mock_report
        mock_response.fleet_score_trend = "stable"
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_fleet_health_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.global_health_check.GlobalHealthCheckUseCase",
                return_value=mock_uc,
            ),
        ):
            result = global_health_check()

        assert isinstance(result, dict)
        assert result["fleet_status"] == "healthy"

    def test_global_health_check_handles_error(self) -> None:
        from hexawyn.mcp.tools.global_health_check import global_health_check

        with patch(
            "hexawyn.mcp.server.build_fleet_health_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = global_health_check()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.global_health_check")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
