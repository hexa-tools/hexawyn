from dataclasses import dataclass


@dataclass(frozen=True)
class GenerateSlaReportCommand:
    quarter: str
