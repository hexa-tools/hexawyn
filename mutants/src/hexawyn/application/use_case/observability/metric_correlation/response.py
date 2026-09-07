from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class MetricCorrelationResponse:
    correlations: list[dict[str, object]] = field(default_factory=list)
    status: str = ""
    primary_service: str = ""
    lag_index: str = ""
    hypothesis: str = ""
    data_point_count: int = 0
    correlated_service: str = ""
    coefficient: str = ""
    error: str | None = None
