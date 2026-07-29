from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.fleet_health import FleetHealthReport


@dataclass
class GlobalHealthCheckResponse:
    report: FleetHealthReport = field(default_factory=FleetHealthReport)
    fleet_score_trend: str | None = None
