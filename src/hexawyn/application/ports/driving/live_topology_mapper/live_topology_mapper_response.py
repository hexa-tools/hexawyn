from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.dependency_graph import DependencyGraph
from hexawyn.domain.services.topology.exporter import (
    DependencyEdgeExport,
    ServiceNodeExport,
    to_structured_dict,
)


@dataclass
class LiveTopologyMapperResponse:
    nodes: list[ServiceNodeExport] = field(default_factory=list)
    edges: list[DependencyEdgeExport] = field(default_factory=list)
    single_points_of_failure: list[str] = field(default_factory=list)
    orphan_nodes: list[str] = field(default_factory=list)
    cycles: list[list[str]] = field(default_factory=list)
    inference_source: str = ""
    truncated: bool = False
    namespace_scope: str | None = None
    mermaid_diagram: str = ""

    @classmethod
    def from_graph(cls, graph: DependencyGraph, mermaid_diagram: str) -> LiveTopologyMapperResponse:
        export = to_structured_dict(graph)
        return cls(
            nodes=export["nodes"],
            edges=export["edges"],
            single_points_of_failure=export["single_points_of_failure"],
            orphan_nodes=export["orphan_nodes"],
            cycles=export["cycles"],
            inference_source=export["inference_source"],
            truncated=export["truncated"],
            namespace_scope=export["namespace_scope"],
            mermaid_diagram=mermaid_diagram,
        )
