from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_command import (
    GitOpsAppsListCommand,
)
from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_response import (
    GitOpsAppsListResponse,
)


class GitOpsAppsListServicePort(ABC):
    @abstractmethod
    def list_apps(self, command: GitOpsAppsListCommand) -> GitOpsAppsListResponse:
        """List all GitOps applications."""
