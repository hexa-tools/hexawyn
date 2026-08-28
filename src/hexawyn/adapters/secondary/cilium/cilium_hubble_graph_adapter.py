"""HubbleDependencyGraphAdapter — builds the service graph from real Cilium flows."""

from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.domain.models.cilium import CiliumFlowQuery
from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest
from hexawyn.domain.services.cilium.graph_builder import build_graph_edges


class HubbleDependencyGraphAdapter(ServiceDependencyGraphPort):
    """Service graph from observed Hubble flows (vs inferred topology)."""

    def __init__(self, hubble_port: CiliumHubblePort) -> None:
        self._hubble_port = hubble_port

    def fetch_edges(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=request.time_window_minutes,
                limit=1000,
            )
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)
