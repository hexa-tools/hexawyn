from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops_source_get.command import (
    GitOpsSourceGetCommand,
)
from hexawyn.application.use_case.gitops_source_get.response import (
    GitOpsSourceGetResponse,
)
from hexawyn.application.ports.driving.gitops_source_get.gitops_source_get_service_port import (
    GitOpsSourceGetServicePort,
)


class GitOpsSourceGetService(GitOpsSourceGetServicePort):
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def get_source(self, command: GitOpsSourceGetCommand) -> GitOpsSourceGetResponse:
        source = self._gitops.get_source(name=command.name, namespace=command.namespace)
        return GitOpsSourceGetResponse(
            name=source.name,
            namespace=source.namespace,
            kind=source.kind,
            url=source.url,
            ready=source.ready,
            last_updated_at=source.last_updated_at,
            message=source.message,
        )
