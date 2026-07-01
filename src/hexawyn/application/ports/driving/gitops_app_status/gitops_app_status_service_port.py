from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_command import (
    GitOpsAppStatusCommand,
)
from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_response import (
    GitOpsAppStatusResponse,
)


class GitOpsAppStatusServicePort(ABC):
    @abstractmethod
    def get_status(self, command: GitOpsAppStatusCommand) -> GitOpsAppStatusResponse:
        """Get sync + health status of a specific GitOps application."""
