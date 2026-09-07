from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.service_dependency_graph.command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.use_case.observability.service_dependency_graph.response import (
    ServiceDependencyGraphResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ServiceDependencyGraphServicePort(ABC):
    @abstractmethod
    def build(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse: ...
