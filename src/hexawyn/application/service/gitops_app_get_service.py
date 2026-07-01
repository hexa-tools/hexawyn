from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_command import (
    GitOpsAppGetCommand,
)
from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_response import (
    GitOpsAppGetResponse,
)
from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_service_port import (
    GitOpsAppGetServicePort,
)


class GitOpsAppGetService(GitOpsAppGetServicePort):
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def get_app(self, command: GitOpsAppGetCommand) -> GitOpsAppGetResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitOpsAppGetResponse(
            name=app.name,
            namespace=app.namespace,
            engine=app.engine.value,
            kind=app.kind,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,
            last_commit=app.last_commit,
            source_url=app.source_url,
            revision=app.revision,
            message=app.message,
        )
