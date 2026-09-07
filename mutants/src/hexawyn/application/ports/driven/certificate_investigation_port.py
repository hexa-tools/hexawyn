from abc import ABC, abstractmethod

from hexawyn.domain.models.tls_certificate_diagnosis import TLSCertificateDiagnosticRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CertificateInvestigationPort(ABC):
    @abstractmethod
    def fetch_certificate_pem(self, request: TLSCertificateDiagnosticRequest) -> str | None: ...
    @abstractmethod
    def fetch_ingress_hostname(self, request: TLSCertificateDiagnosticRequest) -> str: ...
