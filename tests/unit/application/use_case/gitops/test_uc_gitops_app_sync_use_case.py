from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.gitops_app_sync.command import (
    GitopsAppSyncCommand,
)
from hexawyn.application.use_case.gitops.gitops_app_sync.gitops_app_sync_use_case import (
    GitopsAppSyncUseCase,
)
from hexawyn.application.use_case.gitops.gitops_app_sync.response import (
    GitopsAppSyncResponse,
)


class TestGitopsAppSyncUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        app = MagicMock()
        app.name = "my-app"
        app.namespace = "default"
        app.sync_status = MagicMock()
        app.sync_status.value = "Synced"
        app.last_synced_at = "2025-01-15T10:00:00Z"
        app.revision = "main"
        app.message = None
        use_case = GitopsAppSyncUseCase(gitops_port=port)
        result = use_case.execute(GitopsAppSyncCommand(name="my-app", namespace="default"))
        assert isinstance(result, GitopsAppSyncResponse)
