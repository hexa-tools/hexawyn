from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops_app_sync.command import GitopsAppSyncCommand
from hexawyn.application.use_case.gitops_app_sync.response import GitopsAppSyncResponse


class GitopsAppSyncUseCase:
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def execute(self, command: GitopsAppSyncCommand) -> GitopsAppSyncResponse:
        app = self._gitops.get_app(name=command.name, namespace=command.namespace)
        return GitopsAppSyncResponse(
            name=app.name,
            namespace=app.namespace,
            sync_status=app.sync_status.value,
            last_synced_at=app.last_synced_at,
            revision=app.revision,
            message=app.message,
        )
