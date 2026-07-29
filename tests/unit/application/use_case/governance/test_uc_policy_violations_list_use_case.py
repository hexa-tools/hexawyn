from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.governance.policy_violations_list.command import (
    PolicyViolationsListCommand,
)
from hexawyn.application.use_case.governance.policy_violations_list.policy_violations_list_use_case import (  # noqa: E501
    PolicyViolationsListUseCase,
)
from hexawyn.application.use_case.governance.policy_violations_list.response import (
    PolicyViolationsListResponse,
)


class TestPolicyViolationsListUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_violations.return_value = []
        use_case = PolicyViolationsListUseCase(policy_port=port)
        result = use_case.execute(PolicyViolationsListCommand())
        assert isinstance(result, PolicyViolationsListResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.list_violations.return_value = []
        use_case = PolicyViolationsListUseCase(policy_port=port)
        result = use_case.execute(PolicyViolationsListCommand())
        assert isinstance(result, PolicyViolationsListResponse)
