from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyViolationsListCommand:
    namespace: str | None = None
