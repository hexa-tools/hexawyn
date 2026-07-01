from abc import ABC, abstractmethod

from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest


class ServiceDependencyGraphPort(ABC):
    @abstractmethod
    def fetch_edges(self, request: DependencyGraphRequest) -> list[dict[str, object]]: ...
