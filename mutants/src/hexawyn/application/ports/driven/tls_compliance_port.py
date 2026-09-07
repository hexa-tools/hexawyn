from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class TLSServiceRawData(TypedDict):
    service_name: str
    namespace: str
    tls_configured: bool
    cert_expiry_days: int
    cert_issuer: str
    is_self_signed: bool
    proxy_tls_termination: bool


class TLSCompliancePort(ABC):
    @abstractmethod
    def scan_services(self) -> list[TLSServiceRawData]: ...
