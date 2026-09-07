from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ErrorAttributionCommand:
    gateway: str = ""
    time_window_minutes: str = ""
