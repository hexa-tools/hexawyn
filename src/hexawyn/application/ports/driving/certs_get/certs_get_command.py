from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CertsGetCommand:
    name: str
    namespace: str
