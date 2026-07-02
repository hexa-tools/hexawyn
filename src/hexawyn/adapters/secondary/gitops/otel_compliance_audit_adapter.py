from __future__ import annotations

from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort
from hexawyn.domain.models.sensitive_data_audit import AccessMatch, SensitiveAccessRequest


class OTelComplianceAuditAdapter(ComplianceAuditPort):
    def fetch_access_matches(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        return []
