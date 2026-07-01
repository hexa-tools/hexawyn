from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CertsRequestsListCommand:
    namespace: str | None = None
