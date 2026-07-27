from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.gitops_apps_list.command import (
    GitopsAppsListCommand,
)
from hexawyn.application.use_case.gitops.gitops_apps_list.gitops_apps_list_use_case import (
    GitopsAppsListUseCase,
)
from hexawyn.application.use_case.gitops.gitops_apps_list.response import (
    GitopsAppsListResponse,
)


class TestGitopsAppsListUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_apps.return_value = []

        use_case = GitopsAppsListUseCase(gitops_port=port)
        result = use_case.execute(GitopsAppsListCommand())

        assert isinstance(result, GitopsAppsListResponse)

    def test_execute_empty_namespace(self) -> None:
        port = MagicMock()
        port.list_apps.return_value = []

        use_case = GitopsAppsListUseCase(gitops_port=port)
        result = use_case.execute(GitopsAppsListCommand(namespace="default"))

        assert len(result.apps) == 0
