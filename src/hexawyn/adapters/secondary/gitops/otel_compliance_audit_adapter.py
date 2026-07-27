from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.compliance_audit_port import (  # type: ignore
    AccessMatch,
    ComplianceAuditPort,
)
from hexawyn.domain.models.sensitive_data_audit import SensitiveAccessRequest


class OTelComplianceAuditAdapter(ComplianceAuditPort):
    def fetch_access_matches(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(  # type: ignore
                        trace_id=trace["traceID"],
                        service="unknown",
                        pattern_matched=request.pattern,
                        span_count=trace.get("spanCount", 0),
                    )
                )
        return result
