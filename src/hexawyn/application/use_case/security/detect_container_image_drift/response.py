from dataclasses import dataclass, field
from typing import TypedDict


class ContainerImageDriftDict(TypedDict):
    container_name: str
    pod_name: str
    namespace: str
    current_image: str
    latest_image: str
    drift_days: int
    severity: str
    recommendation: str


@dataclass
class DetectContainerImageDriftResponse:
    out_of_sync: list[ContainerImageDriftDict] = field(default_factory=list)
    in_sync_count: int = 0
    excluded_count: int = 0
    total_checked: int = 0
    summary: str = ""
    error: str | None = None
