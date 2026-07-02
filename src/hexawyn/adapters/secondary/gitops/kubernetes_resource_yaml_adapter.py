from __future__ import annotations

from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest


class KubernetesResourceYAMLAdapter(ResourceYAMLPort):
    def fetch_resource(self, request: ResourceYAMLRequest) -> dict[str, object]:
        return {}

    def resource_exists(self, request: ResourceYAMLRequest) -> bool:
        return False
