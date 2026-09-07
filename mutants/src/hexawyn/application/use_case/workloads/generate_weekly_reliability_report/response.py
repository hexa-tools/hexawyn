from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GenerateWeeklyReliabilityReportResponse:
    result: dict[str, object] | None = None
    error: str | None = None
