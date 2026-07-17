"""Unit tests for MCP tool: report_stale_credentials."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestReportStaleCredentialsTool:
    def test_report_stale_credentials_returns_dict(self) -> None:
        from hexawyn.mcp.tools.report_stale_credentials import report_stale_credentials

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_stale_credentials_adapter", return_value=MagicMock()),
        ):
            result = report_stale_credentials()

        assert isinstance(result, dict)

    def test_report_stale_credentials_handles_error(self) -> None:
        from hexawyn.mcp.tools.report_stale_credentials import report_stale_credentials

        with (
            patch(
                "hexawyn.mcp.server.build_stale_credentials_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = report_stale_credentials()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.report_stale_credentials")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
