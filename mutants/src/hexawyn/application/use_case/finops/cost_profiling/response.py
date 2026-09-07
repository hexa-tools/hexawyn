from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CostProfilingResponse:
    time_window_minutes: int = 60
    ranked_endpoints: list[dict[str, object]] = field(default_factory=list)
    optimisation_candidates: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
