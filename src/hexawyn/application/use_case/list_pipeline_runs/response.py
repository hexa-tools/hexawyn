from dataclasses import dataclass, field


@dataclass
class ListPipelineRunsResponse:
    pipeline_runs: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
