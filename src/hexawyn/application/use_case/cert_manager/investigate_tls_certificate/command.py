from dataclasses import dataclass


@dataclass(frozen=True)
class InvestigateTLSCertificateCommand:
    ingress_name: str = ""
    namespace: str = ""
