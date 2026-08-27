from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.fleet_health import FleetHealthReport


@dataclass
class GlobalHealthCheckResponse:
    report: FleetHealthReport = field(default_factory=FleetHealthReport)
    fleet_score_trend: str | None = None
    total_contexts: int = 0
    page: int = 1
    page_size: int = 0
    has_more: bool = False
