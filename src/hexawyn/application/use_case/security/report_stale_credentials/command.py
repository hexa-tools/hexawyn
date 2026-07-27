from dataclasses import dataclass


@dataclass(frozen=True)
class ReportStaleCredentialsCommand:
    min_days: int = 90
