"""Unit tests for MCP tool: report_night_interventions."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestReportNightInterventionsTool:
    def test_report_night_interventions_returns_dict(self) -> None:
        from hexawyn.mcp.tools.report_night_interventions import (
            report_night_interventions,
        )

        with patch(
            "hexawyn.mcp.server.build_night_intervention_adapter",
            return_value=MagicMock(),
        ):
            result = report_night_interventions()

        assert isinstance(result, dict)
        assert "error" in result

    def test_report_night_interventions_handles_error(self) -> None:
        from hexawyn.mcp.tools.report_night_interventions import (
            report_night_interventions,
        )

        with patch(
            "hexawyn.mcp.server.build_night_intervention_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = report_night_interventions()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.report_night_interventions")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
