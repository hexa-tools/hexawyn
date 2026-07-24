from dataclasses import dataclass


@dataclass(frozen=True)
class GetNamespaceEventsCommand:
    namespace: str | None = None
