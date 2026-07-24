from dataclasses import dataclass


@dataclass(frozen=True)
class SlowestTracesCommand:
    limit: int = 10
