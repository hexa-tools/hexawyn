from __future__ import annotations

from dataclasses import dataclass, field


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
