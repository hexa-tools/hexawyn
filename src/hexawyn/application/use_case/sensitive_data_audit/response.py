from dataclasses import dataclass, field


@dataclass
class SensitiveDataAuditResponse:
    findings: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
