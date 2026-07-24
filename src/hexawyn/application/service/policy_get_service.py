from __future__ import annotations

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.policy_get.command import (
    PolicyGetCommand,
)
from hexawyn.application.use_case.policy_get.response import (
    PolicyGetResponse,
)
from hexawyn.application.ports.driving.policy_get.policy_get_service_port import (
    PolicyGetServicePort,
)


class PolicyGetService(PolicyGetServicePort):
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def get_policy(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(
            name=p.name,
            namespace=p.namespace,
            engine=p.engine.value,
            kind=p.kind,
            action=p.action.value,
            description=p.description,
            rules_count=p.rules_count,
            violations_count=p.violations_count,
            ready=p.ready,
        )
