from dataclasses import asdict

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.policy_violations_list.command import PolicyViolationsListCommand
from hexawyn.application.use_case.policy_violations_list.response import (
    PolicyViolationsListResponse,
)


class PolicyViolationsListUseCase:
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def execute(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        violations = self._policy.list_violations(namespace=command.namespace)
        return PolicyViolationsListResponse(violations=[asdict(v) for v in violations])
