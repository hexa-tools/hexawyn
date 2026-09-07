from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class SlowestTracesResponse:
    traces: list[dict[str, object]] = field(default_factory=list)
    total_traces_found: int = 0
    slowest_traces: str = ""
    pod_name: str = ""
    note: str = ""
    error: str | None = None
