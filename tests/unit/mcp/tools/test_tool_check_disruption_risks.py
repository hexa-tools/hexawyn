"""Unit tests for MCP tool: check_disruption_risks."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckDisruptionRisksTool:
    def test_check_disruption_risks_returns_dict(self) -> None:
        from hexawyn.mcp.tools.check_disruption_risks import check_disruption_risks

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_disruption_risk_adapter", return_value=MagicMock()),
        ):
            result = check_disruption_risks()

        assert isinstance(result, dict)

    def test_check_disruption_risks_handles_error(self) -> None:
        from hexawyn.mcp.tools.check_disruption_risks import check_disruption_risks

        with (
            patch(
                "hexawyn.mcp.server.build_disruption_risk_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = check_disruption_risks()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.check_disruption_risks")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
