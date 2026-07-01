from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class NodeType(Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"
    ORPHAN = "ORPHAN"


class InferenceSource(Enum):
    ISTIO_VIRTUAL_SERVICE = "ISTIO_VIRTUAL_SERVICE"
    NETWORK_POLICY = "NETWORK_POLICY"


@dataclass
class ServiceNode:
    name: str
    namespace: str
    replicas: int
    node_type: NodeType
    in_degree: int = 0
    out_degree: int = 0
    is_spof: bool = False


@dataclass(frozen=True)
class DependencyEdge:
    caller: str
    callee: str


@dataclass
class DependencyGraph:
    nodes: list[ServiceNode]
    edges: list[DependencyEdge]
    inference_source: InferenceSource
    cycles: list[list[str]] = field(default_factory=list)
    truncated: bool = False
    namespace_scope: str | None = None

    @property
    def single_points_of_failure(self) -> list[str]:
        return [node.name for node in self.nodes if node.is_spof]

    @property
    def orphan_nodes(self) -> list[str]:
        return [node.name for node in self.nodes if node.node_type is NodeType.ORPHAN]
