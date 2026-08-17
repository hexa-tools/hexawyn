from __future__ import annotations

from pathlib import Path

import duckdb

from hexawyn.application.ports.driven.pipeline_run_history_port import (
    PipelineRunHistoryPort,
    PipelineRunSnapshot,
    TaskRunSnapshot,
)

SQL_DIR = Path(__file__).parent / "sql"


def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


class PipelineRunHistoryRepository(PipelineRunHistoryPort):
    """Persists Tekton PipelineRun/TaskRun snapshots to DuckDB.

    Best-effort: storage failures are swallowed — history persistence must
    never block the caller's pipeline response. Records are upserted by name
    so repeated listing does not duplicate history.
    """

    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def save_pipeline_runs(self, runs: list[PipelineRunSnapshot]) -> None:
        if not runs:
            return
        try:
            for run in runs:
                self._conn.execute(
                    _load_sql("insert_tekton_pipeline_run.sql"),
                    [
                        run["name"],
                        run["namespace"],
                        run["pipeline_name"],
                        run["status"],
                        run["duration_seconds"],
                        run["start_time"],
                        run["completion_time"],
                    ],
                )
        except Exception:
            pass

    def save_task_runs(self, task_runs: list[TaskRunSnapshot]) -> None:
        if not task_runs:
            return
        try:
            for task_run in task_runs:
                self._conn.execute(
                    _load_sql("insert_tekton_task_run.sql"),
                    [
                        task_run["name"],
                        task_run["namespace"],
                        task_run["task_name"],
                        task_run["pipeline_run_name"],
                        task_run["duration_seconds"],
                    ],
                )
        except Exception:
            pass
