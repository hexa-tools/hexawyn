from __future__ import annotations

from hexawyn.domain.models.service_dependency_graph import (
    DependencyGraph,
    DependencyGraphRequest,
    ServiceEdge,
    ServiceNode,
)


class TestServiceNode:
    def test_create(self) -> None:
        node = ServiceNode(service_name="api-gateway")
        assert node.service_name == "api-gateway"


class TestServiceEdge:
    def test_create(self) -> None:
        edge = ServiceEdge(
            source="api-gateway",
            target="auth-service",
            call_count=12450,
            avg_latency_ms=82.0,
            error_rate=0.02,
        )
        assert edge.source == "api-gateway"
        assert edge.call_count == 12450
        assert edge.error_rate == 0.02


class TestDependencyGraph:
    def test_build_from_spans(self) -> None:
        raw = [
            {
                "from": "api-gateway",
                "to": "auth-service",
                "count": 12450,
                "avg_ms": 82.0,
                "errors": 249,
            },
            {
                "from": "api-gateway",
                "to": "auth-service",
                "count": 300,
                "avg_ms": 90.0,
                "errors": 0,
            },
            {
                "from": "payment-service",
                "to": "postgres-db",
                "count": 24600,
                "avg_ms": 35.0,
                "errors": 0,
            },
        ]
        graph = DependencyGraph.compute(
            request=DependencyGraphRequest(time_window_minutes=60),
            raw_edges=raw,
        )
        assert len(graph.nodes) == 4
        assert len(graph.edges) == 2
        edge_ag = [e for e in graph.edges if e.source == "api-gateway"][0]
        assert edge_ag.call_count == 12750

    def test_no_edges(self) -> None:
        graph = DependencyGraph.compute(
            request=DependencyGraphRequest(),
            raw_edges=[],
        )
        assert graph.nodes == []
        assert graph.edges == []
