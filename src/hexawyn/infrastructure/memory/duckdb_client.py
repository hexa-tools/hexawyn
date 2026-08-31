import datetime
import threading
from pathlib import Path
from typing import TypedDict

import duckdb

from hexawyn.domain.errors import DuckDBUnavailableError, EncryptionError
from hexawyn.domain.models.quota import UNLIMITED
from hexawyn.infrastructure.memory.encryption import (
    derive_key,
    is_encryption_disabled,
    prepare_db,
)

SQL_DIR = Path(__file__).parent / "sql"

_DB_SIZE_WARNING_THRESHOLD: int = 1_073_741_824


def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


class SimilarInvestigationDict(TypedDict):
    id: str
    timestamp: str
    age_days: int
    cluster_name: str
    namespace: str | None
    tool_name: str
    resource_name: str | None
    resource_kind: str | None
    cause: str | None
    solution: str | None
    severity: str
    weight: float
    score: float


HEXAWYN_DIR = Path.home() / ".hexawyn"
DB_PATH = HEXAWYN_DIR / "memory.duckdb"

_conn_lock = threading.RLock()
_singleton_conn: duckdb.DuckDBPyConnection | None = None
_singleton_init_done = False


def reset_connection_state() -> None:
    """Drop the cached connection so a fresh one is created (test isolation)."""
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        _singleton_conn = None
        _singleton_init_done = False


def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


_UNLIMITED_HISTORY_DAYS = 36500  # 100 years — effectively no date filter


def search_similar(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def get_db_size_bytes(db_path: Path | None = None) -> int:
    target = db_path if db_path is not None else DB_PATH
    if not target.exists():
        return 0
    return target.stat().st_size


def is_db_over_threshold(
    db_path: Path | None = None,
    threshold_bytes: int | None = None,
) -> bool:
    threshold = threshold_bytes if threshold_bytes is not None else _DB_SIZE_WARNING_THRESHOLD
    return get_db_size_bytes(db_path) > threshold


def purge_expired_incidents(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def purge_older_than(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count
