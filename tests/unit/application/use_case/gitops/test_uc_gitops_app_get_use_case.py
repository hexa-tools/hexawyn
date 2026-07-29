from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.gitops_app_get.command import (
    GitopsAppGetCommand,
)
from hexawyn.application.use_case.gitops.gitops_app_get.gitops_app_get_use_case import (
    GitopsAppGetUseCase,
)
from hexawyn.application.use_case.gitops.gitops_app_get.response import (
    GitopsAppGetResponse,
)


class TestGitopsAppGetUseCase:
    def test_execute_returns_response(self) -> None:
        app = MagicMock()
        app.name = "my-app"
        app.namespace = "default"
        app.engine = MagicMock()
        app.engine.value = "ArgoCD"
        app.kind = "Application"
        app.sync_status = MagicMock()
        app.sync_status.value = "Synced"
        app.health_status = MagicMock()
        app.health_status.value = "Healthy"
        app.last_synced_at = "2025-01-15T10:00:00Z"
        app.last_commit = "abc123"
        app.source_url = "https://github.com/org/repo"
        app.revision = "main"
        app.message = None

        port = MagicMock()
        port.get_app.return_value = app

        use_case = GitopsAppGetUseCase(gitops_port=port)
        result = use_case.execute(GitopsAppGetCommand(name="my-app", namespace="default"))

        assert isinstance(result, GitopsAppGetResponse)
        assert result.name == "my-app"
        assert result.sync_status == "Synced"

    def test_execute_with_empty_message(self) -> None:
        app = MagicMock()
        app.name = "app"
        app.namespace = "ns"
        app.engine = MagicMock()
        app.engine.value = "ArgoCD"
        app.kind = "Application"
        app.sync_status = MagicMock()
        app.sync_status.value = "OutOfSync"
        app.health_status = MagicMock()
        app.health_status.value = "Degraded"
        app.last_synced_at = None
        app.last_commit = ""
        app.source_url = ""
        app.revision = None
        app.message = None

        port = MagicMock()
        port.get_app.return_value = app

        use_case = GitopsAppGetUseCase(gitops_port=port)
        result = use_case.execute(GitopsAppGetCommand(name="failing-app", namespace="production"))

        assert result.health_status == "Degraded"
