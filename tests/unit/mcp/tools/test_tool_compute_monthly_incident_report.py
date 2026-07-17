"""Unit tests for MCP tool: compute_monthly_incident_report."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeMonthlyIncidentReportTool:
    def test_compute_monthly_incident_report_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_monthly_incident_report import (
            compute_monthly_incident_report,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_monthly_incident_adapter", return_value=MagicMock()),
        ):
            result = compute_monthly_incident_report()

        assert isinstance(result, dict)

    def test_compute_monthly_incident_report_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_monthly_incident_report import (
            compute_monthly_incident_report,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_monthly_incident_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = compute_monthly_incident_report()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_monthly_incident_report")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
