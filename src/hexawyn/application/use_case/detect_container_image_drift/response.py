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
    drifts: list[ContainerImageDriftDict] = field(default_factory=list)
    total_drifted: int = 0
    error: str | None = None
