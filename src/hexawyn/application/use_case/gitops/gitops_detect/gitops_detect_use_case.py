from __future__ import annotations

from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops.gitops_detect.command import GitopsDetectCommand
from hexawyn.application.use_case.gitops.gitops_detect.response import GitopsDetectResponse


class GitopsDetectUseCase:
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def execute(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        result = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=result.engine.value,
            version=result.version,  # type: ignore
            namespace=result.namespace,  # type: ignore
            apps_count=result.apps_count,
            out_of_sync_count=result.out_of_sync_count,
            failed_count=result.failed_count,
        )
