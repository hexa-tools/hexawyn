from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_command import (
    ManualChangeOutsideGitOpsCommand,
)
from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_response import (
    ManualChangeOutsideGitOpsResponse,
)
from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_service_port import (
    ManualChangeOutsideGitOpsServicePort,
)
from hexawyn.application.use_case.manual_change_outside_gitops.manual_change_outside_gitops_use_case import (
    ManualChangeOutsideGitOpsUseCase,
)


class TestManualChangeOutsideGitOpsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=ManualChangeOutsideGitOpsServicePort)
        expected = ManualChangeOutsideGitOpsResponse()
        service.detect_manual_changes.return_value = expected
        use_case = ManualChangeOutsideGitOpsUseCase(service=service)
        command = ManualChangeOutsideGitOpsCommand(namespace="production")

        result = use_case.execute(command)

        service.detect_manual_changes.assert_called_once_with(command)
        assert result is expected
