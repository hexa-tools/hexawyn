from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.application.use_case.resource_yaml.command import ResourceYamlCommand
from hexawyn.application.use_case.resource_yaml.response import ResourceYamlResponse


class ResourceYAMLUseCase:
    def __init__(self, port: ResourceYAMLPort) -> None:
        self._port = port

    def execute(self, c: ResourceYamlCommand) -> ResourceYamlResponse:
        yaml_str = self._port.get_resource_yaml(kind=c.kind, name=c.name, namespace=c.namespace)
        return ResourceYamlResponse(yaml_content=yaml_str)
