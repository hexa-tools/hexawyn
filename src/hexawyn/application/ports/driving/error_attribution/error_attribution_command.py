from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ErrorAttributionCommand:
    gateway: str
    time_window_minutes: int = 30
