from dataclasses import dataclass


@dataclass(frozen=True)
class ListPipelineRunsCommand:
    service_name: str = ""
    namespace: str | None = None
