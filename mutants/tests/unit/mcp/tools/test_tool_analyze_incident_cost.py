"""Unit tests for MCP tool: analyze_incident_cost."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAnalyzeIncidentCostTool:
    def test_analyze_incident_cost_returns_dict(self) -> None:
        from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

        with patch("hexawyn.mcp.server.build_incident_cost_adapter", return_value=MagicMock()):
            result = analyze_incident_cost()

        assert isinstance(result, dict)
        assert "error" in result

    def test_analyze_incident_cost_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

        with patch(
            "hexawyn.mcp.server.build_incident_cost_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = analyze_incident_cost()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_analyze_incident_cost_success_path(self) -> None:
        from hexawyn.mcp.tools.analyze_incident_cost import analyze_incident_cost

        mock_report = MagicMock()
        mock_report.business_service_name = "test-svc"
        mock_report.downtime_minutes = 30
        mock_report.revenue_impact_eur = 1000.0
        mock_report.total_cost_eur = 1500.0
        mock_response = MagicMock()
        mock_response.result = mock_report
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_incident_cost_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.analyze_incident_cost.AnalyzeIncidentCostUseCase",
                return_value=mock_uc,
            ),
        ):
            result = analyze_incident_cost()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_incident_cost")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
