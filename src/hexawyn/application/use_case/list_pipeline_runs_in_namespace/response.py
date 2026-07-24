from dataclasses import dataclass, field


@dataclass
class ListPipelineRunsInNamespaceResponse:
    runs: list[dict[str, object]] = field(default_factory=list)
    stuck_runs: list[str] = field(default_factory=list)
    note: str | None = None
    error: str | None = None
