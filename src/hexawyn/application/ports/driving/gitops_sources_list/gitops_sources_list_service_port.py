from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_sources_list.command import (  # type: ignore
    GitOpsSourcesListCommand,
)
from hexawyn.application.use_case.gitops.gitops_sources_list.response import (  # type: ignore
    GitOpsSourcesListResponse,
)


class GitOpsSourcesListServicePort(ABC):
    @abstractmethod
    def list_sources(self, command: GitOpsSourcesListCommand) -> GitOpsSourcesListResponse: ...
