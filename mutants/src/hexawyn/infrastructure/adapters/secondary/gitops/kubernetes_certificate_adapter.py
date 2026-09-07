from __future__ import annotations

from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)
from hexawyn.domain.models.tls_certificate_diagnosis import TLSCertificateDiagnosticRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KubernetesCertificateAdapter(CertificateInvestigationPort):
    def fetch_certificate_pem(self, request: TLSCertificateDiagnosticRequest) -> str | None:
        return None

    def fetch_ingress_hostname(self, request: TLSCertificateDiagnosticRequest) -> str:
        return request.ingress_name
