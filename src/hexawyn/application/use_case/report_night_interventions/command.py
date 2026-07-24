from dataclasses import dataclass


@dataclass(frozen=True)
class ReportNightInterventionsCommand:
    history_months: int = 6
