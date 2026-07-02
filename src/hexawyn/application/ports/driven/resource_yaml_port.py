from abc import ABC, abstractmethod

from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest


class ResourceYAMLPort(ABC):
    @abstractmethod
    def fetch_resource(self, request: ResourceYAMLRequest) -> dict[str, object]: ...
    @abstractmethod
    def resource_exists(self, request: ResourceYAMLRequest) -> bool: ...
