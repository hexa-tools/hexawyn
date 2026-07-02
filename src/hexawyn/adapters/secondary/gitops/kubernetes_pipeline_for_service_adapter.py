from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_for_service_port import PipelineForServicePort
from hexawyn.domain.models.pipeline_for_service import PipelineForServiceRequest, ServicePipeline


class KubernetesPipelineForServiceAdapter(PipelineForServicePort):
    def find_pipelines(self, request: PipelineForServiceRequest) -> list[ServicePipeline]:
        return []
