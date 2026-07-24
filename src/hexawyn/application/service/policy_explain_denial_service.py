from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.policy_explain_denial.command import (
    PolicyExplainDenialCommand,
)
from hexawyn.application.use_case.policy_explain_denial.response import (
    PolicyExplainDenialResponse,
)
from hexawyn.application.ports.driving.policy_explain_denial.policy_explain_denial_service_port import (
    PolicyExplainDenialServicePort,
)


class PolicyExplainDenialService(PolicyExplainDenialServicePort):
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def explain(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        e = self._policy.explain_denial(
            resource_kind=command.resource_kind,
            resource_name=command.resource_name,
            namespace=command.namespace,
        )
        return PolicyExplainDenialResponse(
            policy_name=e.policy_name,
            rule_name=e.rule_name,
            raw_message=e.raw_message,
            human_explanation=e.human_explanation,
            fix_suggestion=e.fix_suggestion,
        )
