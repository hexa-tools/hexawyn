from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class LatencyDiagnosticCommand:
    service_name: str
    time_window_minutes: int = 15
    threshold_ms: float = 500.0
