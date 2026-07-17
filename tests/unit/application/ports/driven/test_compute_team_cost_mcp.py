"""RED → GREEN — MCP tool: compute_team_cost."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.team_cost_port import (
    NamespaceResourceData,
    TeamCostPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestComputeTeamCostTool:
    def test_delegates_and_returns_dict(self) -> None:
        mock_port = MagicMock(spec=TeamCostPort)
        mock_port.fetch_namespace_resources.return_value = [
            NamespaceResourceData(
                namespace="payments-prod",
                team_label="payments",
                cpu_cores=20.0,
                memory_gb=80.0,
                storage_gb=100.0,
                month="2026-07",
                days_active=31,
            ),
        ]

        with patch(
            "hexawyn.mcp.server.build_team_cost_adapter",
            return_value=mock_port,
        ):
            from hexawyn.mcp.tools.compute_team_cost import compute_team_cost

            result = compute_team_cost()

        assert len(result["teams"]) == 1
        assert result["teams"][0]["team_name"] == "payments"
        assert result["error"] is None

    def test_handles_exception_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_team_cost_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.compute_team_cost import compute_team_cost

            result = compute_team_cost()

        assert result["total_cost"] == 0.0
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.compute_team_cost import register

        assert callable(register)
