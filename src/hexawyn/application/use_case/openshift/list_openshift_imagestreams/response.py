from dataclasses import dataclass, field


@dataclass
class ListOpenshiftImagestreamsResponse:
    items: list[dict[str, object]] = field(default_factory=list)
    count: int = 0
    error: str | None = None
