from dataclasses import dataclass

from hexawyn.domain.models.incident_cost import IncidentCostReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class AnalyzeIncidentCostResponse:
    result: IncidentCostReport
