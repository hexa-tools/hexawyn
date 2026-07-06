from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.service_cost_comparison import ServiceCostComparison


@dataclass
class CompareServiceCostResponse:
    result: ServiceCostComparison
