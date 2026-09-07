from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class SlowestTracesCommand:
    pod_name: str = ""
    time_window_minutes: str = ""
    top_n: str = ""
