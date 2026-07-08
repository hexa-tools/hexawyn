from __future__ import annotations

from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)
from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_response import (
    TLSCertificateDiagnosisResponse,
)
from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_service_port import (
    TLSCertificateDiagnosisServicePort,
)
from hexawyn.domain.models.tls_certificate_diagnosis import (
    CertificateDiagnosis,
    TLSCertificateDiagnosticRequest,
)


class TLSCertificateDiagnosisService(TLSCertificateDiagnosisServicePort):
    def __init__(self, port: CertificateInvestigationPort) -> None:
        self._port = port

    def diagnose(self, command: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        req = TLSCertificateDiagnosticRequest(
            ingress_name=command.ingress_name, namespace=command.namespace
        )
        pem = self._port.fetch_certificate_pem(req)
        hostname = self._port.fetch_ingress_hostname(req)
        r = CertificateDiagnosis.compute(request=req, cert_pem=pem, hostname=hostname)
        return TLSCertificateDiagnosisResponse(
            ingress_name=command.ingress_name,
            namespace=command.namespace,
            status=r.status.value,
            diagnosis=r.diagnosis,
            expiry_date=r.expiry_date,
            days_remaining=r.days_remaining,
            cipher_info=r.cipher_info,
            san_list=r.san_list,
        )
