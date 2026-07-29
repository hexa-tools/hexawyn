"""Unit tests for MCP tool: report_platform_reliability."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestReportPlatformReliabilityTool:
    def test_report_platform_reliability_returns_dict(self) -> None:
        from hexawyn.mcp.tools.report_platform_reliability import (
            report_platform_reliability,
        )

        with patch(
            "hexawyn.mcp.server.build_platform_reliability_adapter",
            return_value=MagicMock(),
        ):
            result = report_platform_reliability()

        assert isinstance(result, dict)
        assert "error" in result

    def test_report_platform_reliability_handles_error(self) -> None:
        from hexawyn.mcp.tools.report_platform_reliability import (
            report_platform_reliability,
        )

        with patch(
            "hexawyn.mcp.server.build_platform_reliability_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = report_platform_reliability()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_report_platform_reliability_success_path(self) -> None:
        from hexawyn.mcp.tools.report_platform_reliability import (
            report_platform_reliability,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_platform_reliability_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.report_platform_reliability.ReportPlatformReliabilityUseCase"
            ) as mock_uc,
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = report_platform_reliability()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.report_platform_reliability")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
