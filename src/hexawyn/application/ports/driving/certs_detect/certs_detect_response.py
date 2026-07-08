from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CertsDetectResponse:
    installed: bool = False
    version: str | None = None
    namespace: str | None = None
    total_certs: int = 0
    ready_certs: int = 0
    expiring_soon: int = 0
    failed_certs: int = 0
    active_challenges: int = 0
    error: str | None = None
