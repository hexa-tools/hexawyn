from __future__ import annotations

from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest


class OTelDependencyGraphAdapter(ServiceDependencyGraphPort):
    def fetch_edges(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        return []
