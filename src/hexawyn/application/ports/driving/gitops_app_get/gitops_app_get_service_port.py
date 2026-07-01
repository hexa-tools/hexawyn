from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_command import (
    GitOpsAppGetCommand,
)
from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_response import (
    GitOpsAppGetResponse,
)


class GitOpsAppGetServicePort(ABC):
    @abstractmethod
    def get_app(self, command: GitOpsAppGetCommand) -> GitOpsAppGetResponse:
        """Get detailed status of a specific GitOps application."""
