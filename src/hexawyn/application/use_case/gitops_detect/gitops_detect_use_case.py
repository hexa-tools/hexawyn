from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.use_case.gitops_detect.command import GitopsDetectCommand
from hexawyn.application.use_case.gitops_detect.response import GitopsDetectResponse


class GitopsDetectUseCase:
    def __init__(self, gitops_port: GitOpsPort) -> None:
        self._gitops = gitops_port

    def execute(self, command: GitopsDetectCommand) -> GitopsDetectResponse:
        r = self._gitops.detect_engine()
        return GitopsDetectResponse(
            engine=r.engine.value,
            version=r.version,
            namespace=r.namespace,
            apps_count=r.apps_count,
            out_of_sync_count=r.out_of_sync_count,
            failed_count=r.failed_count,
        )
