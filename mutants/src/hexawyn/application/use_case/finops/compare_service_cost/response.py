from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.service_cost_comparison import ServiceCostComparison


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CompareServiceCostResponse:
    result: ServiceCostComparison = field(default_factory=ServiceCostComparison)
