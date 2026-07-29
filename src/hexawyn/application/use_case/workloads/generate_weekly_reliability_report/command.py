from dataclasses import dataclass


@dataclass(frozen=True)
class GenerateWeeklyReliabilityReportCommand:
    window_days: str = ""
