from dataclasses import dataclass, field


@dataclass
class CertsListResponse:
    certificates: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
