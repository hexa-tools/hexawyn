from dataclasses import dataclass


@dataclass
class GenerateWeeklyReliabilityReportResponse:
    result: dict[str, object] | None = None
    error: str | None = None
