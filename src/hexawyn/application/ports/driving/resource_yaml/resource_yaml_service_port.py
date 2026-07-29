from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.resource_yaml.command import (  # type: ignore
    ResourceYAMLCommand,
)
from hexawyn.application.use_case.cluster.resource_yaml.response import (  # type: ignore
    ResourceYAMLResponse,
)


class ResourceYAMLServicePort(ABC):
    @abstractmethod
    def get_resource(self, command: ResourceYAMLCommand) -> ResourceYAMLResponse: ...
