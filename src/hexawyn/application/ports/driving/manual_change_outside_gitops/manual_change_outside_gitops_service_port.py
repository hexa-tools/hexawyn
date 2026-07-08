from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_command import (
    ManualChangeOutsideGitOpsCommand,
)
from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_response import (
    ManualChangeOutsideGitOpsResponse,
)


class ManualChangeOutsideGitOpsServicePort(ABC):
    @abstractmethod
    def detect_manual_changes(
        self, command: ManualChangeOutsideGitOpsCommand
    ) -> ManualChangeOutsideGitOpsResponse: ...
