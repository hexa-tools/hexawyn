"""Unit tests for MCP tool: report_critical_vulnerabilities."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestReportCriticalVulnerabilitiesTool:
    def test_report_critical_vulnerabilities_returns_dict(self) -> None:
        from hexawyn.mcp.tools.report_critical_vulnerabilities import (
            report_critical_vulnerabilities,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_critical_cve_adapter", return_value=MagicMock()),
        ):
            result = report_critical_vulnerabilities()

        assert isinstance(result, dict)

    def test_report_critical_vulnerabilities_handles_error(self) -> None:
        from hexawyn.mcp.tools.report_critical_vulnerabilities import (
            report_critical_vulnerabilities,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_critical_cve_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = report_critical_vulnerabilities()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.report_critical_vulnerabilities")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
