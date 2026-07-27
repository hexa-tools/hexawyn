from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.governance.policy_get.command import (
    PolicyGetCommand,
)
from hexawyn.application.use_case.governance.policy_get.response import (
    PolicyGetResponse,
)


class PolicyGetUseCase:
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def execute(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,  # type: ignore
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,  # type: ignore
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )
