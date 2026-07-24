from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.audit_rbac_permissions.command import AuditRbacPermissionsCommand
from hexawyn.application.use_case.audit_rbac_permissions.response import (
    AuditRbacPermissionsResponse,
)


class AuditRbacPermissionsUseCase:
    def __init__(self, k8s_port: K8sPort) -> None:
        self._port = k8s_port

    def execute(self, command: AuditRbacPermissionsCommand) -> AuditRbacPermissionsResponse:
        return AuditRbacPermissionsResponse()
