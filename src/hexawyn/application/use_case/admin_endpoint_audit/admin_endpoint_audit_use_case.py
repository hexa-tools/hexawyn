from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.application.use_case.admin_endpoint_audit.command import AdminEndpointAuditCommand
from hexawyn.application.use_case.admin_endpoint_audit.response import AdminEndpointAuditResponse


class AdminEndpointAuditUseCase:
    def __init__(self, port: SecurityAuditPort) -> None:
        self._port = port

    def execute(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        return AdminEndpointAuditResponse()
