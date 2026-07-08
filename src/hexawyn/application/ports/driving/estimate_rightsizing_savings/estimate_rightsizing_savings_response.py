from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.rightsizing import RightsizingReport


@dataclass
class EstimateRightsizingSavingsResponse:
    report: RightsizingReport = field(default_factory=RightsizingReport)
    metrics_server_available: bool = True
