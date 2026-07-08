from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CertsIssuersListCommand:
    namespace: str | None = None
