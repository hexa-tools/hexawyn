from unittest.mock import MagicMock, patch

import duckdb
import pytest
from hexawyn.domain.errors import DuckDBUnavailableError
from hexawyn.infrastructure.memory.duckdb_client import (
    search_similar,
)


@pytest.fixture(autouse=True)
def _reset_connection_state() -> None:
    from hexawyn.infrastructure.memory.duckdb_client import reset_connection_state

    reset_connection_state()
    yield
    reset_connection_state()


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
        ({defaults["id"]}, {defaults["timestamp"]}, {defaults["age_days"]},
         '{defaults["cluster_name"]}', {defaults["namespace"]},
         '{defaults["tool_name"]}',
         {defaults["resource_name"]}, {defaults["resource_kind"]},
         '{defaults["cause"]}', '{defaults["solution"]}',
         '{defaults["severity"]}', {defaults["weight"]},
         {defaults["embedding"]},
         {defaults["retained_until"]}, {defaults["sanitized"]})
    """
    )


class TestGetConnection:
    def test_creates_in_memory_db(self):
        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
        assert conn is not None
        conn.close()

    def test_get_connection_uses_machine_bound_key(self, monkeypatch):
        """get_connection() decrypts with a machine-bound key, never kubeconfig."""
        import hexawyn.infrastructure.memory.duckdb_client as client_mod

        fake_conn = MagicMock()
        patched_connect = MagicMock(return_value=fake_conn)

        with patch("hexawyn.infrastructure.memory.duckdb_client.derive_key") as mock_derive:
            with patch("hexawyn.infrastructure.memory.duckdb_client.prepare_db") as mock_prepare:
                with patch(
                    "hexawyn.infrastructure.memory.duckdb_client.duckdb.connect", patched_connect
                ):
                    mock_derive.return_value = b"x" * 32
                    conn = client_mod.get_connection()

        mock_derive.assert_called_once_with()
        mock_prepare.assert_called_once_with(b"x" * 32)
        patched_connect.assert_called_once()
        assert conn is fake_conn

    def test_get_connection_is_a_singleton(self, monkeypatch):
        """Repeated calls share one connection, so no lock conflict can occur."""
        import hexawyn.infrastructure.memory.duckdb_client as client_mod

        fake_conn = MagicMock()
        patched_connect = MagicMock(return_value=fake_conn)

        with patch(
            "hexawyn.infrastructure.memory.duckdb_client.is_encryption_disabled",
            return_value=True,
        ):
            with patch(
                "hexawyn.infrastructure.memory.duckdb_client.duckdb.connect", patched_connect
            ):
                first = client_mod.get_connection()
                second = client_mod.get_connection()

        assert first is fake_conn
        assert second is fake_conn
        patched_connect.assert_called_once()

    def test_get_connection_skips_encryption_when_disabled(self, monkeypatch):
        import hexawyn.infrastructure.memory.duckdb_client as client_mod

        fake_conn = MagicMock()

        with (
            patch(
                "hexawyn.infrastructure.memory.duckdb_client.is_encryption_disabled",
                return_value=True,
            ),
            patch(
                "hexawyn.infrastructure.memory.duckdb_client.duckdb.connect",
                return_value=fake_conn,
            ),
            patch("hexawyn.infrastructure.memory.duckdb_client.derive_key") as mock_derive,
        ):
            client_mod.get_connection()

        mock_derive.assert_not_called()

    def test_get_connection_passes_through_encryption_error(self, monkeypatch):
        import hexawyn.infrastructure.memory.duckdb_client as client_mod
        from hexawyn.domain.errors import EncryptionError

        with (
            patch(
                "hexawyn.infrastructure.memory.duckdb_client.is_encryption_disabled",
                return_value=False,
            ),
            patch(
                "hexawyn.infrastructure.memory.duckdb_client.derive_key",
                side_effect=EncryptionError("boom"),
            ),
        ):
            with pytest.raises(EncryptionError):
                client_mod.get_connection()

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
