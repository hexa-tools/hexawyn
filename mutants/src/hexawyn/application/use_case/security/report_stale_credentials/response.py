from dataclasses import dataclass

from hexawyn.domain.models.stale_credentials import StaleCredentialsReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ReportStaleCredentialsResponse:
    result: StaleCredentialsReport
