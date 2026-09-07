from dataclasses import dataclass

from hexawyn.domain.models.sla_report import SlaReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GenerateSLAReportResponse:
    result: SlaReport
