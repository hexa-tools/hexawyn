from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.gitops_detect.gitops_detect_command import (
    GitOpsDetectCommand,
)
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_response import (
    GitOpsDetectResponse,
)


class GitOpsDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: GitOpsDetectCommand) -> GitOpsDetectResponse:
        """Detect which GitOps engine is installed in the cluster."""
