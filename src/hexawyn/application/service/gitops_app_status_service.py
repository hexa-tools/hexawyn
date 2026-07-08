from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_command import (
    GitOpsAppStatusCommand,
)
from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_response import (
    GitOpsAppStatusResponse,
)
from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_service_port import (
    GitOpsAppStatusServicePort,
)


class GitOpsAppStatusService(GitOpsAppStatusServicePort):
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def get_status(self, command: GitOpsAppStatusCommand) -> GitOpsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitOpsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,
            revision=app.revision,
            message=app.message,
        )
