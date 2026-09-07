from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class AdminEndpointAuditResponse:
    endpoint_pattern: str = ""
    total_requests: int = 0
    total_403s: int = 0
    rate_403_pct: float = 0.0
    flagged_callers: list[dict[str, object]] = field(default_factory=list)
