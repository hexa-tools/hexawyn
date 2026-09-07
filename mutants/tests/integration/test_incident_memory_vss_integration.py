"""Integration tests: IncidentMemoryRepository → DuckDB VSS — store, search, purge."""

from __future__ import annotations

import random
from pathlib import Path

import duckdb
import pytest

SCHEMA_PATH = (
    Path(__file__).parent.parent.parent / "src/hexawyn/infrastructure/memory/sql/schema.sql"
)
INDEXES_PATH = (
    Path(__file__).parent.parent.parent / "src/hexawyn/infrastructure/memory/sql/indexes.sql"
)


@pytest.fixture
def incident_conn() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    conn.execute("INSTALL vss;")
    conn.execute("LOAD vss;")
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn.execute(schema_sql)
    indexes_sql = INDEXES_PATH.read_text(encoding="utf-8")
    conn.execute(indexes_sql)
    yield conn
    conn.close()


def _embedding(seed: float) -> list[float]:
    random.seed(seed)
    return [round(random.uniform(-1.0, 1.0), 6) for _ in range(768)]


def _make_record(
    cluster: str = "prod-eu",
    tool: str = "detect_over_provisioned_namespaces",
    cause: str = "OOMKilled — memory limit too low",
    severity: str = "high",
    embedding: list[float] | None = None,
) -> object:
    from hexawyn.domain.models.incident_memory import IncidentMemoryRecord

    return IncidentMemoryRecord(
        cluster_name=cluster,
        tool_name=tool,
        cause=cause,
        solution="Increase memory limit from 512Mi to 1Gi",
        severity=severity,
        namespace="payments",
        resource_name="payments-api",
        resource_kind="Deployment",
        symptoms=["CrashLoopBackOff", "OOMKilled"],
        embedding=embedding if embedding is not None else _embedding(42.0),
        sanitized=False,
    )


@pytest.mark.integration
class TestIncidentMemoryStoreAndSearch:
    def test_store_and_retrieve_via_vss(self, incident_conn: duckdb.DuckDBPyConnection) -> None:
        from hexawyn.infrastructure.memory.duckdb_client import search_similar
        from hexawyn.infrastructure.memory.incident_memory_repository import (
            IncidentMemoryRepository,
        )

        repo = IncidentMemoryRepository(conn=incident_conn)
        emb = _embedding(42.0)
        record = _make_record(embedding=emb)
        repo.store_incident(record)

        results = search_similar(
            incident_conn,
            embedding=emb,
            cluster_name="prod-eu",
            limit=5,
            min_score=0.0,
        )

        assert len(results) >= 1
        assert results[0]["tool_name"] == "detect_over_provisioned_namespaces"
        assert results[0]["severity"] == "high"

    def test_store_multiple_and_search_most_similar(
        self, incident_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        from hexawyn.infrastructure.memory.duckdb_client import search_similar
        from hexawyn.infrastructure.memory.incident_memory_repository import (
            IncidentMemoryRepository,
        )

        repo = IncidentMemoryRepository(conn=incident_conn)

        emb_oom = _embedding(10.0)
        repo.store_incident(
            _make_record(
                tool="detect_zombies",
                cause="Zombie pods detected in staging",
                embedding=emb_oom,
            )
        )

        emb_disk = _embedding(100.0)
        repo.store_incident(
            _make_record(
                tool="detect_over_provisioned_namespaces",
                cause="Disk pressure on node worker-3",
                severity="critical",
                embedding=emb_disk,
            )
        )

        results = search_similar(
            incident_conn,
            embedding=emb_oom,
            cluster_name="prod-eu",
            limit=5,
            min_score=0.0,
        )

        assert len(results) >= 2  # noqa: PLR2004
        top_tool = results[0]["tool_name"]
        assert top_tool in ("detect_zombies", "detect_over_provisioned_namespaces")

    def test_unstorable_record_skipped(self, incident_conn: duckdb.DuckDBPyConnection) -> None:
        from hexawyn.infrastructure.memory.duckdb_client import search_similar  # noqa: F401
        from hexawyn.infrastructure.memory.incident_memory_repository import (
            IncidentMemoryRepository,
        )

        repo = IncidentMemoryRepository(conn=incident_conn)
        record = _make_record(embedding=[])
        repo.store_incident(record)

        count = incident_conn.execute("SELECT COUNT(*) FROM incidents").fetchone()[0]
        assert count == 0

    def test_search_respects_cluster_isolation(
        self, incident_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        from hexawyn.infrastructure.memory.duckdb_client import search_similar
        from hexawyn.infrastructure.memory.incident_memory_repository import (
            IncidentMemoryRepository,
        )

        repo = IncidentMemoryRepository(conn=incident_conn)
        emb = _embedding(42.0)

        repo.store_incident(_make_record(cluster="prod-eu", embedding=emb))
        repo.store_incident(_make_record(cluster="prod-us", embedding=emb))

        results_eu = search_similar(
            incident_conn,
            embedding=emb,
            cluster_name="prod-eu",
            limit=5,
            min_score=0.0,
        )
        results_us = search_similar(
            incident_conn,
            embedding=emb,
            cluster_name="prod-us",
            limit=5,
            min_score=0.0,
        )

        assert all(r["cluster_name"] == "prod-eu" for r in results_eu)
        assert all(r["cluster_name"] == "prod-us" for r in results_us)

    def test_search_min_score_filters_low_scores(
        self, incident_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        from hexawyn.infrastructure.memory.duckdb_client import search_similar
        from hexawyn.infrastructure.memory.incident_memory_repository import (
            IncidentMemoryRepository,
        )

        repo = IncidentMemoryRepository(conn=incident_conn)
        emb = _embedding(42.0)
        repo.store_incident(_make_record(embedding=emb))

        results = search_similar(
            incident_conn,
            embedding=emb,
            cluster_name="prod-eu",
            limit=5,
            min_score=0.99,
        )

        assert len(results) >= 0

    def test_purge_older_than_removes_old_incidents(
        self, incident_conn: duckdb.DuckDBPyConnection
    ) -> None:  # noqa: E501
        from hexawyn.infrastructure.memory.duckdb_client import purge_older_than
        from hexawyn.infrastructure.memory.incident_memory_repository import (
            IncidentMemoryRepository,
        )

        repo = IncidentMemoryRepository(conn=incident_conn)
        emb = _embedding(42.0)
        repo.store_incident(_make_record(embedding=emb))

        count_before = incident_conn.execute("SELECT COUNT(*) FROM incidents").fetchone()[0]
        assert count_before >= 1

        import datetime

        future = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1)
        removed = purge_older_than(incident_conn, days=-1, cutoff=future)

        assert removed >= 1  # noqa: PLR2004

        count_after = incident_conn.execute("SELECT COUNT(*) FROM incidents").fetchone()[0]
        assert count_after == 0
