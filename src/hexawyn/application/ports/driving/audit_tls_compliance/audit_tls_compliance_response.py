from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.tls_compliance import TLSComplianceReport


@dataclass
class AuditTLSComplianceResponse:
    result: TLSComplianceReport
