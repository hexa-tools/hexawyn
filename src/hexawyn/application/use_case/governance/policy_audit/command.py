from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyAuditCommand:
    namespace: str | None = None
