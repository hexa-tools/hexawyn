from dataclasses import dataclass, field


@dataclass
class GitopsSourcesListResponse:
    sources: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
