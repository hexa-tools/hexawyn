from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.ports.driving.tls_certificate_diagnosis.tls_certificate_diagnosis_response import (
    TLSCertificateDiagnosisResponse,
)


class TLSCertificateDiagnosisServicePort(ABC):
    @abstractmethod
    def diagnose(
        self, command: TLSCertificateDiagnosisCommand
    ) -> TLSCertificateDiagnosisResponse: ...
