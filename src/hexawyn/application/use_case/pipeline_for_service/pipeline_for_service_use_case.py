from __future__ import annotations

from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_command import (
    PipelineForServiceCommand,
)
from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_response import (
    PipelineForServiceResponse,
)
from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_service_port import (
    PipelineForServiceServicePort,
)


class PipelineForServiceUseCase:
    def __init__(self, service: PipelineForServiceServicePort) -> None:
        self._svc = service

    def execute(self, cmd: PipelineForServiceCommand) -> PipelineForServiceResponse:
        return self._svc.find(cmd)
