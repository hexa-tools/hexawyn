from dataclasses import dataclass, field


@dataclass
class PipelineRunStatusResponse:
    total_runs: int = 0
    runs: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
