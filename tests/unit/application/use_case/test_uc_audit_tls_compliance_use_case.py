"""Unit tests for AuditTLSComplianceUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_service_port import (
    AuditTLSComplianceServicePort,
)
from hexawyn.application.use_case.audit_tls_compliance.audit_tls_compliance_use_case import (
    AuditTLSComplianceUseCase,
)


class TestAuditTLSComplianceUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AuditTLSComplianceServicePort)
        use_case = AuditTLSComplianceUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.audit.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AuditTLSComplianceServicePort)
        mock_service.audit.side_effect = RuntimeError("test error")
        use_case = AuditTLSComplianceUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
