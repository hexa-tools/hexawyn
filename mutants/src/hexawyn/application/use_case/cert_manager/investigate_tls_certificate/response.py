from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class InvestigateTLSCertificateResponse:
    ingress_name: str = ""
    namespace: str = ""
    certificate_found: bool = False
    days_until_expiry: int = 0
    issuer: str = ""
    status: str = ""
    findings: list[str] = field(default_factory=list)
    error: str | None = None
