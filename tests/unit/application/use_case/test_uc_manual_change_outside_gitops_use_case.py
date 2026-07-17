"""Unit tests for ManualChangeOutsideGitOpsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_service_port import (
    ManualChangeOutsideGitOpsServicePort,
)
from hexawyn.application.use_case.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (
    ManualChangeOutsideGitOpsUseCase,
)


class TestManualChangeOutsideGitOpsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ManualChangeOutsideGitOpsServicePort)
        use_case = ManualChangeOutsideGitOpsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_manual_changes.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ManualChangeOutsideGitOpsServicePort)
        mock_service.detect_manual_changes.side_effect = RuntimeError("test error")
        use_case = ManualChangeOutsideGitOpsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
