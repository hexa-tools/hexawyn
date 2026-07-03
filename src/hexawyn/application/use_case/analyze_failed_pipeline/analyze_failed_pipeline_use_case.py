from __future__ import annotations

from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_response import (
    AnalyzeFailedPipelineResponse,
)
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_service_port import (
    AnalyzeFailedPipelineServicePort,
)


class AnalyzeFailedPipelineUseCase:
    def __init__(self, service: AnalyzeFailedPipelineServicePort) -> None:
        self._svc = service

    def execute(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse:
        return self._svc.analyze(command)
