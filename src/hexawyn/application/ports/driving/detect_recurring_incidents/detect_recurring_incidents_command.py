from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DetectRecurringIncidentsCommand:
    window_days: int = 30
