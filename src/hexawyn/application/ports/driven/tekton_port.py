from abc import ABC, abstractmethod
from typing import TypedDict


class TaskRunInfo(TypedDict):
    name: str
    task_ref: str
    status: str
    start_time: str | None
    duration: str | None
    failing_step: str | None
    failing_step_error: str | None


class TektonPort(ABC):
    """Port for Tekton pipeline operations — read-only CRD access."""

    @abstractmethod
    def list_task_runs(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        """List all TaskRuns for a pipeline.

        Raises PipelineNotFoundError when the pipeline has no TaskRuns.
        Raises ClusterUnreachableError when the Tekton API cannot be reached.
        """
