from __future__ import annotations

from hexawyn.application.ports.driving.gitops_app_sync.gitops_app_sync_command import (
    GitOpsAppSyncCommand,
)
from hexawyn.application.ports.driving.gitops_app_sync.gitops_app_sync_response import (
    GitOpsAppSyncResponse,
)
from hexawyn.application.ports.driving.gitops_app_sync.gitops_app_sync_service_port import (
    GitOpsAppSyncServicePort,
)


class GitOpsAppSyncUseCase:
    def __init__(self, service: GitOpsAppSyncServicePort) -> None:
        self._service = service

    def execute(self, command: GitOpsAppSyncCommand) -> GitOpsAppSyncResponse:
        return self._service.get_sync_status(command)
