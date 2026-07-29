from dataclasses import dataclass


@dataclass(frozen=True)
class GetPipelineRunStatusCommand:
    namespace: str = ""
    limit: int = 50
    hours_window: int = 24
