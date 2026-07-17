import datetime
from pathlib import Path

import duckdb
from hexawyn.infrastructure.memory.duckdb_client import (
    _DB_SIZE_WARNING_THRESHOLD,
    get_db_size_bytes,
    is_db_over_threshold,
    purge_expired_incidents,
    purge_older_than,
)

INCIDENTS_DDL = """
    CREATE TABLE incidents (
        id UUID DEFAULT gen_random_uuid(),
        timestamp TIMESTAMPTZ DEFAULT now(),
        retained_until TIMESTAMPTZ NOT NULL DEFAULT now() + INTERVAL '90 days',
        age_days INTEGER DEFAULT 0,
        cluster_name VARCHAR DEFAULT 'test',
        namespace VARCHAR,
        resource_name VARCHAR,
        resource_kind VARCHAR,
        tool_name VARCHAR DEFAULT 'test',
        cause TEXT,
        symptoms TEXT[],
        solution TEXT,
        severity VARCHAR DEFAULT 'low',
        feedback INTEGER DEFAULT 0,
        weight FLOAT DEFAULT 1.0,
        embedding FLOAT[3],
        sanitized BOOLEAN DEFAULT false
    )
"""


def _insert_row(
    conn: duckdb.DuckDBPyConnection,
    *,
    timestamp: str = "now()",
    retained_until: str = "now() + INTERVAL '90 days'",
    cluster_name: str = "test-cluster",
    tool_name: str = "describe_pod",
    cause: str = "OOMKill",
) -> None:
    conn.execute(
        f"""
        INSERT INTO incidents (timestamp, retained_until, cluster_name, tool_name, cause, embedding)
        VALUES ({timestamp}, {retained_until}, '{cluster_name}', '{tool_name}', '{cause}', [1.0, 0.0, 0.0])
    """
    )


class TestDBFileSize:
    def test_returns_zero_when_file_does_not_exist(self, tmp_path: Path) -> None:
        nonexistent = tmp_path / "nonexistent.duckdb"
        size = get_db_size_bytes(nonexistent)
        assert size == 0

    def test_returns_positive_bytes_for_existing_file(self, tmp_path: Path) -> None:
        db_file = tmp_path / "test.duckdb"
        conn = duckdb.connect(str(db_file))
        conn.execute("CREATE TABLE t (x INTEGER)")
        conn.execute("INSERT INTO t VALUES (42)")
        conn.close()
        size = get_db_size_bytes(db_file)
        assert size > 0

    def test_is_db_over_threshold_false_for_small_file(self, tmp_path: Path) -> None:
        db_file = tmp_path / "small.duckdb"
        conn = duckdb.connect(str(db_file))
        conn.execute("CREATE TABLE t (x INTEGER)")
        conn.close()
        assert is_db_over_threshold(db_file) is False

    def test_is_db_over_threshold_true_when_exceeds(self, tmp_path: Path) -> None:
        db_file = tmp_path / "big.duckdb"
        conn = duckdb.connect(str(db_file))
        conn.execute("CREATE TABLE t (x INTEGER)")
        conn.close()
        assert is_db_over_threshold(db_file, threshold_bytes=0) is True

    def test_is_db_over_threshold_false_when_file_missing(self, tmp_path: Path) -> None:
        nonexistent = tmp_path / "ghost.duckdb"
        assert is_db_over_threshold(nonexistent) is False

    def test_default_threshold_is_1_gb(self) -> None:
        assert _DB_SIZE_WARNING_THRESHOLD == 1_073_741_824


class TestPurgeExpired:
    def test_deletes_rows_past_retained_until(self) -> None:
        conn = duckdb.connect(":memory:")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn, retained_until="now() - INTERVAL '1 day'")
        _insert_row(conn, retained_until="now() + INTERVAL '90 days'")

        deleted = purge_expired_incidents(conn)
        assert deleted == 1

        count = conn.execute("SELECT COUNT(*) FROM incidents").fetchone()
        assert count is not None
        assert count[0] == 1
        conn.close()

    def test_deletes_nothing_when_all_fresh(self) -> None:
        conn = duckdb.connect(":memory:")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn)
        _insert_row(conn)

        deleted = purge_expired_incidents(conn)
        assert deleted == 0

        count = conn.execute("SELECT COUNT(*) FROM incidents").fetchone()
        assert count is not None
        assert count[0] == 2
        conn.close()

    def test_returns_zero_for_empty_table(self) -> None:
        conn = duckdb.connect(":memory:")
        conn.execute(INCIDENTS_DDL)
        deleted = purge_expired_incidents(conn)
        assert deleted == 0
        conn.close()


class TestPurgeOlderThan:
    def test_deletes_rows_older_than_n_days(self) -> None:
        conn = duckdb.connect(":memory:")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn, timestamp="now() - INTERVAL '31 days'")
        _insert_row(conn, timestamp="now() - INTERVAL '1 day'")

        deleted = purge_older_than(conn, days=30)
        assert deleted == 1

        count = conn.execute("SELECT COUNT(*) FROM incidents").fetchone()
        assert count is not None
        assert count[0] == 1
        conn.close()

    def test_deletes_nothing_when_all_recent(self) -> None:
        conn = duckdb.connect(":memory:")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn)

        deleted = purge_older_than(conn, days=30)
        assert deleted == 0
        conn.close()

    def test_deletes_all_when_days_is_zero(self) -> None:
        conn = duckdb.connect(":memory:")
        conn.execute(INCIDENTS_DDL)
        _insert_row(conn, timestamp="now() - INTERVAL '1 day'")
        _insert_row(conn, timestamp="now() - INTERVAL '2 days'")

        cutoff = datetime.datetime.now(datetime.UTC)
        deleted = purge_older_than(conn, days=0, cutoff=cutoff)
        assert deleted == 2
        conn.close()
