from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GetPodEventsResponse:
    pod_name: str = ""
    namespace: str = ""
    events: list[dict[str, object]] = field(default_factory=list)
    total_events: int = 0
    error: str | None = None
