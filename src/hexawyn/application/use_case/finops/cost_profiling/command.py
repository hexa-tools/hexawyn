from dataclasses import dataclass


@dataclass(frozen=True)
class CostProfilingCommand:
    time_window_minutes: int = 60
    top_n: int = 10
