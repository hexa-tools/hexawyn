from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class TraceK8sEventsResponse:
    trace_id: str = ""
    matching_events: list[dict[str, object]] = field(default_factory=list)
    slowest_span: str = ""
    conclusion: str = ""
    events: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
