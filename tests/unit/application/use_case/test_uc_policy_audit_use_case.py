"""Unit tests for PolicyAuditUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.policy_audit.policy_audit_service_port import (
    PolicyAuditServicePort,
)
from hexawyn.application.use_case.policy_audit.policy_audit_use_case import PolicyAuditUseCase


class TestPolicyAuditUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PolicyAuditServicePort)
        use_case = PolicyAuditUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.audit.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PolicyAuditServicePort)
        mock_service.audit.side_effect = RuntimeError("test error")
        use_case = PolicyAuditUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
