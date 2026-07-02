from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.pipeline_for_service_port import PipelineForServicePort
from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_command import (
    PipelineForServiceCommand,
)
from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_response import (
    PipelineForServiceResponse,
)
from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_service_port import (
    PipelineForServiceServicePort,
)
from hexawyn.domain.models.pipeline_for_service import (
    PipelineForServiceRequest,
    PipelineForServiceResult,
)


class PipelineForServiceService(PipelineForServiceServicePort):
    def __init__(self, port: PipelineForServicePort) -> None:
        self._port = port

    def find(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )
