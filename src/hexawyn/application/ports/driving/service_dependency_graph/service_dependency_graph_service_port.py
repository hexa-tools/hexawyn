from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_response import (
    ServiceDependencyGraphResponse,
)


class ServiceDependencyGraphServicePort(ABC):
    @abstractmethod
    def build(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse: ...
