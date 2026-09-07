from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PipelineRunRecord(TypedDict):
    name: str
    status: str
    duration_seconds: int | None
    start_time: str | None
    completion_time: str | None


class TaskRunRecord(TypedDict):
    name: str
    task_name: str
    pipeline_run_name: str
    duration_seconds: int | None


class PipelineBaselinePort(ABC):
    @abstractmethod
    def list_pipeline_runs(
        self, pipeline_name: str, namespace: str, limit: int
    ) -> list[PipelineRunRecord]:
        """List PipelineRuns filtered by pipeline label."""

    @abstractmethod
    def list_task_runs_for_pipeline(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        """List child TaskRuns for a PipelineRun."""
