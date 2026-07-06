from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ComputeMTTRTrendCommand:
    months: list[str] = field(default_factory=list)
