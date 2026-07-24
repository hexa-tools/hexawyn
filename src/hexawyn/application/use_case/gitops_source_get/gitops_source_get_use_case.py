from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops_source_get.command import GitopsSourceGetCommand
from hexawyn.application.use_case.gitops_source_get.response import GitopsSourceGetResponse


class GitopsSourceGetUseCase:
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def execute(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        s = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=s.name,
            namespace=s.namespace,
            kind=s.kind,
            url=s.url,
            ready=s.ready,
            last_updated_at=s.last_updated_at,
            message=s.message,
        )
