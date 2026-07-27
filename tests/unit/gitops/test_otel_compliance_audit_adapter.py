# Auto-generated test for otel_compliance_audit_adapter

from __future__ import annotations


class TestOtelComplianceAuditAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter import (
            OTelComplianceAuditAdapter,
        )
        from hexawyn.domain.models.sensitive_data_audit import SensitiveAccessRequest

        adapter = OTelComplianceAuditAdapter()
        result = adapter.fetch_access_matches(SensitiveAccessRequest(pattern="credit_card"))
        assert isinstance(result, list)
