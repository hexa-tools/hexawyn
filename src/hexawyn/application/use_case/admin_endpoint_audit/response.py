from dataclasses import dataclass, field


@dataclass
class AdminEndpointAuditResponse:
    endpoints: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
