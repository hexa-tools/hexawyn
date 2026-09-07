from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DetectLogAnomaliesCommand:
    pod_name: str
    namespace: str
    time_window_minutes: int = 240
    zscore_threshold: float = 3.0
