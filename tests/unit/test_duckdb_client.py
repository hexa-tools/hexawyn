import duckdb
import pytest

from hexawyn.domain.errors import DuckDBUnavailableError
from hexawyn.infrastructure.memory.duckdb_client import (
    get_connection,
    search_similar,
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
            try:
                client_mod.get_connection()
            finally:
                client_mod.DB_PATH = original_db


class TestSearchSimilar:
    def test_returns_empty_list_for_empty_db(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        conn.execute("""
            CREATE TABLE incidents (
                id UUID,
                cluster_name VARCHAR,
                tool_name VARCHAR,
                cause TEXT,
                solution TEXT,
                severity VARCHAR,
                weight FLOAT,
                embedding DOUBLE[3],
                retained_until TIMESTAMPTZ,
                sanitized BOOLEAN
            )
        """)
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
        conn.execute("""
            CREATE TABLE incidents (
                id UUID,
                cluster_name VARCHAR,
                tool_name VARCHAR,
                cause TEXT,
                solution TEXT,
                severity VARCHAR,
                weight FLOAT,
                embedding DOUBLE[3],
                retained_until TIMESTAMPTZ,
                sanitized BOOLEAN
            )
        """)
        conn.execute(
            """
            INSERT INTO incidents VALUES
            (gen_random_uuid(), 'prod', 'describe_pod', 'OOMKill',
             'Increase memory', 'high', 1.0, [1.0, 0.0, 0.0],
             now() + INTERVAL '10 days', false)
        """
        )
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
        conn.execute("""
            CREATE TABLE incidents (
                id UUID,
                cluster_name VARCHAR,
                tool_name VARCHAR,
                cause TEXT,
                solution TEXT,
                severity VARCHAR,
                weight FLOAT,
                embedding DOUBLE[3],
                retained_until TIMESTAMPTZ,
                sanitized BOOLEAN
            )
        """)
        conn.execute(
            """
            INSERT INTO incidents VALUES
            (gen_random_uuid(), 'prod', 'describe_pod', 'OOMKill',
             'Increase memory', 'high', 1.0, [1.0, 0.0, 0.0],
             now() + INTERVAL '10 days', false)
        """
        )
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
        conn.execute("""
            CREATE TABLE incidents (
                id UUID,
                cluster_name VARCHAR,
                tool_name VARCHAR,
                cause TEXT,
                solution TEXT,
                severity VARCHAR,
                weight FLOAT,
                embedding DOUBLE[3],
                retained_until TIMESTAMPTZ,
                sanitized BOOLEAN
            )
        """)
        conn.execute(
            """
            INSERT INTO incidents VALUES
            (gen_random_uuid(), 'prod', 'describe_pod', 'OOMKill',
             'Increase memory', 'high', 1.0, [1.0, 0.0, 0.0],
             now() + INTERVAL '10 days', false)
        """
        )
        results = search_similar(
            conn,
            embedding=[1.0, 0.0, 0.0],
            cluster_name="staging",
            min_score=0.0,
        )
        assert results == []
        conn.close()
