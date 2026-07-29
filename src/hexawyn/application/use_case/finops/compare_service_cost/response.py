from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.service_cost_comparison import ServiceCostComparison


@dataclass
class CompareServiceCostResponse:
    result: ServiceCostComparison = field(default_factory=ServiceCostComparison)
