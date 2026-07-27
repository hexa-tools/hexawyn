from dataclasses import dataclass, field
from typing import TypedDict


class ProposedWorkloadDict(TypedDict):
    name: str
    cpu_request_per_pod: str
    memory_request_per_pod: str
    replicas: int


@dataclass(frozen=True)
class ClusterHeadroomSimulationCommand:
    namespace: str | None = None
    proposed_workloads: list[ProposedWorkloadDict] = field(
        default_factory=list,
    )
