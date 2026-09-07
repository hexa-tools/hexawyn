from __future__ import annotations

from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)
from hexawyn.domain.models.tls_certificate_diagnosis import TLSCertificateDiagnosticRequest


class KubernetesCertificateAdapter(CertificateInvestigationPort):
    def fetch_certificate_pem(self, request: TLSCertificateDiagnosticRequest) -> str | None:
        return None

    def fetch_ingress_hostname(self, request: TLSCertificateDiagnosticRequest) -> str:
        return request.ingress_name
