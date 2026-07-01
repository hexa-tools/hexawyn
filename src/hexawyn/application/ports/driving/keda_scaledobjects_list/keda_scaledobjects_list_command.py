from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledObjectsListCommand:
    namespace: str | None = None
