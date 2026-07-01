from __future__ import annotations

from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_response import (
    ServiceDependencyGraphResponse,
)
from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_service_port import (
    ServiceDependencyGraphServicePort,
)


class ServiceDependencyGraphUseCase:
    def __init__(self, service: ServiceDependencyGraphServicePort) -> None:
        self._svc = service

    def execute(self, cmd: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        return self._svc.build(cmd)
