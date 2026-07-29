from dataclasses import dataclass


@dataclass(frozen=True)
class PodSecurityStandardsAuditCommand:
    namespaces: list[str] | None = None
