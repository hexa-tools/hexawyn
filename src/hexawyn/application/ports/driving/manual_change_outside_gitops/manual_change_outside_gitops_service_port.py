# mypy: ignore-errors
from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.gitops.manual_change_outside_gitops.command import (  # noqa: E501  # type: ignore
    ManualChangeOutsideGitOpsCommand,
)
from hexawyn.application.use_case.gitops.manual_change_outside_gitops.response import (  # noqa: E501  # type: ignore
    ManualChangeOutsideGitOpsResponse,
)


class ManualChangeOutsideGitOpsServicePort(ABC):
    @abstractmethod
    def detect_manual_changes(
        self, command: ManualChangeOutsideGitOpsCommand
    ) -> ManualChangeOutsideGitOpsResponse: ...
