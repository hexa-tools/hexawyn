from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.gitops_app_status.command import (
    GitopsAppStatusCommand,
)
from hexawyn.application.use_case.gitops.gitops_app_status.gitops_app_status_use_case import (  # noqa: E501
    GitopsAppStatusUseCase,
)
from hexawyn.application.use_case.gitops.gitops_app_status.response import (
    GitopsAppStatusResponse,
)


class TestGitopsAppStatusUseCase:
    def test_execute_returns_response(self) -> None:
        app = MagicMock()
        app.name = "my-app"
        app.namespace = "default"
        app.sync_status = MagicMock()
        app.sync_status.value = "Synced"
        app.health_status = MagicMock()
        app.health_status.value = "Healthy"
        app.last_synced_at = "2025-01-15T10:00:00Z"
        app.last_commit = "abc123"
        app.revision = "main"
        app.message = None

        port = MagicMock()
        port.get_app.return_value = app

        use_case = GitopsAppStatusUseCase(gitops_port=port)
        result = use_case.execute(GitopsAppStatusCommand(name="my-app", namespace="default"))

        assert isinstance(result, GitopsAppStatusResponse)
        assert result.sync_status == "Synced"
        assert result.health_status == "Healthy"

    def test_execute_health_degraded(self) -> None:
        app = MagicMock()
        app.name = "bad"
        app.namespace = "default"
        app.sync_status = MagicMock()
        app.sync_status.value = "OutOfSync"
        app.health_status = MagicMock()
        app.health_status.value = "Degraded"
        app.last_synced_at = None
        app.last_commit = ""
        app.revision = None
        app.message = "sync failed"

        port = MagicMock()
        port.get_app.return_value = app

        use_case = GitopsAppStatusUseCase(gitops_port=port)
        result = use_case.execute(GitopsAppStatusCommand(name="bad", namespace="default"))

        assert result.health_status == "Degraded"
