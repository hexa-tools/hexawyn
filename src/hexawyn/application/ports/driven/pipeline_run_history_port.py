from abc import ABC, abstractmethod
from typing import TypedDict


class PipelineRunSnapshot(TypedDict):
    name: str
    namespace: str
    pipeline_name: str
    status: str
    duration_seconds: int | None
    start_time: str | None
    completion_time: str | None


class TaskRunSnapshot(TypedDict):
    name: str
    namespace: str
    task_name: str
    pipeline_run_name: str
    duration_seconds: int | None


class PipelineRunHistoryPort(ABC):
    """Persists Tekton PipelineRun/TaskRun snapshots to DuckDB for baseline analysis.

    Best-effort: implementations must not raise on storage failure — history
    persistence must never block the caller's pipeline response.
    """

    @abstractmethod
    def save_pipeline_runs(self, runs: list[PipelineRunSnapshot]) -> None:
        """Persist a batch of PipelineRun snapshots (upsert by name)."""

    @abstractmethod
    def save_task_runs(self, task_runs: list[TaskRunSnapshot]) -> None:
        """Persist a batch of TaskRun snapshots (upsert by name)."""
