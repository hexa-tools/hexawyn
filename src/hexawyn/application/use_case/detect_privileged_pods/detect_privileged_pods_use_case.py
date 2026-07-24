from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    PodSecurityContextAuditPort,
)
from hexawyn.application.use_case.detect_privileged_pods.command import DetectPrivilegedPodsCommand
from hexawyn.application.use_case.detect_privileged_pods.response import (
    DetectPrivilegedPodsResponse,
)


class DetectPrivilegedPodsUseCase:
    def __init__(self, port: PodSecurityContextAuditPort) -> None:
        self._port = port

    def execute(self, command: DetectPrivilegedPodsCommand) -> DetectPrivilegedPodsResponse:
        return DetectPrivilegedPodsResponse()
