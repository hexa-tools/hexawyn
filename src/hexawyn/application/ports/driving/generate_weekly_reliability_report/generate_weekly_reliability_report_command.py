from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GenerateWeeklyReliabilityReportCommand:
    window_days: int = 7
