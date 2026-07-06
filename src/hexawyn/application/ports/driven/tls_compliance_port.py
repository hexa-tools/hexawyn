from abc import ABC, abstractmethod
from typing import TypedDict


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
