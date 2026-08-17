"""Integration tests: TopologySnapshotRepository → real DuckDB — save, retrieve, edge cases."""

from __future__ import annotations

import json
from pathlib import Path

import duckdb
import pytest
from hexawyn.domain.services.topology.exporter import (
    DependencyEdgeExport,
    DependencyGraphExport,
    ServiceNodeExport,
)
from hexawyn.infrastructure.memory.topology_snapshot_repository import (
    TopologySnapshotRepository,
)

SCHEMA_PATH = (
    Path(__file__).parent.parent.parent / "src/hexawyn/infrastructure/memory/sql/schema.sql"
)


@pytest.fixture
def topo_conn() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn.execute(schema_sql)
    yield conn
    conn.close()


@pytest.fixture
def topo_repo(
    topo_conn: duckdb.DuckDBPyConnection,
) -> TopologySnapshotRepository:
    return TopologySnapshotRepository(conn=topo_conn)


def _make_node(
    name: str = "payments-api",
    namespace: str = "payments",
    replicas: int = 3,
    node_type: str = "Deployment",
    is_spof: bool = False,
) -> ServiceNodeExport:
    return ServiceNodeExport(
        name=name,
        namespace=namespace,
        replicas=replicas,
        type=node_type,
        is_spof=is_spof,
    )


def _make_edge(
    caller: str = "checkout",
    callee: str = "payments-api",
) -> DependencyEdgeExport:
    return DependencyEdgeExport(caller=caller, callee=callee)


def _make_graph(  # noqa: PLR0913
    nodes: list[ServiceNodeExport] | None = None,
    edges: list[DependencyEdgeExport] | None = None,
    spofs: list[str] | None = None,
    orphans: list[str] | None = None,
    cycles: list[list[str]] | None = None,
    source: str = "istio-sidecar",
    truncated: bool = False,
    namespace_scope: str | None = None,
) -> DependencyGraphExport:
    return DependencyGraphExport(
        nodes=nodes if nodes is not None else [_make_node()],
        edges=edges if edges is not None else [_make_edge()],
        single_points_of_failure=spofs if spofs is not None else [],
        orphan_nodes=orphans if orphans is not None else [],
        cycles=cycles if cycles is not None else [],
        inference_source=source,
        truncated=truncated,
        namespace_scope=namespace_scope,
    )


@pytest.mark.integration
class TestTopologySnapshotIntegration:
    def test_save_and_verify_stored(
        self, topo_repo: TopologySnapshotRepository, topo_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        graph = _make_graph()
        topo_repo.save_snapshot("prod-eu", graph)

        row = topo_conn.execute(
            "SELECT cluster_name, snapshot FROM topology_snapshots ORDER BY timestamp DESC LIMIT 1"  # noqa: E501
        ).fetchone()

        assert row is not None
        assert row[0] == "prod-eu"
        parsed = json.loads(row[1])
        assert len(parsed["nodes"]) == 1  # noqa: PLR2004
        assert parsed["nodes"][0]["name"] == "payments-api"

    def test_two_saves_same_cluster_both_persisted(
        self, topo_repo: TopologySnapshotRepository, topo_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        topo_repo.save_snapshot("prod-eu", _make_graph(nodes=[_make_node(name="v1")]))
        topo_repo.save_snapshot("prod-eu", _make_graph(nodes=[_make_node(name="v2")]))

        count = topo_conn.execute(
            "SELECT COUNT(*) FROM topology_snapshots WHERE cluster_name = 'prod-eu'"
        ).fetchone()[0]

        assert count == 2  # noqa: PLR2004

    def test_latest_snapshot_is_most_recent(
        self, topo_repo: TopologySnapshotRepository, topo_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        topo_repo.save_snapshot("prod-eu", _make_graph(nodes=[_make_node(name="old-deploy")]))
        topo_repo.save_snapshot("prod-eu", _make_graph(nodes=[_make_node(name="new-deploy")]))

        row = topo_conn.execute(
            "SELECT snapshot FROM topology_snapshots WHERE cluster_name = 'prod-eu' ORDER BY timestamp DESC LIMIT 1"  # noqa: E501
        ).fetchone()

        parsed = json.loads(row[0])
        assert parsed["nodes"][0]["name"] == "new-deploy"

    def test_empty_graph_persisted(
        self, topo_repo: TopologySnapshotRepository, topo_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        empty = _make_graph(nodes=[], edges=[])
        topo_repo.save_snapshot("empty-cluster", empty)

        row = topo_conn.execute(
            "SELECT snapshot FROM topology_snapshots WHERE cluster_name = 'empty-cluster'"
        ).fetchone()

        parsed = json.loads(row[0])
        assert parsed["nodes"] == []
        assert parsed["edges"] == []
        assert parsed["truncated"] is False

    def test_spof_and_orphan_fields_roundtrip(
        self, topo_repo: TopologySnapshotRepository, topo_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        graph = _make_graph(
            spofs=["payment-gateway", "auth-service"],
            orphans=["old-batch-job"],
            cycles=[["a", "b", "a"]],
            truncated=True,
        )
        topo_repo.save_snapshot("prod-eu", graph)

        row = topo_conn.execute(
            "SELECT snapshot FROM topology_snapshots WHERE cluster_name = 'prod-eu'"
        ).fetchone()

        parsed = json.loads(row[0])
        assert "payment-gateway" in parsed["single_points_of_failure"]
        assert "old-batch-job" in parsed["orphan_nodes"]
        assert ["a", "b", "a"] in parsed["cycles"]
        assert parsed["truncated"] is True

    def test_cluster_isolation(
        self, topo_repo: TopologySnapshotRepository, topo_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        topo_repo.save_snapshot("prod-eu", _make_graph(nodes=[_make_node(name="eu-only")]))
        topo_repo.save_snapshot("prod-us", _make_graph(nodes=[_make_node(name="us-only")]))

        eu_nodes = topo_conn.execute(
            "SELECT snapshot FROM topology_snapshots WHERE cluster_name = 'prod-eu'"
        ).fetchall()
        us_nodes = topo_conn.execute(
            "SELECT snapshot FROM topology_snapshots WHERE cluster_name = 'prod-us'"
        ).fetchall()

        eu_parsed = json.loads(eu_nodes[0][0])
        us_parsed = json.loads(us_nodes[0][0])
        assert eu_parsed["nodes"][0]["name"] == "eu-only"
        assert us_parsed["nodes"][0]["name"] == "us-only"

    def test_best_effort_does_not_raise_on_failure(
        self, topo_repo: TopologySnapshotRepository
    ) -> None:  # noqa: E501
        graph = _make_graph()
        topo_repo.save_snapshot("production", graph)

    def test_large_graph_roundtrip(
        self, topo_repo: TopologySnapshotRepository, topo_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        large_nodes = [_make_node(name=f"service-{i}") for i in range(50)]
        large_edges = [_make_edge(caller=f"svc-{i}", callee=f"svc-{i+1}") for i in range(49)]
        graph = _make_graph(nodes=large_nodes, edges=large_edges)
        topo_repo.save_snapshot("large-cluster", graph)

        row = topo_conn.execute(
            "SELECT snapshot FROM topology_snapshots WHERE cluster_name = 'large-cluster'"
        ).fetchone()

        parsed = json.loads(row[0])
        assert len(parsed["nodes"]) == 50  # noqa: PLR2004
        assert len(parsed["edges"]) == 49  # noqa: PLR2004

    def test_multiple_clusters_multiple_snapshots(
        self, topo_repo: TopologySnapshotRepository, topo_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        for cluster in ("prod-eu", "prod-us", "staging"):
            for i in range(3):
                topo_repo.save_snapshot(
                    cluster, _make_graph(nodes=[_make_node(name=f"{cluster}-v{i}")])
                )

        counts = topo_conn.execute(
            "SELECT cluster_name, COUNT(*) FROM topology_snapshots GROUP BY cluster_name"
        ).fetchall()

        assert len(counts) == 3  # noqa: PLR2004
        for _cluster, count in counts:
            assert count == 3  # noqa: PLR2004
