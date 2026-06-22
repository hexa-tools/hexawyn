from pathlib import Path
from typing import TypedDict

import duckdb

from hexawyn.domain.errors import DuckDBUnavailableError


class SimilarInvestigationDict(TypedDict):
    id: str
    cluster_name: str
    tool_name: str
    cause: str | None
    solution: str | None
    severity: str
    weight: float
    score: float

HEXAWYN_DIR = Path.home() / ".hexawyn"
DB_PATH = HEXAWYN_DIR / "memory.duckdb"

SCHEMA_SQL = """
-- Incidents table: stores all investigations with embeddings
CREATE TABLE IF NOT EXISTS incidents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    age_days INTEGER GENERATED ALWAYS AS (
        DATEDIFF('day', timestamp, now())
    ) VIRTUAL,
    cluster_name VARCHAR NOT NULL,
    tool_name VARCHAR NOT NULL,
    cause TEXT,
    symptoms TEXT[],
    solution TEXT,
    severity VARCHAR DEFAULT 'low',
    feedback INTEGER DEFAULT 0,
    weight FLOAT DEFAULT 1.0,
    embedding DOUBLE[1536],
    retained_until TIMESTAMPTZ DEFAULT now() + INTERVAL '90 days',
    sanitized BOOLEAN DEFAULT false
);

-- Topology snapshots
CREATE TABLE IF NOT EXISTS topology_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    cluster_name VARCHAR NOT NULL,
    snapshot JSON NOT NULL
);

-- Security audits
CREATE TABLE IF NOT EXISTS security_audits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    cluster_name VARCHAR NOT NULL,
    findings JSON NOT NULL,
    severity VARCHAR NOT NULL
);

-- Schema version tracking
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY,
    applied_at TIMESTAMPTZ DEFAULT now(),
    description VARCHAR
);
"""

HNSW_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS idx_incidents_embedding
ON incidents
USING HNSW (embedding)
WITH (metric = 'cosine');
"""


def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.
    Raises DuckDBUnavailableError if anything fails.
    """
    try:
        HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)
        conn = duckdb.connect(str(DB_PATH))

        # Install VSS extension (vector similarity search)
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")

        # Create all tables
        conn.execute(SCHEMA_SQL)

        # Enable HNSW persistence (required for file-backed databases)
        conn.execute("SET hnsw_enable_experimental_persistence = true;")

        # Create HNSW index for cosine similarity search
        conn.execute(HNSW_INDEX_SQL)

        return conn

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
) -> list[SimilarInvestigationDict]:
    """
    VSS search: find similar past investigations using cosine similarity.
    Uses HNSW index for fast approximate nearest neighbor search.
    NEVER uses SELECT * (enforced by hexa_guard.py R8).
    """
    embedding_literal = f"[{','.join(str(x) for x in embedding)}]"
    embedding_dim = len(embedding)

    results = conn.execute(
        f"""
        SELECT
            id,
            cluster_name,
            tool_name,
            cause,
            solution,
            severity,
            weight,
            array_cosine_similarity(embedding, {embedding_literal}::DOUBLE[{embedding_dim}]) * weight AS score
        FROM incidents
        WHERE cluster_name = ?
          AND retained_until > now()
          AND sanitized = false
        ORDER BY score DESC
        LIMIT ?
    """,
        [cluster_name, limit],
    ).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[7] is not None and row[7] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    cluster_name=str(row[1]) if row[1] else "",
                    tool_name=str(row[2]) if row[2] else "",
                    cause=str(row[3]) if row[3] else None,
                    solution=str(row[4]) if row[4] else None,
                    severity=str(row[5]) if row[5] else "low",
                    weight=float(row[6]) if row[6] else 1.0,
                    score=float(row[7]),
                )
            )
    return output
