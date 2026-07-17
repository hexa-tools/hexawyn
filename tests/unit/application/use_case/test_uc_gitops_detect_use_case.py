"""Unit tests for GitOpsDetectUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_service_port import (
    GitOpsDetectServicePort,
)
from hexawyn.application.use_case.gitops_detect.gitops_detect_use_case import GitOpsDetectUseCase


class TestGitOpsDetectUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GitOpsDetectServicePort)
        use_case = GitOpsDetectUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GitOpsDetectServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = GitOpsDetectUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
