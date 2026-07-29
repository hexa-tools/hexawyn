from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.list_task_runs.command import (
    ListTaskRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_task_runs.response import (
    ListTaskRunsResponse,
)
from hexawyn.application.use_case.pipelines.list_task_runs.sort_task_runs import (
    sort_by_start_time_desc,
)


class ListTaskRunsUseCase:
    """Lists TaskRuns for a pipeline, sorted by start time descending."""

    def __init__(self, tekton_port: TektonPort) -> None:
        self._tekton = tekton_port

    def execute(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        task_runs = self._tekton.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=command.namespace,  # type: ignore
        )
        sorted_runs = sort_by_start_time_desc(task_runs)
        return ListTaskRunsResponse(task_runs=sorted_runs)
