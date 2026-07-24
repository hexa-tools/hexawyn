from dataclasses import dataclass, field


@dataclass
class ListTaskRunsResponse:
    task_runs: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
