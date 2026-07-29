from dataclasses import dataclass, field


@dataclass
class DetectNetworkSegmentationGapsResponse:
    findings: list[dict[str, object]] = field(default_factory=list)
    excluded_namespaces: list[str] = field(default_factory=list)
    total_namespaces_checked: int = 0
    fully_open_count: int = 0
    partially_restricted_count: int = 0
    restricted_count: int = 0
    summary: str = ""
    error: str | None = None
