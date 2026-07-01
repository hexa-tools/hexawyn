from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CheckResourceConstraintsCommand:
    namespace: str
    cpu_threshold_pct: float = 80.0
    memory_threshold_pct: float = 85.0
