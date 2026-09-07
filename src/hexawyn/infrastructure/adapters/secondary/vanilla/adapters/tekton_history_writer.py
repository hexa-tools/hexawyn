from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_history_port import (
    PipelineRunHistoryPort,
    PipelineRunSnapshot,
    TaskRunSnapshot,
)
from hexawyn.application.ports.driven.tekton_port import (
    NamespacedPipelineRunInfo,
    PipelineRunInfo,
    TaskRunInfo,
    TektonPort,
)


class TektonHistoryWriter(TektonPort):
    """Reads Tekton CRDs from the cluster and persists snapshots to DuckDB.

    Best-effort: a DuckDB write failure must never break the pipeline listing
    returned to the caller. The Tekton error semantics are preserved — empty
    lists are returned on ServiceNotFound / PipelineNotFound so callers see the
    same behaviour as the plain TektonPort.
    """

    def __init__(
        self,
        tekton_port: TektonPort,
        history_port: PipelineRunHistoryPort,
    ) -> None:
        self._tekton = tekton_port
        self._history = history_port

    def list_pipeline_runs_in_namespace(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        return self._tekton.list_pipeline_runs_in_namespace(namespace, limit)

    def list_pipeline_runs(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        try:
            runs = self._tekton.list_pipeline_runs(service_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[PipelineRunSnapshot] = [
                {
                    "name": run["name"],
                    "namespace": namespace,
                    "pipeline_name": service_name,
                    "status": run["status"],
                    "duration_seconds": run["duration_seconds"],
                    "start_time": run["start_time"],
                    "completion_time": None,
                }
                for run in runs
            ]
            self._history.save_pipeline_runs(snapshots)
        except Exception:
            pass
        return runs

    def list_task_runs(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        try:
            task_runs = self._tekton.list_task_runs(pipeline_name, namespace)
        except Exception:
            return []
        try:
            snapshots: list[TaskRunSnapshot] = [
                {
                    "name": task["name"],
                    "namespace": namespace,
                    "task_name": task["task_ref"],
                    "pipeline_run_name": pipeline_name,
                    "duration_seconds": None,
                }
                for task in task_runs
            ]
            self._history.save_task_runs(snapshots)
        except Exception:
            pass
        return task_runs
