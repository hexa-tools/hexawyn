from __future__ import annotations

from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_command import (
    GitOpsAppStatusCommand,
)
from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_response import (
    GitOpsAppStatusResponse,
)
from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_service_port import (
    GitOpsAppStatusServicePort,
)


class GitOpsAppStatusUseCase:
    def __init__(self, service: GitOpsAppStatusServicePort) -> None:
        self._service = service

    def execute(self, command: GitOpsAppStatusCommand) -> GitOpsAppStatusResponse:
        return self._service.get_status(command)
