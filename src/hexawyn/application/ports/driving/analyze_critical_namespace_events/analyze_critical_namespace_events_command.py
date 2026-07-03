from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AnalyzeCriticalNamespaceEventsCommand:
    namespace: str
    time_window_minutes: int = 15
