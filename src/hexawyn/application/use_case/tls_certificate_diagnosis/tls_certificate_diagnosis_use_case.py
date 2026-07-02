from __future__ import annotations

from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_response import (
    TLSCertificateDiagnosisResponse,
)
from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_service_port import (
    TLSCertificateDiagnosisServicePort,
)


class TLSCertificateDiagnosisUseCase:
    def __init__(self, service: TLSCertificateDiagnosisServicePort) -> None:
        self._svc = service

    def execute(self, cmd: TLSCertificateDiagnosisCommand) -> TLSCertificateDiagnosisResponse:
        return self._svc.diagnose(cmd)
