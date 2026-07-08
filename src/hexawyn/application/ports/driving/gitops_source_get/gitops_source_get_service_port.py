from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.gitops_source_get.gitops_source_get_command import (
    GitOpsSourceGetCommand,
)
from hexawyn.application.ports.driving.gitops_source_get.gitops_source_get_response import (
    GitOpsSourceGetResponse,
)


class GitOpsSourceGetServicePort(ABC):
    @abstractmethod
    def get_source(self, command: GitOpsSourceGetCommand) -> GitOpsSourceGetResponse:
        """Get detailed status of a specific GitOps source."""
