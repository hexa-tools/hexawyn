import duckdb
import pytest
from hexawyn.domain.errors import DuckDBUnavailableError
from hexawyn.infrastructure.memory.duckdb_client import (
    search_similar,
)

INCIDENTS_DDL = """
    CREATE TABLE incidents (
        id UUID,
        timestamp TIMESTAMP,
        age_days INTEGER,
        cluster_name VARCHAR,
        namespace VARCHAR,
        tool_name VARCHAR,
        resource_name VARCHAR,
        resource_kind VARCHAR,
        cause TEXT,
        solution TEXT,
        severity VARCHAR,
        weight FLOAT,
        embedding FLOAT[3],
        retained_until TIMESTAMPTZ,
        sanitized BOOLEAN
    )
"""


def _insert_row(conn, **kwargs):
    defaults = {
        "id": "gen_random_uuid()",
        "timestamp": "now()",
        "age_days": 0,
        "cluster_name": "prod",
        "namespace": "NULL",
        "tool_name": "describe_pod",
        "resource_name": "NULL",
        "resource_kind": "NULL",
        "cause": "OOMKill",
        "solution": "Increase memory",
        "severity": "high",
        "weight": 1.0,
        "embedding": "[1.0, 0.0, 0.0]",
        "retained_until": "now() + INTERVAL '10 days'",
        "sanitized": "false",
    }
    defaults.update(kwargs)
    conn.execute(
        f"""
        INSERT INTO incidents VALUES
        ({defaults['id']}, {defaults['timestamp']}, {defaults['age_days']},
         '{defaults['cluster_name']}', {defaults['namespace']},
         '{defaults['tool_name']}',
         {defaults['resource_name']}, {defaults['resource_kind']},
         '{defaults['cause']}', '{defaults['solution']}',
         '{defaults['severity']}', {defaults['weight']},
         {defaults['embedding']},
         {defaults['retained_until']}, {defaults['sanitized']})
    """
    )


class TestGetConnection:
    def test_creates_in_memory_db(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        assert conn is not None
        conn.close()

    def test_raises_duckdb_unavailable_on_failure(self, tmp_path):
        bad_path = tmp_path / "readonly" / "db.duckdb"
        bad_path.parent.mkdir(mode=0o444)

        with pytest.raises(DuckDBUnavailableError):
            import hexawyn.infrastructure.memory.duckdb_client as client_mod

            original_db = client_mod.DB_PATH
            client_mod.DB_PATH = bad_path
            import os

            try:
                os.environ["HEXAWYN_DISABLE_ENCRYPTION"] = "true"
                client_mod.get_connection()
            finally:
                client_mod.DB_PATH = original_db
                del os.environ["HEXAWYN_DISABLE_ENCRYPTION"]


class TestSearchSimilar:
    def test_returns_empty_list_for_empty_db(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        conn.execute(INCIDENTS_DDL)
        results = search_similar(
            conn,
            embedding=[1.0, 0.0, 0.0],
            cluster_name="prod",
        )
        assert results == []
        conn.close()

    def test_finds_similar_embedding(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn)
        results = search_similar(
            conn,
            embedding=[0.99, 0.01, 0.0],
            cluster_name="prod",
            min_score=0.0,
        )
        assert len(results) >= 1
        assert results[0]["cluster_name"] == "prod"
        assert results[0]["tool_name"] == "describe_pod"
        conn.close()

    def test_respects_min_score(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn)
        results = search_similar(
            conn,
            embedding=[0.1, 0.9, 0.0],
            cluster_name="prod",
            min_score=0.95,
        )
        assert results == []
        conn.close()

    def test_filters_by_cluster_name(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn)
        results = search_similar(
            conn,
            embedding=[1.0, 0.0, 0.0],
            cluster_name="staging",
            min_score=0.0,
        )
        assert results == []
        conn.close()

    def test_filters_by_namespace(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        conn.execute(INCIDENTS_DDL)
        _insert_row(
            conn, cluster_name="prod", namespace="'payments'", resource_name="'payment-api'"
        )
        _insert_row(conn, cluster_name="prod", namespace="'web'", resource_name="'nginx'")
        results = search_similar(
            conn,
            embedding=[1.0, 0.0, 0.0],
            cluster_name="prod",
            namespace="payments",
            min_score=0.0,
        )
        assert len(results) == 1
        assert results[0]["namespace"] == "payments"
        conn.close()

    def test_filters_by_resource_name(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn, cluster_name="prod", resource_name="'payment-api'")
        _insert_row(conn, cluster_name="prod", resource_name="'auth-svc'")
        results = search_similar(
            conn,
            embedding=[1.0, 0.0, 0.0],
            cluster_name="prod",
            resource_name="auth-svc",
            min_score=0.0,
        )
        assert len(results) == 1
        assert results[0]["resource_name"] == "auth-svc"
        conn.close()

    def test_has_resource_fields_in_result(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        conn.execute(INCIDENTS_DDL)
        _insert_row(
            conn,
            cluster_name="prod",
            namespace="'payments'",
            resource_name="'payment-api-7d9f8b-m3ql'",
            resource_kind="'Pod'",
        )
        results = search_similar(
            conn,
            embedding=[1.0, 0.0, 0.0],
            cluster_name="prod",
            min_score=0.0,
        )
        assert len(results) >= 1
        assert results[0]["namespace"] == "payments"
        assert results[0]["resource_name"] == "payment-api-7d9f8b-m3ql"
        assert results[0]["resource_kind"] == "Pod"
        conn.close()
