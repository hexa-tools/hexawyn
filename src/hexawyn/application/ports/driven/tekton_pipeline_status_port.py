from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class PipelineRunRecord(TypedDict):
    name: str
    status: str
    start_time: str | None
    duration_seconds: int | None
    failure_reason: str | None
    pipeline_ref: str


class TektonPipelineStatusPort(ABC):
    """Outbound port — fetches raw PipelineRun data from a Tekton-enabled cluster."""

    @abstractmethod
    def list_pipeline_runs(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        """Return all PipelineRuns in *namespace*.

        Raises InsufficientPermissionsError on RBAC 403.
        Raises ComponentNotInstalledError when Tekton CRDs are absent (404).
        Raises ClusterUnreachableError on other API failures.
        """
