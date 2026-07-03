from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AdvancedNamespaceEventAnalyticsCommand:
    namespace: str
    time_window_minutes: int = 360
