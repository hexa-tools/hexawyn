from __future__ import annotations

from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_response import (
    LiveTopologyMapperResponse,
)
from hexawyn.domain.models.dependency_graph import (
    DependencyEdge,
    DependencyGraph,
    InferenceSource,
    NodeType,
    ServiceNode,
)


class TestLiveTopologyMapperResponse:
    def test_defaults(self) -> None:
        response = LiveTopologyMapperResponse()
        assert response.nodes == []
        assert response.edges == []
        assert response.single_points_of_failure == []
        assert response.orphan_nodes == []
        assert response.cycles == []
        assert response.inference_source == ""
        assert response.truncated is False
        assert response.namespace_scope is None
        assert response.mermaid_diagram == ""

    def test_from_graph_maps_all_fields(self) -> None:
        graph = DependencyGraph(
            nodes=[
                ServiceNode(
                    name="auth-service",
                    namespace="production",
                    replicas=1,
                    node_type=NodeType.INTERNAL,
                    in_degree=1,
                    is_spof=True,
                )
            ],
            edges=[DependencyEdge(caller="api-gateway", callee="auth-service")],
            inference_source=InferenceSource.NETWORK_POLICY,
            truncated=True,
            namespace_scope="production",
        )

        response = LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram="graph TD")

        assert response.single_points_of_failure == ["auth-service"]
        assert response.edges == [{"caller": "api-gateway", "callee": "auth-service"}]
        assert response.inference_source == "NETWORK_POLICY"
        assert response.truncated is True
        assert response.namespace_scope == "production"
        assert response.mermaid_diagram == "graph TD"
