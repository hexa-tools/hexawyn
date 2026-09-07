from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ErrorAttributionResponse:
    total_errors: int = 0
    pareto_culprit: str = ""
    gateway: str = ""
    attribution: str = ""
    error: str | None = None
