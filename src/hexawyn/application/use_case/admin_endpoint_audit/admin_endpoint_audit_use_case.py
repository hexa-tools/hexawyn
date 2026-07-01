from __future__ import annotations

from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_command import (
    AdminEndpointAuditCommand,
)
from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_response import (
    AdminEndpointAuditResponse,
)
from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_service_port import (
    AdminEndpointAuditServicePort,
)


class AdminEndpointAuditUseCase:
    def __init__(self, service: AdminEndpointAuditServicePort) -> None:
        self._svc = service

    def execute(self, cmd: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        return self._svc.audit(cmd)
