from dataclasses import dataclass


@dataclass(frozen=True)
class AnalyzeCriticalNamespaceEventsCommand:
    namespace: str | None = None
