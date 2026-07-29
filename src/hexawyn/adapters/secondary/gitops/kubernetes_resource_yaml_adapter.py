from __future__ import annotations

import subprocess

from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.domain.models.resource_yaml import ResourceYAMLRequest


class KubernetesResourceYAMLAdapter(ResourceYAMLPort):
    def fetch_resource(self, request: ResourceYAMLRequest) -> dict[str, object]:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                    "-o",
                    "yaml",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode == 0 and result.stdout.strip():
                return {"kind": request.kind, "name": request.resource_name, "yaml": result.stdout}
            return {}
        except Exception:
            return {}

    def resource_exists(self, request: ResourceYAMLRequest) -> bool:
        try:
            result = subprocess.run(
                [
                    "kubectl",
                    "get",
                    request.kind.lower(),
                    request.resource_name,
                    "-n",
                    request.namespace,
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return result.returncode == 0
        except Exception:
            return False
