from abc import ABC, abstractmethod

from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ServiceDependencyGraphPort(ABC):
    @abstractmethod
    def fetch_edges(self, request: DependencyGraphRequest) -> list[dict[str, object]]: ...
