from dataclasses import dataclass, field


@dataclass
class CertsRequestsListResponse:
    requests: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
