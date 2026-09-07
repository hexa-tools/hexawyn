from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.governance.policy_get.command import (
    PolicyGetCommand,
)
from hexawyn.application.use_case.governance.policy_get.policy_get_use_case import (
    PolicyGetUseCase,
)
from hexawyn.application.use_case.governance.policy_get.response import (
    PolicyGetResponse,
)


class TestPolicyGetUseCase:
    def test_execute_returns_response(self) -> None:
        policy = MagicMock()
        policy.name = "restrictive"
        policy.namespace = "default"
        policy.engine = MagicMock()
        policy.engine.value = "Kyverno"
        policy.kind = "ClusterPolicy"
        policy.action = MagicMock()
        policy.action.value = "Enforce"
        policy.description = "Restrictive security policy"
        policy.rules_count = 5
        policy.violations_count = 2
        policy.ready = True

        port = MagicMock()
        port.get_policy.return_value = policy

        use_case = PolicyGetUseCase(policy_port=port)
        result = use_case.execute(PolicyGetCommand(name="restrictive", namespace="default"))

        assert isinstance(result, PolicyGetResponse)
        assert result.name == "restrictive"
        assert result.ready is True
