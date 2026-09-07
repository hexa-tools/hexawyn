"""Unit tests for MCP tool: generate_sla_report."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGenerateSlaReportTool:
    def test_generate_sla_report_returns_dict(self) -> None:
        from hexawyn.mcp.tools.generate_sla_report import generate_sla_report

        mock_uc = MagicMock()
        mock_uc.execute.return_value = MagicMock()

        with (
            patch(
                "hexawyn.mcp.tools.generate_sla_report.GenerateSLAReportUseCase",
                return_value=mock_uc,
            ),
            patch("hexawyn.mcp.server.build_sla_report_adapter", return_value=MagicMock()),
        ):
            result = generate_sla_report()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_generate_sla_report_handles_error(self) -> None:
        from hexawyn.mcp.tools.generate_sla_report import generate_sla_report

        with patch(
            "hexawyn.mcp.server.build_sla_report_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = generate_sla_report()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.generate_sla_report")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
