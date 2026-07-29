from dataclasses import dataclass, field


@dataclass
class PolicyAuditResponse:
    results: dict[str, object] = field(default_factory=dict)
    error: str | None = None
