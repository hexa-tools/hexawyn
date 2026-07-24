from hexawyn.application.use_case.list_task_runs.command import ListTaskRunsCommand
from hexawyn.application.use_case.list_task_runs.response import ListTaskRunsResponse


class ListTaskRunsUseCase:
    def __init__(self, tekton_port) -> None:
        self._port = tekton_port

    def execute(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        runs = self._port.list_task_runs(
            pipeline_name=command.pipeline_name,
            namespace=command.namespace,
        )
        return ListTaskRunsResponse(task_runs=list(runs))
