from dataclasses import dataclass


@dataclass(frozen=True)
class ListTaskRunsCommand:
    pipeline_name: str
    namespace: str
