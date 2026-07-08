from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CertsIssuerGetResponse:
    name: str = ""
    namespace: str | None = None
    kind: str = ""
    issuer_type: str = "unknown"
    ready: bool = False
    server: str | None = None
    message: str | None = None
    error: str | None = None
