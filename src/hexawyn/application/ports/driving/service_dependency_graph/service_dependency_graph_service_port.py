from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.service_dependency_graph.command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.use_case.observability.service_dependency_graph.response import (
    ServiceDependencyGraphResponse,
)


class ServiceDependencyGraphServicePort(ABC):
    @abstractmethod
    def build(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse: ...
