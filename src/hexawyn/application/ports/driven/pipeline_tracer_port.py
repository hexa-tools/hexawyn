from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class PipelineRunRecord(TypedDict):
    name: str
    namespace: str
    status: str
    start_time: str | None
    completion_time: str | None
    pipeline_ref: str


class TaskRunRecord(TypedDict):
    name: str
    namespace: str
    pipeline_run_name: str
    start_time: str | None
    completion_time: str | None
    status: str
    run_after: list[str]
    failure_reason: str


class PipelineTracerPort(ABC):
    @abstractmethod
    def get_pipeline_run(self, namespace: str, name: str) -> PipelineRunRecord:
        """Fetch a single PipelineRun by name and namespace.

        Raises PipelineNotFoundError on 404.
        Raises InsufficientPermissionsError on 403.
        Raises ClusterUnreachableError on other API failures.
        """

    @abstractmethod
    def list_task_runs_for_pipeline(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        """List all TaskRuns associated with a PipelineRun.

        Raises TektonNotInstalledError on 404.
        Raises InsufficientPermissionsError on 403.
        Raises ClusterUnreachableError on other API failures.
        """
