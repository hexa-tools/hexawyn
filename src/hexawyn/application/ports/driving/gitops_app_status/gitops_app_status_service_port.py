from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_app_status.command import (  # type: ignore
    GitOpsAppStatusCommand,
)
from hexawyn.application.use_case.gitops.gitops_app_status.response import (  # type: ignore
    GitOpsAppStatusResponse,
)


class GitOpsAppStatusServicePort(ABC):
    @abstractmethod
    def get_status(self, command: GitOpsAppStatusCommand) -> GitOpsAppStatusResponse: ...
