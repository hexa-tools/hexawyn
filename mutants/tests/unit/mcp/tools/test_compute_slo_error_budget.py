"""Unit tests for MCP tool: compute_slo_error_budget."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestComputeSloErrorBudgetTool:
    def test_compute_slo_error_budget_returns_dict(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.workloads.compute_slo_error_budget.compute_slo_error_budget_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.workloads.compute_slo_error_budget.command"] = (
            MagicMock()
        )

        from hexawyn.mcp.tools.compute_slo_error_budget import compute_slo_error_budget

        mock_uc = MagicMock()
        mock_uc.execute.return_value = MagicMock()

        with (
            patch(
                "hexawyn.mcp.tools.compute_slo_error_budget.ComputeSLOErrorBudgetUseCase",
                return_value=mock_uc,
            ),
            patch("hexawyn.mcp.server.build_error_budget_adapter", return_value=MagicMock()),
        ):
            result = compute_slo_error_budget()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_compute_slo_error_budget_handles_error(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.workloads.compute_slo_error_budget.compute_slo_error_budget_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.workloads.compute_slo_error_budget.command"] = (
            MagicMock()
        )

        from hexawyn.mcp.tools.compute_slo_error_budget import compute_slo_error_budget

        with patch(
            "hexawyn.mcp.server.build_error_budget_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = compute_slo_error_budget()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.workloads.compute_slo_error_budget.compute_slo_error_budget_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.workloads.compute_slo_error_budget.command"] = (
            MagicMock()
        )
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_slo_error_budget")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
