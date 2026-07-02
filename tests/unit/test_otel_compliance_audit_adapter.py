from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter import (
    OTelComplianceAuditAdapter,
)
from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort
from hexawyn.domain.models.sensitive_data_audit import SensitiveAccessRequest


class TestOTelComplianceAuditAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelComplianceAuditAdapter(), ComplianceAuditPort)

    def test_fetch_returns_empty(self) -> None:
        r = OTelComplianceAuditAdapter().fetch_access_matches(SensitiveAccessRequest(pattern="/x"))
        assert r == []
