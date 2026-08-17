"""Integration tests: Tekton pipeline run history → real DuckDB.

Writes PipelineRun/TaskRun snapshots via PipelineRunHistoryRepository and
verifies the TektonPipelineBaselineAdapter can read them back.
"""

from __future__ import annotations

from pathlib import Path

import duckdb
import pytest

SCHEMA_PATH = (
    Path(__file__).parent.parent.parent / "src/hexawyn/infrastructure/memory/sql/schema.sql"
)


@pytest.fixture
def tekton_conn() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn.execute(schema_sql)
    yield conn
    conn.close()


@pytest.mark.integration
class TestTektonRunHistoryIntegration:
    def test_write_then_read_pipeline_runs(self, tekton_conn: duckdb.DuckDBPyConnection) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_baseline_adapter import (
            TektonPipelineBaselineAdapter,
        )
        from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
            PipelineRunHistoryRepository,
        )

        repo = PipelineRunHistoryRepository(conn=tekton_conn)
        repo.save_pipeline_runs(  # type: ignore[arg-type]
            [
                {
                    "name": "run-1",
                    "namespace": "ci",
                    "pipeline_name": "payment-service",
                    "status": "Succeeded",
                    "duration_seconds": 120,
                    "start_time": "2026-01-01T00:00:00Z",
                    "completion_time": "2026-01-01T00:02:00Z",
                },
                {
                    "name": "run-2",
                    "namespace": "ci",
                    "pipeline_name": "payment-service",
                    "status": "Failed",
                    "duration_seconds": 60,
                    "start_time": "2026-01-02T00:00:00Z",
                    "completion_time": "2026-01-02T00:01:00Z",
                },
            ]
        )

        adapter = TektonPipelineBaselineAdapter()
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr("hexawyn.mcp.server.get_connection", lambda: tekton_conn)
            runs = adapter.list_pipeline_runs("payment-service", "ci", 10)

        assert len(runs) == 2  # noqa: PLR2004
        assert runs[0]["name"] == "run-2"  # most recent first
        assert runs[0]["status"] == "Failed"
        assert runs[1]["duration_seconds"] == 120  # noqa: PLR2004

    def test_upsert_does_not_duplicate(self, tekton_conn: duckdb.DuckDBPyConnection) -> None:
        from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
            PipelineRunHistoryRepository,
        )

        repo = PipelineRunHistoryRepository(conn=tekton_conn)
        run = {
            "name": "run-1",
            "namespace": "ci",
            "pipeline_name": "payment-service",
            "status": "Running",
            "duration_seconds": None,
            "start_time": "2026-01-01T00:00:00Z",
            "completion_time": None,
        }

        repo.save_pipeline_runs([run])  # type: ignore[arg-type]
        repo.save_pipeline_runs([run])  # type: ignore[arg-type]

        count = tekton_conn.execute(
            "SELECT COUNT(*) FROM tekton_pipeline_runs WHERE name = 'run-1'"
        ).fetchone()[0]
        assert count == 1  # noqa: PLR2004

    def test_write_task_runs_and_read_for_pipeline(
        self, tekton_conn: duckdb.DuckDBPyConnection
    ) -> None:
        from hexawyn.adapters.secondary.tekton_pipeline_baseline_adapter import (
            TektonPipelineBaselineAdapter,
        )
        from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
            PipelineRunHistoryRepository,
        )

        repo = PipelineRunHistoryRepository(conn=tekton_conn)
        repo.save_task_runs(  # type: ignore[arg-type]
            [
                {
                    "name": "task-1",
                    "namespace": "ci",
                    "task_name": "build",
                    "pipeline_run_name": "run-1",
                    "duration_seconds": 60,
                },
                {
                    "name": "task-2",
                    "namespace": "ci",
                    "task_name": "test",
                    "pipeline_run_name": "run-1",
                    "duration_seconds": 90,
                },
            ]
        )

        adapter = TektonPipelineBaselineAdapter()
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr("hexawyn.mcp.server.get_connection", lambda: tekton_conn)
            task_runs = adapter.list_task_runs_for_pipeline("ci", "run-1")

        assert len(task_runs) == 2  # noqa: PLR2004
        assert task_runs[0]["task_name"] == "build"
        assert task_runs[1]["duration_seconds"] == 90  # noqa: PLR2004
