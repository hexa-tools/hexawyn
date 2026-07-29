from __future__ import annotations

from unittest.mock import patch


class TestOtelComplianceAuditAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter import (
            OTelComplianceAuditAdapter,
        )
        from hexawyn.domain.models.sensitive_data_audit import SensitiveAccessRequest

        adapter = OTelComplianceAuditAdapter()
        result = adapter.fetch_access_matches(SensitiveAccessRequest(pattern="credit_card"))
        assert isinstance(result, list)

    def test_empty_pattern_returns_empty_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter import (
            OTelComplianceAuditAdapter,
        )
        from hexawyn.domain.models.sensitive_data_audit import SensitiveAccessRequest

        adapter = OTelComplianceAuditAdapter()
        result = adapter.fetch_access_matches(SensitiveAccessRequest(pattern=""))
        assert result == []

    def test_error_traces_produce_matches(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter import (
            OTelComplianceAuditAdapter,
        )
        from hexawyn.domain.models.sensitive_data_audit import SensitiveAccessRequest

        mock_traces = [
            {"traceID": "trace-err-001", "hasErrors": True, "spanCount": 3},
            {"traceID": "trace-ok-001", "hasErrors": False, "spanCount": 1},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelComplianceAuditAdapter()
            result = adapter.fetch_access_matches(SensitiveAccessRequest(pattern="pii"))
            assert len(result) == 1
            assert result[0].caller_service == "unknown"
