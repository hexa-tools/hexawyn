from dataclasses import dataclass

from hexawyn.domain.models.tls_compliance import TLSComplianceReport


@dataclass
class AuditTlsComplianceResponse:
    result: TLSComplianceReport
