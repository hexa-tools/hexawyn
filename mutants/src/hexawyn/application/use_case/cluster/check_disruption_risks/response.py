from dataclasses import dataclass

from hexawyn.domain.models.disruption_risk import DisruptionRiskReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CheckDisruptionRisksResponse:
    result: DisruptionRiskReport
