from dataclasses import dataclass

from hexawyn.domain.models.critical_cve import CriticalCveReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ReportCriticalVulnerabilitiesResponse:
    result: CriticalCveReport
