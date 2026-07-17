"""Unit tests for GitOpsAppStatusUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.gitops_app_status.gitops_app_status_service_port import (
    GitOpsAppStatusServicePort,
)
from hexawyn.application.use_case.gitops_app_status.gitops_app_status_use_case import (
    GitOpsAppStatusUseCase,
)


class TestGitOpsAppStatusUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GitOpsAppStatusServicePort)
        use_case = GitOpsAppStatusUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_status.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GitOpsAppStatusServicePort)
        mock_service.get_status.side_effect = RuntimeError("test error")
        use_case = GitOpsAppStatusUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
