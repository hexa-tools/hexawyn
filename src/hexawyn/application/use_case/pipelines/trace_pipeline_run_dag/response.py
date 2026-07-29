from dataclasses import dataclass, field


@dataclass
class TracePipelineRunDagResponse:
    pipeline_run_name: str = ""
    namespace: str = ""
    dag: dict[str, object] = field(default_factory=dict)
    tasks: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
