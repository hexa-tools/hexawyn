from __future__ import annotations

from hexawyn.domain.models.dependency_graph import (
    DependencyEdge,
    DependencyGraph,
    InferenceSource,
    NodeType,
    ServiceNode,
)


class TestServiceNode:
    def test_all_fields_populated(self) -> None:
        node = ServiceNode(
            name="auth-service",
            namespace="production",
            replicas=1,
            node_type=NodeType.INTERNAL,
            in_degree=3,
            out_degree=1,
            is_spof=True,
        )
        assert node.name == "auth-service"
        assert node.namespace == "production"
        assert node.replicas == 1
        assert node.node_type is NodeType.INTERNAL
        assert node.in_degree == 3
        assert node.out_degree == 1
        assert node.is_spof is True

    def test_defaults(self) -> None:
        node = ServiceNode(
            name="checkout-service",
            namespace="production",
            replicas=3,
            node_type=NodeType.INTERNAL,
        )
        assert node.in_degree == 0
        assert node.out_degree == 0
        assert node.is_spof is False


class TestDependencyEdge:
    def test_is_frozen(self) -> None:
        edge = DependencyEdge(caller="api-gateway", callee="auth-service")
        assert edge.caller == "api-gateway"
        assert edge.callee == "auth-service"


class TestNodeType:
    def test_has_three_types(self) -> None:
        assert {t.name for t in NodeType} == {"INTERNAL", "EXTERNAL", "ORPHAN"}


class TestInferenceSource:
    def test_has_two_sources(self) -> None:
        assert {s.name for s in InferenceSource} == {
            "ISTIO_VIRTUAL_SERVICE",
            "NETWORK_POLICY",
        }


class TestDependencyGraph:
    def _build_graph(self) -> DependencyGraph:
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
                ServiceNode(
                    name="reporting-service",
                    namespace="production",
                    replicas=2,
                    node_type=NodeType.ORPHAN,
                ),
            ],
            edges=[DependencyEdge(caller="api-gateway", callee="auth-service")],
            inference_source=InferenceSource.NETWORK_POLICY,
        )

    def test_single_points_of_failure_lists_spof_names(self) -> None:
        graph = self._build_graph()
        assert graph.single_points_of_failure == ["auth-service"]

    def test_orphan_nodes_lists_orphan_names(self) -> None:
        graph = self._build_graph()
        assert graph.orphan_nodes == ["reporting-service"]

    def test_defaults(self) -> None:
        graph = self._build_graph()
        assert graph.cycles == []
        assert graph.truncated is False
        assert graph.namespace_scope is None
