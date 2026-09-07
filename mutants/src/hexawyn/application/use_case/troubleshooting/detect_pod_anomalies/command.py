from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class DetectPodAnomaliesCommand:
    namespace: str
    baseline_window_days: int = 7
