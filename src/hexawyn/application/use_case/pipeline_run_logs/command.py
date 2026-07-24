from dataclasses import dataclass


@dataclass(frozen=True)
class PipelineRunLogsCommand:
    pipeline_run_name: str
    namespace: str
    task_name: str | None = None
