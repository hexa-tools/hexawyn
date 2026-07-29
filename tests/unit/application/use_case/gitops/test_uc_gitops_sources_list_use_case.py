from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.gitops_sources_list.command import (
    GitopsSourcesListCommand,
)
from hexawyn.application.use_case.gitops.gitops_sources_list.gitops_sources_list_use_case import (
    GitopsSourcesListUseCase,
)
from hexawyn.application.use_case.gitops.gitops_sources_list.response import (
    GitopsSourcesListResponse,
)


class TestGitopsSourcesListUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_sources.return_value = []
        use_case = GitopsSourcesListUseCase(gitops_port=port)
        result = use_case.execute(GitopsSourcesListCommand())
        assert isinstance(result, GitopsSourcesListResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.list_sources.return_value = []
        use_case = GitopsSourcesListUseCase(gitops_port=port)
        result = use_case.execute(GitopsSourcesListCommand())
        assert isinstance(result, GitopsSourcesListResponse)
