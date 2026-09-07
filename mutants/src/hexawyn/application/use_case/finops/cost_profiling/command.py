from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CostProfilingCommand:
    time_window_minutes: int = 60
    top_n: int = 10
