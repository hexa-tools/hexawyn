from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    KustomizePatchAnalysisPort,
)
from hexawyn.application.use_case.detect_kustomize_patch_conflicts.command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.use_case.detect_kustomize_patch_conflicts.response import (
    DetectKustomizePatchConflictsResponse,
)


class DetectKustomizePatchConflictsUseCase:
    def __init__(self, analysis_port: KustomizePatchAnalysisPort) -> None:
        self._port = analysis_port

    def execute(
        self, command: DetectKustomizePatchConflictsCommand
    ) -> DetectKustomizePatchConflictsResponse:
        return DetectKustomizePatchConflictsResponse()
