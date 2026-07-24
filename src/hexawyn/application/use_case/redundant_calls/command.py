from dataclasses import dataclass


@dataclass(frozen=True)
class RedundantCallsCommand:
    namespace: str | None = None
