from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_app_status.command import GitopsAppStatusCommand
from hexawyn.application.use_case.gitops.gitops_app_status.response import GitopsAppStatusResponse


class GitopsAppStatusUseCase:
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def execute(self, command: GitopsAppStatusCommand) -> GitopsAppStatusResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppStatusResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            health_status=app.health_status.value,
            last_synced_at=app.last_synced_at,  # type: ignore
            last_commit=app.last_commit,  # type: ignore
            revision=app.revision,  # type: ignore
            message=app.message,  # type: ignore
        )
