from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
    PipelineRunHistoryRepository,
)


def _pipeline_run(  # noqa: PLR0913
    name: str = "run-1",
    namespace: str = "ci",
    pipeline: str = "payment-service",
    status: str = "Succeeded",
    duration: int | None = 120,
    start: str | None = "2026-01-01T00:00:00Z",
    completion: str | None = "2026-01-01T00:02:00Z",
) -> dict[str, object]:
    return {
        "name": name,
        "namespace": namespace,
        "pipeline_name": pipeline,
        "status": status,
        "duration_seconds": duration,
        "start_time": start,
        "completion_time": completion,
    }


def _task_run(
    name: str = "task-1",
    namespace: str = "ci",
    task: str = "build",
    pipeline_run: str = "run-1",
    duration: int | None = 60,
) -> dict[str, object]:
    return {
        "name": name,
        "namespace": namespace,
        "task_name": task,
        "pipeline_run_name": pipeline_run,
        "duration_seconds": duration,
    }


class TestPipelineRunHistoryRepository:
    def test_save_pipeline_runs_executes_upsert(self) -> None:
        conn = MagicMock()
        repo = PipelineRunHistoryRepository(conn=conn)
        run = _pipeline_run()

        repo.save_pipeline_runs([run])  # type: ignore[arg-type]

        assert conn.execute.call_count == 1
        params = conn.execute.call_args.args[1]
        assert params[0] == "run-1"
        assert params[1] == "ci"
        assert params[2] == "payment-service"

    def test_save_pipeline_runs_empty_noop(self) -> None:
        conn = MagicMock()
        repo = PipelineRunHistoryRepository(conn=conn)

        repo.save_pipeline_runs([])

        assert conn.execute.call_count == 0

    def test_save_task_runs_executes_upsert(self) -> None:
        conn = MagicMock()
        repo = PipelineRunHistoryRepository(conn=conn)
        task = _task_run()

        repo.save_task_runs([task])  # type: ignore[arg-type]

        assert conn.execute.call_count == 1
        params = conn.execute.call_args.args[1]
        assert params[0] == "task-1"
        assert params[1] == "ci"
        assert params[2] == "build"
        assert params[3] == "run-1"

    def test_save_task_runs_empty_noop(self) -> None:
        conn = MagicMock()
        repo = PipelineRunHistoryRepository(conn=conn)

        repo.save_task_runs([])

        assert conn.execute.call_count == 0

    def test_storage_failure_is_best_effort(self) -> None:
        conn = MagicMock()
        conn.execute.side_effect = RuntimeError("duckdb down")
        repo = PipelineRunHistoryRepository(conn=conn)
        run = _pipeline_run()

        repo.save_pipeline_runs([run])  # type: ignore[arg-type]

        assert conn.execute.call_count == 1

    def test_task_run_storage_failure_is_best_effort(self) -> None:
        conn = MagicMock()
        conn.execute.side_effect = RuntimeError("duckdb down")
        repo = PipelineRunHistoryRepository(conn=conn)
        task = _task_run()

        repo.save_task_runs([task])  # type: ignore[arg-type]

        assert conn.execute.call_count == 1

    def test_uses_external_conn(self) -> None:
        from hexawyn.infrastructure.memory.pipeline_run_history_repository import (
            SQL_DIR,
        )

        conn = MagicMock()
        repo = PipelineRunHistoryRepository(conn=conn)
        assert repo._conn is conn
        assert SQL_DIR.exists()
