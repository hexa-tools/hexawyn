from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.compliance_audit_port import (
    ComplianceAuditPort,
)
from hexawyn.domain.models.sensitive_data_audit import AccessMatch, SensitiveAccessRequest


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
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
