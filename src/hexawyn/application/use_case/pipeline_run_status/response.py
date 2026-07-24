from dataclasses import dataclass


@dataclass
class PipelineRunStatusResponse:
    error: str | None = None
