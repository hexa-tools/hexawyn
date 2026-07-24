from dataclasses import dataclass


@dataclass(frozen=True)
class SummarizeNamespaceEventsCommand:
    namespace: str
    time_window_minutes: int = 15
