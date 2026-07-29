from dataclasses import dataclass, field


@dataclass
class PipelineRunLogsResponse:
    pipeline_run_name: str = ""
    namespace: str = ""
    pipeline_run_found: bool = False
    is_still_running: bool = False
    failed_step_count: int = 0
    total_step_count: int = 0
    steps: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
