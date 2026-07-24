from hexawyn.application.ports.driven.tekton_port import TaskRunInfo, TektonPort
from hexawyn.application.use_case.list_task_runs.command import (
    ListTaskRunsCommand,
)
from hexawyn.application.use_case.list_task_runs.response import (
    ListTaskRunsResponse,
)
from hexawyn.application.ports.driving.list_task_runs.list_task_runs_service_port import (
    ListTaskRunsServicePort,
)


class ListTaskRunsService(ListTaskRunsServicePort):
    """Lists TaskRuns for a pipeline, sorted by start time descending."""

    def __init__(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def list_task_runs(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=command.namespace,
        )
        sorted_runs = sorted(task_runs, key=_start_time_sort_key, reverse=True)
        return ListTaskRunsResponse(task_runs=sorted_runs)


def _start_time_sort_key(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["start_time"]
    if start_time is None:
        return (0, "")
    return (1, start_time)
