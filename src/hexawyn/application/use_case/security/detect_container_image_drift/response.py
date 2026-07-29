from dataclasses import dataclass, field
from typing import TypedDict


class ContainerImageDriftDict(TypedDict):
    deployment: str
    namespace: str
    container: str
    running_image: str
    declared_image: str
    source_of_truth: str
    drift_type: str
    severity: str


@dataclass
class DetectContainerImageDriftResponse:
    out_of_sync: list[ContainerImageDriftDict] = field(default_factory=list)
    in_sync_count: int = 0
    excluded_count: int = 0
    total_checked: int = 0
    summary: str = ""
    error: str | None = None
