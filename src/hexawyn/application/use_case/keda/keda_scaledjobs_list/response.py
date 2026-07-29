from dataclasses import dataclass, field


@dataclass
class KedaScaledjobsListResponse:
    scaled_jobs: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
