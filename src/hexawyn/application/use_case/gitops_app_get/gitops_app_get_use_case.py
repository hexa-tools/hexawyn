from __future__ import annotations

from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_command import (
    GitOpsAppGetCommand,
)
from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_response import (
    GitOpsAppGetResponse,
)
from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_service_port import (
    GitOpsAppGetServicePort,
)


class GitOpsAppGetUseCase:
    def __init__(self, service: GitOpsAppGetServicePort) -> None:
        self._service = service

    def execute(self, command: GitOpsAppGetCommand) -> GitOpsAppGetResponse:
        return self._service.get_app(command)
