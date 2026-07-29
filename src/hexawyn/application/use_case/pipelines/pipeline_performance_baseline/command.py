from dataclasses import dataclass


@dataclass(frozen=True)
class PipelinePerformanceBaselineCommand:
    pipeline_name: str
    namespace: str = "ci"
    limit: int = 30
