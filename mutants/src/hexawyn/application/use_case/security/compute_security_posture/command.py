from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ComputeSecurityPostureCommand:
    previous_score_pct: float | None = None
