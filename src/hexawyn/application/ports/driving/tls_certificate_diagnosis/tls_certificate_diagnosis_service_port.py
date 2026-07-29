from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.response import (
    TLSCertificateDiagnosisResponse,
)


class TLSCertificateDiagnosisServicePort(ABC):
    @abstractmethod
    def diagnose(
        self, command: TLSCertificateDiagnosisCommand
    ) -> TLSCertificateDiagnosisResponse: ...
