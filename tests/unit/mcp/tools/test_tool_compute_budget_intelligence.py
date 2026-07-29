"""Unit tests for MCP tool: compute_budget_intelligence."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeBudgetIntelligenceTool:
    def test_compute_budget_intelligence_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_budget_intelligence import compute_budget_intelligence

        with patch(
            "hexawyn.mcp.server.build_budget_intelligence_adapter", return_value=MagicMock()
        ):
            result = compute_budget_intelligence()

        assert isinstance(result, dict)
        assert "error" in result

    def test_compute_budget_intelligence_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_budget_intelligence import compute_budget_intelligence

        with patch(
            "hexawyn.mcp.server.build_budget_intelligence_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = compute_budget_intelligence()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_compute_budget_intelligence_success_path(self) -> None:
        from hexawyn.mcp.tools.compute_budget_intelligence import compute_budget_intelligence

        with (
            patch(
                "hexawyn.mcp.server.build_budget_intelligence_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.compute_budget_intelligence.ComputeBudgetIntelligenceUseCase"
            ) as mock_uc,
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = compute_budget_intelligence()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_budget_intelligence")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
