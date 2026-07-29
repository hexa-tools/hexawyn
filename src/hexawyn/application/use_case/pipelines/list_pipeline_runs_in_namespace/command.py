from dataclasses import dataclass


@dataclass(frozen=True)
class ListPipelineRunsInNamespaceCommand:
    namespace: str
    limit: int = 100
