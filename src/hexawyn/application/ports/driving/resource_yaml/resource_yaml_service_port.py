from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.resource_yaml.resource_yaml_command import (
    ResourceYAMLCommand,
)
from hexawyn.application.ports.driving.resource_yaml.resource_yaml_response import (
    ResourceYAMLResponse,
)


class ResourceYAMLServicePort(ABC):
    @abstractmethod
    def get_resource(self, command: ResourceYAMLCommand) -> ResourceYAMLResponse: ...
