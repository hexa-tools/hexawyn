from dataclasses import dataclass, field


@dataclass
class GitopsAppsListResponse:
    apps: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
