from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_response import (
    DetectKustomizePatchConflictsResponse,
)


class DetectKustomizePatchConflictsServicePort(ABC):
    @abstractmethod
    def detect_conflicts(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse: ...
