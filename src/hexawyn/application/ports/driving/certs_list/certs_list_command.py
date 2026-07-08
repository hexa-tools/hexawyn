from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CertsListCommand:
    namespace: str | None = None
