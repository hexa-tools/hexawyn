from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class SpanBottleneckAnalysisCommand:
    service_name: str = ""
    time_window_minutes: int = 60
