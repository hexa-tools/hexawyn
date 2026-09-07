from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class SLOBreachPredictionResponse:
    at_risk: list[dict[str, object]] = field(default_factory=list)
    safe_count: int = 0
    error: str | None = None
