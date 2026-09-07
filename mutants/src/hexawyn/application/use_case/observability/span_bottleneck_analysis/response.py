from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class SpanBottleneckAnalysisResponse:
    bottlenecks: list[dict[str, object]] = field(default_factory=list)
    redis_slowest: str = ""
    redis_avg_ms: str = ""
    reasons: str = ""
    db_slowest: str = ""
    db_avg_ms: str = ""
    confidence: str = ""
    bottleneck_pct_of_total: str = ""
    bottleneck: str = ""
    error: str | None = None
