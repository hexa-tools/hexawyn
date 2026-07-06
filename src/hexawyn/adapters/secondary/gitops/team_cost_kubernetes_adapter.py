from __future__ import annotations

from hexawyn.application.ports.driven.team_cost_port import (
    NamespaceResourceData,
    TeamCostPort,
)


class TeamCostKubernetesAdapter(TeamCostPort):
    def fetch_namespace_resources(self, month: str) -> list[NamespaceResourceData]:
        return []
