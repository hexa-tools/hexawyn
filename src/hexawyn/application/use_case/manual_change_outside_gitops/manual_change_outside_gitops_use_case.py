from __future__ import annotations

from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_command import (
    ManualChangeOutsideGitOpsCommand,
)
from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_response import (
    ManualChangeOutsideGitOpsResponse,
)
from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_service_port import (
    ManualChangeOutsideGitOpsServicePort,
)


class ManualChangeOutsideGitOpsUseCase:
    def __init__(self, service: ManualChangeOutsideGitOpsServicePort) -> None:
        self._svc = service

    def execute(
        self, command: ManualChangeOutsideGitOpsCommand
    ) -> ManualChangeOutsideGitOpsResponse:
        return self._svc.detect_manual_changes(command)
