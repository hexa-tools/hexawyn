from hexawyn.application.ports.driven.tekton_pipeline_status_port import TektonPipelineStatusPort
from hexawyn.application.use_case.get_pipeline_run_status.command import GetPipelineRunStatusCommand
from hexawyn.application.use_case.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)


class GetPipelineRunStatusUseCase:
    def __init__(self, port: TektonPipelineStatusPort) -> None:
        self._port = port

    def execute(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        return GetPipelineRunStatusResponse()
