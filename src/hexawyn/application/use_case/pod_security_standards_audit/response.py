from dataclasses import dataclass


@dataclass
class PodSecurityStandardsAuditResponse:
    error: str | None = None
