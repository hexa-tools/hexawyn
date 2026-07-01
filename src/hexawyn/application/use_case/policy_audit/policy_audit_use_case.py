from __future__ import annotations

from hexawyn.application.ports.driving.policy_audit.policy_audit_command import (
    PolicyAuditCommand,
)
from hexawyn.application.ports.driving.policy_audit.policy_audit_response import (
    PolicyAuditResponse,
)
from hexawyn.application.ports.driving.policy_audit.policy_audit_service_port import (
    PolicyAuditServicePort,
)


class PolicyAuditUseCase:
    def __init__(self, service: PolicyAuditServicePort) -> None:
        self._service = service

    def execute(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        return self._service.audit(command)
