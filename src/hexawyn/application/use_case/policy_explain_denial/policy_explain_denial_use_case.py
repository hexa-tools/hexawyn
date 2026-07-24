from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.policy_explain_denial.command import PolicyExplainDenialCommand
from hexawyn.application.use_case.policy_explain_denial.response import PolicyExplainDenialResponse


class PolicyExplainDenialUseCase:
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def execute(self, command: PolicyExplainDenialCommand) -> PolicyExplainDenialResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyExplainDenialResponse(explanation=p.message or "No explanation available")
