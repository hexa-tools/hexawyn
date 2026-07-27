from __future__ import annotations

from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.application.use_case.cluster.resource_yaml.command import (
    ResourceYamlCommand,
)
from hexawyn.application.use_case.cluster.resource_yaml.response import (
    ResourceYamlResponse,
)
from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest, ResourceYAMLResult


class ResourceYAMLUseCase:
    def __init__(self, port: ResourceYAMLPort) -> None:
        self._port = port

    def execute(self, command: ResourceYamlCommand) -> ResourceYamlResponse:
        req = ResourceYAMLRequest(
            resource_name=command.name, namespace=command.namespace, kind=command.kind
        )
        found = self._port.resource_exists(req)
        data = self._port.fetch_resource(req) if found else {}
        r = ResourceYAMLResult.compute(request=req, yaml_data=data, resource_found=found)
        return ResourceYamlResponse(
            resource_name=r.resource_name,
            namespace=r.namespace,
            kind=r.kind,
            resource_found=r.resource_found,
            yaml_data=r.yaml_data,  # type: ignore
            image_tags=r.image_tags,
            resource_limits=r.resource_limits,  # type: ignore
        )
