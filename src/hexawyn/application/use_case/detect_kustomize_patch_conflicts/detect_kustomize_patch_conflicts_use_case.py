from __future__ import annotations

from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_response import (
    DetectKustomizePatchConflictsResponse,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_service_port import (
    DetectKustomizePatchConflictsServicePort,
)


class DetectKustomizePatchConflictsUseCase:
    def __init__(self, service: DetectKustomizePatchConflictsServicePort) -> None:
        self._service = service

    def execute(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        return self._service.detect_conflicts(command)
