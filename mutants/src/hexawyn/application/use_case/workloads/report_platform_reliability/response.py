from dataclasses import dataclass

from hexawyn.domain.models.platform_reliability import PlatformReliabilityReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ReportPlatformReliabilityResponse:
    result: PlatformReliabilityReport
