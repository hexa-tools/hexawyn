from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class _ProposedWorkloadRequired(TypedDict):
    name: str
    cpu_request_per_pod: str
    memory_request_per_pod: str


class ProposedWorkloadDict(_ProposedWorkloadRequired, total=False):
    replicas: int


@dataclass(frozen=True)
class ClusterHeadroomSimulationCommand:
    proposed_workloads: list[ProposedWorkloadDict] = field(default_factory=list)
