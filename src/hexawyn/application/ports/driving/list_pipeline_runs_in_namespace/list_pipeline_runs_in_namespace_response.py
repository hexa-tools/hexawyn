from dataclasses import dataclass, field

from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo


@dataclass
class ListPipelineRunsInNamespaceResponse:
    runs: list[NamespacedPipelineRunInfo] = field(default_factory=list)
    stuck_runs: list[str] = field(default_factory=list)
    note: str | None = None
