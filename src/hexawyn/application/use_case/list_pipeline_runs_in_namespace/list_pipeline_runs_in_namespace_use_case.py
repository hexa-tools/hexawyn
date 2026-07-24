from datetime import UTC, datetime

from hexawyn.application.use_case.list_pipeline_runs_in_namespace.command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.list_pipeline_runs_in_namespace.response import (
    ListPipelineRunsInNamespaceResponse,
)

_STUCK_THRESHOLD_SECONDS = 3600


def _find_stuck_runs(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(
                str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ"
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


from hexawyn.application.ports.driven.tekton_port import TektonPort


class ListPipelineRunsInNamespaceUseCase:
    def __init__(self, tekton_port: TektonPort) -> None:
        self._port = tekton_port

    def execute(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        runs = self._port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=command.limit
        )
        runs_list: list[dict[str, object]] = [dict(r) for r in runs]
        stuck_runs = _find_stuck_runs(runs_list)
        note = (
            f"No PipelineRuns found in namespace '{command.namespace}'."
            if not runs_list
            else None
        )
        return ListPipelineRunsInNamespaceResponse(
            runs=runs_list, stuck_runs=stuck_runs, note=note
        )
