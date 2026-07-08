from __future__ import annotations

from collections.abc import Iterable
from typing import TypedDict

from hexawyn.domain.models.dependency_graph import (
    DependencyEdge,
    DependencyGraph,
    InferenceSource,
    NodeType,
    ServiceNode,
)

MAX_NODES_DEFAULT = 200


class RawServiceRecord(TypedDict):
    name: str
    namespace: str
    replicas: int
    is_external: bool


class RawEdgeRecord(TypedDict):
    caller: str
    callee: str


class TopologyGraphBuilderService:
    def build_graph(
        self,
        services: list[RawServiceRecord],
        edges: list[RawEdgeRecord],
        inference_source: InferenceSource,
        namespace_scope: str | None = None,
        max_nodes: int = MAX_NODES_DEFAULT,
    ) -> DependencyGraph:
        selected_services, truncated = _select_services(services, namespace_scope, max_nodes)
        known_names = {service["name"] for service in selected_services}

        valid_edges = [
            DependencyEdge(caller=edge["caller"], callee=edge["callee"])
            for edge in edges
            if edge["caller"] in known_names and edge["callee"] in known_names
        ]

        in_degree = _count_degree(edge.callee for edge in valid_edges)
        out_degree = _count_degree(edge.caller for edge in valid_edges)
        nodes = [_build_node(service, in_degree, out_degree) for service in selected_services]
        cycles = _detect_cycles(valid_edges)

        return DependencyGraph(
            nodes=nodes,
            edges=valid_edges,
            inference_source=inference_source,
            cycles=cycles,
            truncated=truncated,
            namespace_scope=namespace_scope,
        )


def _select_services(
    services: list[RawServiceRecord], namespace_scope: str | None, max_nodes: int
) -> tuple[list[RawServiceRecord], bool]:
    if namespace_scope is not None or len(services) <= max_nodes:
        return services, False
    truncated_services = sorted(services, key=lambda service: service["name"])[:max_nodes]
    return truncated_services, True


def _count_degree(names: Iterable[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in names:
        counts[name] = counts.get(name, 0) + 1
    return counts


def _build_node(
    service: RawServiceRecord, in_degree: dict[str, int], out_degree: dict[str, int]
) -> ServiceNode:
    name = service["name"]
    node_in_degree = in_degree.get(name, 0)
    node_out_degree = out_degree.get(name, 0)

    if service["is_external"]:
        node_type = NodeType.EXTERNAL
    elif node_in_degree == 0 and node_out_degree == 0:
        node_type = NodeType.ORPHAN
    else:
        node_type = NodeType.INTERNAL

    return ServiceNode(
        name=name,
        namespace=service["namespace"],
        replicas=service["replicas"],
        node_type=node_type,
        in_degree=node_in_degree,
        out_degree=node_out_degree,
        is_spof=service["replicas"] == 1 and node_in_degree > 0,
    )


def _detect_cycles(edges: list[DependencyEdge]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = {}
    for edge in edges:
        adjacency.setdefault(edge.caller, []).append(edge.callee)

    cycles: list[list[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        visiting.add(node)
        path.append(node)
        for neighbor in adjacency.get(node, []):
            if neighbor in visiting:
                cycle_start = path.index(neighbor)
                cycles.append([*path[cycle_start:], neighbor])
            elif neighbor not in visited:
                visit(neighbor, path)
        path.pop()
        visiting.discard(node)
        visited.add(node)

    for start in adjacency:
        if start not in visited:
            visit(start, [])

    return cycles
