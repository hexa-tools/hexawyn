from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.ports.driving.policy_audit.policy_audit_command import (
    PolicyAuditCommand,
)
from hexawyn.application.ports.driving.policy_audit.policy_audit_response import (
    PolicyAuditResponse,
)
from hexawyn.application.ports.driving.policy_audit.policy_audit_service_port import (
    PolicyAuditServicePort,
)


class PolicyAuditService(PolicyAuditServicePort):
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def audit(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        results = self._policy.audit(namespace=command.namespace)
        return PolicyAuditResponse(results=results)
