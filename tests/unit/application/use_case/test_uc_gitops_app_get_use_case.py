"""Unit tests for GitOpsAppGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.gitops_app_get.gitops_app_get_service_port import (
    GitOpsAppGetServicePort,
)
from hexawyn.application.use_case.gitops_app_get.gitops_app_get_use_case import GitOpsAppGetUseCase


class TestGitOpsAppGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GitOpsAppGetServicePort)
        use_case = GitOpsAppGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_app.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GitOpsAppGetServicePort)
        mock_service.get_app.side_effect = RuntimeError("test error")
        use_case = GitOpsAppGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
