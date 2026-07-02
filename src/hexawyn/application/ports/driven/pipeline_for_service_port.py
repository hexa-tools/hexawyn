from abc import ABC, abstractmethod

from hexawyn.domain.models.pipeline_for_service import PipelineForServiceRequest, ServicePipeline


class PipelineForServicePort(ABC):
    @abstractmethod
    def find_pipelines(self, request: PipelineForServiceRequest) -> list[ServicePipeline]: ...
