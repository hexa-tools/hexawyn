from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TLSCertificateDiagnosisResponse:
    ingress_name: str = ""
    namespace: str = ""
    status: str = "error"
    diagnosis: str = ""
    expiry_date: str | None = None
    days_remaining: int | None = None
    cipher_info: str = ""
    san_list: list[str] = field(default_factory=list)
    error: str | None = None
