from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.governance.policy_audit.command import (
    PolicyAuditCommand,
)
from hexawyn.application.use_case.governance.policy_audit.policy_audit_use_case import (
    PolicyAuditUseCase,
)
from hexawyn.application.use_case.governance.policy_audit.response import (
    PolicyAuditResponse,
)


class TestPolicyAuditUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.audit.return_value = []
        use_case = PolicyAuditUseCase(policy_port=port)
        result = use_case.execute(PolicyAuditCommand())
        assert isinstance(result, PolicyAuditResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.audit.return_value = []
        use_case = PolicyAuditUseCase(policy_port=port)
        result = use_case.execute(PolicyAuditCommand())
        assert isinstance(result, PolicyAuditResponse)
