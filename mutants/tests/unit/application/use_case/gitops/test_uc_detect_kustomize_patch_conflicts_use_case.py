from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.command import (
    DetectKustomizePatchConflictsCommand,
)
from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_use_case import (  # noqa: E501
    DetectKustomizePatchConflictsUseCase,
)
from hexawyn.application.use_case.gitops.detect_kustomize_patch_conflicts.response import (  # noqa: E501
    DetectKustomizePatchConflictsResponse,
)


class TestDetectKustomizePatchConflictsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.extract_patch_fields.return_value = []
        port.extract_base_fields.return_value = []

        use_case = DetectKustomizePatchConflictsUseCase(analysis_port=port)
        use_case._engine.compute = MagicMock(
            return_value={
                "total_conflicts": 0,
                "patch_conflicts": [],
            }
        )

        result = use_case.detect_conflicts(
            DetectKustomizePatchConflictsCommand(overlay_path="/path")
        )

        assert isinstance(result, DetectKustomizePatchConflictsResponse)

    def test_execute_no_conflicts(self) -> None:
        port = MagicMock()
        port.extract_patch_fields.return_value = []
        port.extract_base_fields.return_value = []

        use_case = DetectKustomizePatchConflictsUseCase(analysis_port=port)
        use_case._engine.compute = MagicMock(
            return_value={
                "total_conflicts": 0,
            }
        )

        result = use_case.detect_conflicts(
            DetectKustomizePatchConflictsCommand(overlay_path="/path")
        )

        assert result.result["total_conflicts"] == 0
