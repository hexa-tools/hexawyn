from dataclasses import dataclass


@dataclass(frozen=True)
class CheckResourceConstraintsCommand:
    namespace: str = ""
    cpu_threshold_pct: int = 80
    memory_threshold_pct: int = 80
