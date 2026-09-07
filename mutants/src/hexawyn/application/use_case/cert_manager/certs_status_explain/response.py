from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CertsStatusExplainResponse:
    status: str = "unknown"
    message: str | None = None
    explanation: str = ""
    fix_suggestion: str = ""
    error: str | None = None
