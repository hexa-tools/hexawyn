from __future__ import annotations

from hexawyn.application.ports.driving.resource_yaml.resource_yaml_command import (
    ResourceYAMLCommand,
)
from hexawyn.application.ports.driving.resource_yaml.resource_yaml_response import (
    ResourceYAMLResponse,
)
from hexawyn.application.ports.driving.resource_yaml.resource_yaml_service_port import (
    ResourceYAMLServicePort,
)


class ResourceYAMLUseCase:
    def __init__(self, service: ResourceYAMLServicePort) -> None:
        self._svc = service

    def execute(self, cmd: ResourceYAMLCommand) -> ResourceYAMLResponse:
        return self._svc.get_resource(cmd)
