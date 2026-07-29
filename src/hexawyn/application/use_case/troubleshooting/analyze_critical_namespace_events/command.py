from dataclasses import dataclass


@dataclass(frozen=True)
class AnalyzeCriticalNamespaceEventsCommand:
    namespace: str | None = None
    time_window_minutes: int = 360
