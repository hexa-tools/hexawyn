from dataclasses import dataclass


@dataclass(frozen=True)
class AnalyzeFailedPipelineCommand:
    namespace: str = ""
    pipeline_name: str = ""
