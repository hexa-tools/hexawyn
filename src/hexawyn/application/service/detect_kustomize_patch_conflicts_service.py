from __future__ import annotations

from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    KustomizePatchAnalysisPort,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_response import (
    DetectKustomizePatchConflictsResponse,
)
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_service_port import (
    DetectKustomizePatchConflictsServicePort,
)
from hexawyn.domain.services.kustomize_patch_conflict.kustomize_patch_conflict_engine import (
    KustomizePatchConflictEngine,
)


class DetectKustomizePatchConflictsService(DetectKustomizePatchConflictsServicePort):
    def __init__(self, analysis_port: KustomizePatchAnalysisPort) -> None:
        self._port = analysis_port
        self._engine = KustomizePatchConflictEngine()

    def detect_conflicts(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        patches_raw = self._port.extract_patch_fields(command.overlay_path)
        base_raw = self._port.extract_base_fields(command.overlay_path)

        patches: list[dict[str, object]] = [dict(p) for p in patches_raw]
        base: list[dict[str, object]] = [dict(b) for b in base_raw]

        result = self._engine.compute(patches, base)
        return DetectKustomizePatchConflictsResponse(result=result)
