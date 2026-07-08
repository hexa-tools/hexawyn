from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class KedaScaledJobsListResponse:
    scaled_jobs: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
