from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CanaryComparisonCommand:
    service_name: str
    time_window_minutes: int = 30
    traffic_split_pct: float = 5.0
