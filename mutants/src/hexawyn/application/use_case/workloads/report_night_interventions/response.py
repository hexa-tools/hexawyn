from dataclasses import dataclass

from hexawyn.domain.models.engineer_workload import NightInterventionReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ReportNightInterventionsResponse:
    result: NightInterventionReport
