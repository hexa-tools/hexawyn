from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case import (  # noqa: E501
    AuditTLSComplianceUseCase,
)
from hexawyn.application.use_case.security.audit_tls_compliance.command import (
    AuditTlsComplianceCommand,
)
from hexawyn.application.use_case.security.audit_tls_compliance.response import (
    AuditTlsComplianceResponse,
)


class TestAuditTlsComplianceUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.scan_services.return_value = []

        use_case = AuditTLSComplianceUseCase(tls_port=port)
        result = use_case.execute(AuditTlsComplianceCommand())

        assert isinstance(result, AuditTlsComplianceResponse)

    def test_execute_with_services(self) -> None:
        port = MagicMock()
        port.scan_services.return_value = [
            {"name": "svc-a", "namespace": "default", "tls_enabled": False},
            {"name": "svc-b", "namespace": "default", "tls_enabled": True},
        ]

        use_case = AuditTLSComplianceUseCase(tls_port=port)
        result = use_case.execute(AuditTlsComplianceCommand())

        assert isinstance(result, AuditTlsComplianceResponse)
        assert result.result is not None
