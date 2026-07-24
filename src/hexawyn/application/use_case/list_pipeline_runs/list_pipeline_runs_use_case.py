from hexawyn.application.use_case.list_pipeline_runs.command import ListPipelineRunsCommand
from hexawyn.application.use_case.list_pipeline_runs.response import ListPipelineRunsResponse


class ListPipelineRunsUseCase:
    def __init__(self, tekton_port) -> None:
        self._port = tekton_port

    def execute(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        runs = self._port.list_pipeline_runs(
            service_name=command.service_name,
            namespace=command.namespace,
        )
        return ListPipelineRunsResponse(pipeline_runs=list(runs))
