from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_audit.command import (
    PolicyAuditCommand,
)
from hexawyn.application.use_case.governance.policy_audit.response import (
    PolicyAuditResponse,
)


class PolicyAuditUseCase:
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def execute(self, command: PolicyAuditCommand) -> PolicyAuditResponse:
        results = self._policy.audit(namespace=command.namespace)
        return PolicyAuditResponse(results=results)
