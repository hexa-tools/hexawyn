from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.command import (
    CiliumServiceGraphCommand,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.response import (
    CiliumServiceGraphResponse,
)
from hexawyn.domain.models.service_dependency_graph import (
    DependencyGraph,
    DependencyGraphRequest,
)


class CiliumServiceGraphUseCase:
    def __init__(self, port: ServiceDependencyGraphPort) -> None:
        self._port = port

    def execute(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )
