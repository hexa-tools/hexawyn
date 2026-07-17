"""Unit tests for DetectKustomizePatchConflictsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_service_port import (
    DetectKustomizePatchConflictsServicePort,
)
from hexawyn.application.use_case.detect_kustomize_patch_conflicts.detect_kustomize_patch_conflicts_use_case import (
    DetectKustomizePatchConflictsUseCase,
)


class TestDetectKustomizePatchConflictsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectKustomizePatchConflictsServicePort)
        use_case = DetectKustomizePatchConflictsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_conflicts.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectKustomizePatchConflictsServicePort)
        mock_service.detect_conflicts.side_effect = RuntimeError("test error")
        use_case = DetectKustomizePatchConflictsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
