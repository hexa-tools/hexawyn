from __future__ import annotations

from hexawyn.application.ports.driving.gitops_source_get.gitops_source_get_command import (
    GitOpsSourceGetCommand,
)
from hexawyn.application.ports.driving.gitops_source_get.gitops_source_get_response import (
    GitOpsSourceGetResponse,
)
from hexawyn.application.ports.driving.gitops_source_get.gitops_source_get_service_port import (
    GitOpsSourceGetServicePort,
)


class GitOpsSourceGetUseCase:
    def __init__(self, service: GitOpsSourceGetServicePort) -> None:
        self._service = service

    def execute(self, command: GitOpsSourceGetCommand) -> GitOpsSourceGetResponse:
        return self._service.get_source(command)
