from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops_sources_list.command import (
    GitOpsSourcesListCommand,
)
from hexawyn.application.use_case.gitops_sources_list.response import (
    GitOpsSourcesListResponse,
)
from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_service_port import (
    GitOpsSourcesListServicePort,
)


class GitOpsSourcesListService(GitOpsSourcesListServicePort):
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def list_sources(self, command: GitOpsSourcesListCommand) -> GitOpsSourcesListResponse:
        sources = self._gitops.list_sources(namespace=command.namespace)
        return GitOpsSourcesListResponse(
            sources=[asdict(source) for source in sources],
        )
