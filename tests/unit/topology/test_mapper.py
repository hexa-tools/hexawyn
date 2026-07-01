from __future__ import annotations

from hexawyn.domain.models.dependency_graph import InferenceSource, NodeType
from hexawyn.domain.services.topology.mapper import (
    RawEdgeRecord,
    RawServiceRecord,
    TopologyGraphBuilderService,
)


def _service(
    name: str, replicas: int = 1, namespace: str = "production", is_external: bool = False
) -> RawServiceRecord:
    return RawServiceRecord(
        name=name, namespace=namespace, replicas=replicas, is_external=is_external
    )


def _edge(caller: str, callee: str) -> RawEdgeRecord:
    return RawEdgeRecord(caller=caller, callee=callee)


class TestBuildGraph:
    def setup_method(self) -> None:
        self.engine = TopologyGraphBuilderService()

    def test_five_service_chain_returns_correct_graph(self) -> None:
        services = [
            _service("a", replicas=3),
            _service("b", replicas=3),
            _service("c", replicas=3),
            _service("d", replicas=3),
            _service("e", replicas=3),
        ]
        edges = [_edge("a", "b"), _edge("b", "c"), _edge("c", "d"), _edge("d", "e")]

        graph = self.engine.build_graph(services, edges, InferenceSource.NETWORK_POLICY)

        assert {node.name for node in graph.nodes} == {"a", "b", "c", "d", "e"}
        assert len(graph.edges) == 4
        assert graph.edges[0].caller == "a"
        assert graph.edges[0].callee == "b"

    def test_replica_one_with_three_dependents_is_flagged_spof(self) -> None:
        services = [
            _service("api-gateway", replicas=3),
            _service("auth-service", replicas=1),
            _service("payment-service", replicas=2),
            _service("checkout-service", replicas=2),
        ]
        edges = [
            _edge("api-gateway", "auth-service"),
            _edge("payment-service", "auth-service"),
            _edge("checkout-service", "auth-service"),
        ]

        graph = self.engine.build_graph(services, edges, InferenceSource.NETWORK_POLICY)

        assert graph.single_points_of_failure == ["auth-service"]

    def test_replica_one_with_no_dependents_is_not_spof(self) -> None:
        services = [_service("standalone-job", replicas=1)]

        graph = self.engine.build_graph(services, [], InferenceSource.NETWORK_POLICY)

        assert graph.single_points_of_failure == []

    def test_isolated_service_with_no_callers_or_callees_is_orphan(self) -> None:
        services = [
            _service("a", replicas=3),
            _service("b", replicas=3),
            _service("isolated", replicas=2),
        ]
        edges = [_edge("a", "b")]

        graph = self.engine.build_graph(services, edges, InferenceSource.NETWORK_POLICY)

        assert graph.orphan_nodes == ["isolated"]

    def test_circular_dependency_is_detected(self) -> None:
        services = [_service("a", replicas=2), _service("b", replicas=2)]
        edges = [_edge("a", "b"), _edge("b", "a")]

        graph = self.engine.build_graph(services, edges, InferenceSource.NETWORK_POLICY)

        assert len(graph.cycles) == 1
        assert set(graph.cycles[0]) == {"a", "b"}

    def test_acyclic_graph_has_no_cycles(self) -> None:
        services = [_service("a", replicas=2), _service("b", replicas=2)]
        edges = [_edge("a", "b")]

        graph = self.engine.build_graph(services, edges, InferenceSource.NETWORK_POLICY)

        assert graph.cycles == []

    def test_external_name_service_is_marked_external(self) -> None:
        services = [
            _service("auth-service", replicas=2),
            _service("stripe-external", replicas=0, is_external=True),
        ]
        edges = [_edge("auth-service", "stripe-external")]

        graph = self.engine.build_graph(services, edges, InferenceSource.NETWORK_POLICY)

        external_node = next(n for n in graph.nodes if n.name == "stripe-external")
        assert external_node.node_type is NodeType.EXTERNAL

    def test_truncates_when_over_200_services_and_no_namespace_scope(self) -> None:
        services = [_service(f"svc-{i}", replicas=2) for i in range(250)]

        graph = self.engine.build_graph(services, [], InferenceSource.NETWORK_POLICY)

        assert graph.truncated is True
        assert len(graph.nodes) == 200

    def test_namespace_scope_prevents_truncation_even_over_200(self) -> None:
        services = [_service(f"svc-{i}", replicas=2) for i in range(250)]

        graph = self.engine.build_graph(
            services, [], InferenceSource.NETWORK_POLICY, namespace_scope="production"
        )

        assert graph.truncated is False
        assert len(graph.nodes) == 250
        assert graph.namespace_scope == "production"

    def test_edge_referencing_deleted_service_is_dropped(self) -> None:
        services = [_service("a", replicas=2)]
        edges = [_edge("a", "deleted-service")]

        graph = self.engine.build_graph(services, edges, InferenceSource.NETWORK_POLICY)

        assert graph.edges == []

    def test_inference_source_is_propagated(self) -> None:
        graph = self.engine.build_graph(
            [_service("a", replicas=2)], [], InferenceSource.ISTIO_VIRTUAL_SERVICE
        )

        assert graph.inference_source is InferenceSource.ISTIO_VIRTUAL_SERVICE
