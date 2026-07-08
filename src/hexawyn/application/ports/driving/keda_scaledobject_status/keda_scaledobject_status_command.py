from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledObjectStatusCommand:
    name: str
    namespace: str
