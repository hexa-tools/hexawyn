from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.command import (
    TLSCertificateDiagnosisCommand,
)
from hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.response import (
    TLSCertificateDiagnosisResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class TLSCertificateDiagnosisServicePort(ABC):
    @abstractmethod
    def diagnose(
        self, command: TLSCertificateDiagnosisCommand
    ) -> TLSCertificateDiagnosisResponse: ...
