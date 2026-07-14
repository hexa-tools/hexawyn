from pathlib import Path

import duckdb

from hexawyn.application.ports.driven.incident_memory_port import IncidentMemoryPort
from hexawyn.domain.models.incident_memory import IncidentMemoryRecord

SQL_DIR = Path(__file__).parent / "sql"


def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


class IncidentMemoryRepository(IncidentMemoryPort):
    """Persists completed investigations in DuckDB for similarity retrieval.

    Best-effort: storage failures are swallowed — memory persistence must
    never block the caller's investigation response. Records without an
    embedding (or missing cluster/tool) are skipped, since they cannot be
    retrieved by the VSS search path.
    """

    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def store_incident(self, record: IncidentMemoryRecord) -> None:
        if not record.is_storable:
            return
        try:
            self._conn.execute(
                _load_sql("insert_incident.sql"),
                [
                    record.cluster_name,
                    record.namespace,
                    record.resource_name,
                    record.resource_kind,
                    record.tool_name,
                    record.cause,
                    record.symptoms,
                    record.solution,
                    record.severity,
                    record.embedding,
                    record.sanitized,
                ],
            )
        except Exception:
            pass
