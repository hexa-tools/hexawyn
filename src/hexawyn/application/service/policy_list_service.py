from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.ports.driving.policy_list.policy_list_command import (
    PolicyListCommand,
)
from hexawyn.application.ports.driving.policy_list.policy_list_response import (
    PolicyListResponse,
)
from hexawyn.application.ports.driving.policy_list.policy_list_service_port import (
    PolicyListServicePort,
)


class PolicyListService(PolicyListServicePort):
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def list_policies(self, command: PolicyListCommand) -> PolicyListResponse:
        policies = self._policy.list_policies(namespace=command.namespace)
        return PolicyListResponse(policies=[asdict(p) for p in policies])
