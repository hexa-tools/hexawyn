from pathlib import Path
from typing import TypedDict

import duckdb

from hexawyn.domain.errors import DuckDBUnavailableError, EncryptionError
from hexawyn.domain.models.quota import FREE_HISTORY_DAYS
from hexawyn.infrastructure.config.kubeconfig_reader import get_kubeconfig_stable_content
from hexawyn.infrastructure.memory.encryption import (
    derive_key,
    is_encryption_disabled,
    prepare_db,
)

SQL_DIR = Path(__file__).parent / "sql"


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


def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the kubeconfig's stable parts (CA certificates + server URLs)
    using PBKDF2-HMAC-SHA256 with 600k iterations.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    try:
        HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

        if not is_encryption_disabled():
            kubeconfig_content = get_kubeconfig_stable_content()
            if kubeconfig_content is not None:
                key = derive_key(kubeconfig_content)
                prepare_db(key)

        conn = duckdb.connect(str(DB_PATH))

        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")

        conn.execute(_load_sql("schema.sql"))

        conn.execute("SET hnsw_enable_experimental_persistence = true;")

        conn.execute(_load_sql("indexes.sql"))

        return conn

    except EncryptionError:
        raise
    except Exception as e:
        raise DuckDBUnavailableError(
            f"Failed to initialize DuckDB at {DB_PATH}: {e}",
            context={"path": str(DB_PATH), "error": str(e)},
        ) from e


def search_similar(
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    limit: int = 5,
    min_score: float = 0.80,
    history_days: int = FREE_HISTORY_DAYS,
    namespace: str | None = None,
    resource_name: str | None = None,
) -> list[SimilarInvestigationDict]:
    """
    VSS search: find similar past investigations using cosine similarity
    weighted by recency (recent investigations score higher).
    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    embedding_dim = len(embedding)
    sql = (
        _load_sql("search_similar.sql")
        .replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")
        .replace("<HISTORY_DAYS>", str(history_days))
    )

    params: list[str | int | float | list[float] | None] = [embedding, cluster_name]

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
