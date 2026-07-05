from __future__ import annotations

from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_response import (
    DetectPrivilegedPodsResponse,
)
from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_service_port import (
    DetectPrivilegedPodsServicePort,
)


class DetectPrivilegedPodsUseCase:
    def __init__(self, service: DetectPrivilegedPodsServicePort) -> None:
        self._svc = service

    def execute(self, command: DetectPrivilegedPodsCommand) -> DetectPrivilegedPodsResponse:
        return self._svc.audit_pod_security(command)
