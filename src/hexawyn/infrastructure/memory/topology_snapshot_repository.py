import json
from pathlib import Path

import duckdb

from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
from hexawyn.domain.services.topology.exporter import DependencyGraphExport

SQL_DIR = Path(__file__).parent / "sql"


def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


class TopologySnapshotRepository(TopologySnapshotPort):
    """Persists topology graph snapshots in DuckDB for historical comparison.

    Best-effort: storage failures are swallowed — history persistence must
    never block the caller's topology mapping response.
    """

    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def save_snapshot(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        try:
            self._conn.execute(
                _load_sql("insert_topology_snapshot.sql"),
                [cluster_name, json.dumps(graph_export)],
            )
        except Exception:
            pass
