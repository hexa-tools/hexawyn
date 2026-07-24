from __future__ import annotations

from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)
from hexawyn.application.use_case.tls_certificate_diagnosis.command import (
    TlsCertificateDiagnosisCommand,
)
from hexawyn.application.use_case.tls_certificate_diagnosis.response import (
    TlsCertificateDiagnosisResponse,
)
from hexawyn.domain.models.tls_certificate_diagnosis import (
    CertificateDiagnosis,
    TLSCertificateDiagnosticRequest,
)


class TLSCertificateDiagnosisUseCase:
    def __init__(self, port: CertificateInvestigationPort) -> None:
        self._port = port

    def execute(self, command: TlsCertificateDiagnosisCommand) -> TlsCertificateDiagnosisResponse:
        request = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        cert_pem = self._port.fetch_certificate_pem(request)
        hostname = self._port.fetch_ingress_hostname(request)
        diagnosis = CertificateDiagnosis.compute(request, cert_pem, hostname)

        return TlsCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=diagnosis.status.value if diagnosis.status else "unknown",
            diagnosis=diagnosis.diagnosis,
            expiry_date=diagnosis.expiry_date,
            days_remaining=diagnosis.days_remaining,
            cipher_info=diagnosis.cipher_info,
            san_list=diagnosis.san_list,
        )
