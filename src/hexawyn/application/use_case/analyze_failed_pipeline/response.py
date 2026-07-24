from dataclasses import dataclass


@dataclass
class AnalyzeFailedPipelineResponse:
    error: str | None = None
