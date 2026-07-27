from dataclasses import dataclass, field


@dataclass
class DetectOutdatedHelmReleasesResponse:
    result: dict[str, object] = field(default_factory=dict)
    error: str | None = None
