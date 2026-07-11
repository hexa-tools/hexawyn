from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.disruption_risk import DisruptionRiskReport


@dataclass
class CheckDisruptionRisksResponse:
    result: DisruptionRiskReport
