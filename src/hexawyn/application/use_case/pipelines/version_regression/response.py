from dataclasses import dataclass, field


@dataclass
class VersionRegressionResponse:
    service_name: str = ""
    baseline_version: str = ""
    current_version: str = ""
    verdict: str = ""
    p99_delta_pct: float = 0.0
    error_delta_pct: float = 0.0
    flags: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
    verdict: str = "no_regression"  # type: ignore
    p99_delta_pct: float = 0.0  # type: ignore
    error_delta_pct: float = 0.0  # type: ignore
    flags: list[dict[str, object]] = field(default_factory=list)  # type: ignore
    error: str | None = None  # type: ignore
