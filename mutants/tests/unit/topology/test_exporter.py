from __future__ import annotations

from hexawyn.domain.models.dependency_graph import (
    DependencyEdge,
    DependencyGraph,
    InferenceSource,
    NodeType,
    ServiceNode,
)
from hexawyn.domain.services.topology.exporter import to_mermaid, to_structured_dict


def _graph_with_spof() -> DependencyGraph:
    return DependencyGraph(
        nodes=[
            ServiceNode(
                name="api-gateway",
                namespace="production",
                replicas=3,
                node_type=NodeType.INTERNAL,
                out_degree=1,
            ),
            ServiceNode(
                name="auth-service",
                namespace="production",
                replicas=1,
                node_type=NodeType.INTERNAL,
                in_degree=1,
                is_spof=True,
            ),
        ],
        edges=[DependencyEdge(caller="api-gateway", callee="auth-service")],
        inference_source=InferenceSource.NETWORK_POLICY,
        cycles=[["a", "b", "a"]],
        truncated=True,
        namespace_scope="production",
    )


class TestToStructuredDict:
    def test_shape_matches_graph(self) -> None:
        export = to_structured_dict(_graph_with_spof())

        assert export["nodes"] == [
            {
                "name": "api-gateway",
                "namespace": "production",
                "replicas": 3,
                "type": "INTERNAL",
                "is_spof": False,
            },
            {
                "name": "auth-service",
                "namespace": "production",
                "replicas": 1,
                "type": "INTERNAL",
                "is_spof": True,
            },
        ]
        assert export["edges"] == [{"caller": "api-gateway", "callee": "auth-service"}]
        assert export["single_points_of_failure"] == ["auth-service"]
        assert export["orphan_nodes"] == []
        assert export["cycles"] == [["a", "b", "a"]]
        assert export["inference_source"] == "NETWORK_POLICY"
        assert export["truncated"] is True
        assert export["namespace_scope"] == "production"


class TestToMermaid:
    def test_contains_graph_declaration(self) -> None:
        mermaid = to_mermaid(_graph_with_spof())
        assert mermaid.startswith("graph TD")

    def test_contains_node_and_edge_lines(self) -> None:
        mermaid = to_mermaid(_graph_with_spof())
        assert "api_gateway" in mermaid
        assert "auth_service" in mermaid
        assert "api_gateway --> auth_service" in mermaid

    def test_spof_node_gets_styled_class(self) -> None:
        mermaid = to_mermaid(_graph_with_spof())
        assert "classDef spof" in mermaid
        assert "class auth_service spof" in mermaid

    def test_no_spof_styling_when_no_spof(self) -> None:
        graph = DependencyGraph(
            nodes=[
                ServiceNode(
                    name="a", namespace="production", replicas=3, node_type=NodeType.INTERNAL
                )
            ],
            edges=[],
            inference_source=InferenceSource.NETWORK_POLICY,
        )
        mermaid = to_mermaid(graph)
        assert "classDef spof" not in mermaid
