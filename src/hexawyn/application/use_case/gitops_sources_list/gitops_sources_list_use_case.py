from __future__ import annotations

from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_command import (
    GitOpsSourcesListCommand,
)
from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_response import (
    GitOpsSourcesListResponse,
)
from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_service_port import (
    GitOpsSourcesListServicePort,
)


class GitOpsSourcesListUseCase:
    def __init__(self, service: GitOpsSourcesListServicePort) -> None:
        self._service = service

    def execute(self, command: GitOpsSourcesListCommand) -> GitOpsSourcesListResponse:
        return self._service.list_sources(command)
