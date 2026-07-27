from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.gitops_detect.command import (  # type: ignore
    GitOpsDetectCommand,
)
from hexawyn.application.use_case.gitops.gitops_detect.response import (  # type: ignore
    GitOpsDetectResponse,
)


class GitOpsDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: GitOpsDetectCommand) -> GitOpsDetectResponse: ...
