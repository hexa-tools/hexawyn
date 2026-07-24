from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.policy_violations_list.command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.use_case.policy_violations_list.response import (
    PolicyViolationsListResponse,
)
from hexawyn.application.ports.driving.policy_violations_list.policy_violations_list_service_port import (
    PolicyViolationsListServicePort,
)


class PolicyViolationsListService(PolicyViolationsListServicePort):
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def list_violations(self, command: PolicyViolationsListCommand) -> PolicyViolationsListResponse:
        violations = self._policy.list_violations(namespace=command.namespace)
        return PolicyViolationsListResponse(violations=[asdict(v) for v in violations])
