from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_response import (
    ServiceDependencyGraphResponse,
)
from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_service_port import (
    ServiceDependencyGraphServicePort,
)
from hexawyn.domain.models.service_dependency_graph import DependencyGraph, DependencyGraphRequest


class ServiceDependencyGraphService(ServiceDependencyGraphServicePort):
    def __init__(self, port: ServiceDependencyGraphPort) -> None:
        self._port = port

    def build(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )
