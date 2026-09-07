from dataclasses import dataclass, field

from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ListPipelineRunsInNamespaceResponse:
    runs: list[NamespacedPipelineRunInfo] = field(default_factory=list)
    stuck_runs: list[str] = field(default_factory=list)
    note: str | None = None
    error: str | None = None
