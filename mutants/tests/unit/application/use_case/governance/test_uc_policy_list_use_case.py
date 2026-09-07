from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.governance.policy_list.command import (
    PolicyListCommand,
)
from hexawyn.application.use_case.governance.policy_list.policy_list_use_case import (
    PolicyListUseCase,
)
from hexawyn.application.use_case.governance.policy_list.response import (
    PolicyListResponse,
)


class TestPolicyListUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_policies.return_value = []
        use_case = PolicyListUseCase(policy_port=port)
        result = use_case.execute(PolicyListCommand())
        assert isinstance(result, PolicyListResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.list_policies.return_value = []
        use_case = PolicyListUseCase(policy_port=port)
        result = use_case.execute(PolicyListCommand())
        assert isinstance(result, PolicyListResponse)
