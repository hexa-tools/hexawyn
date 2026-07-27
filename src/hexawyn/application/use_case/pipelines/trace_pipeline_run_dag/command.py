from dataclasses import dataclass


@dataclass(frozen=True)
class TracePipelineRunDagCommand:
    pipeline_run_name: str
    namespace: str
