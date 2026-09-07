from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_history_port import (
    PipelineRunHistoryPort,
    PipelineRunSnapshot,
    TaskRunSnapshot,
)


class TestPipelineRunHistoryPort:
    def test_pipeline_run_snapshot_typed_dict(self) -> None:
        snapshot: PipelineRunSnapshot = {
            "name": "run-1",
            "namespace": "ci",
            "pipeline_name": "payment-service",
            "status": "Succeeded",
            "duration_seconds": 120,
            "start_time": "2026-01-01T00:00:00Z",
            "completion_time": "2026-01-01T00:02:00Z",
        }
        assert snapshot["name"] == "run-1"
        assert snapshot["pipeline_name"] == "payment-service"

    def test_task_run_snapshot_typed_dict(self) -> None:
        snapshot: TaskRunSnapshot = {
            "name": "task-1",
            "namespace": "ci",
            "task_name": "build",
            "pipeline_run_name": "run-1",
            "duration_seconds": 60,
        }
        assert snapshot["name"] == "task-1"
        assert snapshot["task_name"] == "build"

    def test_port_is_abstract(self) -> None:
        import inspect

        assert inspect.isabstract(PipelineRunHistoryPort)
        assert hasattr(PipelineRunHistoryPort, "save_pipeline_runs")
        assert hasattr(PipelineRunHistoryPort, "save_task_runs")
