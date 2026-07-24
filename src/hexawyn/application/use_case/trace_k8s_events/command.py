from dataclasses import dataclass


@dataclass(frozen=True)
class TraceK8sEventsCommand:
    namespace: str | None = None
