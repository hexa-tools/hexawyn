# Auto-generated test for otel_security_audit_adapter

from __future__ import annotations


class TestOtelSecurityAuditAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_security_audit_adapter import (
            OTelSecurityAuditAdapter,
        )
        from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest

        adapter = OTelSecurityAuditAdapter()
        result = adapter.fetch_failed_admin_calls(AdminAuditRequest(time_window_minutes=30))
        assert isinstance(result, list)
