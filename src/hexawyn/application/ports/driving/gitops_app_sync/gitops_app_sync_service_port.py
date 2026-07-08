from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.gitops_app_sync.gitops_app_sync_command import (
    GitOpsAppSyncCommand,
)
from hexawyn.application.ports.driving.gitops_app_sync.gitops_app_sync_response import (
    GitOpsAppSyncResponse,
)


class GitOpsAppSyncServicePort(ABC):
    @abstractmethod
    def get_sync_status(self, command: GitOpsAppSyncCommand) -> GitOpsAppSyncResponse:
        """Get the last sync status — read-only, never triggers sync."""
