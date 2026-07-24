from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.manual_change_outside_gitops.command import (
    ManualChangeOutsideGitopsCommand,
)
from hexawyn.application.use_case.manual_change_outside_gitops.response import (
    ManualChangeOutsideGitopsResponse,
)


class ManualChangeOutsideGitopsUseCase:
    def __init__(self, port: GitOpsPort) -> None:
        self._port = port

    def execute(
        self, command: ManualChangeOutsideGitopsCommand
    ) -> ManualChangeOutsideGitopsResponse:
        return ManualChangeOutsideGitopsResponse()
