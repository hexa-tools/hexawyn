"""Unit tests for GitOpsAppSyncUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.gitops_app_sync.gitops_app_sync_service_port import (
    GitOpsAppSyncServicePort,
)
from hexawyn.application.use_case.gitops_app_sync.gitops_app_sync_use_case import (
    GitOpsAppSyncUseCase,
)


class TestGitOpsAppSyncUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GitOpsAppSyncServicePort)
        use_case = GitOpsAppSyncUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_sync_status.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GitOpsAppSyncServicePort)
        mock_service.get_sync_status.side_effect = RuntimeError("test error")
        use_case = GitOpsAppSyncUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
