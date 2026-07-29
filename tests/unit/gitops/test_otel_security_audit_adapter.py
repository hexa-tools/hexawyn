from __future__ import annotations

from unittest.mock import patch


class TestOtelSecurityAuditAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_security_audit_adapter import (
            OTelSecurityAuditAdapter,
        )
        from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest

        adapter = OTelSecurityAuditAdapter()
        result = adapter.fetch_failed_admin_calls(AdminAuditRequest(time_window_minutes=30))
        assert isinstance(result, list)

    def test_empty_time_window_returns_empty_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_security_audit_adapter import (
            OTelSecurityAuditAdapter,
        )
        from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest

        adapter = OTelSecurityAuditAdapter()
        result = adapter.fetch_failed_admin_calls(AdminAuditRequest(time_window_minutes=0))
        assert result == []

    def test_error_traces_populate_failed_calls(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_security_audit_adapter import (
            OTelSecurityAuditAdapter,
        )
        from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest

        mock_traces = [
            {"traceID": "err-trace-1111111122222222", "hasErrors": True},
            {"traceID": "clean-trace", "hasErrors": False},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_security_audit_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelSecurityAuditAdapter()
            result = adapter.fetch_failed_admin_calls(AdminAuditRequest(time_window_minutes=30))
            assert len(result) == 1
            assert result[0].endpoint == "trace:err-trac"
