from dataclasses import dataclass, field

from hexawyn.application.ports.driven.k8s_port import PodInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ChatCliResponse:
    kind: str
    lines: list[tuple[str, str]] = field(default_factory=list)
    pods: list[PodInfo] | None = None
    summary: str | None = None
    suggestions: list[str] = field(default_factory=list)
    duration_ms: int = 0
