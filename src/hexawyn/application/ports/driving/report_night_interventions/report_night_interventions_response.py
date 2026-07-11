from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.engineer_workload import NightInterventionReport


@dataclass
class ReportNightInterventionsResponse:
    result: NightInterventionReport
