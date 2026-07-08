from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GetNamespaceEventsCommand:
    namespace: str
    time_window_minutes: int = 15
    top_n: int = 20
