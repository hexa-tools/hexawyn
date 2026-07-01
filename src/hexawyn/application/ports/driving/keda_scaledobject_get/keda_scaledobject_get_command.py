from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledObjectGetCommand:
    name: str
    namespace: str
