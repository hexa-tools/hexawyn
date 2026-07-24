from hexawyn.application.ports.driven.pipeline_for_service_port import PipelineForServicePort
from hexawyn.application.use_case.pipeline_for_service.command import PipelineForServiceCommand
from hexawyn.application.use_case.pipeline_for_service.response import PipelineForServiceResponse


class PipelineForServiceUseCase:
    def __init__(self, port: PipelineForServicePort) -> None:
        self._port = port

    def execute(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        return PipelineForServiceResponse()
