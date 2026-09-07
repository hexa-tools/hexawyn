"""Unit tests for MCP tool: compute_monthly_incident_report."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeMonthlyIncidentReportTool:
    def test_compute_monthly_incident_report_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_monthly_incident_report import (
            compute_monthly_incident_report,
        )

        with patch("hexawyn.mcp.server.build_monthly_incident_adapter", return_value=MagicMock()):
            result = compute_monthly_incident_report()

        assert isinstance(result, dict)
        assert "error" in result

    def test_compute_monthly_incident_report_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_monthly_incident_report import (
            compute_monthly_incident_report,
        )

        with patch(
            "hexawyn.mcp.server.build_monthly_incident_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = compute_monthly_incident_report()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_compute_monthly_incident_report_success_path(self) -> None:
        from hexawyn.mcp.tools.compute_monthly_incident_report import (
            compute_monthly_incident_report,
        )

        mock_severity = MagicMock()
        mock_severity.count = 1
        mock_severity.downtime_minutes = 30
        mock_service = MagicMock()
        mock_service.service_name = "test-svc"
        mock_service.total_downtime = 30
        mock_service.incident_count = 1
        mock_result = MagicMock()
        mock_result.month = "2024-01"
        mock_result.total_count = 5
        mock_result.total_downtime_minutes = 120
        mock_result.per_severity = {"P1": mock_severity}
        mock_result.most_impacted_services = [mock_service]
        mock_result.previous_month_total_count = 3
        mock_result.previous_month_downtime_minutes = 90
        mock_result.incidents_decreasing = False
        mock_response = MagicMock()
        mock_response.result = mock_result
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_monthly_incident_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.compute_monthly_incident_report.ComputeMonthlyIncidentReportUseCase",
                return_value=mock_uc,
            ),
        ):
            result = compute_monthly_incident_report()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_monthly_incident_report")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
