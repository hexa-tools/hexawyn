from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HotNodeAnalysisCommand:
    window_hours: int = 24
