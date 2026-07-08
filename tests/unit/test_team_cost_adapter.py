"""RED → GREEN — TeamCostKubernetesAdapter unit tests."""

from hexawyn.adapters.secondary.gitops.team_cost_kubernetes_adapter import (
    TeamCostKubernetesAdapter,
)
from hexawyn.application.ports.driven.team_cost_port import TeamCostPort


class TestTeamCostKubernetesAdapter:
    def test_implements_port(self) -> None:
        adapter = TeamCostKubernetesAdapter()
        assert isinstance(adapter, TeamCostPort)

    def test_fetch_namespace_resources_returns_empty(self) -> None:
        adapter = TeamCostKubernetesAdapter()
        result = adapter.fetch_namespace_resources("2026-07")
        assert result == []
