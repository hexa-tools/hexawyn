from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops_app_sync.command import (
    GitOpsAppSyncCommand,
)
from hexawyn.application.use_case.gitops_app_sync.response import (
    GitOpsAppSyncResponse,
)
from hexawyn.application.ports.driving.gitops_app_sync.gitops_app_sync_service_port import (
    GitOpsAppSyncServicePort,
)


class GitOpsAppSyncService(GitOpsAppSyncServicePort):
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def get_sync_status(self, command: GitOpsAppSyncCommand) -> GitOpsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitOpsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,
            revision=app.revision,
            message=app.message,
        )
