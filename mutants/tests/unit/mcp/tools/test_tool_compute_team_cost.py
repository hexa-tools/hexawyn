"""Unit tests for MCP tool: compute_team_cost."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeTeamCostTool:
    def test_compute_team_cost_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_team_cost import compute_team_cost

        with patch("hexawyn.mcp.server.build_team_cost_adapter", return_value=MagicMock()):
            result = compute_team_cost()

        assert isinstance(result, dict)
        assert "error" in result

    def test_compute_team_cost_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_team_cost import compute_team_cost

        with patch(
            "hexawyn.mcp.server.build_team_cost_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = compute_team_cost()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_compute_team_cost_success_path(self) -> None:
        from hexawyn.mcp.tools.compute_team_cost import compute_team_cost

        mock_team = MagicMock()
        mock_team.team_name = "team-a"
        mock_team.total_cost = 100.0
        mock_team.cpu_cost = 50.0
        mock_team.memory_cost = 30.0
        mock_team.storage_cost = 20.0
        mock_team.namespace_count = 3
        mock_team.days_active = 30
        mock_team.is_prorated = False
        mock_prev = MagicMock()
        mock_prev.team_name = "team-a"
        mock_prev.total_cost = 90.0
        mock_result = MagicMock()
        mock_result.month = "2024-01"
        mock_result.total_cost = 100.0
        mock_result.unattributed_cost = 10.0
        mock_result.teams = [mock_team]
        mock_result.previous_month_teams = [mock_prev]
        mock_response = MagicMock()
        mock_response.result = mock_result
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_team_cost_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.compute_team_cost.ComputeTeamCostUseCase",
                return_value=mock_uc,
            ),
        ):
            result = compute_team_cost()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_team_cost")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
