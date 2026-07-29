"""Unit tests for MCP tool: check_disruption_risks."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckDisruptionRisksTool:
    def test_check_disruption_risks_returns_dict(self) -> None:
        from hexawyn.mcp.tools.check_disruption_risks import check_disruption_risks

        mock_result = MagicMock()
        mock_result.period_label = "This Week"
        mock_result.has_risks = False
        mock_result.has_data = True
        mock_result.risks = []
        mock_result.warning = ""

        mock_response = MagicMock()
        mock_response.result = mock_result
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_disruption_risk_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.check_disruption_risks.CheckDisruptionRisksUseCase",
                return_value=mock_uc,
            ),
        ):
            result = check_disruption_risks()

        assert isinstance(result, dict)
        assert "has_risks" in result

    def test_check_disruption_risks_handles_error(self) -> None:
        from hexawyn.mcp.tools.check_disruption_risks import check_disruption_risks

        with patch(
            "hexawyn.mcp.server.build_disruption_risk_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = check_disruption_risks()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.check_disruption_risks")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
