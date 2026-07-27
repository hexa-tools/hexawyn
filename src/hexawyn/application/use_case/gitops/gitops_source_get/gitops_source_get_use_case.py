from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_source_get.command import GitopsSourceGetCommand
from hexawyn.application.use_case.gitops.gitops_source_get.response import GitopsSourceGetResponse


class GitopsSourceGetUseCase:
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def execute(self, command: GitopsSourceGetCommand) -> GitopsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitopsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,  # type: ignore
            message=source.message,  # type: ignore
        )
