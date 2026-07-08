from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SlowestTracesCommand:
    pod_name: str
    time_window_minutes: int = 60
    top_n: int = 5
