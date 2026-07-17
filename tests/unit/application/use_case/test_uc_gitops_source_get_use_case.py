"""Unit tests for GitOpsSourceGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.gitops_source_get.gitops_source_get_service_port import (
    GitOpsSourceGetServicePort,
)
from hexawyn.application.use_case.gitops_source_get.gitops_source_get_use_case import (
    GitOpsSourceGetUseCase,
)


class TestGitOpsSourceGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GitOpsSourceGetServicePort)
        use_case = GitOpsSourceGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_source.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GitOpsSourceGetServicePort)
        mock_service.get_source.side_effect = RuntimeError("test error")
        use_case = GitOpsSourceGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
