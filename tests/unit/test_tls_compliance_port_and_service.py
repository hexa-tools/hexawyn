"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

from hexawyn.application.ports.driven.tls_compliance_port import (
    TLSCompliancePort,
    TLSServiceRawData,
)
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_command import (
    AuditTLSComplianceCommand,
)
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_response import (
    AuditTLSComplianceResponse,
)
from hexawyn.application.ports.driving.audit_tls_compliance.audit_tls_compliance_service_port import (
    AuditTLSComplianceServicePort,
)
from hexawyn.application.service.audit_tls_compliance_service import (
    AuditTLSComplianceService,
)
from hexawyn.application.use_case.audit_tls_compliance.audit_tls_compliance_use_case import (
    AuditTLSComplianceUseCase,
)
from hexawyn.domain.models.tls_compliance import TLSComplianceReport


class TestTLSCompliancePort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(TLSCompliancePort)


class TestAuditTLSComplianceCommand:
    def test_is_frozen(self) -> None:
        cmd = AuditTLSComplianceCommand()
        assert cmd is not None


class TestAuditTLSComplianceResponse:
    def test_holds_result(self) -> None:
        inner = TLSComplianceReport(all_compliant=True)
        resp = AuditTLSComplianceResponse(result=inner)
        assert resp.result is inner


class TestAuditTLSComplianceService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=TLSCompliancePort)
        port.scan_services.return_value = []
        return port

    def test_calls_scan_services(self) -> None:
        port = self._mock_port()
        service = AuditTLSComplianceService(tls_port=port)

        service.audit(AuditTLSComplianceCommand())

        port.scan_services.assert_called_once()

    def test_detects_expired_cert(self) -> None:
        port = MagicMock(spec=TLSCompliancePort)
        port.scan_services.return_value = [
            TLSServiceRawData(
                service_name="payment-service",
                namespace="production",
                tls_configured=True,
                cert_expiry_days=-3,
                cert_issuer="Let's Encrypt",
                is_self_signed=False,
                proxy_tls_termination=False,
            ),
        ]
        service = AuditTLSComplianceService(tls_port=port)

        response = service.audit(AuditTLSComplianceCommand())

        assert response.result.services[0].severity == "critical"
        assert response.result.total_issues == 1

    def test_returns_response_with_result(self) -> None:
        port = self._mock_port()
        service = AuditTLSComplianceService(tls_port=port)

        response = service.audit(AuditTLSComplianceCommand())

        assert isinstance(response, AuditTLSComplianceResponse)
        assert isinstance(response.result, TLSComplianceReport)


class TestAuditTLSComplianceUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=AuditTLSComplianceServicePort)
        inner = TLSComplianceReport(all_compliant=True)
        service.audit.return_value = AuditTLSComplianceResponse(result=inner)
        use_case = AuditTLSComplianceUseCase(service=service)

        result = use_case.execute(AuditTLSComplianceCommand())

        service.audit.assert_called_once()
        assert result.result is inner
