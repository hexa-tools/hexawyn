from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_command import (
    GitOpsSourcesListCommand,
)
from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_response import (
    GitOpsSourcesListResponse,
)


class GitOpsSourcesListServicePort(ABC):
    @abstractmethod
    def list_sources(self, command: GitOpsSourcesListCommand) -> GitOpsSourcesListResponse:
        """List all GitOps sources."""
