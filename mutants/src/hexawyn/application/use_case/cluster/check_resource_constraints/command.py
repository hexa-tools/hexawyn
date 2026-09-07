from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CheckResourceConstraintsCommand:
    namespace: str = ""
    cpu_threshold_pct: int = 80
    memory_threshold_pct: int = 80
