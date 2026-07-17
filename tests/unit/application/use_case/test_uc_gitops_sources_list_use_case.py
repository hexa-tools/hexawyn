"""Unit tests for GitOpsSourcesListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.gitops_sources_list.gitops_sources_list_service_port import (
    GitOpsSourcesListServicePort,
)
from hexawyn.application.use_case.gitops_sources_list.gitops_sources_list_use_case import (
    GitOpsSourcesListUseCase,
)


class TestGitOpsSourcesListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GitOpsSourcesListServicePort)
        use_case = GitOpsSourcesListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_sources.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GitOpsSourcesListServicePort)
        mock_service.list_sources.side_effect = RuntimeError("test error")
        use_case = GitOpsSourcesListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
