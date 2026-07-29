from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_sources_list.command import GitopsSourcesListCommand
from hexawyn.application.use_case.gitops.gitops_sources_list.response import (
    GitopsSourcesListResponse,
)


class GitopsSourcesListUseCase:
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def execute(self, command: GitopsSourcesListCommand) -> GitopsSourcesListResponse:
        sources = self._gitops.list_sources(namespace=command.namespace)
        return GitopsSourcesListResponse(sources=[asdict(source) for source in sources])
