from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hexawyn.domain.models.dependency_graph import DependencyGraph


@dataclass
class LiveTopologyMapperResponse:
    nodes: list[dict[str, object]] = field(default_factory=list)
    edges: list[dict[str, object]] = field(default_factory=list)
    single_points_of_failure: list[dict[str, object]] = field(default_factory=list)
    orphan_nodes: list[dict[str, object]] = field(default_factory=list)
    cycles: list[dict[str, object]] = field(default_factory=list)
    inference_source: str = ""
    truncated: bool = False
    namespace_scope: str | None = None
    mermaid_diagram: str = ""

    @classmethod
    def from_graph(
        cls,
        graph: DependencyGraph,
        mermaid_diagram: str = "",
    ) -> LiveTopologyMapperResponse:
        return cls(
            nodes=[{"name": n.service_name} for n in graph.nodes],  # type: ignore
            edges=[{"source": e.source, "target": e.target} for e in graph.edges],  # type: ignore
            single_points_of_failure=[{"name": n.service_name} for n in graph.nodes if n.is_spof],  # type: ignore
            orphan_nodes=[{"name": n.service_name} for n in graph.nodes if n.is_orphan],  # type: ignore
            cycles=[{"nodes": list(c)} for c in graph.cycles],
            mermaid_diagram=mermaid_diagram,
        )
