from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class GetNamespaceEventsCommand:
    namespace: str
    time_window_minutes: int = 15
    top_n: int = 20
