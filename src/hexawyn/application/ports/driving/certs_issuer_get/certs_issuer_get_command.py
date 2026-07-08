from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CertsIssuerGetCommand:
    name: str
    namespace: str | None = None
