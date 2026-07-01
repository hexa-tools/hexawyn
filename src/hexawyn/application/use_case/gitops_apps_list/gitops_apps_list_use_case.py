from __future__ import annotations

from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_command import (
    GitOpsAppsListCommand,
)
from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_response import (
    GitOpsAppsListResponse,
)
from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_service_port import (
    GitOpsAppsListServicePort,
)


class GitOpsAppsListUseCase:
    def __init__(self, service: GitOpsAppsListServicePort) -> None:
        self._service = service

    def execute(self, command: GitOpsAppsListCommand) -> GitOpsAppsListResponse:
        return self._service.list_apps(command)
