"""Unit tests for GitOpsAppsListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.gitops_apps_list.gitops_apps_list_service_port import (
    GitOpsAppsListServicePort,
)
from hexawyn.application.use_case.gitops_apps_list.gitops_apps_list_use_case import (
    GitOpsAppsListUseCase,
)


class TestGitOpsAppsListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GitOpsAppsListServicePort)
        use_case = GitOpsAppsListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_apps.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GitOpsAppsListServicePort)
        mock_service.list_apps.side_effect = RuntimeError("test error")
        use_case = GitOpsAppsListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
