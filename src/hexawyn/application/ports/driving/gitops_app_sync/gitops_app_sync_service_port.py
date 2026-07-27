from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_app_sync.command import (  # type: ignore
    GitOpsAppSyncCommand,
)
from hexawyn.application.use_case.gitops.gitops_app_sync.response import (  # type: ignore
    GitOpsAppSyncResponse,
)


class GitOpsAppSyncServicePort(ABC):
    @abstractmethod
    def get_sync_status(self, command: GitOpsAppSyncCommand) -> GitOpsAppSyncResponse: ...
