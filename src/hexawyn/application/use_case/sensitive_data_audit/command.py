from dataclasses import dataclass


@dataclass(frozen=True)
class SensitiveDataAuditCommand:
    namespace: str | None = None
