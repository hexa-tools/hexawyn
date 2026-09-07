from __future__ import annotations

from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest
from hexawyn.infrastructure.adapters.secondary.gitops.otel_security_audit_adapter import (
    OTelSecurityAuditAdapter,
)


class TestOTelSecurityAuditAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelSecurityAuditAdapter(), SecurityAuditPort)

    def test_fetch_returns_empty(self) -> None:
        r = OTelSecurityAuditAdapter().fetch_failed_admin_calls(AdminAuditRequest())
        assert r == []

    def test_fetch_total_returns_zero(self) -> None:
        r = OTelSecurityAuditAdapter().fetch_total_requests(AdminAuditRequest())
        assert r == 0
