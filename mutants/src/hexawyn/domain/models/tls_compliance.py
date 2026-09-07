from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class TLSServiceStatus:
    service_name: str
    namespace: str
    tls_configured: bool
    cert_expiry_days: int
    days_remaining: int
    severity: str
    cert_issuer: str
    is_self_signed: bool
    proxy_tls_termination: bool


@dataclass
class TLSComplianceReport:
    services: list[TLSServiceStatus] = field(default_factory=list)
    all_compliant: bool = True
    total_issues: int = 0
