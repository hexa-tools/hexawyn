from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.gitops_source_get.command import (
    GitopsSourceGetCommand,
)
from hexawyn.application.use_case.gitops.gitops_source_get.gitops_source_get_use_case import (
    GitopsSourceGetUseCase,
)
from hexawyn.application.use_case.gitops.gitops_source_get.response import (
    GitopsSourceGetResponse,
)


class TestGitopsSourceGetUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        src = MagicMock()
        src.name = "repo"
        src.namespace = "default"
        src.kind = "GitRepository"
        src.url = "https://github.com/org/repo"
        src.ready = True
        src.last_updated_at = "2025-01-15"
        src.message = None
        use_case = GitopsSourceGetUseCase(gitops_port=port)
        result = use_case.execute(GitopsSourceGetCommand(name="repo", namespace="default"))
        assert isinstance(result, GitopsSourceGetResponse)
