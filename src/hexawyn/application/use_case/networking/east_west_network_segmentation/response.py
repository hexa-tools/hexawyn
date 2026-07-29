from dataclasses import dataclass, field


@dataclass
class EastWestNetworkSegmentationResponse:
    namespace: str = ""
    total_namespaces: int = 0
    findings: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
