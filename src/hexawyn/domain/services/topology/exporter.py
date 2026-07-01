from __future__ import annotations

from typing import TypedDict

from hexawyn.domain.models.dependency_graph import DependencyGraph


class ServiceNodeExport(TypedDict):
    name: str
    namespace: str
    replicas: int
    type: str
    is_spof: bool


class DependencyEdgeExport(TypedDict):
    caller: str
    callee: str


class DependencyGraphExport(TypedDict):
    nodes: list[ServiceNodeExport]
    edges: list[DependencyEdgeExport]
    single_points_of_failure: list[str]
    orphan_nodes: list[str]
    cycles: list[list[str]]
    inference_source: str
    truncated: bool
    namespace_scope: str | None


def to_structured_dict(graph: DependencyGraph) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=[
            ServiceNodeExport(
                name=node.name,
                namespace=node.namespace,
                replicas=node.replicas,
                type=node.node_type.value,
                is_spof=node.is_spof,
            )
            for node in graph.nodes
        ],
        edges=[
            DependencyEdgeExport(caller=edge.caller, callee=edge.callee) for edge in graph.edges
        ],
        single_points_of_failure=graph.single_points_of_failure,
        orphan_nodes=graph.orphan_nodes,
        cycles=graph.cycles,
        inference_source=graph.inference_source.value,
        truncated=graph.truncated,
        namespace_scope=graph.namespace_scope,
    )


def to_mermaid(graph: DependencyGraph) -> str:
    lines = ["graph TD"]

    for node in graph.nodes:
        lines.append(f'    {_safe_id(node.name)}["{node.name}"]')

    for edge in graph.edges:
        lines.append(f"    {_safe_id(edge.caller)} --> {_safe_id(edge.callee)}")

    if graph.single_points_of_failure:
        lines.append("    classDef spof fill:#f96,stroke:#900,stroke-width:2px")
        spof_ids = ",".join(_safe_id(name) for name in graph.single_points_of_failure)
        lines.append(f"    class {spof_ids} spof")

    return "\n".join(lines)


def _safe_id(name: str) -> str:
    return name.replace("-", "_")
