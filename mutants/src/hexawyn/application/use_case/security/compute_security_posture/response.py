from dataclasses import dataclass

from hexawyn.domain.models.security_posture import SecurityPostureReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ComputeSecurityPostureResponse:
    result: SecurityPostureReport
    error: str | None = None
