from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyListCommand:
    namespace: str | None = None
