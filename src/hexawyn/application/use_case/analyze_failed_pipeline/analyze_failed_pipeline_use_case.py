from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.use_case.analyze_failed_pipeline.command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.use_case.analyze_failed_pipeline.response import (
    AnalyzeFailedPipelineResponse,
)


class AnalyzeFailedPipelineUseCase:
    def __init__(self, port: PipelineRunLogsPort) -> None:
        self._port = port

    def execute(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        return AnalyzeFailedPipelineResponse()
