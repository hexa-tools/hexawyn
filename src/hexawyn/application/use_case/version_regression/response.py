from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VersionRegressionResponse:
    service_name: str = ""
    baseline_version: str = ""
    current_version: str = ""
    verdict: str = "no_regression"
    p99_delta_pct: float = 0.0
    error_delta_pct: float = 0.0
    flags: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
