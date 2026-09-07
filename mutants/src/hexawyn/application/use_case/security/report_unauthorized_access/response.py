from dataclasses import dataclass

from hexawyn.domain.models.unauthorized_access import UnauthorizedAccessReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ReportUnauthorizedAccessResponse:
    result: UnauthorizedAccessReport
