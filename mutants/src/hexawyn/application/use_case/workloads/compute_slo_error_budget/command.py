from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ComputeSLOErrorBudgetCommand:
    service_name: str = ""
    slo_target: float = 99.9
    rolling_window_days: int = 30
