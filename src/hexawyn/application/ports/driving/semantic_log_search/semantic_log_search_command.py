from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SemanticLogSearchCommand:
    pattern: str
    is_regex: bool = False
    namespace: str | None = None
    time_window_minutes: int = 60
