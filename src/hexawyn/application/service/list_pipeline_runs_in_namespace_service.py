from datetime import UTC, datetime

from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo, TektonPort
from hexawyn.application.use_case.list_pipeline_runs_in_namespace.command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.list_pipeline_runs_in_namespace.response import (
    ListPipelineRunsInNamespaceResponse,
)
from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_service_port import (
    ListPipelineRunsInNamespaceServicePort,
)

_STUCK_THRESHOLD_SECONDS = 3600
_STATUS_PRIORITY: dict[str, int] = {"Failed": 0, "Running": 1, "Succeeded": 2}


class ListPipelineRunsInNamespaceService(ListPipelineRunsInNamespaceServicePort):
    """Fetches all PipelineRuns in a namespace, sorts (Failed first), detects stuck runs."""

    def __init__(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def list_pipeline_runs_in_namespace(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        all_runs = self._tekton.list_pipeline_runs_in_namespace(
            namespace=command.namespace,
            limit=command.limit,
        )
        runs = _sort_by_status_then_time(all_runs)[: command.limit]
        stuck_runs = _find_stuck_runs(runs)
        note = f"No PipelineRuns found in namespace '{command.namespace}'." if not runs else None
        return ListPipelineRunsInNamespaceResponse(runs=runs, stuck_runs=stuck_runs, note=note)


def _sort_by_status_then_time(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(runs, key=lambda r: r["start_time"] or "", reverse=True)
    return sorted(by_time, key=lambda r: _STATUS_PRIORITY.get(r["status"], 3))


def _find_stuck_runs(runs: list[NamespacedPipelineRunInfo]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(run["start_time"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck
