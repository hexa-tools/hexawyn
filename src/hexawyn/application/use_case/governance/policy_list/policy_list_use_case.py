from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_list.command import (
    PolicyListCommand,
)
from hexawyn.application.use_case.governance.policy_list.response import (
    PolicyListResponse,
)


class PolicyListUseCase:
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def execute(self, command: PolicyListCommand) -> PolicyListResponse:
        policies = self._policy.list_policies(namespace=command.namespace)
        return PolicyListResponse(policies=[asdict(p) for p in policies])
