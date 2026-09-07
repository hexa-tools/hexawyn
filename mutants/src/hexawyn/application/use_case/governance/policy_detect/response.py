from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class PolicyDetectResponse:
    engine: str = ""
    version: str | None = None
    namespace: str | None = None
    total_policies: int = 0
    enforce_policies: int = 0
    audit_policies: int = 0
    total_violations: int = 0
    high_severity: int = 0
    error: str | None = None
