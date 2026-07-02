from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TLSCertificateDiagnosisCommand:
    ingress_name: str
    namespace: str
