"""Unit tests for SensitiveDataAuditUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.sensitive_data_audit.sensitive_data_audit_service_port import (
    SensitiveDataAuditServicePort,
)
from hexawyn.application.use_case.sensitive_data_audit.sensitive_data_audit_use_case import (
    SensitiveDataAuditUseCase,
)


class TestSensitiveDataAuditUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=SensitiveDataAuditServicePort)
        use_case = SensitiveDataAuditUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.audit.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=SensitiveDataAuditServicePort)
        mock_service.audit.side_effect = RuntimeError("test error")
        use_case = SensitiveDataAuditUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
