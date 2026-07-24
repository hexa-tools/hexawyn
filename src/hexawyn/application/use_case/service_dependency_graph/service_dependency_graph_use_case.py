from dataclasses import asdict

from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.application.use_case.service_dependency_graph.command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.use_case.service_dependency_graph.response import (
    ServiceDependencyGraphResponse,
)


class ServiceDependencyGraphUseCase:
    def __init__(self, port: ServiceDependencyGraphPort) -> None:
        self._port = port

    def execute(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        graph = self._port.get_service_dependency_graph(namespace=command.namespace)
        return ServiceDependencyGraphResponse(
            nodes=[asdict(n) for n in graph.nodes], edges=[asdict(e) for e in graph.edges]
        )
