from __future__ import annotations

from hexawyn.application.ports.driving.gitops_detect.gitops_detect_command import (
    GitOpsDetectCommand,
)
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_response import (
    GitOpsDetectResponse,
)
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_service_port import (
    GitOpsDetectServicePort,
)


class GitOpsDetectUseCase:
    def __init__(self, service: GitOpsDetectServicePort) -> None:
        self._service = service

    def execute(self, command: GitOpsDetectCommand) -> GitOpsDetectResponse:
        return self._service.detect(command)
