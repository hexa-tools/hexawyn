from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class MetricCorrelationCommand:
    service_name: str = ""
    primary_service: str = ""
    correlated_service: str = ""
    time_window_minutes: int = 60
