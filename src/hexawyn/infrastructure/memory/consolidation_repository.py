"""DuckDB adapter for memory consolidation."""

from pathlib import Path
from typing import Any

import duckdb

from hexawyn.application.ports.driven.consolidation_port import (
    ConsolidationConfig,
    ConsolidationPort,
)

SQL_DIR = Path(__file__).parent / "sql"


def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


class DuckDBConsolidationRepository(ConsolidationPort):
    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def find_incident_groups(
        self, config: ConsolidationConfig, cluster_name: str
    ) -> list[tuple[str, str, str, int]]:
        rows = self._conn.execute(
            _load_sql("find_groups.sql"),
            [cluster_name, config["max_age_days"], config["min_occurrences"]],
        ).fetchall()
        return [(str(r[0] or ""), str(r[1] or ""), str(r[2] or ""), int(r[3])) for r in rows]

    def get_incidents_for_group(  # noqa: PLR0913
        self,
        namespace: str,
        resource_name: str,
        tool_name: str,
        cluster_name: str,
        max_age_days: int,
    ) -> list[str]:
        rows = self._conn.execute(
            _load_sql("get_group_incidents.sql"),
            [namespace, resource_name, tool_name, cluster_name, max_age_days],
        ).fetchall()
        return [str(r[0]) for r in rows]

    def store_knowledge(  # noqa: PLR0913
        self,
        id: str,
        pattern: str,
        tool_name: str,
        cluster_name: str,
        occurrence_count: int,
        resource_name: str | None = None,
        resource_kind: str | None = None,
        namespace: str | None = None,
        first_seen: str = "",
        last_seen: str = "",
        source_incident_ids: list[str] | None = None,
        embedding: list[float] | None = None,
        weight: float = 1.0,
        confidence: float = 0.5,
    ) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_consolidated.sql"),
                [
                    id,
                    pattern,
                    resource_name,
                    resource_kind,
                    namespace,
                    tool_name,
                    cluster_name,
                    occurrence_count,
                    first_seen,
                    last_seen,
                    source_incident_ids or [],
                    embedding or [],
                    weight,
                    confidence,
                ],
            )
        except Exception:
            pass

    def mark_consolidated(self, incident_ids: list[str], knowledge_id: str) -> None:
        self._conn.execute(
            _load_sql("mark_consolidated.sql"),
            [knowledge_id, incident_ids],
        )

    def search_consolidated(
        self, embedding: list[float], cluster_name: str, limit: int
    ) -> list[dict[str, object]]:
        rows = self._conn.execute(
            _load_sql("search_consolidated.sql"),
            [embedding, cluster_name, limit],
        ).fetchall()
        return _parse_consolidated_rows(rows)


def _parse_consolidated_rows(
    rows: list[Any],
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for r in rows:
        results.append(
            {
                "id": str(r[0]),
                "pattern": str(r[1]),
                "resource_name": str(r[2]) if r[2] else None,
                "resource_kind": str(r[3]) if r[3] else None,
                "namespace": str(r[4]) if r[4] else None,
                "tool_name": str(r[5]),
                "occurrence_count": int(r[6]),
                "first_seen": str(r[7]),
                "last_seen": str(r[8]),
                "weight": float(r[9]),
                "confidence": float(r[10]),
            }
        )
    return results
