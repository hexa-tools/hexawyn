from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class MemorySaturationResponse:
    prediction_window_minutes: int = 30
    critical_pods: list[dict[str, object]] = field(default_factory=list)
    safe_pod_count: int = 0
