from dataclasses import dataclass, field


@dataclass
class CanaryComparisonResponse:
    service_name: str = ""
    canary_version: str = ""
    stable_version: str = ""
    verdict: str = ""
    confidence: str = ""
    p99_delta_pct: float = 0.0
    error_rate_delta_pct: float = 0.0
    canary_count: int = 0
    stable_count: int = 0
    traffic_split_pct: float = 0.0
    reasons: list[str] = field(default_factory=list)
    error: str | None = None
