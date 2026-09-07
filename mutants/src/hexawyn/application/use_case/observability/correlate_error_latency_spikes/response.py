from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class CorrelateErrorLatencySpikesUseCaseResponse:
    namespace: str = ""
    pods: list[dict[str, object]] = field(default_factory=list)
    total_pods: int = 0
    error: str | None = None
