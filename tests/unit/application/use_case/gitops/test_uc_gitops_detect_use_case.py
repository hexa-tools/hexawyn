from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.gitops_detect.command import (
    GitopsDetectCommand,
)
from hexawyn.application.use_case.gitops.gitops_detect.gitops_detect_use_case import (
    GitopsDetectUseCase,
)
from hexawyn.application.use_case.gitops.gitops_detect.response import (
    GitopsDetectResponse,
)


class TestGitopsDetectUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.detect_engine.return_value = MagicMock()
        use_case = GitopsDetectUseCase(gitops_port=port)
        result = use_case.execute(GitopsDetectCommand())
        assert isinstance(result, GitopsDetectResponse)
