from dataclasses import dataclass


@dataclass(frozen=True)
class TlsCertificateDiagnosisCommand:
    ingress_name: str
    namespace: str
