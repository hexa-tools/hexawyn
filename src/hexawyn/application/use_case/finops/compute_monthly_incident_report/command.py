from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeMonthlyIncidentReportCommand:
    month: str | None = None
