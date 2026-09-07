"""Unit tests for MCP tool: report_unauthorized_access."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestReportUnauthorizedAccessTool:
    def test_report_unauthorized_access_returns_dict(self) -> None:
        from hexawyn.mcp.tools.report_unauthorized_access import (
            report_unauthorized_access,
        )

        with patch(
            "hexawyn.mcp.server.build_unauthorized_access_adapter",
            return_value=MagicMock(),
        ):
            result = report_unauthorized_access()

        assert isinstance(result, dict)
        assert "error" in result

    def test_report_unauthorized_access_handles_error(self) -> None:
        from hexawyn.mcp.tools.report_unauthorized_access import (
            report_unauthorized_access,
        )

        with patch(
            "hexawyn.mcp.server.build_unauthorized_access_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = report_unauthorized_access()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.report_unauthorized_access")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
