from __future__ import annotations

from hexawyn.application.ports.driving.policy_explain_denial.policy_explain_denial_command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.ports.driving.policy_explain_denial.policy_explain_denial_response import (
    PolicyExplainDenialResponse,
)
from hexawyn.application.ports.driving.policy_explain_denial.policy_explain_denial_service_port import (
    PolicyExplainDenialServicePort,
)


class PolicyExplainDenialUseCase:
    def __init__(self, service: PolicyExplainDenialServicePort) -> None:
        self._service = service

    def execute(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        return self._service.explain(command)
