from abc import ABC, abstractmethod

from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ResourceYAMLPort(ABC):
    @abstractmethod
    def fetch_resource(self, request: ResourceYAMLRequest) -> dict[str, object]: ...
    @abstractmethod
    def resource_exists(self, request: ResourceYAMLRequest) -> bool: ...
