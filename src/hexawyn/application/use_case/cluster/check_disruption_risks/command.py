from dataclasses import dataclass


@dataclass(frozen=True)
class CheckDisruptionRisksCommand:
    warning_days: int = 7
