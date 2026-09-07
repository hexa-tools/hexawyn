from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.resource_yaml.command import (  # type: ignore
    ResourceYAMLCommand,
)
from hexawyn.application.use_case.cluster.resource_yaml.response import (  # type: ignore
    ResourceYAMLResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ResourceYAMLServicePort(ABC):
    @abstractmethod
    def get_resource(self, command: ResourceYAMLCommand) -> ResourceYAMLResponse: ...
