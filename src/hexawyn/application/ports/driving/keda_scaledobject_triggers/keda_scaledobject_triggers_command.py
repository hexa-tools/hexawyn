from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledObjectTriggersCommand:
    name: str
    namespace: str
