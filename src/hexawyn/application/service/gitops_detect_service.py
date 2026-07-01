from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_command import (
    GitOpsDetectCommand,
)
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_response import (
    GitOpsDetectResponse,
)
from hexawyn.application.ports.driving.gitops_detect.gitops_detect_service_port import (
    GitOpsDetectServicePort,
)


class GitOpsDetectService(GitOpsDetectServicePort):
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def detect(self, command: GitOpsDetectCommand) -> GitOpsDetectResponse:
        result = self._gitops.detect_engine()
        return GitOpsDetectResponse(
            engine=result.engine.value,
            version=result.version,
            namespace=result.namespace,
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )
