from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.response import (
    DetectKustomizePatchConflictsResponse,
)


class DetectKustomizePatchConflictsServicePort(ABC):
    @abstractmethod
    def detect_conflicts(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse: ...
