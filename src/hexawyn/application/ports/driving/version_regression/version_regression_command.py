from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VersionRegressionCommand:
    service_name: str
    time_window_minutes: int = 120
