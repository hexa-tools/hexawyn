from __future__ import annotations

from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.application.use_case.resource_yaml.command import (
    ResourceYAMLCommand,
)
from hexawyn.application.use_case.resource_yaml.response import (
    ResourceYAMLResponse,
)
from hexawyn.application.ports.driving.resource_yaml.resource_yaml_service_port import (
    ResourceYAMLServicePort,
)
from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest, ResourceYAMLResult


class ResourceYAMLService(ResourceYAMLServicePort):
    def __init__(self, port: ResourceYAMLPort) -> None:
        self._port = port

    def get_resource(self, command: ResourceYAMLCommand) -> ResourceYAMLResponse:
        req = ResourceYAMLRequest(
            resource_name=command.resource_name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYAMLResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,
        )
