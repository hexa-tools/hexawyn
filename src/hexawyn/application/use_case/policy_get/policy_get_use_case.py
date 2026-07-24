from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.use_case.policy_get.command import PolicyGetCommand
from hexawyn.application.use_case.policy_get.response import PolicyGetResponse


class PolicyGetUseCase:
    def __init__(self, policy_port: PolicyPort) -> None:
        self._policy = policy_port

    def execute(self, command: PolicyGetCommand) -> PolicyGetResponse:
        p = self._policy.get_policy(name=command.name, namespace=command.namespace)
        return PolicyGetResponse(name=p.name, kind=p.kind, action=p.action, status=p.status)
