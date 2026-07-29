from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.pipeline_for_service_port import PipelineForServicePort
from hexawyn.application.use_case.pipelines.pipeline_for_service.command import (
    PipelineForServiceCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_for_service.response import (
    PipelineForServiceResponse,
)
from hexawyn.domain.models.pipeline_for_service import (
    PipelineForServiceRequest,
    PipelineForServiceResult,
)


class PipelineForUseCaseUseCase:
    def __init__(self, port: PipelineForServicePort) -> None:
        self._port = port

    def execute(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse:
        req = PipelineForServiceRequest(service_name=command.service_name)
        pipelines = self._port.find_pipelines(req)
        r = PipelineForServiceResult.compute(request=req, pipelines=pipelines)
        return PipelineForServiceResponse(
            service_name=r.service_name,
            pipelines_found=r.pipelines_found,
            pipelines=[asdict(p) for p in r.pipelines],
        )
